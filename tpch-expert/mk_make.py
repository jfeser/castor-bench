#!/usr/bin/env python3

from jsmin import jsmin
import json
import shlex

DEBUG = False


def value_to_castor(type_, value):
    if type_ == 'int' or type_ == 'fixed' or type_ == 'bool':
        return value
    elif type_ == 'date':
        return 'date("%s")' % value
    elif type_ == 'string':
        return '"%s"' % value
    else:
        raise RuntimeError('Unexpected type %s.' % type_)


def gen_params(b):
    params = []
    for [p, v] in b['params']:
        type_ = p.split(':')[1]
        params.append('-p \'%s=%s\'' % (p, value_to_castor(type_, v)))
    return ' '.join(params)


def gen_param_types(b):
    params = []
    for [p, v] in b['params']:
        params.append('-p \'%s\'' % p)
    return ' '.join(params)


def gen_param_values(b):
    params = []
    for [p, v] in b['params']:
        params.append('\'%s\'' % v)
    return ' '.join(params)


with open('../tpch/queries.json', 'r') as f:
    bench = json.loads(jsmin(f.read()))

print('SHELL:=/bin/bash')
print('COMPILE_PATH=../../castor/bin/compile.exe')
print('COMPILE=dune exec --no-build $(COMPILE_PATH) -- ')
if DEBUG:
    print('CFLAGS=-debug -v')
else:
    print('CFLAGS=-v')
print('TIME_CMD=/usr/bin/time')
print('TIME_PER_BENCH=1')

print('''
compile: %s
.PHONY: compile
''' % (' '.join(['%s-gold' % b['name'] for b in bench])))

print('''
run: %s
.PHONY: run
''' % (' '.join(['%s-gold.csv' % b['name'] for b in bench])))

print('''
time: %s
.PHONY: time
''' % (' '.join(['%s-gold.time' % b['name'] for b in bench])))

print('''
validate: %s
.PHONY: validate
''' % (' '.join(['analysis_%s.log' % b['name'] for b in bench])))

for b in bench:
    print('''
{0}-gold: ../../castor/bench/tpch/{0}-gold.txt
\tmkdir -p $@
\t$(COMPILE) $(CFLAGS) -o $@ {1} $< > $@/compile.log 2>&1
'''.format(b['name'], gen_param_types(b)))

    print('''
{0}-gold.csv:
\t./{0}-gold/scanner.exe -p {0}-gold/data.bin {1} > $@
'''.format(b['name'], gen_param_values(b)))

    print('''
{0}-gold.time:
\t./{0}-gold/scanner.exe -t $(TIME_PER_BENCH) {0}-gold/data.bin {1} > $@
\t$(TIME_CMD) -v ./{0}-gold/scanner.exe -t $(TIME_PER_BENCH) {0}/data.bin {1} 2> {0}-gold.mem > /dev/null
'''.format(b['name'], gen_param_values(b)))

    print('''
analysis_{0}.log:
\t../bin/validate.py {0} {1} {0}-gold.csv
    '''.format(b['name'], str(b['ordered'])))

print('''
.PHONY: clean
clean:
\trm -rf */ *.csv *.mem *.time analysis*log
''')

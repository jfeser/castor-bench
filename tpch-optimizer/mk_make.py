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


def in_file(b):
    return '$(BENCH_DIR)/%s.txt' % b['name']


def out_file(b):
    return '%s-opt.txt' % b['name']


def out_dir(b):
    return '%s-opt' % b['name']


with open('../tpch/queries.json', 'r') as f:
    bench = json.loads(jsmin(f.read()))

print('SHELL:=/bin/bash')

print ('OPT=../../_build/default/castor-opt/bin/opt.exe')
print ('OPT_TIMEOUT=7200')
print ('OPT_FLAGS=-cost-timeout 5.0 -v -set-log-level-castor.ops warning -set-log-level-castor.type warning -timeout $(OPT_TIMEOUT)')

print('COMPILE_PATH=../../castor/bin/compile.exe')
print('COMPILE=dune exec --no-build $(COMPILE_PATH) -- ')
if DEBUG:
    print('CFLAGS=-debug -v')
else:
    print('CFLAGS=-v')

print('BENCH_DIR=../tpch/')
print('TIME_CMD=/usr/bin/time')
print('TIME_PER_BENCH=1')
print('all: opt compile run time')

print('''
opt: %s
.PHONY: opt
''' % (' '.join([out_file(b) for b in bench])))

print('''
compile: %s
.PHONY: compile
''' % (' '.join([out_dir(b) for b in bench])))

print('''
run: %s
.PHONY: run
''' % (' '.join(['%s-opt.csv' % b['name'] for b in bench])))

print('''
time: %s
.PHONY: time
''' % (' '.join(['%s-opt.time' % b['name'] for b in bench])))

print('''
validate: %s
.PHONY: validate
''' % (' '.join(['analysis_%s-opt.csv.log' % b['name'] for b in bench])))

for b in bench:
    print('''
{out_file}:
\t$(OPT) $(OPT_FLAGS) -o {out_dir} -f {out_file} {params} {in_file} 2> >(tee {log} >&2)
    '''.format(
        out_file=out_file(b),
        out_dir=out_dir(b),
        params=gen_params(b),
        in_file=in_file(b),
        log='%s-opt.log' % b['name']))

    print('''
{0}-opt.csv:
\t./{1}/scanner.exe -p {1}/data.bin {2} > $@
'''.format(b['name'], out_dir(b), gen_param_values(b)))

    print('''
{name}-opt.time:
\t./{build_dir}/scanner.exe -t $(TIME_PER_BENCH) {build_dir}/data.bin {params} > $@
\t$(TIME_CMD) -v ./{build_dir}/scanner.exe -t $(TIME_PER_BENCH) {build_dir}/data.bin {params} 2> {name}-opt.mem > /dev/null
'''.format(name=b['name'],
           build_dir=out_dir(b),
           params=gen_param_values(b)))

    print('''
analysis_{0}-opt.csv.log:
\t../bin/validate.py {0} {2} {0}-opt.csv
    '''.format(b['name'], out_dir(b), str(b['ordered'])))

print('''
.PHONY: clean
clean:
\trm -rf *-opt.txt *-opt *-opt.csv *-opt.log *-opt.time analysis_*.log *-trial *-opt.mem \
         hashes.txt
''')

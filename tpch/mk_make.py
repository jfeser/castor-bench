#!/usr/bin/env python3

from jsmin import jsmin
import json
import shlex

DEBUG = False


def param_values_sql(b):
    return [v for [_, v] in b['params']]


with open('queries.json', 'r') as f:
    bench = json.loads(jsmin(f.read()))


print('''
all: %s
''' % (' '.join(['%s.csv' % b['name'] for b in bench])))

for b in bench:
    print('''
{0}.csv:
\t../bin/run_psql.py postgres:///tpch {0}.sql {1} > $@
    '''.format(b['name'], shlex.quote(json.dumps(param_values_sql(b)))))

print('''
.PHONY: clean
clean:
\trm -rf *.csv
''')

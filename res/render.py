#!/usr/bin/env python3

import yaml, os, re, sys
import shutil

yfile = 'thesis.yaml' if len(sys.argv) == 1 else sys.argv[1]
meta = yaml.load(open(yfile, encoding='utf-8'), Loader=yaml.FullLoader)

shutil.rmtree('build')
os.mkdir('build')

for file in os.listdir('res'):
    if file.endswith('lyx'):
        shutil.copy(os.path.join('res', file), os.path.join('build', file))

shutil.copy('res/thesis.layout', 'build/thesis.layout')

def gen(fname):
    with open("build/%s" % fname, encoding='utf-8') as fp:
        contents = fp.read()
        
    def repl(m):
        key = m.group(1).strip()
        if key in meta:
            return str(meta[key])
        else:
            return "\\textcolor{red}{Undefined (%s)}" % key
        
    contents = re.sub(r'-\{\{-(.*?)-\}\}-', repl, contents)

    with open("build/%s" % fname, "w", encoding='utf-8') as fp:
        fp.write(contents)

for f in ['thesis.layout', 'grad.lyx']:
    gen(f)

print('success')
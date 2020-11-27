from pathlib import Path
import re, sys

name = sys.argv[1]

base_str = '!commands edit !{} $(eval var q=[{}];q[Math.floor(Math.random()*{})])'

js_code = Path.cwd() / '{}.txt'.format(name)

num_quotes=0

quotes = []

for ln in js_code.read_text().split("\n"):
    quotes.append(ln)
    num_quotes += 1

res = base_str.format(name, ",".join(('"{}"'.format(x)) for x in quotes), num_quotes)

print(res)

# print(base_str.format(minified))
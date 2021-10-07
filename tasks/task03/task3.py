import re
texts = [
   "Hello, World!",
   "The world is mine",
   "Hello, how are you?"
]
al = []
dictn = {}
dls = {}
t = 0
for index, line in enumerate(texts):
   for l in line.split():
      al.append(re.sub('[^a-zA-Z]+', '', l.lower()))
      dictn[index, re.sub('[^a-zA-Z]+', '', l.lower())] = t
      t = t + 1
tp = tuple(dictn)
for inx, v in enumerate(tp):
   if v[1] not in dls:
      dls[v[1]] = al.count(v[1].lower()), v[0]
print(f'{"word"}     {"count"}  {"line"}')
for k, f in dls.items():
   print(f'{k:5}{f[0]:5}{f[1]:7}')


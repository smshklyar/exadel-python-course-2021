import re
texts = [
   "Hello, World!",
   "The world is mine",
   "Hello, how are you?"
]
al = []
dictn = {}
t = 0
for index, line in enumerate(texts):
   for l in line.split():
      al.append(re.sub('[^a-zA-Z]+', '', l.lower()))
      t = t + 1
      dictn[index, re.sub('[^a-zA-Z]+', '', l.lower())] = t
tp = tuple(dictn)
for inx, v in enumerate(tp):
   if inx == 0:
      print("word", "count", "line")
   print(v[1], al.count(v[1].lower()), v[0])

d = {}
fhand = requests.get('https://www.py4e.com/code3/words.txt')
for line in fhand:
  words = line.split()
  # print(words)
  for word in words:
    if word not in d:
      d[word] = 1
    else:
      d[word] += 1
  #  d[word] = 'default'
    #  d['word'] = 'default'
  # print('Debug', words)
print(d)

string = str(input())
string = string[0].upper() + string[1:]
words = string.split()
for i in range(1, len(words)):
  if i + 1 < len(words):
    if words[i][-1] in '.!?':
      words[i + 1] = words[i + 1][0].upper() + words[i + 1][1:]
print(' '.join(words))

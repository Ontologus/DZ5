string_1 = input().split()
nstring_1 = ''.join(string_1)
list_1 = list(nstring_1)
nlist_1 = set(list_1)
string_2 = input().split()
nstring_2 = ''.join(string_2)
list_2 = list(nstring_2)
nlist_2 = set(list_2)
if nlist_1.intersection(nlist_2) == nlist_1:
  print('Эти строки являются анаграммами')
else:
  print('Эти строки не являются анаграммами')

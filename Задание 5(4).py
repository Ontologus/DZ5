s_alg = input().split()
s_geo = input().split()
s_trygono = input().split()
ns_alg = set(s_alg)
ns_geo = set(s_geo)
ns_trygono = set(s_trygono)
vse = ns_alg & ns_geo & ns_trygono
if len(vse) > 0:
  print(' '.join(vse))
else:
  print('Все три задачи никто не решил')

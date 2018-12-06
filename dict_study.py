def func(arg1):
  for key,value in arg1.items():
    print(key, 'has', value)

dct1 = {}
for i in range(10):
  dct1.setdefault('List %i'%i+1,[]).append(i+1)

func(dct1)
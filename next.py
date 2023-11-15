f = open('example1.txt')

# print(f.readline())
# print(f.readline())

print(next(f))
print(next(f))
# print(next(f))

f2 = open('example2.txt')
for i in f2 : # Итератор файла
  print(i)
  
f.close()
f2.close()
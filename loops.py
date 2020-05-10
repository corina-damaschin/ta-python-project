# for
a = [1, 64, 58, 96]
print(a[2], a[-1])

s = 58
for i in a:
  print(i)
  if i == 58:
    print(i+2)
    break
  else:
    print(i+1)

thisset1 = {"apple", "banana", "cherry"}

for x in thisset1:
  print(x)

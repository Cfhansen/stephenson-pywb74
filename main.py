###solution to exercise 74 from ben stephenson's "the python workbook"

print('\t', end="")
for i in range(1,11):
  print(str(i) + '\t', end="")
print('\n')

for i in range(1,11):
  print(str(i) + '\t', end="")
  for j in range(1,11):
    print(str(i * j) + '\t', end = "")
  print('\n')

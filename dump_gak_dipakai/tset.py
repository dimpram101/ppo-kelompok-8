b = [
  [1, -8, -6, 0, 0, 0, 0],
  [0, 4, 2, 1, 0, 60, 0],
  [0, 2, 4, 0, 1, 48, 0]
]

minValue = []

for i in b:
  minValue.append(min(i))

minimal = min(minValue)


index = 0
for j in range(len(b)):
  if minimal in b[j]:
    key = j
    index = b[j].index(minimal)
    break


print(key, index)
print(1 ==1.0)
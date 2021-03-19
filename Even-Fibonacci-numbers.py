fibNumbers = [0,1]
while fibNumbers[-1] <= 4000000:
    fibNumbers.append(fibNumbers[-1] + fibNumbers[-2])

fibNumbers.pop(-1)
result = 0

for i in fibNumbers:
    if i % 2 == 0:
        result = result + i
print(result)

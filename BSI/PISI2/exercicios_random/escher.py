n = int(input())
m = []
for i in range(n):
    m.append(int(input()))

i, j = 0, -1
escher = m[i] + m[j]
while i <= j:
    if (escher != m[i]+m[j]):
        print("n")
        break
    i += 1
    j -= 1
print("s")

a, b, c = map(int, input().split())
haiku = [a, b, c]
count=0
for i in haiku:
    if i == 5:
        count += 1
        
if count == 2:
    print("YES")
else:
    print("NO")


# 他の例
A = list(map(int, input().split()))
A.sort()

if A==[5, 5, 7]:
    print("YES")
else:
    print("NO")
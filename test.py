n=int(input())
for i in range(1,n**0,5+1):
    if n%i==0:
        print("NO")
        exit()
print("YES")
a=input()
b=input()
c=input()
x=a[12:]
y=int(b[20:])
z=int(c[18:])
kq=z-y
p=kq
ans=0
l=[0,50,100,200,300,400]
k=[1984,2050,2380,2998,3350,3460]
for i in range(1,6):
	if kq<=l[i]:
		kq-=l[i-1]
		ans+=(kq*k[i-1])
		kq=0
		break
	ans+=(l[i]-l[i-1])*k[i-1]
if kq>400:
	ans+=((kq-400)*3460)
print("Ho va ten:",x)
print("Tien phai tra la:",round(ans*1.08))
		
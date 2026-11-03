a,b,c=map(float,input().split())
if a+b>c and b+c>a and a+c>b :
	p=(a+b+c)/2
	print(round((p*(p-a)*(p-b)*(p-c))**0.5,1))
else: print("Khong phai 3 canh cua tam giac")
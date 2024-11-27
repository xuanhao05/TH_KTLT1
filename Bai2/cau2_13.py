print("sv:Nguyen Xuan Hao")
print("mssv:235752021610096")
#general equation
a = float(input("enter a (a<>0):"))
b = float(input("nhap b: "))
c = float(input("enter c: "))
delta=b*b-4*a*c;
if delta==0:
    print("phuong trinh co nghiem kep x1=x2", (-b/2*a))
if delta>0:
    print(" pt co 2 nghiem x1=", (-b+delta**0.5/(2*a), "ca x2=", (-b-delta**0.5/)
if delta<0:
    print("pt vo nghiem")

print("sv:Nguyen Xuan Hao")
print("mssv:235752021610096")
def benefit(t,n,k):
    return n* (1+t/100) **k

# Nhap tu ban phim
t = float(input(" Nhap lai suat (%/thang):"))
n= float(input(" Nhap so von ban đau:"))
k=int(input("Nhập sổ thang gui:"))

# Tinh so tien nhan duoc sau k thang gui
so_tien = lợi ích (t,n,k)
print (f"so tien nhan duoc sau {k} tháng gui la: { so_tien:.2f}"

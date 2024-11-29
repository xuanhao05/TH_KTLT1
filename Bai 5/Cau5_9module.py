print("sv:Nguyen Xuan Hao")
print("mssv:235752021610096")
# Chương trình chính

n = int(input("Nhập số lượng phần tử trong danh sách: "))

lst = []
for i in range(n):
    element = int(input(f"Nhập phần tử thứ {i+1}: "))
    lst.append(element)

lst.sort()

value = int(input("Nhập phần tử cần tìm kiếm: "))

import binary_search

# Gọi hàm binary_search
found = binary_search.binary_search(lst, value)

# In kết quả
if found:
    print(f"Phần tử {value} có trong danh sách.")
else:
    print(f"Phần tử {value} không có trong danh sách.")

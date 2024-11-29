print("sv:Nguyen Xuan Hao")
print("mssv:235752021610096")

n = int(input("Nhập số lượng phần tử trong danh sách: "))

dlist = []
for i in range(n):
    element = int(input(f"Nhập phần tử thứ {i+1}: "))
    dlist.append(element)

item = int(input("Nhập phần tử cần tìm kiếm: "))

import sequential_search

found, index = sequential_search.Sequential_Search(dlist, item)

# In kết quả
if found:
    print(f"Phần tử {item} được tìm thấy ở chỉ số {index}.")
else:
    print(f"Phần tử {item} không có trong danh sách.")

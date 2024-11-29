print("sv:Nguyen Xuan Hao")
print("mssv:235752021610096")
n = int(input("Nhập số lượng phần tử của danh sách: "))
lst = []
for i in range(n):
    element = int(input(f"Nhập phần tử thứ {i+1}: "))
    lst.append(element)

import sort_and_find

sorted_lst, max_element = sort_and_find.sort_and_find(lst)

min_element = sorted_lst[0]

# In ra kết quả
print(f"Danh sách sau khi sắp xếp: {sorted_lst}")
print(f"Phần tử lớn nhất là: {max_element}")
print(f"Phần tử nhỏ nhất là: {min_element}")

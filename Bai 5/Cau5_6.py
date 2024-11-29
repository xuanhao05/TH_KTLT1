print("sv:Nguyen Xuan Hao")
print("mssv:235752021610096")
# Chương trình chính

# Nhập số lượng phần tử và danh sách từ người dùng
n = int(input("Nhập số lượng phần tử của danh sách: "))
lst = []
for i in range(n):
    element = int(input(f"Nhập phần tử thứ {i+1}: "))
    lst.append(element)

# Nhập module sort_and_find để sắp xếp và tìm phần tử lớn nhất
import sort_and_find

# Gọi hàm sort_and_find để xử lý danh sách
sorted_lst, max_element = sort_and_find.sort_and_find(lst)

# Tìm phần tử nhỏ nhất trong danh sách (phần tử đầu tiên sau khi sắp xếp)
min_element = sorted_lst[0]

# In ra kết quả
print(f"Danh sách sau khi sắp xếp: {sorted_lst}")
print(f"Phần tử lớn nhất là: {max_element}")
print(f"Phần tử nhỏ nhất là: {min_element}")

print("sv:Nguyen Xuan Hao")
print("mssv:235752021610096")
from bubble_sort import bubbleSort

input_list = input("Nhập danh sách các số (cách nhau bởi dấu phẩy): ")
nlist = [int(x) for x in input_list.split(",")]

sorted_list = bubbleSort(nlist)

print("Danh sách đã sắp xếp:", sorted_list)

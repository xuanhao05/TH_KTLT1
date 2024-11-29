print("sv:Nguyen Xuan Hao")
print("mssv:235752021610096")
# binary_search.py

def binary_search(lst, value):
    """
    Hàm tìm kiếm nhị phân. Trả về True nếu phần tử value tìm thấy trong lst, 
    ngược lại trả về False.
    Danh sách lst phải được sắp xếp theo thứ tự tăng dần.
    """
    low = 0
    high = len(lst) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == value:
            return True
        elif lst[mid] > value:
            high = mid - 1
        else:
            low = mid + 1
    
    return False

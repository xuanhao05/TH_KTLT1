print("sv:Nguyen Xuan Hao")
print("mssv:235752021610096")
# sequential_search.py

def Sequential_Search(dlist, item):
    """
    Hàm tìm kiếm tuyến tính (sequential search).
    Trả về (True, index) nếu phần tử item tìm thấy trong dlist,
    ngược lại trả về (False, -1).
    """
    for index in range(len(dlist)):
        if dlist[index] == item:
            return True, index
    return False, -1

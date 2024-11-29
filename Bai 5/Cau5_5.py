print("sv:Nguyen Xuan Hao")
print("mssv:235752021610096")
def sort_and_find(lst):
    """
    Sắp xếp danh sách và tìm phần tử lớn nhất.
    Trả về danh sách đã sắp xếp và phần tử lớn nhất.
    """
    lst.sort()  
    max_element = lst[-1]  
    return lst, max_element

print("sv:Nguyen Xuan Hao")
print("mssv:235752021610096")
def count_lines (file_path):
    try:
        with open(file_path, 'r') as file:
            line count = sum(1 for line in file)
        return line_count
    except Exception as e:
        return f"Lỗi: {e}"
line_count = count_lines('test.txt')
print (f"Số dòng trong tệp: {line_count}")

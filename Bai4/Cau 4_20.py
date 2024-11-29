print("sv:Nguyen Xuan Hao")
print("mssv:235752021610096)
def pascal_triangle(n):
    """Hàm tạo n dòng đầu tiên của tam giác Pascal."""
    triangle = []
    for i in range(n):
        row = [1]  # Dòng bắt đầu với số 1
        if triangle:  # Nếu không phải dòng đầu tiên
            last_row = triangle[-1]
            for j in range(len(last_row) - 1):
                row.append(last_row[j] + last_row[j + 1])
            row.append(1)  # Kết thúc dòng với số 1
        triangle.append(row)
    return triangle

n = int(input("Nhập số dòng của tam giác Pascal: "))

triangle = pascal_triangle(n)
print("Tam giác Pascal:")
for row in triangle:
    print(row)

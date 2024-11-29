print("sv:Nguyen Xuan Hao")
print("mssv:235752021610096)
binary_numbers = input("Nhập chuỗi các số nhị phân (phân tách bởi dấu phẩy): ").split(',')

valid_numbers = []
for binary in binary_numbers:
    if len(binary) == 4 and binary.isdigit() and set(binary) <= {'0', '1'}:
        if int(binary, 2) % 5 == 0:
            valid_numbers.append(binary)

print("Các số nhị phân chia hết cho 5 là:", ','.join(valid_numbers))

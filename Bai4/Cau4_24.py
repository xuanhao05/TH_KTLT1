print("sv:Nguyen Xuan Hao")
print("mssv:235752021610096")
input_string = input("Nhập một câu: ")

uppercase_count = 0
lowercase_count = 0

for char in sentence:
    if char.isupper():  
        uppercase_count += 1
    elif char.islower():  
        lowercase_count += 1

print(f"Chữ hoa: {uppercase_count}")
print(f"Chữ thường: {lowercase_count}")

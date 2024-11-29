print("sv:Nguyen Xuan Hao")
print("mssv:235752021610096")
even_digit_numbers = []
for num in range(1000, 3001):  # Bao gồm cả 3000
    if all(int(digit) % 2 == 0 for digit in str(num)):  
        even_digit_numbers.append(str(num))

print(",".join(even_digit_numbers))

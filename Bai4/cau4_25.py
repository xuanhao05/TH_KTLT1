print("sv:Nguyen Xuan Hao")
print("mssv:235752021610096)
def filter_odd_numbers (numbers):
    return [num for num in numbers if num % 2 != 0]
input_numbers = input("Nhập các số cách nhau bởi dấu phẩy: ")
numbers_list = [int(num.strip()) for num in input_numbers.split(',')
odd_numbers filter_odd_numbers (numbers_list)
print("Các số lẻ trong danh sách là:", odd_numbers)

print("sv:Nguyen Xuan Hao")
print("mssv:235752021610096")
def write_list_to_file(file_path, data_list):
    try:
        with open (file_path, 'w') as file:
            for item in data list:
                file.write(str(item) + '\n')
        print("Nội dung danh sách đã được ghi vào tệp.")
    except Exception as e:
        print (f"Lỗi: {e}")
data = ['Apple', 'Banana', 'Cherry', 'Date']
write_list_to_file('output.txt', data)

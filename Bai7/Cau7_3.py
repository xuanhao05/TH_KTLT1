print("sv:Nguyen Xuan Hao")
print("mssv:235752021610096")
def read_file(file_path):
    try:
        print(open(file_path, 'r').read())
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print (f"Error: {e}")
read_file('your_file.txt')

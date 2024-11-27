print("sv:Nguyen Xuan Hao")
print("mssv:235752021610096")
input_string = input(" Nhap mot day cac tu:")

words = input_string.split()

max_length = max(len(word)for word in words)

print("Cac tu dai nhat la:")
for word in words:
  if len(word) == max_length:
    print(word)

print("sv:Nguyen Xuan Hao")
print("mssv:235752021610096")
transactions = []
while True:
    transaction = input("Nhập giao dịch (hoặc nhấn Enter để kết thúc): ")
    if not transaction:  
        break
    transactions.append(transaction)

balance = 0

for transaction in transactions:
    action, amount = transaction.split() 
    amount = int(amount)
    if action == "D":  # Nếu là tiền gửi
        balance += amount
    elif action == "W":  # Nếu là tiền rút
        balance -= amount


print(f"Số dư tài khoản là: {balance}")

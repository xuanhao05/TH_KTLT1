print("sv:Nguyen Xuan Hao")
print("mssv:235752021610096")
import tkinter as tk

# Khởi tạo cửa sổ chính
window = tk.Tk()
window.title("Cửa sổ Tkinter Đơn Giản")
window.geometry("300x200")

# Tạo một nhãn và nút bấm
label = tk.Label(window, text="Xin chào Tkinter!")
label.pack(pady=20)

button = tk.Button(window, text="Mở", command=lambda: label.config(text="Đã mở!"))
button.pack(pady=10)

button = tk.Button(window, text="Đóng", command=lambda: label.config(text="Đã đóng!"))
button.pack(pady=10)
 

# Chạy vòng lặp chính của Tkinter
window.mainloop()

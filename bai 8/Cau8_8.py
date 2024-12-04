print("sv: Nguyen Xuan Hao")
print("mssv:235752021610096")
import tkinter as tk
from tkinter import messagebox

# Hàm để hiển thị thông tin cá nhân
def show_personal_info():
    name = entry_name.get()
    dob = entry_dob.get()
    mssv = entry_mssv.get()
    major = entry_major.get()
    
    messagebox.showinfo("Thông tin cá nhân", f"Họ tên: {name}\nNgày sinh: {dob}\nMSSV: {mssv}\nNgành học: {major}")

# Hàm để xử lý khi người dùng click vào nút "Click Me"
def show_radio_choice():
    choice = var.get()
    messagebox.showinfo("Thông tin lựa chọn", f"Bạn đã chọn số: {choice}")

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Thông tin cá nhân & Radio Button")

# Phần form thông tin cá nhân
frame_info = tk.LabelFrame(root, text="Thông tin cá nhân", padx=10, pady=10)
frame_info.grid(row=0, column=0, padx=20, pady=20)

# Label và Entry cho Họ tên
tk.Label(frame_info, text="Họ tên:").grid(row=0, column=0, sticky="e")
entry_name = tk.Entry(frame_info)
entry_name.grid(row=0, column=1)

# Label và Entry cho Ngày tháng năm sinh
tk.Label(frame_info, text="Ngày sinh (dd/mm/yyyy):").grid(row=1, column=0, sticky="e")
entry_dob = tk.Entry(frame_info)
entry_dob.grid(row=1, column=1)

# Label và Entry cho MSSV
tk.Label(frame_info, text="MSSV:").grid(row=2, column=0, sticky="e")
entry_mssv = tk.Entry(frame_info)
entry_mssv.grid(row=2, column=1)

# Label và Entry cho Ngành học
tk.Label(frame_info, text="Ngành học:").grid(row=3, column=0, sticky="e")
entry_major = tk.Entry(frame_info)
entry_major.grid(row=3, column=1)

# Nút để hiển thị thông tin cá nhân
btn_show_info = tk.Button(frame_info, text="Hiển thị thông tin", command=show_personal_info)
btn_show_info.grid(row=4, columnspan=2, pady=10)

# Phần form radio button
frame_radio = tk.LabelFrame(root, text="Lựa chọn", padx=10, pady=10)
frame_radio.grid(row=1, column=0, padx=20, pady=20)

# Tạo biến để lưu giá trị lựa chọn của radio button
var = tk.IntVar()

# Các radio button
tk.Radiobutton(frame_radio, text="First", variable=var, value=1).grid(row=0, column=0, sticky="w")
tk.Radiobutton(frame_radio, text="Second", variable=var, value=2).grid(row=0, column=1, sticky="w")
tk.Radiobutton(frame_radio, text="Third", variable=var, value=3).grid(row=0, column=2, sticky="w")

# Nút để hiển thị thông tin lựa chọn radio button
btn_show_choice = tk.Button(frame_radio, text="Click Me", command=show_radio_choice)
btn_show_choice.grid(row=1, columnspan=10, pady=10)

# Bắt đầu vòng lặp giao diện
root.mainloop()

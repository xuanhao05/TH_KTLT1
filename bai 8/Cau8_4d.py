print("sv:Nguyen Xuan Hao")
print("mssv:235752021610096")
from tkinter import * 
window = Tk() 
window.title(" Chào mừng đến với ứng dụng LikeGeeks") 
window.geometry('350x200') 
lbl = Label(window, text=" Xin chào",fg="red",bg="blue") 
lbl.grid(column=0, row=0) 
def clicked(): 
    lbl.configure(text=" Nút đã được nhấp !!",fg="black",bg="yellow") 
btn = Button(window, text="Nhấp vào tôi",fg="pink", command=clicked) 
btn.grid(column=1, row=0) 
window.mainloop()



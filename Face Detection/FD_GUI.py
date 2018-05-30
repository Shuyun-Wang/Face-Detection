import face_api
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

# 获取文本框内容
def getname():  
    name=name_text.get()
    face_api.face_detection(File,name)

# 获取图片路径
def getfile():
    global File
    File = filedialog.askopenfilename(parent=window,title='Choose an image.')
    filename = ImageTk.PhotoImage(Image.open(File))
    canvas.image = filename  # <--- keep reference of your image
    canvas.create_image(0,0,anchor='nw',image=filename)

# 生成窗口
window = Tk()        #实例化出一个父窗口
window.title("人脸检测工具_v1.0")
window.geometry('700x433')      #700x433为窗口大小
window.attributes("-alpha",0.8)       #虚化 值越小虚化程度越高

# 生成名称
l1 = Label(window,text="输入您的名字(全拼)：")
l1.pack() #指定包管理器放置组件 
# 创建文本框 
name_text= Entry()
name_text.pack() 

# 生成选图框
frame = Frame(window, bd=2, relief=SUNKEN)
frame.grid_rowconfigure(0, weight=1)
frame.grid_columnconfigure(0, weight=1)
xscroll = Scrollbar(frame, orient=HORIZONTAL)
xscroll.grid(row=1, column=0, sticky=E+W)
yscroll = Scrollbar(frame)
yscroll.grid(row=0, column=1, sticky=N+S)
canvas = Canvas(frame, bd=0, xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)
canvas.grid(row=0, column=0, sticky=N+S+E+W)
xscroll.config(command=canvas.xview)
yscroll.config(command=canvas.yview)
frame.pack(fill=BOTH,expand=1)

#command绑定获取文本框内容方法
Button(window,text='选择图片(最好为正脸照)',command=getfile).pack()
Button(window,text="开始",command=getname).pack()

#父窗口进入事件循环，可以理解为保持窗口运行，否则界面不展示
window.mainloop()

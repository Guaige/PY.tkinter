# coding=UTF-8<code>
#reference for keyboard monitoring : https://www.cnblogs.com/anita-harbour/p/9449757.html
#reference for tkinter : https://blog.csdn.net/weixin_30483495/article/details/95835191
from tkinter import *

def processKeyboardEvent(key):
    print("key.char", key.char)  # 按键对应的字符
    move_obj(tank, id_obj, key.char)
    #print("ke.keycode", ke.keycode)  # 按键的唯一代码，用于判断按下的是哪个键</class></key></button-1>

def move_obj(tank, idx, pos):  # 移动坐标
    if pos == 'd':
        coord[0] += step
        coord[2] += step
        #tank.coords(idx, (330, 330, 470, 470))
    elif pos == 'a':
        coord[0] -= step
        coord[2] -= step
        #tank.coords(idx, (330, 130, 470, 270))
    elif pos == 's':
        coord[1] += step
        coord[3] += step
        #tank.coords(idx, (130, 130, 270, 270))
    elif pos == 'w':
        coord[1] -= step
        coord[3] -= step
        #tank.coords(idx, (130, 330, 270, 470))
    else:
        raise Exception('TBE')
        #To Be Edited
    tank.coords(idx, coord)
    print(coord)
    return


step = 50
coord = [250, 250, 350, 350]
tk = Tk()  # 画布
#tk.title('EIT_tank')
tk.resizable(0, 0)  # 固定窗口大小
tank = Canvas(tk, width=600, height=600, bg='ivory')
tank.focus_set()
tank.pack()  # 默认布局
#tank.create_oval(30, 30, 570, 570, width=1.5)  # 横轴x
#tank.create_line(30, 300, 570, 300, width=1.5, fill='red', dash=6)  # 网格,虚线
#tank.create_line(300, 30, 300, 570, width=1.5, fill='red', dash=6)

id_obj = tank.create_oval(coord, width=0, fill='gray')
tank.bind(sequence="<Key>", func=processKeyboardEvent)

tank.mainloop()

'''
print(coord[0])# 物体
tk.update_idletasks()
#print(id_obj)
tk.update()
time.sleep(2)
tank.coords(id_obj, (350, 250, 450, 350))
tk.update_idletasks()
tk.update()
time.sleep(2)
'''




'''
while 1:
    move_obj(tank, id_obj, 1)
    time.sleep(0.5)
    tk.update_idletasks()
    tk.update()

    move_obj(tank, id_obj, 3)
    time.sleep(0.5)
    tk.update_idletasks()
    tk.update()

    move_obj(tank, id_obj, 2)
    time.sleep(0.5)
    tk.update_idletasks()
    tk.update()

    move_obj(tank, id_obj, 4)
    time.sleep(0.5)
    tk.update_idletasks()
    tk.update()

mainloop()
'''
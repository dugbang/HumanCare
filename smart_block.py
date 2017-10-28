
import time


CONTROL_BLOCK = {
    '블록에러': 0,
    '시작하기': 1,
    '종료하기': 2,
    '취소하기': 3,
    '다음페이지': 4,
    '이전페이지': 5,
    '캐릭터': 6,
    '튜토리얼': 7,
}

EMOTION_BLOCK = {
    '행복': 21,
    '슬픔': 22,
    '기쁨': 23,
    '짜증': 24,
    '외로움': 25,
    '두려움': 26,
    '쓸쓸함': 27,
}

ALPHABAT_BLOCK = {
    'A': 51,
    'B': 52,
    'C': 53,
    'D': 54,
    'E': 55,
    'F': 56,
    'G': 57,
    'H': 58,
    'I': 59,
    'J': 60,
    'K': 61,
    'L': 62,
    'M': 63,
    'N': 64,
    'O': 65,
    'P': 66,
    'Q': 67,
    'R': 68,
    'S': 69,
    'T': 70,
    'U': 71,
    'V': 72,
    'W': 73,
    'X': 74,
    'Y': 75,
    'Z': 76,
}

FIGURE_BLOCK = {
    '삼각형': 81,
    '사각형': 82,
    '원': 83,
    '별': 84,
}

USER_BLOCK = {
    # 유치원일 경우 위치가 잘못될 것으로 판단 > 100 이상은 사용자 ID 로 지정 > 150 명까지 가능
    '사용자1': 101,
    '사용자2': 102,
    '사용자3': 103,
    '사용자4': 104,
    '사용자5': 105,
}

# SMART BLOCK ID => 24 bit
# STORY_ID => 23~8 bit
# BLOCK ID => 0~7 bit
STORY_100_BLOCK = {
    '레오': 100 + 256 + 1,
    '아빠사자': 100 + 256 + 2,
    '엄마사자': 100 + 256 + 3,
    '엄마 얼룩말': 100 + 256 + 4,
    '아기 얼룩말': 100 + 256 + 5,
    '기린': 100 + 256 + 6,

    'DIY 01': 100 + 256 + 101,
    'DIY 02': 100 + 256 + 102,
    'DIY 03': 100 + 256 + 103,
    'DIY 04': 100 + 256 + 104,
    'DIY 05': 100 + 256 + 105,
}




def map_display(using_map):
    out = list(using_map.keys())
    #for k in using_map.keys():
    #    out.append(using_map[k])
        #print('{:2} > {}'.format(k, using_map[k]))

    print('map length; {}'.format(len(using_map)))
    return out



import unittest

class MyUnitTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_nothing(self):
        pass


import tkinter as tk
#from Tkinter import *


class App(object):

    def __init__(self):
        self.root = tk.Tk()

        # create a Frame for the Text and Scrollbar
        txt_frm = tk.Frame(self.root, width=600, height=200)
        txt_frm.pack(fill="both", expand=True)
        # ensure a consistent GUI size
        txt_frm.grid_propagate(False)
        # implement stretchability
        txt_frm.grid_rowconfigure(0, weight=1)
        txt_frm.grid_columnconfigure(0, weight=1)

        # create a Text widget
        self.txt = tk.Text(txt_frm, borderwidth=3, relief="sunken")
        self.txt.config(font=("consolas", 12), undo=True, wrap='word')
        self.txt.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)

        # create a Scrollbar and associate it with txt
        scrollb = tk.Scrollbar(txt_frm, command=self.txt.yview)
        scrollb.grid(row=0, column=4, sticky='nsew')
        self.txt['yscrollcommand'] = scrollb.set


        out_txt = tk.Button(text="PRINT...", command=self.print_txt)
        out_txt.pack()
        #delete.grid(row=1, column=0, sticky=tk.NS)

        delete = tk.Button(text="DELETE", command=self.clear_txt)
        delete.pack()
        #delete.grid(row=1, column=0, sticky=tk.NS)

        quit = tk.Button(text="QUIT", fg="red", command=self.root.destroy)
        quit.pack(side="bottom")
        #quit.grid(row=1, column=0)

    def print_txt(self):
        self.txt.insert(0.0, "hi there, everyone!\n")
        self.txt.insert(0.0, "hi there, everyone!\n")
        self.txt.insert(0.0, "hi there, everyone!\n")

    def clear_txt(self):
        #idx = self.print.index(0.0)
        #idx = self.print.get(0.0, 1.0)
        self.txt.delete(0.0, tk.END)


class Application(tk.Frame):
    '''
    lbl = Label(root, text="이름")
    lbl.grid(row=0, column=0)
    txt = Entry(root)
    txt.grid(row=0, column=1)
    btn = Button(root, text="OK", width=15)
    btn.grid(row=1, column=1)
    '''

    def __init__(self, master=None):
        super().__init__(master)
        self.root = master

        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        #self.hi_there["command"] = self.say_hi
        self.hi_there["command"] = lambda: self.say_hi_2(5)
        self.hi_there.pack(side="top")

        self.print = tk.Text(self)
        self.print.pack()

        scr = tk.Scrollbar(self.root, orient=tk.VERTICAL, command=self.print.yview)
        self.print['yscrollcommand'] = scr.set

        self.delete = tk.Button(self, text="DELETE", command=self.clear_print)
        self.delete.pack()

        self.quit = tk.Button(self, text="QUIT", fg="red", command=self.root.destroy)
        self.quit.pack(side="bottom")

    def clear_print(self):
        #idx = self.print.index(0.0)
        #idx = self.print.get(0.0, 1.0)
        self.print.delete(0.0, tk.END)

    def say_hi(self):
        self.print.insert(0.0, "hi there, everyone!\n")

    def say_hi_2(self, num):
        self.print.insert(0.0, "hi there, everyone! {}\n".format(num))

def test_tk_00():
    root = tk.Tk()
    root.geometry("600x500")
    app = Application(master=root)
    app.mainloop()

def test_tk_02():
    app = App()
    app.root.mainloop()

def test_tk_01():
    #from tkinter import *
    root = tk.Tk()

    lbl = tk.Label(root, text="이름")
    lbl.grid(row=0, column=0)
    txt = tk.Entry(root)
    txt.grid(row=0, column=1)
    btn = tk.Button(root, text="OK", width=15)
    btn.grid(row=1, column=1)

    root.mainloop()

def block_displey():

    record = []

    record += map_display(CONTROL_BLOCK)
    record += map_display(EMOTION_BLOCK)
    record += map_display(ALPHABAT_BLOCK)
    record += map_display(FIGURE_BLOCK)
    record += map_display(USER_BLOCK)
    record += map_display(STORY_100_BLOCK)

    col = 6
    #for r in record:
    #    print(r)
    st = 0
    end = col
    while end < len(record):
        print(record[st:end])
        st += col
        end += col

    print(record[st:end])
    #print(record[0:6])
    #print('block length; {}'.format(len(record)))



if __name__ == '__main__':
    t = time.time()

    block_displey()
    #test_tk_01()
    #test_tk_00()
    #test_tk_02()

    #process_time = (timeit.default_timer() - t)    # 신규 CPU 에서 오류는 없는가?
    process_time = (time.time() - t)
    tm = time.localtime()
    if process_time < 100:
        print(__file__, 'Python Elapsed {:.02f} seconds, current time; {:02d}:{:02d}'.format(
            process_time, tm.tm_hour, tm.tm_min))
    else:
        print(__file__, 'Python Elapsed {:.02f} seconds, current time; {:02d}:{:02d}'.format(
            process_time / 60, tm.tm_hour, tm.tm_min))


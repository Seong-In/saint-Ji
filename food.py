from tkinter import *
from tkinter import font
from io import BytesIO
import urllib
import urllib.request
from PIL import Image, ImageTk
import tkinter.messagebox
g_Tk = Tk()
DataList = []
g_Tk.geometry("800x600")




# openapi로 이미지 url을 가져옴.
url = "http://postfiles14.naver.net/20160517_285/mannam013_1463451327005ye90T_JPEG/%BE%C8%BC%BA%C8%DE%B0%D4%BC%D2_%BE%C8%BC%BA%B1%B9%B9%E4_%B9%F6%BC%B8%BA%D2%B0%ED%B1%E21.jpg?type=w773"
with urllib.request.urlopen(url) as u:
    raw_data = u.read()

im = Image.open(BytesIO(raw_data))
image = ImageTk.PhotoImage(im)

label = Label(g_Tk, image=image, height=350, width=400)
label.pack()
label.place(x=400, y=215)




def InitTopText():
    TempFont = font.Font(g_Tk, size=20, weight='bold', family = 'Consolas')
    MainText = Label(g_Tk, font = TempFont, text="[휴게소 대표음식]")
    MainText.pack()
    MainText.place(x=20)


def InitSearchListBox():
    global SearchListBox


    TempFont = font.Font(g_Tk, size=15, weight='bold', family='Consolas')
    SearchListBox = Listbox(g_Tk, font=TempFont, activestyle='none',
                            width=10, height=1, borderwidth=12, relief='ridge')

    SearchListBox.insert(1, "휴게소")

    SearchListBox.pack()
    SearchListBox.place(x=10, y=50)


def InitInputLabel():
    global InputLabel
    TempFont = font.Font(g_Tk, size=15, weight='bold', family = 'Consolas')
    InputLabel = Entry(g_Tk, font = TempFont, width = 26, borderwidth = 12, relief = 'ridge')
    InputLabel.pack()
    InputLabel.place(x=10, y=105)

def InitSearchButton():
    TempFont = font.Font(g_Tk, size=12, weight='bold', family = 'Consolas')
    SearchButton = Button(g_Tk, font = TempFont, text="검색",  command=SearchButtonAction)
    SearchButton.pack()
    SearchButton.place(x=330, y=110)


def SearchButtonAction():
    global SearchListBox

    RenderText.configure(state='normal')
    RenderText.delete(0.0, END)  # ?댁쟾 異쒕젰 ?띿뒪??紐⑤몢 ??젣
    iSearchIndex = SearchListBox.curselection()[0]
    if iSearchIndex == 0:  # ?꾩꽌愿
        SearchLibrary()
    elif iSearchIndex == 1:  # 紐⑤쾾?뚯떇
        pass#SearchGoodFoodService()
    elif iSearchIndex == 2:  # 留덉폆
        pass#SearchMarket()
    elif iSearchIndex == 3:
        pass#SearchCultural()

    RenderText.configure(state='disabled')


def SearchLibrary():
    import http.client
    from xml.dom.minidom import parse, parseString
    conn = http.client.HTTPConnection("data.ex.co.kr")
    conn.request("GET", "/exopenapi/business/representFoodServiceArea?serviceKey=ULx0dmA5vWHvXJ4vC79V9c9i2suuEGqXRJdfniXk4p6%2FV9IooCh7SmChiFUm9zmHn0%2BIrCETAP813RCG1le8Dw%3D%3D&type=xml&numOfRows=10&pageSize=10&pageNo=1&startPage=1")
    req = conn.getresponse()

    global DataList
    DataList.clear()

    if req.status == 200:
        BooksDoc = req.read().decode('utf-8')
        if BooksDoc == None:
            print("에러")
        else:
            parseData = parseString(BooksDoc)
            data = parseData.childNodes
            list = data[0].childNodes

            for item in list:
                if item.nodeName == "list":
                    subitems = item.childNodes

                    if subitems[6].firstChild.nodeValue == InputLabel.get():
                        DataList.append((subitems[0].firstChild.nodeValue, subitems[6].firstChild.nodeValue+"휴게소", subitems[4].firstChild.nodeValue))
                    elif subitems[4].firstChild.nodeValue == InputLabel.get():
                        DataList.append((subitems[0].firstChild.nodeValue, subitems[6].firstChild.nodeValue + "휴게소",subitems[4].firstChild.nodeValue))
                    else:
                        continue

            for i in range(len(DataList)):
                RenderText.insert(INSERT, "대표음식: ")
                RenderText.insert(INSERT, DataList[i][0])
                RenderText.insert(INSERT, "\n")
                RenderText.insert(INSERT, "파는곳: ")
                RenderText.insert(INSERT, DataList[i][1])
                RenderText.insert(INSERT, "\n")
                RenderText.insert(INSERT, "가격: ")
                RenderText.insert(INSERT, DataList[i][2])
                RenderText.insert(INSERT, "\n\n")


def InitRenderText():
    global RenderText

    RenderTextScrollbar = Scrollbar(g_Tk)
    RenderTextScrollbar.pack()
    RenderTextScrollbar.place(x=375, y=200)

    TempFont = font.Font(g_Tk, size=10, family='Consolas')
    RenderText = Text(g_Tk, width=49, height=27, borderwidth=12, relief='ridge', yscrollcommand=RenderTextScrollbar.set)
    RenderText.pack()
    RenderText.place(x=10, y=215)
    RenderTextScrollbar.config(command=RenderText.yview)
    RenderTextScrollbar.pack(side=RIGHT, fill=BOTH)

    RenderText.configure(state='disabled')


InitTopText()
InitSearchListBox()
InitInputLabel()
InitSearchButton()
InitRenderText()
#InitSendEmailButton()
#InitSortListBox()
#InitSortButton()

g_Tk.mainloop()
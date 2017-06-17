from tkinter import *
from tkinter import font
from io import BytesIO
import urllib
import urllib.request
from PIL import Image, ImageTk
import tkinter.messagebox
g_Tk = Tk()
DataList = [1]
g_Tk.geometry("800x700")



def InitTopText():
    TempFont = font.Font(g_Tk, size=20, weight='bold', family = 'Consolas')
    MainText = Label(g_Tk, font = TempFont, text="[휴게소 대표음식]")
    MainText.pack()
    MainText.place(x=250)


def InitSearchListBox():
    global SearchListBox
    ListBoxScrollbar = Scrollbar(g_Tk)
    ListBoxScrollbar.pack()
    ListBoxScrollbar.place(x=150, y=50)

    TempFont = font.Font(g_Tk, size=15, weight='bold', family='Consolas')
    SearchListBox = Listbox(g_Tk, font=TempFont, activestyle='none',
                            width=10, height=1, borderwidth=12, relief='ridge',
                            yscrollcommand=ListBoxScrollbar.set)

    SearchListBox.insert(1, "휴게소1")
    SearchListBox.insert(2, "휴게소2")

    SearchListBox.pack()
    SearchListBox.place(x=10, y=50)
    ListBoxScrollbar.config(command=SearchListBox.yview)


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
    RenderText.delete(0.0, END)

    iSearchIndex = SearchListBox.curselection()[0]
    if iSearchIndex == 0:
        Service()

    elif iSearchIndex == 1:
        TwoService()
    RenderText.configure(state='disabled')



def Service():
    import http.client
    from xml.dom.minidom import parse, parseString
    conn = http.client.HTTPConnection("data.ex.co.kr")
    conn.request("GET", "/exopenapi/business/representFoodServiceArea?serviceKey=ULx0dmA5vWHvXJ4vC79V9c9i2suuEGqXRJdfniXk4p6%2FV9IooCh7SmChiFUm9zmHn0%2BIrCETAP813RCG1le8Dw%3D%3D&type=xml&numOfRows=99&pageSize=99&pageNo=1&startPage=1")
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

                    if subitems[1].firstChild.nodeValue!="0010":
                        if subitems[1].firstChild.nodeValue != "0120":
                            if subitems[1].firstChild.nodeValue != "0150":
                                if subitems[6].firstChild.nodeValue == InputLabel.get():
                                    DataList.append((subitems[0].firstChild.nodeValue, subitems[6].firstChild.nodeValue+"휴게소", subitems[4].firstChild.nodeValue))
                                elif subitems[4].firstChild.nodeValue == InputLabel.get():
                                    DataList.append((subitems[0].firstChild.nodeValue, subitems[6].firstChild.nodeValue + "휴게소",subitems[4].firstChild.nodeValue))
                                else:
                                    continue

            for i in range(len(DataList)):
                RenderText.insert(INSERT,"대표음식:")
                RenderText.insert(INSERT, DataList[i][0])
                RenderText.insert(INSERT,"\n")
                RenderText.insert(INSERT,"파는곳:")
                RenderText.insert(INSERT,DataList[i][1])
                RenderText.insert(INSERT,"\n")
                RenderText.insert(INSERT,"가격:")
                RenderText.insert(INSERT,DataList[i][2])
                RenderText.insert(INSERT,"\n\n\n")



def TwoService():
    import http.client
    from xml.dom.minidom import parse, parseString
    conn = http.client.HTTPConnection("data.ex.co.kr")
    conn.request("GET", "/exopenapi/business/representFoodServiceArea?serviceKey=ULx0dmA5vWHvXJ4vC79V9c9i2suuEGqXRJdfniXk4p6%2FV9IooCh7SmChiFUm9zmHn0%2BIrCETAP813RCG1le8Dw%3D%3D&type=xml&numOfRows=99&pageSize=99&pageNo=2&startPage=1")
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

                    if subitems[1].firstChild.nodeValue!="0300":
                        if subitems[1].firstChild.nodeValue != "0350":
                            if subitems[1].firstChild.nodeValue != "0400":
                                if subitems[1].firstChild.nodeValue != "0450":
                                    if subitems[1].firstChild.nodeValue != "0500":
                                        if subitems[1].firstChild.nodeValue != "0650":
                                            if subitems[1].firstChild.nodeValue != "1000":
                                                if subitems[6].firstChild.nodeValue == InputLabel.get():
                                                    DataList.append((subitems[0].firstChild.nodeValue, subitems[6].firstChild.nodeValue+"휴게소", subitems[4].firstChild.nodeValue))
                                                elif subitems[4].firstChild.nodeValue == InputLabel.get():
                                                    DataList.append((subitems[0].firstChild.nodeValue, subitems[6].firstChild.nodeValue + "휴게소",subitems[4].firstChild.nodeValue))
                                                else:
                                                        continue

            for i in range(len(DataList)):
                RenderText.insert(INSERT, "★★대표음식★★")
                RenderText.insert(INSERT, DataList[i][0])
                RenderText.insert(INSERT, "\n")
                RenderText.insert(INSERT, "파는곳")
                RenderText.insert(INSERT, DataList[i][1])
                RenderText.insert(INSERT, "\n")
                RenderText.insert(INSERT, "가격")
                RenderText.insert(INSERT, DataList[i][2])
                RenderText.insert(INSERT, "\n\n\n")





def InitRenderText():
    global RenderText

    RenderTextScrollbar = Scrollbar(g_Tk)
    RenderTextScrollbar.pack()
    RenderTextScrollbar.place(x=375, y=200)

    TempFont = font.Font(g_Tk, size=10, family='Consolas')
    RenderText = Text(g_Tk,font='helvetica 16 italic',bg="green",fg="white",width=20, height=17, borderwidth=12, relief='ridge', yscrollcommand=RenderTextScrollbar.set)
    RenderText.pack()
    RenderText.place(x=10, y=215)
    RenderTextScrollbar.config(command=RenderText.yview)
    RenderTextScrollbar.pack(side=RIGHT, fill=BOTH)

    RenderText.configure(state='disabled')


def test():
    path=search.get()
    img = PhotoImage(file=path)
    imageLabel.configure(image=img)
    imageLabel.image = img



photo=PhotoImage(file="안성국밥.png")
imageLabel=Label(g_Tk,image=photo)
imageLabel.pack()
imageLabel.place(x=310,y=215)
TempFont = font.Font(g_Tk, size=15, weight='bold', family = 'Consolas')
search = Entry(g_Tk, font = TempFont, width = 20, borderwidth = 12, relief = 'ridge')
search.pack()
search.place(x=450,y=105)

TempFont = font.Font(g_Tk, size=12, weight='bold', family = 'Consolas')
button = Button(g_Tk, text='클릭', command=test,font=TempFont)
button.pack()
button.place(x=700, y=110)

InitTopText()
InitSearchListBox()
InitInputLabel()
InitSearchButton()
InitRenderText()
#InitSendEmailButton()
#InitSortListBox()
#InitSortButton()

g_Tk.mainloop()
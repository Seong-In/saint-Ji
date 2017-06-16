from tkinter import *
from tkinter import font
from io import BytesIO
import urllib
import urllib.request
from PIL import Image, ImageTk
import tkinter.messagebox
g_Tk = Tk()
DataList = [1]
g_Tk.geometry("800x800")



def InitTopText():
    TempFont = font.Font(g_Tk, size=20, weight='bold', family = 'Consolas')
    MainText = Label(g_Tk, font = TempFont, text="[휴게소 대표음식]")
    MainText.pack()
    MainText.place(x=20)


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
    mail()

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
                RenderText.insert(INSERT, "대표음식: ")
                RenderText.insert(INSERT, DataList[i][0])
                RenderText.insert(INSERT, "\n")
                RenderText.insert(INSERT, "파는곳: ")
                RenderText.insert(INSERT, DataList[i][1])
                RenderText.insert(INSERT, "\n")
                RenderText.insert(INSERT, "가격: ")
                RenderText.insert(INSERT, DataList[i][2])
                RenderText.insert(INSERT, "\n\n")


def TwoService():
    import http.client
    from xml.dom.minidom import parse, parseString
    conn = http.client.HTTPConnection("data.ex.co.kr")
    conn.request("GET", "/exopenapi/business/representFoodServiceArea?serviceKey=ULx0dmA5vWHvXJ4vC79V9c9i2suuEGqXRJdfniXk4p6%2FV9IooCh7SmChiFUm9zmHn0%2BIrCETAP813RCG1le8Dw%3D%3D&type=xml&numOfRows=10&pageSize=99&pageNo=2&startPage=1")
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
                RenderText.insert(INSERT, "대표음식: ")
                RenderText.insert(INSERT, DataList[i][0])
                RenderText.insert(INSERT, "\n")
                RenderText.insert(INSERT, "파는곳: ")
                RenderText.insert(INSERT, DataList[i][1])
                RenderText.insert(INSERT, "\n")
                RenderText.insert(INSERT, "가격: ")
                RenderText.insert(INSERT, DataList[i][2])
                RenderText.insert(INSERT, "\n\n")


def mail():
    # -*- coding: cp949 -*-
    import mimetypes
    import smtplib
    from email.mime.base import MIMEBase
    from email.mime.text import MIMEText

    # global value
    host = "smtp.gmail.com"  # Gmail STMP 서버 주소.
    port = "587"
    htmlFileName = "logo.gif"

    senderAddr = "ahstmxj101@gmail.com"  # 보내는 사람 email 주소.
    recipientAddr = "ahstmxj101@naver.com"  # 받는 사람 email 주소.

    msg = MIMEBase("multipart", "alternative")
    msg['Subject'] = "Test email in Python 3.0"
    msg['From'] = senderAddr
    msg['To'] = recipientAddr

    # MIME 문서를 생성합니다.
    htmlFD = Service()
    HtmlPart = MIMEText(htmlFD, 'html', _charset='UTF-8')

    # 만들었던 mime을 MIMEBase에 첨부 시킨다.
    msg.attach(HtmlPart)

    # 메일을 발송한다.
    s = smtplib.SMTP(host, port)
    # s.set_debuglevel(1)        # 디버깅이 필요할 경우 주석을 푼다.
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login("ahstmxj101@gmail.com", "ahstmxj100")
    s.sendmail(senderAddr, [recipientAddr], msg.as_string())
    s.close()


def InitRenderText():
    global RenderText

    RenderTextScrollbar = Scrollbar(g_Tk)
    RenderTextScrollbar.pack()
    RenderTextScrollbar.place(x=375, y=200)

    TempFont = font.Font(g_Tk, size=10, family='Consolas')
    RenderText = Text(g_Tk, width=49, height=40, borderwidth=12, relief='ridge', yscrollcommand=RenderTextScrollbar.set)
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
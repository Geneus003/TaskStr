import datetime
from threading import Thread
from tkinter import *
import time
from PIL import Image, ImageDraw
import tkinter as tk
from PIL import ImageTk
import sqlite3
import os.path

root = Tk()
root.minsize(width=1280, height=720)


checkDB = os.path.isfile('test.db')
checkID = os.path.isfile('taskID.txt')

def taskDBandID():
    if checkDB == True:
        print("hello im DB")
    else:
        taskStrDB = sqlite3.connect('test.db')
        taskStrDB.execute('''CREATE TABLE TASK
            (NAME         TEXT    NOT NULL,
            TEXT           TEXT     NOT NULL,
            ID           INT    NOT NULL);''')
        taskStrDB.close()


    global lastIDTask

    if checkID == True:
        lastIDTaskOpen = open("taskID.txt")
        lastIDTask = lastIDTaskOpen.read()
        lastIDTaskOpen.close()
    else:
        lastIDTaskOpen = open("taskID.txt","w")
        lastIDTaskOpen.write('0')
        lastIDTask = "0"
        lastIDTaskOpen.close()

    lastIDTask = int(lastIDTask)

taskDBandID()



def printit():
    while a == True:
        now = datetime.datetime.now()
        ab = now.strftime("%H:%M")
        print (ab)
        labelTime.configure(text=ab)
        time.sleep(1)


def fromCreateTaskSave(event):

    global lastIDTask

    idtask = lastIDTask + 1
    lastIDTask = lastIDTask + 1

    lastIDTaskStr = str(lastIDTask)

    lastIDTaskOpen = open("taskID.txt", "w")
    lastIDTaskOpen.write(lastIDTaskStr)
    lastIDTaskOpen.close()


    taskStrDB = sqlite3.connect('test.db')


    nameOfTaskCreate = titleEntCreate.get().strip()
    textTextCreate = DescriptionCreateText.get('1.0', END)
    textTextCreate = textTextCreate[0:-1]
    print(nameOfTaskCreate,textTextCreate)
    params = (nameOfTaskCreate,textTextCreate,idtask)

    taskStrDB.execute("INSERT INTO TASk VALUES (?, ?, ?)", params)

    taskStrDB.commit()
    taskStrDB.close()

    labelCreateTask.destroy()
    DescriptionCreateText.destroy()
    DescriptionCreateLabel.destroy()
    titleEntCreate.destroy()
    saveCreateBut.destroy()
    cancelCreateBut.destroy()
    titleCreateLabel.destroy()
    toppart1.destroy()

    TaskStr()


def fromCreateTask(event):


    labelCreateTask.destroy()
    DescriptionCreateText.destroy()
    DescriptionCreateLabel.destroy()
    titleEntCreate.destroy()
    saveCreateBut.destroy()
    cancelCreateBut.destroy()
    titleCreateLabel.destroy()
    toppart1.destroy()

    TaskStr()



def TaskStr():

    def foo(e):
        s = titleEntCreate.get().strip()
        s = s[-1] if s else ''
        titleEntCreate.delete('60', END)


    def createWindow(event):

        for j in range(i):
            arrayTaskCreateLabel[j].destroy()
            arrayTaskDesLabel[j].destroy()

        global titleEntCreate
        global a

        global labelCreateTask
        global DescriptionCreateText
        global DescriptionCreateLabel
        global titleEntCreate
        global saveCreateBut
        global cancelCreateBut
        global titleCreateLabel

        a = False

        root["bg"] = "#FAFAFA"

        labelTime.destroy()
        leftpart1.destroy()
        butTaskstr.destroy()
        butRemoveTop.destroy()
        butCalc.destroy()
        butEditTop.destroy()
        butCreateTop.destroy()

        cancelCreateTaskButImg = ImageTk.PhotoImage(file = "Pictures/TaskStr/cancel.png")
        saveCreateTaskButImg = ImageTk.PhotoImage(file = "Pictures/TaskStr/save.png")


        saveCreateBut = Button(root, text='Create', bg='#f3655d', font='Arial 20', fg='#dbe0e4', bd=0,highlightthickness=0, relief='ridge',image=saveCreateTaskButImg)
        cancelCreateBut = Button(root, text='Create', bg='#f3655d', font='Arial 20', fg='#dbe0e4', bd=0,highlightthickness=0, relief='ridge', image=cancelCreateTaskButImg)
        titleCreateLabel = Label(root, text="Title", font="Arial 30", height=1, width=5, bd=0, fg="#6D6D6D",bg = "#FAFAFA")
        titleEntCreate = Entry(root,font = "arial 28", bd=0,highlightthickness=0, relief='ridge',bg = "#EDEDED",fg = "#545454",width  = 41)
        DescriptionCreateLabel = Label(root, text="Description", font="Arial 30", height=1, width=11, bd=0, fg="#6D6D6D",bg = "#FAFAFA")
        DescriptionCreateText = Text(root,bd=0, bg = "#EDEDED",fg = "#545454",font="Arial 28",width=41,height = 7)
        labelCreateTask = Label(root, text = "Create task",bg = "#ea5048",fg = "#EDEDED", font = "Arial 40")


        saveCreateBut.image = saveCreateTaskButImg
        cancelCreateBut.image = cancelCreateTaskButImg


        labelCreateTask.place(x =500,y = 20)
        DescriptionCreateText.place(x = 198, y = 390)
        DescriptionCreateLabel.place(x = 166, y = 330)
        titleEntCreate.place(x = 198, y = 240)
        saveCreateBut.place(x = 1100,y = 18)
        cancelCreateBut.place(x = 30,y = 18)
        titleCreateLabel.place(x = 175,y = 180)


        titleEntCreate.bind('<KeyRelease>',foo)
        cancelCreateBut.bind('<Button->', fromCreateTask)
        saveCreateBut.bind('<Button->', fromCreateTaskSave)


    def readTask(indextask):

        def readTaskE(event):

            editImgBut = ImageTk.PhotoImage(file="Pictures/TaskStr/edit.png")
            cancelImgBut = ImageTk.PhotoImage(file="Pictures/TaskStr/cancel.png")

            butEditTopRead = Button(root, text='Create', bg='#f3655d', font='Arial 20', fg='#dbe0e4', bd=0,highlightthickness=0, relief='ridge', image=editImgBut)
            butCancelTopRead = Button(root, text='Create', bg='#f3655d', font='Arial 20', fg='#dbe0e4', bd=0, highlightthickness=0,relief='ridge', image=cancelImgBut)

            butCancelTopRead.image = cancelImgBut
            butEditTopRead.image = editImgBut


            def fooo(e):
                s = textWithNameTask.get().strip()
                s = s[-1] if s else ''
                textWithNameTask.delete('60', END)


            root["bg"] = "#FAFAFA"

            j = 0

            for j in range(i):
                arrayTaskCreateLabel[j].destroy()
                arrayTaskDesLabel[j].destroy()

            leftpart1.destroy()
            butTaskstr.destroy()
            butRemoveTop.destroy()
            butCalc.destroy()
            butEditTop.destroy()
            butCreateTop.destroy()


            labelTaskName = Label(root, text="Name:", font="Arial 30", height=1, width=5, bd=0, fg="#6D6D6D",bg = "#FAFAFA")
            labelTaskDes = Label(root,text="Description:", font="Arial 30", height=1, width=11, bd=0, fg="#6D6D6D",bg = "#FAFAFA")

            textWithNameTask = Entry(root,font = "arial 28", bd=0,highlightthickness=0, relief='ridge',bg = "#EDEDED",fg = "#545454",width  = 41)
            textWithNameTask.insert(1, arrayTaskName[indextask])

            textWithDesTask = Text(root,bd=0, bg = "#EDEDED",fg = "#545454",font="Arial 28",width=41,height = 7)
            textWithDesTask.insert(1.0, arrayTaskDes[indextask])

            labelTaskName.place(x=198, y=180)
            labelTaskDes.place(x=172, y=300)
            textWithNameTask.place(x = 198, y = 240)
            textWithDesTask.place(x = 198, y = 360)
            butEditTopRead.place(x=880, y=18)
            butCancelTopRead.place(x=230,y = 18)
            textWithNameTask.bind('<KeyRelease>', fooo)


        return readTaskE

    def BDandLabels():

        global arrayTaskDes
        global arrayTaskName
        global arrayTaskCreateLabel
        global arrayTaskDesLabel
        global i
        global arrayIdTask

        arrayTaskName = []
        arrayTaskDes = []
        arrayTaskCreateLabel = []
        arrayTaskDesLabel = []
        arrayIdTask = []


        i = 0
        for i in range(1000):
            arrayTaskName.append(i)
            arrayTaskDes.append(i)
            arrayTaskCreateLabel.append(i)
            arrayTaskDesLabel.append(i)
            arrayIdTask.append(i)



        taskStrDB = sqlite3.connect('test.db')
        cursorTask = taskStrDB.execute("SELECT name, text, id from TASK")

        i = 0
        for row in cursorTask:
            arrayTaskName[i]= row[0]
            arrayTaskDes[i] = row[1]
            arrayIdTask[i] = row[2]
            i = i + 1

        j = 0
        for j in range(i):
            print (arrayTaskName[j])
            print (arrayTaskDes[j])
            print(arrayIdTask[j])

        taskStrDB.close()

        j = 0
        y1 = 150
        y2 = 213

        for j in  range (i):
            arrayTaskDesLabel[j] = Label(root, text = arrayTaskDes[j], fg = "#767676", font = "Arial 19",width = 46, height = 1,anchor = "nw",pady = 3,padx = 60,bg = "#EEEFF0")
            arrayTaskCreateLabel[j] = Label(root,text = arrayTaskName[j], fg = "#494949", font = "Arial 30",width = 30,anchor = "nw",height = 1,pady = 10,padx = 60,bg = "#EEEFF0" )
            arrayTaskDesLabel[j].bind('<Button->',readTask(j))
            arrayTaskCreateLabel[j].bind('<Button->',readTask(j))
            arrayTaskDesLabel[j].place(x= 300, y= y2)
            arrayTaskCreateLabel[j].place(x=300, y=y1)
            y2 = y2 + 115
            y1 = y1 + 115



    BDandLabels()


    root["bg"] = "#FAFAFA"


    createImgBut = ImageTk.PhotoImage(file="Pictures/TaskStr/create.png")
    editImgBut = ImageTk.PhotoImage(file="Pictures/TaskStr/edit.png")
    removeImgBut = ImageTk.PhotoImage(file="Pictures/TaskStr/remove.png")

    global a
    a = True
    global labelTime
    global toppart1


    leftpart1 = Canvas(root,width=150, height=720, bg='#ea5048', bd=0, highlightthickness=0, relief='ridge')
    toppart1 = Canvas(root,width=1280, height=120, bg='#ea5048', bd=0, highlightthickness=0, relief='ridge')
    butTaskstr = Button(root,text="TaskStr", bg='#f3655d', bd=0, font='Arial 20', height=2, width=9, fg='#dbe0e4')
    butCalc = Button(root,text="Calc", bg='#f3655d', bd=0, font='Arial 20', height=2, width=9, fg='#dbe0e4')
    butCreateTop = Button(root,text='Create', bg='#f3655d', font='Arial 20', fg='#dbe0e4', bd=0,highlightthickness=0, relief='ridge',image = createImgBut)
    butEditTop = Button(root,text='Edit', bg='#f3655d', font='Arial 20', fg='#dbe0e4', bd=0,highlightthickness=0, relief='ridge',image = editImgBut)
    butRemoveTop = Button(root,text='Remove', bg='#f3655d', font='Arial 20', fg='#dbe0e4', bd=0,image =  removeImgBut,highlightthickness=0, relief='ridge' )
    labelTime = Label(root, text="19:34", font="Arial 40", height=1, width=5, bd=0, bg='#ea5048', fg="white")

    butCreateTop.image = createImgBut
    butEditTop.image = editImgBut
    butRemoveTop.image = removeImgBut


    Timing = Thread(target=printit)
    Timing.start()

    labelTime.place(x=0, y=30)
    butRemoveTop.place(x=640, y=18)
    butEditTop.place(x=930, y=18)
    butCreateTop.place(x=350, y=18)
    butTaskstr.place(x=0, y=150)
    butCalc.place(x=0, y=237)
    leftpart1.place(x=0, y=0)
    toppart1.place(x=0, y=0)

    butCreateTop.bind('<Button->', createWindow)

    root.mainloop()

    a = False


TaskStr()
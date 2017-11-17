import sqlite3

def createDB():
    taskStrDB = sqlite3.connect('test.db')
    taskStrDB.execute('''CREATE TABLE TASK
                (NAME         TEXT    NOT NULL,
                TEXT           TEXT     NOT NULL,
                ID           INT    NOT NULL);''')
    taskStrDB.close()


def createID():
    lastIDTaskOpen = open("taskID.txt", "w")
    lastIDTaskOpen.write('0')
    lastIDTask = "0"
    lastIDTaskOpen.close()

    return (lastIDTask)


def WhatsID():
    lastIDTaskOpen = open("taskID.txt")
    lastIDTask = lastIDTaskOpen.read()
    lastIDTaskOpen.close()

    return (lastIDTask)


def fromCreateTaskSave(lastIDTask , nameOfTaskCreate , textTextCreate):

    idtask = lastIDTask + 1
    lastIDTask = lastIDTask + 1

    lastIDTaskStr = str(lastIDTask)

    lastIDTaskOpen = open("taskID.txt", "w")
    lastIDTaskOpen.write(lastIDTaskStr)
    lastIDTaskOpen.close()

    taskStrDB = sqlite3.connect('test.db')

    params = (nameOfTaskCreate, textTextCreate, idtask)

    taskStrDB.execute("INSERT INTO TASk VALUES (?, ?, ?)", params)

    taskStrDB.commit()
    taskStrDB.close()


def fromReadTaskEdit(paramsDes,paramsName):
    taskStrDB = sqlite3.connect('test.db')

    taskStrDB.execute("UPDATE TASK set NAME = ? where ID= ?", paramsName)
    taskStrDB.execute("UPDATE TASK set TEXT = ? where ID= ?", paramsDes)

    taskStrDB.commit()
    taskStrDB.close()

def fillArr(i,arrayTaskName,arrayTaskDes,arrayIdTask):
    taskStrDB = sqlite3.connect('test.db')
    cursorTask = taskStrDB.execute("SELECT name, text, id from TASK")

    i = 0
    for row in cursorTask:
        arrayTaskName[i] = row[0]
        arrayTaskDes[i] = row[1]
        arrayIdTask[i] = row[2]
        i += 1

    taskStrDB.close()

    return(i,arrayTaskName,arrayTaskDes,arrayIdTask)
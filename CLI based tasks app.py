tasks = []
count = 0
try:
    with open('tasks.txt') as r:
        data = r.readline()

        while data != '':
            tasks.append(data)
            count += 1
            data = r.readline()

except:
    print('Starting with an empty file')
    print('----------------------------------------------')

num = 0

def Add():
    with open('tasks.txt', 'a') as f:
        task = input('Enter the task : ')
        checkBox = '[ ]'
        taskWithBox = checkBox + ' ' + task + '\n'
        f.writelines(taskWithBox)
        tasks.append(taskWithBox)

def View():
    for line in tasks:
        print(line, end='')

def MarkDone():
    taskNum = int(input('Enter which task number needs to be checked starting from 1 : '))
    taskNum = taskNum - 1

    strin = tasks[taskNum]
    strin = strin[4:]  # Remove old checkbox
    newTask = '[X] ' + strin

    tasks[taskNum] = newTask

    with open('tasks.txt', 'w') as f:
        for data in tasks:
            f.writelines(data)

def Delete():
    taskNum = int(input('Enter the task number you want to delete :'))
    taskNum = taskNum - 1

    tasks.pop(taskNum)

    with open('tasks.txt', 'w') as f:
        for data in tasks:
            f.writelines(data)

while num != 5:
    print('**** MENU ****\n\nPress 1 to Add : ')
    print('Press 2 to View : ')
    print('Press 3 to mark a task : ')
    print('Press 4 to delete a task : ')
    print('Press 5 to exit : \n')

    flag = True

    while flag:
        num = int(input('Enter your choice : '))
        if num >= 1 and num <= 5:
            flag = False

    if num == 1:
        Add()
    elif num == 2:
        View()
    elif num == 3:
        MarkDone()
    elif num == 4:
        Delete()

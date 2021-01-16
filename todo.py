# Author Om Rawal
# 01/01/2021
# 10:23:35


import sys
import os
from datetime import datetime

def help(): # print help
    k='Usage :-\n$ ./todo add "todo item"  # Add a new todo\n$ ./todo ls               # Show remaining todos\n$ ./todo del NUMBER       # Delete a todo\n$ ./todo done NUMBER      # Complete a todo\n$ ./todo help             # Show usage\n$ ./todo report           # Statistics'
    sys.stdout.buffer.write(k.encode('utf8'))


def add(a):  # add new task
    todo=open('todo.txt','a') #open file in append mode
    a+='\n'                 # to store one task per line
    todo.write(a)
    todo.close()
    pass

def printToDo(alst): # prints the todo in required format
    n=len(alst)-1
    while(n>=0):
        k='[{}] {}'.format(n+1,alst[n])
        sys.stdout.buffer.write(k.encode('utf8'))
        n-=1
    pass

def listTodos(): #create a list all pending todos
    if(os.path.exists('todo.txt')):
        todo=open('todo.txt','r')
        task_list=[]
        for i in todo:
            task_list.append(i)
        if(len(task_list)==0):
            print('There are no pending todos!')
        else:
            printToDo(task_list)
        todo.close()
    else:
        print('There are no pending todos!')
    pass

def deleteTodo(n):     #remove a todo
    if(os.path.exists('todo.txt')):
        todo=open('todo.txt','r+')
        task_list=[]
        for i in todo:
            task_list.append(i)
        if(len(task_list)>=n and n>0):
            task_list.remove(task_list[n-1])
            todo.close()
            todo=open('todo.txt','w')
            todo.write('')
            todo.close()
            todo=open('todo.txt','a')
            for i in task_list:
                todo.write(i)
            todo.close()
            print('Deleted todo #{}'.format(n))
        else: # illegal NUMBER parameter can be 0 or more than the lenghth of list of todos
            todo.close()
            print('Error: todo #{} does not exist. Nothing deleted.'.format(n))
    else:   # file doesnt exist implies deletion tried before add command
        print('Error: todo #{} does not exist. Nothing deleted.'.format(n))
    pass

def markAsComplete(n): # marking as done we first extract it in a variable 'doneTodo' than delete everything from file and rewrite file without doneTodo
    todo=open('todo.txt','r+')
    task_list=[]
    for i in todo:
        task_list.append(i)
    if(len(task_list)>=n and n>0):
        doneTodo=task_list[n-1]
        task_list.remove(task_list[n-1])
        todo.close()
        todo=open('todo.txt','w')
        todo.write('')
        todo.close()
        todo=open('todo.txt','a')
        for i in task_list:
            todo.write(i)
        todo.close()
        done=open('done.txt','a')
        k='x '+datetime.today().strftime('%Y-%m-%d')+' '
        done.write(k+doneTodo)
        done.close()
        print('Marked todo #{} as done.'.format(n))
    else:
        todo.close()
        print('Error: todo #{} does not exist.'.format(n))

def getReport():    # as we have stored tasks in single line we just need to count the number of lines in both files
    todo=open('todo.txt','r')
    done=open('done.txt','r')
    todoCount=0
    doneCount=0
    for _ in todo:
        todoCount+=1
    for _ in done:
        doneCount+=1
    todo.close()
    done.close()
    print('{} Pending : {} Completed : {}'.format(datetime.today().strftime('%Y-%m-%d'),todoCount,doneCount))



########### START OF DRIVER CODE

if(len(sys.argv)<2 or sys.argv[1]=='help'): # when no arguments or help as argument
    help()


elif(sys.argv[1]=='ls'):
    listTodos()


elif(sys.argv[1]=='report'):
    getReport()


elif(sys.argv[1]=='add'):

    if(len(sys.argv)==2): # When only one argument is passed
        print('Error: Missing todo string. Nothing added!')

    else:
        add(sys.argv[2]) 
        print('Added todo: "{}"'.format(sys.argv[2]))


elif(sys.argv[1]=='del'):

    if(len(sys.argv)==2): # When only one argument is passed
        print('Error: Missing NUMBER for deleting todo.')

    else:
        deleteTodo(int(sys.argv[2]))


elif(sys.argv[1]=='done'):

    if(len(sys.argv)==2): # When only one argument is passed
        print('Error: Missing NUMBER for marking todo as done.')

    else:
        markAsComplete(int(sys.argv[2]))

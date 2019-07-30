import geocoder
import os.path
from tkinter import *

listOfLogs = []
listOfAll = {}
listOfCounts = {}


def choose_file():
    selector = listbox1.curselection()
    label1 = Label(text=f"{listOfLogs[selector[0]]}", fg="#eee", bg="#333")
    label1.grid(row=2, column=0, pady=10, padx=10)
    input_file(listOfLogs[selector[0]])


def input_file(current_file):
    if os.path.exists(current_file):
        with open(current_file) as file_handler:
            for line in file_handler:
                if 'You are not' in line:
                    nick = line[(line.find('name=') + 5):]
                    nick = nick[:(nick.find(','))]
                    ip = line[(line.find('(/')) + 2:]
                    ip = ip[:(ip.find(':'))]
                    if nick in listOfAll:
                        listOfCounts[nick] += 1
                    else:
                        listOfCounts[nick] = 0
                    listOfAll[nick] = ip        


def players_list():
    for key in listOfAll:
        g = geocoder.ipinfo(listOfAll[key])
        words = ('%-20s %-5s | %15s | %-60s' % (key, listOfCounts[key], listOfAll[key], g.address)) + '\n'
        textbox2.configure(state='normal')
        textbox2.insert(INSERT, f"{words}")
        textbox2.configure(state='disabled')


for each in os.listdir():
    if 'log' in each:
        listOfLogs.append(each)

root = Tk()
root.title('Окно приветствия')
root.resizable(width=True, height=True)

listbox1 = Listbox(root, selectmode=SINGLE)
for i in listOfLogs:
    listbox1.insert(END, i)
listbox1.grid(row=0, column=0, columnspan=1, sticky=N, pady=20, padx= 20)

textbox2 = Text(root, width=100, state= DISABLED)
textbox2.grid(row=0, column=2, rowspan=4, pady=20, padx=20)
add_button = Button(text="Подтвердить выбор файла", command=choose_file)
add_button.grid(row=1, column=0, pady=20, padx=20)
list_button = Button(text='Generate list', command=players_list, width=20)
list_button.grid(row=3, column=0, pady=10, padx=10)
exit_button = Button(text='Exit', command=root.destroy, width=20)
exit_button.grid(row=4, column=0, pady=10, padx=10)


root.mainloop()




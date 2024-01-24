from tkinter import *

window = Tk()
window.title("Rechner")

Zaehler = 0
fertig = 0
zeile = 1
spalte = 0
Zeichen = ['1','2','3','+','-','4','5','6','*','/','7','8','9','↑','C',',','0','←','DEL','→','^','(',')','↓','%','V','e','π']
altetext = ['']
alterechnung =['']
Loesungen = ''
back = 0
Rechnung = '|'
multiplier = ['1','2','3','4','5','6','7','8','9','0',')']
#Funktionen
def eingabe(i, Loesungen):
    Eingabe = Zeichen[i]
    Strichpos = label["text"].find('|')
    Strichposi = Strichpos + 1
    global back
    global Rechnung
    Rstrichpos = Rechnung.find('|')
    global altetext
    global altetext
    global multiplier
    if Eingabe == '↑':
        back = back
    elif Eingabe == '↓':
        back = back
    else:
        back = 0
    if label["text"] == 'Syntax-Fehler':
        label["text"] = ''
        Rechnung = ''
    else:
        label["text"] = label["text"]
    if Eingabe == 'C':
        label["text"] = ''
        Rechnung = ''
    elif Eingabe == ',':
        Rechnung = Rechnung[:Rstrichpos] + '.' + Rechnung[Rstrichpos:]
        Eingabe = label["text"][:Strichpos] + Eingabe + label["text"][Strichpos:]
        label["text"] = Eingabe
    elif Eingabe == '^':
        if Rechnung[Rstrichpos - 1] in multiplier:
            Rechnung = Rechnung[:Rstrichpos] + '**' + Rechnung[Rstrichpos:]
            Rstrichpos += 1
        else:
            Rechnung = Rechnung[:Rstrichpos] + '*' + Rechnung[Rstrichpos:]
        Eingabe = label["text"][:Strichpos] + Eingabe + label["text"][Strichpos:]
        label["text"] = Eingabe
    elif Eingabe == '(':
        try:
            if Rechnung[Rstrichpos - 1] in multiplier:
                Rechnung = Rechnung[:Rstrichpos] + '*(' + Rechnung[Rstrichpos:]
                Rstrichpos += 1
            else:
                Rechnung = Rechnung[:Rstrichpos] + '(' + Rechnung[Rstrichpos:]
        except:
            Rechnung = Rechnung[:Rstrichpos] + '(' + Rechnung[Rstrichpos:]
        Eingabe = label["text"][:Strichpos] + Eingabe + label["text"][Strichpos:]
        label["text"] = Eingabe
    elif Eingabe == 'π':
        if Rechnung[Rstrichpos - 1] in multiplier:
            Rechnung = Rechnung[:Rstrichpos] + '*3.14159265359' + Rechnung[Rstrichpos:]
            Rstrichpos += 13
        else:
            Rechnung = Rechnung[:Rstrichpos] + '3.14159265359' + Rechnung[Rstrichpos:]
            Rstrichpos += 12
        Eingabe = label["text"][:Strichpos] + Eingabe + label["text"][Strichpos:]
        label["text"] = Eingabe
    elif Eingabe == 'e':
        if Rechnung[Rstrichpos - 1] in multiplier:
            Rechnung = Rechnung[:Rstrichpos] + '*2.71828182846' + Rechnung[Rstrichpos:]
            Rstrichpos += 13
        else:
            Rechnung = Rechnung[:Rstrichpos] + '2.71828182846' + Rechnung[Rstrichpos:]
            Rstrichpos += 12
        Eingabe = label["text"][:Strichpos] + Eingabe + label["text"][Strichpos:]
        label["text"] = Eingabe
    elif Eingabe == 'DEL':
        label["text"] = label["text"]
    elif Eingabe == '↑':
        if back > len(altetext):
            back = len(altetext)
        try:
            back = back + 1
            label["text"] = altetext[- back]
            Rechnung = alterechnung[- back]
        except:
            label["text"] = label["text"]
            Rechnung = Rechnung
    elif Eingabe == '↓':
        if back <= 0:
            back = 0
        try:
            back = back - 1
            label["text"] = altetext[- back]
            Rechnung = alterechnung[- back]
        except:
            label["text"] = label["text"]
            Rechnung = Rechnung
    elif Eingabe == '←':
        label["text"] = label["text"]
    elif Eingabe == '→':
        label["text"] = label["text"]
    else:
        Rechnung = Rechnung[:Rstrichpos] + Eingabe + Rechnung[Rstrichpos:]
        Eingabe = label["text"][:Strichpos] + Eingabe + label["text"][Strichpos:]
        label["text"] = Eingabe

    if Eingabe == '←':
        if label["text"][Strichpos - 1] == 'π':
            Strichpos = Strichpos - 1
            Rstrichpos = Rstrichpos -13
            if label["text"][Strichpos - 1] != Rechnung[Rstrichpos - 1]:
                Rstrichpos = Rstrichpos - 1
        elif label["text"][Strichpos - 1] == 'e':
            Strichpos = Strichpos - 1
            Rstrichpos = Rstrichpos -13
            if label["text"][Strichpos - 1] != Rechnung[Rstrichpos - 1]:
                Rstrichpos = Rstrichpos - 1
        elif label["text"][Strichpos - 1] == '(':
            Strichpos = Strichpos - 1
            Rstrichpos = Rstrichpos -1
            if label["text"][Strichpos - 1] != Rechnung[Rstrichpos - 1]:
                Rstrichpos = Rstrichpos - 1
        elif label["text"][Strichpos - 1] == '^':
            Strichpos = Strichpos - 1
            Rstrichpos = Rstrichpos -1
            if label["text"][Strichpos - 1] != Rechnung[Rstrichpos - 1]:
                Rstrichpos = Rstrichpos - 1
        else:
            Strichpos = Strichpos - 1
            Rstrichpos = Rstrichpos - 1
        label["text"] = label["text"].replace('|', '')
        label["text"] = label["text"][:Strichpos] + '|' + label["text"][Strichpos:]
        Rechnung = Rechnung.replace('|', '')
        Rechnung = Rechnung[:Rstrichpos] + '|' + Rechnung[Rstrichpos:]
    elif Eingabe == '→':
        if label["text"][Strichpos + 1] == 'π':
            Strichpos = Strichpos + 1
            Rstrichpos = Rstrichpos +13
            if label["text"][Strichpos + 1] != Rechnung[Rstrichpos + 1]:
                Rstrichpos = Rstrichpos + 1
        elif label["text"][Strichpos + 1] == 'e':
            Strichpos = Strichpos + 1
            Rstrichpos = Rstrichpos +13
            if label["text"][Strichpos + 1] != Rechnung[Rstrichpos + 1]:
                Rstrichpos = Rstrichpos + 1
        elif label["text"][Strichpos + 1] == '(':
            Strichpos = Strichpos + 1
            Rstrichpos = Rstrichpos +1
            if label["text"][Strichpos + 1] != Rechnung[Rstrichpos + 1]:
                Rstrichpos = Rstrichpos + 1
        elif label["text"][Strichpos + 1] == '^':
            Strichpos = Strichpos + 1
            Rstrichpos = Rstrichpos +1
            if label["text"][Strichpos + 1] != Rechnung[Rstrichpos + 1]:
                Rstrichpos = Rstrichpos + 1
        else:
            Strichpos = Strichpos + 1
            Rstrichpos = Rstrichpos + 1
        label["text"] = label["text"].replace('|', '')
        label["text"] = label["text"][:Strichpos] + '|' + label["text"][Strichpos:]
        Rechnung = Rechnung.replace('|', '')
        Rechnung = Rechnung[:Rstrichpos] + '|' + Rechnung[Rstrichpos:]
    elif Eingabe == 'DEL':
        if label["text"][Strichpos - 1] == 'π':
            Rechnung = Rechnung[:Rstrichpos][:-13] + Rechnung[Rstrichpos:]
            label["text"] = label["text"][:Strichpos][:-1] + label["text"][Strichpos:]
            Strichpos = Strichpos - 1
            Rstrichpos = Rstrichpos -13
            if label["text"][Strichpos - 1] != Rechnung[Rstrichpos - 1]:
                Rechnung = Rechnung[:Rstrichpos][:-1] + Rechnung[Rstrichpos:]
                Rstrichpos = Rstrichpos - 1
                print('pi')
        elif label["text"][Strichpos - 1] == 'e':
            Rechnung = Rechnung[:Rstrichpos][:-13] + Rechnung[Rstrichpos:]
            label["text"] = label["text"][:Strichpos][:-1] + label["text"][Strichpos:]
            Strichpos = Strichpos - 1
            Rstrichpos = Rstrichpos -13
            if label["text"][Strichpos - 1] != Rechnung[Rstrichpos - 1]:
                Rechnung = Rechnung[:Rstrichpos][:-1] + Rechnung[Rstrichpos:]
                Rstrichpos = Rstrichpos - 1
                print('e')
        elif label["text"][Strichpos - 1] == '(':
            Rechnung = Rechnung[:Rstrichpos][:-1] + Rechnung[Rstrichpos:]
            label["text"] = label["text"][:Strichpos][:-1] + label["text"][Strichpos:]
            Strichpos = Strichpos - 1
            Rstrichpos = Rstrichpos -1
            if label["text"][Strichpos - 1] != Rechnung[Rstrichpos - 1]:
                Rechnung = Rechnung[:Rstrichpos][:-1] + Rechnung[Rstrichpos:]
                Rstrichpos = Rstrichpos - 1
        elif label["text"][Strichpos - 1] == '^':
            Rechnung = Rechnung[:Rstrichpos][:-1] + Rechnung[Rstrichpos:]
            label["text"] = label["text"][:Strichpos][:-1] + label["text"][Strichpos:]
            Strichpos = Strichpos - 1
            Rstrichpos = Rstrichpos -1
            if label["text"][Strichpos - 1] != Rechnung[Rstrichpos - 1]:
                Rechnung = Rechnung[:Rstrichpos][:-1] + Rechnung[Rstrichpos:]
                Rstrichpos = Rstrichpos - 1
        else:
            Rechnung = Rechnung[:Rstrichpos][:-1] + Rechnung[Rstrichpos:]
            label["text"] = label["text"][:Strichpos][:-1] + label["text"][Strichpos:]
            Strichpos = Strichpos - 1
            Rstrichpos = Rstrichpos -1
        if label["text"][Strichpos - 1] == '^':
            if Rechnung[Rstrichpos - 2] == '*':
                label["text"] = label["text"]
            else:
                Rechnung = Rechnung[:Rstrichpos - 1] + '*' + Rechnung[Rstrichpos - 1:]
    else:
        label["text"] = label["text"].replace('|', '')
        label["text"] = label["text"][:Strichposi] + '|' + label["text"][Strichposi:]
        Rechnung = Rechnung.replace('|', '')
        Rechnung = Rechnung[:Rstrichpos + 1] + '|' + Rechnung[Rstrichpos + 1:]
    print(Rechnung)

def ende(Loesungen):
    global altetext
    global alterechnung
    global Rechnung
    if label["text"] == 'Syntax-Fehler':
        label["text"] = label["text"]
    else:
        Rechnung = Rechnung.replace('|','')
        label["text"] = label["text"].replace('|', '')
        alterechnung.append(Rechnung)
        altetext.append(label["text"])
        try:
            Loesungenint = eval(Rechnung)
            Loesungen = str(Loesungenint)
            label["text"] = ''
            for i in range(len(Loesungen)):
                Loesung = Loesungen[i]
                Loesung = label["text"] + Loesung
                label["text"] = Loesung
                Rechnung = Loesung
            label["text"] = label["text"] + '|'
            Rechnung = Rechnung + '|'
        except:
            label["text"] = 'Syntax-Fehler'
            Rechnung = ''
        if label["text"][0] == '(':
            label["text"] = 'Syntax-Fehler'
            Rechnung = ''
        else:
            label["text"] = label["text"]
        print(altetext)
#Label
label = Label(
        text='|' ,
    borderwidth=0,
    relief="flat",
    width=62,
    height=5,
    bg="white",
    fg="black",
    font=('arial',15)
)
label.grid(row=0, column=0, columnspan=5, padx="0.1", pady="0.1")
#Button
btn = []
for i in range(len(Zeichen)):
    if spalte == 5:
        spalte = 0
        zeile += 1
    btn.append(Button(
            text=Zeichen[Zaehler],
            borderwidth=0,
            relief="flat",
            width=10,
            height=5,
            bg="black",
            fg="white",
            font=('arial',15),
            command =lambda i=i: eingabe(i, Loesungen)
    ))   
    btn[i].grid(row=zeile, column=spalte, padx="0.1", pady="0.1")
    Zaehler += 1
    spalte += 1
    if spalte == 5:
        spalte = 0
        zeile += 1
    weite = 5 - spalte
# = zeichen
equalbtn = Button(
        text='=',
        borderwidth=0,
        relief="flat",
        width=11 * weite,
        height=5,
        bg="black",
        fg="white",
        font=('arial',15),
        command = lambda: ende(Loesungen)
)
equalbtn.grid(row=zeile, column=spalte, columnspan=5, padx="0.1", pady="0.1")

window.mainloop()

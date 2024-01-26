from tkinter import *

window = Tk()
window.title("Rechner")

filler = 0
Zaehler = 0
fertig = 0
zeile = 1
spalte = 0
Zeichen = ['1','2','3','+','-','4','5','6','*','/','7','8','9','↑','C',',','0','←','DEL','→','xʸ','(',')','↓','%','ˣ√y','e','π']
altetext = ['']
alterechnung =['']
Loesungen = ''
back = 0
Rstrichpos = 0
Strichpos = 0
Eingabe = ''
Rechnung = '_'
multiplier = ['1','2','3','4','5','6','7','8','9','0',')','(']
Anzeige = ['1','2','3','4','5','6','7','8','9','0',')','+','-','*','/','xʸ','(','e', 'π']
RZeichen = ['*','/','xʸ']
Pfeile = ['↑','←','→','↓']
Rechenzeichen = ['+','-','*','/','^','(',')']
Besonders = ['π','e']
ZZeichen = ['+','-','/','*','^','(','']
MZeichen = ['xʸ', 'e', 'π', '(', 'ˣ√y']
#ˣ√y
#Funktionen
def maldavor():
    mal = 0
    besonders = 0
    plus = 0
    Pluszeichen = ''
    global Besonders
    global Rechnung
    global Rstrichpos
    global Strichpos
    global multiplier
    global Eingabe
    global filler
    Reingabe = Eingabe
    try:
        if Rechnung[Rstrichpos - 1] in multiplier:
            mal = 1
        else:
            mal = 0
    except:
        filler = filler
    if Eingabe in Besonders:
        besonders = 13
        plus = 1
        if Eingabe == 'e':
            Reingabe = '2.71828182846+'
        else:
            Reingabe = '3.14159265359+'
    elif Eingabe == 'xʸ':
        Reingabe = '{x**{y}}'
        Eingabe = '{x^{y}}'
    elif Eingabe == 'ˣ√y':
        print('jo')
        Reingabe = '[y√[x]]'
        Eingabe = '[y√[x]]'
    else:
        print('no')
        Reingabe = Eingabe
    if plus == 1:
        Pluszeichen = '+'
    else:
        Pluszeichen = ''
    if mal == 1:
        malzeichen = '*'
    else:
        malzeichen = ''
        Rechnung = Rechnung[:Rstrichpos] + malzeichen + Reingabe + Rechnung[Rstrichpos:]
        Eingabe = label["text"][:Strichpos] + Eingabe + Pluszeichen + label["text"][Strichpos:]
        label["text"] = Eingabe
        Rstrichpos += mal + besonders
        Strichpos += plus

def ersetzen():
    global Rechnung
    xy = ['x', 'y']
    global Rstrichpos
    global Strichpos
    global RZeichen
    global Eingabe
    global filler
    malzeichen = ['*','/','^']
    if label["text"][Strichpos - 1] in xy:
        Rechnung = Rechnung[:Rstrichpos][:-1] + Rechnung[Rstrichpos:]
        label["text"] = label["text"][:Strichpos][:-1] + label["text"][Strichpos:]
        Rstrichpos -= 1
        Strichpos = Strichpos - 1
    elif label["text"][Strichpos - 1] in RZeichen:
        if Eingabe in malzeichen:
            altesvorzeichen = label["text"][Strichpos - 1]
            Rechnung = Rechnung[:Rstrichpos][:-1] + Rechnung[Rstrichpos:]
            label["text"] = label["text"][:Strichpos][:-1] + label["text"][Strichpos:]
            Rstrichpos -= 1
            Strichpos = Strichpos - 1
            check = 1
            if altesvorzeichen == '^':
                Rechnung = Rechnung.replace('*','',Rstrichpos)
                Rstrichpos = Rstrichpos - 1

def bewegen():
    global Rechnung
    global Rstrichpos
    global Strichpos
    global RZeichen
    global Eingabe
    global filler
    check = 1
    klammern = ['(','{','[']
    BZeichen = ['π','e','(','{','[','^']
    anderesBZeichen =['π','e']
    if Eingabe == '←':
        if label["text"][Strichpos - 1] in BZeichen:
            if label["text"][Strichpos - 1] in anderesBZeichen:
                Strichpos = Strichpos - 1
                Rstrichpos = Rstrichpos -13
            elif label["text"][Strichpos - 1] in klammern:
                Strichpos = Strichpos - 1
                Rstrichpos = Rstrichpos -1
                if label["text"][Strichpos - 1] == '^':
                    check = 0
            else:
                Strichpos = Strichpos - 1
                Rstrichpos = Rstrichpos -1
            if check == 1:
                if label["text"][Strichpos - 1] != Rechnung[Rstrichpos - 1]:
                    Rstrichpos = Rstrichpos - 1
        else:
            Strichpos = Strichpos - 1
            Rstrichpos = Rstrichpos - 1
        label["text"] = label["text"].replace('_', '')
        label["text"] = label["text"][:Strichpos] + '_' + label["text"][Strichpos:]
        Rechnung = Rechnung.replace('_', '')
        Rechnung = Rechnung[:Rstrichpos] + '_' + Rechnung[Rstrichpos:]
    if Eingabe == '→':
        if label["text"][Strichpos + 1] in BZeichen:
            if label["text"][Strichpos + 1] in anderesBZeichen:
                Strichpos = Strichpos + 1
                Rstrichpos = Rstrichpos + 13
            else:
                Strichpos = Strichpos + 1
                Rstrichpos = Rstrichpos + 1
            if label["text"][Strichpos + 1] != Rechnung[Rstrichpos + 1]:
                Rstrichpos = Rstrichpos + 1
        else:
            Strichpos = Strichpos + 1
            Rstrichpos = Rstrichpos + 1
        label["text"] = label["text"].replace('_', '')
        label["text"] = label["text"][:Strichpos] + '_' + label["text"][Strichpos:]
        Rechnung = Rechnung.replace('_', '')
        Rechnung = Rechnung[:Rstrichpos] + '_' + Rechnung[Rstrichpos:]

def delete():
    global Rechnung
    global Rstrichpos
    global Strichpos
    global RZeichen
    global Eingabe
    global filler
    global checki
    checki = 0
    check = 1
    Klammern = ['{','[',']','}']
    BZeichen = ['π','e']
    anderesBZeichen =['(','^']
    if label["text"][Strichpos - 1] in Klammern:
        filler = filler
    else:
        if label["text"][Strichpos - 1] in BZeichen:
            Rechnung = Rechnung[:Rstrichpos][:-13] + Rechnung[Rstrichpos:]
            label["text"] = label["text"][:Strichpos][:-1] + label["text"][Strichpos:]
            Strichpos = Strichpos - 1
            Rstrichpos = Rstrichpos -13
        elif label["text"][Strichpos - 1] == '(':
            Rechnung = Rechnung[:Rstrichpos][:-1] + Rechnung[Rstrichpos:]
            label["text"] = label["text"][:Strichpos][:-1] + label["text"][Strichpos:]
            Strichpos = Strichpos - 1
            Rstrichpos = Rstrichpos -1
        elif label["text"][Strichpos - 1] == '^':
            klammerdel()
        elif label["text"][Strichpos - 1] == '√':
            klammerdel()
        else:
            Rechnung = Rechnung[:Rstrichpos][:-1] + Rechnung[Rstrichpos:]
            label["text"] = label["text"][:Strichpos][:-1] + label["text"][Strichpos:]
            Strichpos = Strichpos - 1
            Rstrichpos = Rstrichpos -1
        if checki == 0:
            if label["text"][Strichpos - 1] != Rechnung[Rstrichpos - 1]:
                        Rechnung = Rechnung[:Rstrichpos][:-1] + Rechnung[Rstrichpos:]
                        Rstrichpos = Rstrichpos - 1
            if label["text"][Strichpos - 1] == '^':
                if Rechnung[Rstrichpos - 2] == '*':
                    filler = filler
                else:
                    Rechnung = Rechnung[:Rstrichpos - 1] + '*' + Rechnung[Rstrichpos - 1:]
def klammerdel():
    global Rechnung
    global Rstrichpos
    global Strichpos
    global RZeichen
    global Eingabe
    global filler
    global checki
    global Klammerauf
    global Klammerzu
    checkauf1 = 0
    checkzu1 = 0
    i = 0
    if label["text"][Strichpos - 1] == '^':
        Klammerauf = '{'
        Klammerzu = '}'
        label["text"] = label["text"][:Strichpos][:-1] + label["text"][Strichpos:]
        label["text"] = label["text"][:Strichpos + 1][:-1] + label["text"][Strichpos + 1:]
        Rechnung = Rechnung[:Rstrichpos][:-2] + Rechnung[Rstrichpos:]
        Rechnung = Rechnung[:Rstrichpos][:-1] + Rechnung[Rstrichpos:]
        final_klammerdel()
    elif label["text"][Strichpos - 1] == '√':
        Klammerauf = '['
        Klammerzu = ']'
        label["text"] = label["text"][:Strichpos][:-1] + label["text"][Strichpos:]
        label["text"] = label["text"][:Strichpos + 1][:-1] + label["text"][Strichpos + 1:]
        Rechnung = Rechnung[:Rstrichpos][:-1] + Rechnung[Rstrichpos:]
        Rechnung = Rechnung[:Rstrichpos + 1][:-1] + Rechnung[Rstrichpos + 1:]
        final_klammerdel()
def final_klammerdel():
    global Rechnung
    global Rstrichpos
    global Strichpos
    global RZeichen
    global Eingabe
    global filler
    global checki
    global Klammerauf
    global Klammerzu
    checkauf1 = 0
    checkzu1 = 0
    i = 0
    while checkauf1 == 0:
        i += 1
        Checkpos = Strichpos - i - 1
        if label["text"][Checkpos] == Klammerauf:
            label["text"] = label["text"][:Checkpos + 1][:-1] + label["text"][Checkpos + 1:]
            checkauf1 = 1
            continue
        else:
            filler = filler
    Checkpos = 0
    i = -1
    while checkzu1 == 0:
        i += 1
        Checkpos = Strichpos + i
        if label["text"][Checkpos] == Klammerzu:
            label["text"] = label["text"][:Checkpos + 3][:-2] + label["text"][Checkpos + 3:]
            checkzu1 += 1
            continue
        else:
           filler = filler
    #Rechner
    checkauf1 = 0
    checkzu1 = 0
    i = 0
    while checkauf1 == 0:
        i += 1
        Checkpos = Rstrichpos - i - 1
        if Rechnung[Checkpos] == Klammerauf:
            Rechnung = Rechnung[:Checkpos + 1][:-1] + Rechnung[Checkpos + 1:]
            checkauf1 = 1
            continue
        else:
            filler = filler
    Checkpos = 0
    i = -1
    while checkzu1 == 0:
        i += 1
        Checkpos = Rstrichpos + i
        if Rechnung[Checkpos] == Klammerzu:
            Rechnung = Rechnung[:Checkpos + 3][:-2] + Rechnung[Checkpos + 3:]
            checkzu1 += 1
            continue
        else:
            filler = filler
    checki = 1
def eingabe(i, Loesungen):
    global Eingabe
    global Rstrichpos
    global Strichpos
    Eingabe = Zeichen[i]
    Strichpos = label["text"].find('_')
    Strichposi = Strichpos + 1
    global back
    global Rechnung
    global RZeichen
    global Rechenzeichen
    Rstrichpos = Rechnung.find('_')
    global altetext
    global altetext
    global multiplier
    global Besonders
    global ZZeichen
    global MZeichen
    global Anzeige
    filler = 1
    if len(label["text"]) >= 2:
        if Eingabe in Anzeige:
            ersetzen()
    if Eingabe == '↑' or '↓':
        back = back
    else:
        back = 0
    if label["text"] == 'Syntax-Fehler':
        label["text"] = '_'
        Rechnung = '_'
    else:
        filler = filler
    if Eingabe == 'C':
        label["text"] = '_'
        Rechnung = '_'
    elif Eingabe == ',':
        Rechnung = Rechnung[:Rstrichpos] + '.' + Rechnung[Rstrichpos:]
        Eingabe = label["text"][:Strichpos] + Eingabe + label["text"][Strichpos:]
        label["text"] = Eingabe
    elif Eingabe in MZeichen:
        maldavor()
    elif Eingabe == 'DEL':
        filler = filler
    elif Eingabe == '↑':
        if back > len(altetext):
            back = len(altetext)
        try:
            back = back + 1
            label["text"] = altetext[- back]
            Rechnung = alterechnung[- back]
            Rstrichpos = len(Rechnung)
            Strichpos = len(label["text"])
            label["text"] = label["text"].replace('_', '')
            label["text"] = label["text"][:Strichpos] + '_' + label["text"][Strichpos:]
            Rechnung = Rechnung.replace('_', '')
            Rechnung = Rechnung[:Rstrichpos] + '_' + Rechnung[Rstrichpos:]
        except:
            filler = filler
    elif Eingabe == '↓':
        if back <= 0:
            back = 0
        try:
            back = back - 1
            label["text"] = altetext[- back]
            Rechnung = alterechnung[- back]
            Rstrichpos = len(Rechnung)
            Strichpos = len(label["text"])
            label["text"] = label["text"].replace('_', '')
            label["text"] = label["text"][:Strichpos] + '_' + label["text"][Strichpos:]
            Rechnung = Rechnung.replace('_', '')
            Rechnung = Rechnung[:Rstrichpos] + '_' + Rechnung[Rstrichpos:]
        except:
            filler = filler
    elif Eingabe == '←':
        filler = filler
    elif Eingabe == '→':
        filler = filler
    else:
        Rechnung = Rechnung[:Rstrichpos] + Eingabe + Rechnung[Rstrichpos:]
        Eingabe = label["text"][:Strichpos] + Eingabe + label["text"][Strichpos:]
        label["text"] = Eingabe

    if Eingabe == '←':
        bewegen()
    elif Eingabe == '→':
        bewegen()
    elif Eingabe == 'DEL':
        delete()
    print(Rechnung)

def ende(Loesungen):
    global altetext
    global alterechnung
    global Rechnung
    global ZZeichen
    global Besonders
    check = 0
    filler = 1
    Rechnung = Rechnung.replace('_','')
    label["text"] = label["text"].replace('_', '')
    alterechnung.append(Rechnung)
    altetext.append(label["text"])
    Rechnung = Rechnung.replace('[','(')
    label["text"] = label["text"].replace('[','(')
    Rechnung = Rechnung.replace(']',')')
    label["text"] = label["text"].replace(']',')')
    Rechnung = Rechnung.replace('{','(')
    label["text"] = label["text"].replace('{','(')
    Rechnung = Rechnung.replace('}',')')
    label["text"] = label["text"].replace('}',')')
    Rechnung = Rechnung.replace('√(','**(1/')
    for i in range(len(label["text"])):
        if check == 1:
            if label["text"][i] in ZZeichen:
                filler = filler
            else:
                label["text"] = 'Syntax-Fehler'
        else:
            filler = filler
        if label["text"][i] in Besonders:
            check = 1
        else:
            check = 0
    check = 0
    for i in range(len(label["text"])):
        if check == 1:
            if label["text"][i] == '(':
                filler = filler
            else:
                label["text"] = 'Syntax-Fehler'
        else:
            filler = filler
        if label["text"][i] == '^':
            check = 1
        else:
            check = 0
    if label["text"] == 'Syntax-Fehler':
        filler = filler
    else:
        try:
            Loesungenint = eval(Rechnung)
            Loesungen = str(Loesungenint)
            label["text"] = ''
            for i in range(len(Loesungen)):
                Loesung = Loesungen[i]
                Loesung = label["text"] + Loesung
                label["text"] = Loesung
                Rechnung = Loesung
            label["text"] = label["text"] + '_'
            Rechnung = Rechnung + '_'
        except:
            label["text"] = 'Syntax-Fehler'
            Rechnung = ''
#Label
label = Label(
        text='_' ,
    relief="flat",
    width=62,
    height=5,
    borderwidth=0,
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
    if Zeichen[i] in Pfeile:
        colour = "green"
    else:
        colour = "black"
    btn.append(Button(
            text=Zeichen[Zaehler],
            relief="flat",
            width=10,
            height=5,
            borderwidth=0,
            bg=colour,
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
        relief="flat",
        width=11 * weite,
        height=5,
        borderwidth=0,
        bg="black",
        fg="white",
        font=('arial',15),
        command = lambda: ende(Loesungen)
)
equalbtn.grid(row=zeile, column=spalte, columnspan=5, padx="0.1", pady="0.1")

window.mainloop()

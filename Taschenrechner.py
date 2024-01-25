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
RZeichen = ['*','/','^',]
Pfeile = ['↑','←','→','↓']
Rechenzeichen = ['+','-','*','/','^','(',')']
#Funktionen
def eingabe(i, Loesungen):
    Eingabe = Zeichen[i]
    Strichpos = label["text"].find('|')
    Strichposi = Strichpos + 1
    global back
    global Rechnung
    global RZeichen
    global Rechenzeichen
    Rstrichpos = Rechnung.find('|')
    global altetext
    global altetext
    global multiplier
    filler = 1
    check = 0
    if Eingabe in RZeichen:
        if label["text"][Strichpos - 1] in RZeichen:
            altesvorzeichen = label["text"][Strichpos - 1]
            Rechnung = Rechnung[:Rstrichpos][:-1] + Rechnung[Rstrichpos:]
            label["text"] = label["text"][:Strichpos][:-1] + label["text"][Strichpos:]
            Rstrichpos -= 1
            Strichpos = Strichpos - 1
            check = 1
            if altesvorzeichen == '^':
                Rechnung = Rechnung.replace('*','',Rstrichpos)
                Rstrichpos = Rstrichpos - 1
            else:
                filler = filler
        else:
            filler = filler
    else:
        filler = filler
    if Eingabe == '↑' or '↓':
        back = back
    else:
        back = 0
    if label["text"] == 'Syntax-Fehler':
        label["text"] = ''
        Rechnung = ''
    else:
        filler = filler
    if Eingabe == 'C':
        label["text"] = ''
        Rechnung = ''
    elif Eingabe == ',':
        Rechnung = Rechnung[:Rstrichpos] + '.' + Rechnung[Rstrichpos:]
        Eingabe = label["text"][:Strichpos] + Eingabe + label["text"][Strichpos:]
        label["text"] = Eingabe
    elif Eingabe == '^':
        labeli = 1
        ri = 1
        zlabeli = 1
        zri = 1
        if Rechnung[Rstrichpos - 1] in multiplier:
            Rechnung = Rechnung[:Rstrichpos] + '**' + Rechnung[Rstrichpos:]
            Rstrichpos += 1
            alteRstrichpos = Rstrichpos
            Rstrichpos -= 2
        else:
            Rechnung = Rechnung[:Rstrichpos] + '*' + Rechnung[Rstrichpos:]
            alteRstrichpos = Rstrichpos
            Rstrichpos -= 2
        Eingabe = label["text"][:Strichpos] + Eingabe + label["text"][Strichpos:]
        label["text"] = Eingabe
        Rechnung = Rechnung.replace('|', '')
        Klammerauflabel1 = Strichpos + 1
        Klammeraufr1 = alteRstrichpos + 1
        for i in range(len(Rechnung[Rstrichpos:])):
            zlabeli += 1
            zri += 1
            try:
                if label["text"][Strichpos:][zlabeli] in Rechenzeichen:
                    Klammerzulabel = len(label["text"][:Strichpos]) + zlabeli + 1
                    zlabeli -= 1
                else:
                    Klammerzulabel = len(label["text"][Strichpos:])
            except:
                Klammerzulabel = Strichpos + 2
            try:
                if Rechnung[alteRstrichpos:][zri] in Rechenzeichen:
                    Klammerzur = len(Rechnung[alteRstrichpos:]) + zri + 1
                    zri -= 1
                else:
                    Klammerzur = len(Rechnung[alteRstrichpos:])
            except:
                Klammerzur = alteRstrichpos + 2
        try:
            for i in range(len(Rechnung[:Rstrichpos]) + 2):
                labeli += 1
                ri += 1
                if label["text"][:Strichpos][labeli] in Rechenzeichen:
                    Klammerauflabel = len(label["text"][:Strichpos]) - labeli
                    print('Check', Klammerauflabel)
                    labeli -= 1
                else:
                    Klammerauflabel = 0
                if Rechnung[:Rstrichpos][- ri] in Rechenzeichen:
                    Klammeraufr = len(Rechnung[:Rstrichpos]) - ri
                    print('Checkr', Klammeraufr)
                    ri -= 1
                else:
                    Klammeraufr = 0
        except:
            Klammerauflabel = 0
            Klammeraufr = 0
        label["text"] = label["text"][:Klammerauflabel1] + '(' + label["text"][Klammerauflabel1:]
        Rechnung = Rechnung[:Klammeraufr1] + '(' + Rechnung[Klammeraufr1:]
        label["text"] = label["text"][:Klammerzulabel] + '))' + label["text"][Klammerzulabel:]
        Rechnung = Rechnung[:Klammerzur] + '))' + Rechnung[Klammerzur:]
        label["text"] = label["text"][:Klammerauflabel] + '(' + label["text"][Klammerauflabel:]
        Rechnung = Rechnung[:Klammeraufr + 1] + '(' + Rechnung[Klammeraufr + 1:]
        Strichpos += 2
        Rstrichpos += 4
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
        filler = filler
    elif Eingabe == '↑':
        if back > len(altetext):
            back = len(altetext)
        try:
            back = back + 1
            label["text"] = altetext[- back]
            Rechnung = alterechnung[- back]
        except:
            filler = filler
    elif Eingabe == '↓':
        if back <= 0:
            back = 0
        try:
            back = back - 1
            label["text"] = altetext[- back]
            Rechnung = alterechnung[- back]
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

    if check == 1:
        Rstrichpos = Rstrichpos
    else:
        filler = filler

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
            if label["text"][Strichpos - 1] == '^':
                filler = filler
            elif label["text"][Strichpos - 1] != Rechnung[Rstrichpos - 1]:
                Rstrichpos = Rstrichpos - 1
            else:
                filler = filler 
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
        elif label["text"][Strichpos - 1] == 'e':
            Rechnung = Rechnung[:Rstrichpos][:-13] + Rechnung[Rstrichpos:]
            label["text"] = label["text"][:Strichpos][:-1] + label["text"][Strichpos:]
            Strichpos = Strichpos - 1
            Rstrichpos = Rstrichpos -13
            if label["text"][Strichpos - 1] != Rechnung[Rstrichpos - 1]:
                Rechnung = Rechnung[:Rstrichpos][:-1] + Rechnung[Rstrichpos:]
                Rstrichpos = Rstrichpos - 1
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
                filler = filler
            else:
                Rechnung = Rechnung[:Rstrichpos - 1] + '*' + Rechnung[Rstrichpos - 1:]
    else:
        label["text"] = label["text"].replace('|', '')
        label["text"] = label["text"][:Strichpos + 1] + '|' + label["text"][Strichpos + 1:]
        Rechnung = Rechnung.replace('|', '')
        Rechnung = Rechnung[:Rstrichpos + 1] + '|' + Rechnung[Rstrichpos + 1:]
    print(Rechnung)

def ende(Loesungen):
    global altetext
    global alterechnung
    global Rechnung
    filler = 1
    if label["text"] == 'Syntax-Fehler':
        filler = filler
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
            filler = filler
#Label
label = Label(
        text='|' ,
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

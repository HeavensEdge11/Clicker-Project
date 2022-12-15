from tkinter import *
import time
import random

master = Tk()

# Random Variables

Newslist = [
            'Clicker mine collapses. 2 people trapped!', 'Call me -Grandma', 'Error 404. News not found', 'Is Earth getting lighter? Scientists say its due to all the Clicker Mining Quarries'
    ]


# Variables:

click = 0
clickpersecond = 0
clickpersecondDisplay = 0
ReinforcedIndexFingerMulti = 1
autoclickers = 0
autoclickersDisplay = 0
ClickerGranny = 0
ClickerGrannyDisplay = 0
ClickerFarm = 0
ClickerFarmDisplay = 0
ClickerMiner = 0
ClickerMinerDisplay = 0
Clickspersecondlabel = Label(text='Clicks per Second: ' + str(clickpersecond), bg = 'white')
clicklabel = Label(text = "Total Clicks = " + str(click), bg = "white")
autolabel = Label(text = "Auto Clickers = " + str(autoclickersDisplay), bg ="white")
Grannylabel = Label(text= "Clicker Granny's = " + str(ClickerGrannyDisplay), bg= "white")
Farmlabel = Label(text = "Clicker Farms = " + str(ClickerFarmDisplay), bg = "white")
Minerlabel = Label(text = "Clicker Miners = " + str(ClickerMinerDisplay), bg = "white")
RandomNewslabel = Label(text='Clicker News: ', bg = 'white')

# Commands for Purchase Buttons

# Click Button

def buttonCommand():
    global click
    click += 1
    clicklabel.config(text ="Total Clicks = " + str(click))

# Auto Clickers

def purchaseAutoClickerCommand():
    global click
    global autoclickers 
    global autoclickersDisplay
    global purchaseAutoClickerButton
    if click < 20:
        print("Not enough clicks!")
        purchaseAutoClickerButton.config(state="disabled")
    elif click >= 20:
        click = click - 20
        print("Auto clicker purchased!")
        autoclickers += 1
        autoclickersDisplay += 1 
        purchaseAutoClickerButton.config(state="normal")

def autoclick():
    global master
    global click
    global autoclickers
    global autoclickersDisplay
    global ReinforcedIndexFingerMulti
    master.after(1000, autoclick)
    if autoclickers: click + 1
    click += (autoclickers)*(ReinforcedIndexFingerMulti)
    clicklabel.config(text ="Total Clicks = " + str(click))
    autolabel.config(text="Auto Clickers = " + str(autoclickersDisplay))

autoclick()

# Clicker Granny's

def purchaseClickerGrannyCommand():
    global click
    global ClickerGranny
    global ClickerGrannyDisplay
    if click < 50:
        print('Not enough clicks!')
    elif click >= 50:
        click = click - 50
        print('Clicker Granny Purchased!')
        ClickerGranny += 5
        ClickerGrannyDisplay += 1

def ClickerGrannys():
    global master
    global click
    global ClickerGranny
    global ClickerGrannyDisplay
    click += ClickerGranny
    master.after(1000, ClickerGrannys)
    if ClickerGranny: click + 5
    clicklabel.config(text ="Total Clicks = " + str(click))
    Grannylabel.config(text="Clicker Granny's = " + str(ClickerGrannyDisplay))

ClickerGrannys()

# Clicker Farms

def purchaseClickerFarmCommand():
    global click
    global ClickerFarm
    global ClickerFarmDisplay
    if click < 1500:
        print(" ")
    elif click >= 1500:
        click = click - 1500
        ClickerFarm += 10
        ClickerFarmDisplay += 1

def ClickerFarms():
    global master
    global click
    global ClickerFarm
    global ClickerFarmDisplay
    click += ClickerFarm
    master.after(1000, ClickerFarms)
    if ClickerFarm: click + 10
    clicklabel.config(text = "Total Clicks = " + str(click))
    Farmlabel.config(text = "Clciker Farms = " + str(ClickerFarmDisplay))

ClickerFarms()

# Clicker Miners

def purchaseClickerMinerCommand():
    global click
    global ClickerMiner
    global ClickerMinerDisplay
    if click < 15000:
        print (" ")
    elif click >= 15000:
        click = click - 15000
        ClickerMiner += 20
        ClickerMinerDisplay +=1

def ClickerMiners():
    global master
    global click
    global ClickerMiner
    global ClickerMinerDisplay
    click += ClickerMiner
    master.after(1000, ClickerMiners)
    if ClickerMiner: click + 20
    clicklabel.config(text = "Total Clicks = " + str(click))
    Minerlabel.config(text = "Clicker Miners = " + str(ClickerMinerDisplay))

ClickerMiners()

# Upgrade Button Commands

def purchaseAutoClickerUpgradeCommand():
    global click
    global ReinforcedIndexFingerMulti 
    if click < 1000:
        print(" ")
    elif click >= 1000:
        click = click - 1000
        ReinforcedIndexFingerMulti = ReinforcedIndexFingerMulti * 2
        purchaseAutoClickerUpgrade1.pack_forget()

# Calculating Clicks Per Second

def PerSecondMath():
    global master
    global clickpersecondDisplay
    global clickpersecond
    global autoclickers
    global ClickerGranny
    global ClickerFarm
    global ClickerMiner
    clickpersecond = (autoclickers)*ReinforcedIndexFingerMulti + ClickerGranny + ClickerFarm + ClickerMiner
    master.after(1000, PerSecondMath)
    Clickspersecondlabel.config(text='Clicks per Second: ' + str(clickpersecond))

PerSecondMath()

# Rotating News

def RandomNews():
    global Newslist
    global RandomNewslabel
    global random
    global master
    RandomNewslabel.config(text='Clicker News: ' + random.choice(Newslist))
    master.after(7000, RandomNews)

RandomNews()





# Purchase Button Variabels

mainClickButton = Button(master, text="Click!", height=5, width=10, command = buttonCommand)
mainClickButton.pack()
purchaseAutoClickerButton = Button(master, text="Purchase Auto Clicker: 20", command = purchaseAutoClickerCommand)
purchaseAutoClickerButton.pack()
purchaseClickerGrannyButton = Button(master, text="Purchase Clicker Granny: 50", command = purchaseClickerGrannyCommand)
purchaseClickerGrannyButton.pack()
purchaseClickerFarmButton = Button(master, text="Purchase Clicker Farm: 1,500", command= purchaseClickerFarmCommand)
purchaseClickerFarmButton.pack()
purchaseClickerMinerButton = Button(master, text="Purchase Clicker Miner: 15,000", command = purchaseClickerMinerCommand)
purchaseClickerMinerButton.pack()
master.title("Clicker! v0.0.6")
master.geometry("1000x1000")



# All the Upgrade Buttons

purchaseAutoClickerUpgrade1 = Button(master, text="Reinforced Index Finger: 1,000", command = purchaseAutoClickerUpgradeCommand)
purchaseAutoClickerUpgrade1.pack(padx=400, pady=100)


# All the click lables go here:

clicklabel.place(x=50, y=50)
clicklabel.after(100)
Clickspersecondlabel.place(x=50, y=75)
Clickspersecondlabel.after(10)
RandomNewslabel.place(x=50, y=100)
RandomNewslabel.after(7000)
autolabel.place(x=100, y=125)
autolabel.after(500)
Grannylabel.place(x=100, y=150)
Grannylabel.after(500)
Farmlabel.place(x=100, y=175)
Farmlabel.after(500)
Minerlabel.place(x=100, y=200)
Minerlabel.after(500)

mainloop()
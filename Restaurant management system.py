import tkinter
from tkinter import *
from tkinter import filedialog, messagebox
import random
import time
import requests

# Functions
def reset():
    textReceipt.delete(1.0, END)
    e_roti.set('0')
    e_dosa.set('0')
    e_idly.set('0')
    e_chapathi.set('0')
    e_rice.set('0')
    e_chicken.set('0')
    e_mutton.set('0')
    e_curd.set('0')
    e_briyani.set('0')

    e_pepsi.set('0')
    e_coke.set('0')
    e_choco.set('0')
    e_redbull.set('0')
    e_iceCream.set('0')
    e_fanta.set('0')
    e_lime.set('0')
    e_water.set('0')
    e_juice.set('0')

    e_panCake.set('0')
    e_chocoCake.set('0')
    e_normalCake.set('0')
    e_vannila.set('0')
    e_strawberry.set('0')
    e_blueberry.set('0')
    e_iceCake.set('0')
    e_blackforest.set('0')
    e_whiteforest.set('0')

    textroti.config(state=DISABLED)
    textdosa.config(state=DISABLED)
    textidly.config(state=DISABLED)
    textchapathi.config(state=DISABLED)
    textrice.config(state=DISABLED)
    textchicken.config(state=DISABLED)
    textmutton.config(state=DISABLED)
    textcurd.config(state=DISABLED)
    textbriyani.config(state=DISABLED)

    textpepsi.config(state=DISABLED)
    textcoke.config(state=DISABLED)
    textchoco.config(state=DISABLED)
    textredbull.config(state=DISABLED)
    texticeCream.config(state=DISABLED)
    textfanta.config(state=DISABLED)
    textlime.config(state=DISABLED)
    textwater.config(state=DISABLED)
    textjuice.config(state=DISABLED)

    textpanCake.config(state=DISABLED)
    textchocoCake.config(state=DISABLED)
    textnormalCake.config(state=DISABLED)
    textvannila.config(state=DISABLED)
    textstrawberry.config(state=DISABLED)
    textblueberry.config(state=DISABLED)
    texticeCake.config(state=DISABLED)
    textblackforest.config(state=DISABLED)
    textwhiteforest.config(state=DISABLED)

    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)

    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)
    var17.set(0)
    var18.set(0)

    var19.set(0)
    var20.set(0)
    var21.set(0)
    var22.set(0)
    var23.set(0)
    var24.set(0)
    var25.set(0)
    var26.set(0)
    var27.set(0)

    costofdrinkvar.set('')
    costoffoodvar.set('')
    costofcakevar.set('')

    subtotalvar.set('')
    servicetaxvar.set('')
    totalvar.set('')


def send():
    if textReceipt.get(1.0, END) == '\n':
        pass
    else:
        def send_msg():
            message = textarea.get(1.0, END)
            number = numberfield.get()
            auth = 'woVHAjOGldMsPhnT7gS6XRIi4cYr0ym3FZkEWfKv9Qxauq8J2DHDWus7AqZKnkeXlVzQJa3fIRrp925S'
            url = 'https://www.fast2sms.com/dev/bulk'

            params = {
                'authorization': auth,
                'message': message,
                'numbers': number,
                'sender-id': 'FSTSMS',
                'route': 'p',
                'language': 'english'
            }
            response = requests.get(url, params=params)
            dic = response.json()
            result = dic.get('return')
            if result == True:
                messagebox.showinfo('Send Successfully', 'Message sent succesfully')

            else:
                messagebox.showerror('Error', 'Something went wrong')

        root2 = Toplevel()

        root2.title("Send Bill")
        root2.config(bg='red4')
        root2.geometry('485x620+50+50')

        logoImage = PhotoImage(file='sender.png')
        label = Label(root2, image=logoImage, bg='red4')
        label.pack(pady=5)

        numberLabel = Label(root2, text='Mobile Number', font=('arial', 18, 'bold underline'), bg='red4', fg='white')
        numberLabel.pack(pady=5)

        numberfield = Entry(root2, font=('helvetica', 22, 'bold'), bd=3, width=24)
        numberfield.pack(pady=5)

        billLabel = Label(root2, text='Bill Details', font=('arial', 18, 'bold underline'), bg='red4', fg='white')
        billLabel.pack(pady=5)

        textarea = Text(root2, font=('arial', 12, 'bold'), bd=3, width=42, height=14)
        textarea.pack(pady=5)
        textarea.insert(END, 'Receipt Ref:\t\t' + billnumber + '\t\t' + date + '\n\n')

        if costoffoodvar.get() != '0 Rs':
            textarea.insert(END, f'Cost Of Food\t\t\t{priceofFood}Rs\n')

        if costofdrinkvar.get() != '0 Rs':
            textarea.insert(END, f'Cost Of Drinks\t\t\t{priceofDrinks}Rs\n')

        if costofcakevar.get() != '0 Rs':
            textarea.insert(END, f'Cost Of Cakes\t\t\t{priceofCakes}Rs\n')

        textarea.insert(END, f'Sub Total\t\t\t{subtotalofItems}Rs\n')
        textarea.insert(END, f'Service Tax\t\t\t{50}Rs\n')
        textarea.insert(END, f'total \t\t\t{subtotalofItems + 50}Rs\n')

        sendButton = Button(root2, text='SEND', font=('arial', 19, 'bold'), bg='white', fg='red4', bd=7, relief=GROOVE,command=send_msg)
        sendButton.pack(pady=5)

        root2.mainloop()



def save():
    if textReceipt.get(1.0, END) == '\n':
        pass
    else:
        url = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
        if url == None:
            pass
        else:
            bill_data = textReceipt.get(1.0, END)
            url.write(bill_data)
            url.close()
            messagebox.showinfo('Information', 'Your Bill Is Succesfully Saved')


def receipt():
    global billnumber, date
    if costoffoodvar.get() != '' or costofcakevar.get() != '' or costofdrinkvar.get() != '':
        textReceipt.delete(1.0, END)
        x = random.randint(100, 10000)
        billnumber = 'BILL' + str(x)
        date = time.strftime('%d/%m/%Y')

        textReceipt.insert(END, 'Receipt Ref:\t\t' + billnumber + '\t\t' + date + '\n')

        textReceipt.insert(END, '***************************************************************\n')

        textReceipt.insert(END, 'Items:\t\t Cost Of Items(Rs)\n')

        textReceipt.insert(END, '***************************************************************\n')

        if e_roti.get() != '0':
            textReceipt.insert(END, f'Roti\t\t\t{int(e_roti.get()) * 10}\n\n')

        if e_dosa.get() != '0':
            textReceipt.insert(END, f'Dosa\t\t\t{int(e_dosa.get()) * 60}\n\n')

        if e_idly.get() != '0':
            textReceipt.insert(END, f'Idly\t\t\t{int(e_idly.get()) * 100}\n\n')

        if e_chapathi.get() != '0':
            textReceipt.insert(END, f'Chapathi:\t\t\t{int(e_chapathi.get()) * 30}\n\n')

        if e_rice.get() != '0':
            textReceipt.insert(END, f'Rice:\t\t\t{int(e_rice.get()) * 50}\n\n')

        if e_chicken.get() != '0':
            textReceipt.insert(END, f'Chicken:\t\t\t{int(e_chicken.get()) * 100}\n\n')

        if e_mutton.get() != '0':
            textReceipt.insert(END, f'Mutton:\t\t\t{int(e_mutton.get()) * 40}\n\n')

        if e_curd.get() != '0':
            textReceipt.insert(END, f'Curd:\t\t\t{int(e_curd.get()) * 120}\n\n')

        if e_briyani.get() != '0':
            textReceipt.insert(END, f'Briyani:\t\t\t{int(e_briyani.get()) * 120}\n\n')


        if e_pepsi.get() != '0':
            textReceipt.insert(END, f'Pepsi:\t\t\t{int(e_pepsi.get()) * 50}\n\n')

        if e_coke.get() != '0':
            textReceipt.insert(END, f'Coke:\t\t\t{int(e_coke.get()) * 40}\n\n')

        if e_choco.get() != '0':
            textReceipt.insert(END, f'Choco:\t\t\t{int(e_choco.get()) * 80}\n\n')

        if e_redbull.get() != '0':
            textReceipt.insert(END, f'Redbull:\t\t\t{int(e_redbull.get()) * 30}\n\n')

        if e_iceCream.get() != '0':
            textReceipt.insert(END, f'IceCream:\t\t\t{int(e_iceCream.get()) * 40}\n\n')

        if e_fanta.get() != '0':
            textReceipt.insert(END, f'Fanta:\t\t\t{int(e_fanta.get()) * 60}\n\n')

        if e_lime.get() != '0':
            textReceipt.insert(END, f'Lime:\t\t\t{int(e_lime.get()) * 20}\n\n')

        if e_water.get() != '0':
            textReceipt.insert(END, f'Water:\t\t\t{int(e_water.get()) * 50}\n\n')

        if e_juice.get() != '0':
            textReceipt.insert(END, f'Juice:\t\t\t{int(e_juice.get()) * 80}\n\n')


        if e_panCake.get() != '0':
            textReceipt.insert(END, f'panCake:\t\t\t{int(e_panCake.get()) * 400}\n\n')

        if e_chocoCake.get() != '0':
            textReceipt.insert(END, f'ChocoCake:\t\t\t{int(e_chocoCake.get()) * 300}\n\n')

        if e_normalCake.get() != '0':
            textReceipt.insert(END, f'NormalCake:\t\t\t{int(e_normalCake.get()) * 500}\n\n')

        if e_vannila.get() != '0':
            textReceipt.insert(END, f'Vannila:\t\t\t{int(e_vannila.get()) * 450}\n\n')

        if e_strawberry.get() != '0':
            textReceipt.insert(END, f'strawberry:\t\t\t{int(e_strawberry.get()) * 800}\n\n')

        if e_blueberry.get() != '0':
            textReceipt.insert(END, f'blueberry:\t\t\t{int(e_blueberry.get()) * 620}\n\n')

        if e_iceCake.get() != '0':
            textReceipt.insert(END, f'Ice Cake:\t\t\t{int(e_iceCake.get()) * 700}\n\n')

        if e_blackforest.get() != '0':
            textReceipt.insert(END, f'Black Forest:\t\t\t{int(e_blackforest.get()) * 550}\n\n')

        if e_whiteforest.get() != '0':
            textReceipt.insert(END, f'whiteforest:\t\t\t{int(e_whiteforest.get()) * 550}\n\n')


        textReceipt.insert(END, '***************************************************************\n')

        if costoffoodvar.get() != '0 Rs':
            textReceipt.insert(END, f'Cost Of Food\t\t\t{priceofFood}Rs\n\n')

        if costofdrinkvar.get() != '0 Rs':
            textReceipt.insert(END, f'Cost Of Drinks\t\t\t{priceofDrinks}Rs\n\n')

        if costofcakevar.get() != '0 Rs':
            textReceipt.insert(END, f'Cost Of Cakes\t\t\t{priceofCakes}Rs\n\n')

        textReceipt.insert(END, f'Sub Total\t\t\t{subtotalofItems}Rs\n\n')
        textReceipt.insert(END, f'Service Tax\t\t\t{50}Rs\n\n')
        textReceipt.insert(END, f'Total\t\t\t{subtotalofItems + 50}Rs\n\n')

        textReceipt.insert(END, '***************************************************************\n')

    else:
        messagebox.showerror('Error', 'No Item Is selected')



def total():
    global priceofFood, priceofDrinks, priceofCakes, subtotalofItems
    if var1.get() != 0 or var2.get() != 0 or var3.get() != 0 or var4.get() != 0 or var5.get() != 0 or \
            var6.get() != 0 or var7.get() != 0 or var8.get() != 0 or var9.get() != 0 or var10.get() != 0 or \
            var11.get() != 0 or var12.get() != 0 or var13.get() != 0 or var14.get() != 0 or var15.get() != 0 or \
            var16.get() != 0 or var17.get() != 0 or var18.get() != 0 or var19.get() != 0 or var20.get() != 0 or \
            var21.get() != 0 or var22.get() != 0 or var23.get() != 0 or var24.get() != 0 or var25.get() != 0 or \
            var26.get() != 0 or var27.get() != 0:

        item1 = int(e_roti.get())
        item2 = int(e_dosa.get())
        item3 = int(e_idly.get())
        item4 = int(e_chapathi.get())
        item5 = int(e_rice.get())
        item6 = int(e_chicken.get())
        item7 = int(e_mutton.get())
        item8 = int(e_curd.get())
        item9 = int(e_briyani.get())

        item10 = int(e_pepsi.get())
        item11 = int(e_coke.get())
        item12 = int(e_choco.get())
        item13 = int(e_redbull.get())
        item14 = int(e_iceCream.get())
        item15 = int(e_fanta.get())
        item16 = int(e_lime.get())
        item17 = int(e_water.get())
        item18 = int(e_juice.get())

        item19 = int(e_panCake.get())
        item20 = int(e_chocoCake.get())
        item21 = int(e_normalCake.get())
        item22 = int(e_vannila.get())
        item23 = int(e_strawberry.get())
        item24 = int(e_blueberry.get())
        item25 = int(e_iceCake.get())
        item26 = int(e_blackforest.get())
        item27 = int(e_whiteforest.get())

        priceofFood=(item1*10)+(item2*60)+(item3*100)+(item4*50)+(item5*40)+(item6*30)+(item7*120)+(item8*100)+(item9*120)
        priceofDrinks=(item10*50)+(item11*40)+(item12*80)+(item13*30)+(item14*40)+(item15*60)+(item16*20)+(item17*50)+(item18*80)
        priceofCakes=(item19*400)+(item20*300)+(item21*500)+(item22*550)+(item23*450)+(item24*800)+(item25*620)+(item26*700)+(item27*550)

        costoffoodvar.set(str(priceofFood) + ' Rs')
        costofdrinkvar.set(str(priceofDrinks) + ' Rs')
        costofcakevar.set(str(priceofCakes) + ' Rs')

        subtotalofItems = priceofFood + priceofDrinks + priceofCakes
        subtotalvar.set(str(subtotalofItems) + ' Rs')

        servicetaxvar.set('50 Rs')

        total= subtotalofItems + 50
        totalvar.set(str(total) + ' Rs')

    else:
        messagebox.showerror('Error', 'No Item Is selected')


def roti():
    if var1.get()==1:
        textroti.config(state=NORMAL)
        textroti.delete(0,END)
        textroti.focus()
    else:
        textroti.config(state=DISABLED)
        e_roti.set('0')

def dosa():
    if var2.get()==1:
        textdosa.config(state=NORMAL)
        textdosa.delete(0,END)
        textdosa.focus()
    else:
        textdosa.config(state=DISABLED)
        e_dosa.set('0')

def idly():
    if var3.get()==1:
        textidly.config(state=NORMAL)
        textidly.delete(0,END)
        textidly.focus()
    else:
        textidly.config(state=DISABLED)
        e_idly.set('0')

def chapathi():
    if var4.get()==1:
        textchapathi.config(state=NORMAL)
        textchapathi.delete(0,END)
        textchapathi.focus()
    else:
        textchapathi.config(state=DISABLED)
        e_chapathi.set('0')

def rice():
    if var5.get()==1:
        textrice.config(state=NORMAL)
        textrice.delete(0,END)
        textrice.focus()
    else:
        textrice.config(state=DISABLED)
        e_rice.set('0')

def chicken():
    if var6.get()==1:
        textchicken.config(state=NORMAL)
        textchicken.delete(0,END)
        textchicken.focus()
    else:
        textchicken.config(state=DISABLED)
        e_chicken.set('0')

def mutton():
    if var7.get()==1:
        textmutton.config(state=NORMAL)
        textmutton.delete(0,END)
        textmutton.focus()
    else:
        textmutton.config(state=DISABLED)
        e_mutton.set('0')

def curd():
    if var8.get()==1:
        textcurd.config(state=NORMAL)
        textcurd.delete(0,END)
        textcurd.focus()
    else:
        textcurd.config(state=DISABLED)
        e_curd.set('0')

def briyani():
    if var9.get()==1:
        textbriyani.config(state=NORMAL)
        textbriyani.delete(0,END)
        textbriyani.focus()
    else:
        textbriyani.config(state=DISABLED)
        e_briyani.set('0')



def pepsi():
    if var10.get()==1:
        textpepsi.config(state=NORMAL)
        textpepsi.delete(0,END)
        textpepsi.focus()
    else:
        textpepsi.config(state=DISABLED)
        e_pepsi.set('0')

def coke():
    if var11.get()==1:
        textcoke.config(state=NORMAL)
        textcoke.delete(0,END)
        textcoke.focus()
    else:
        textcoke.config(state=DISABLED)
        e_coke.set('0')

def choco():
    if var12.get()==1:
        textchoco.config(state=NORMAL)
        textchoco.delete(0,END)
        textchoco.focus()
    else:
        textchoco.config(state=DISABLED)
        e_choco.set('0')

def redbull():
    if var13.get()==1:
        textredbull.config(state=NORMAL)
        textredbull.delete(0,END)
        textredbull.focus()
    else:
        textredbull.config(state=DISABLED)
        e_redbull.set('0')

def icecream():
    if var14.get()==1:
        texticeCream.config(state=NORMAL)
        texticeCream.delete(0,END)
        texticeCream.focus()
    else:
        texticeCream.config(state=DISABLED)
        e_icecream.set('0')

def fanta():
    if var15.get()==1:
        textfanta.config(state=NORMAL)
        textfanta.delete(0,END)
        textfanta.focus()
    else:
        textfanta.config(state=DISABLED)
        e_fanta.set('0')

def lime():
    if var16.get()==1:
        textlime.config(state=NORMAL)
        textlime.delete(0,END)
        textlime.focus()
    else:
        textlime.config(state=DISABLED)
        e_lime.set('0')

def water():
    if var17.get()==1:
        textwater.config(state=NORMAL)
        textwater.delete(0,END)
        textwater.focus()
    else:
        textwater.config(state=DISABLED)
        e_water.set('0')

def juice():
    if var18.get()==1:
        textjuice.config(state=NORMAL)
        textjuice.delete(0,END)
        textjuice.focus()
    else:
        textjuice.config(state=DISABLED)
        e_juice.set('0')



def pancake():
    if var19.get()==1:
        textpanCake.config(state=NORMAL)
        textpanCake.delete(0,END)
        textpanCake.focus()
    else:
        textpanCake.config(state=DISABLED)
        e_pancake.set('0')

def chococake():
    if var20.get()==1:
        textchocoCake.config(state=NORMAL)
        textchocoCake.delete(0,END)
        textchocoCake.focus()
    else:
        textchocoCake.config(state=DISABLED)
        e_chococake.set('0')

def normalcake():
    if var21.get()==1:
        textnormalCake.config(state=NORMAL)
        textnormalCake.delete(0,END)
        textnormalCake.focus()
    else:
        textnormalCake.config(state=DISABLED)
        e_normalcake.set('0')

def vannila():
    if var22.get()==1:
        textvannila.config(state=NORMAL)
        textvannila.delete(0,END)
        textvannila.focus()
    else:
        textvannila.config(state=DISABLED)
        e_vannila
        a.set('0')

def strawberry():
    if var23.get()==1:
        textstrawberry.config(state=NORMAL)
        textstrawberry.delete(0,END)
        textstrawberry.focus()
    else:
        textstrawberry.config(state=DISABLED)
        e_strawberry.set('0')

def blueberry():
    if var24.get()==1:
        textblueberry.config(state=NORMAL)
        textblueberry.delete(0,END)
        textblueberry.focus()
    else:
        textblueberry.config(state=DISABLED)
        e_blueberry.set('0')

def icecake():
    if var25.get()==1:
        texticeCake.config(state=NORMAL)
        texticeCake.delete(0,END)
        texticeCake.focus()
    else:
        texticeCake.config(state=DISABLED)
        e_icecake.set('0')

def blackforest():
    if var26.get()==1:
        textblackforest.config(state=NORMAL)
        textblackforest.delete(0,END)
        textblackforest.focus()
    else:
        textblackforest.config(state=DISABLED)
        e_blackforest.set('0')

def whiteforest():
    if var27.get()==1:
        textwhiteforest.config(state=NORMAL)
        textwhiteforest.delete(0,END)
        textwhiteforest.focus()
    else:
        textwhiteforest.config(state=DISABLED)
        e_whiteforest.set('0')


root = Tk()
root.geometry('1270x690+0+0')
root.resizable(0,0)
root.title("Resturant Management system")
root.config(bg='#4285f4')

topFrame = Frame(root,bd=10,relief=RIDGE,bg='firebrick4')
topFrame.pack(side=TOP)

labelTitle = Label(topFrame,text='Resturant Management system',font=('arial',30,'bold'),fg='yellow',bd=9,bg='red4',width=51)
labelTitle.grid(row=0,column=0)

#frames
menuFrame=Frame(root,bd=10,relief=RIDGE,bg='firebrick4')
menuFrame.pack(side=LEFT)

costFrame=Frame(menuFrame,bd=4,relief=RIDGE,bg='firebrick4',pady=10)
costFrame.pack(side=BOTTOM)

foodFrame=LabelFrame(menuFrame,text='Food',font=('arial',19,'bold'),bd=10,relief=RIDGE,fg='red4')
foodFrame.pack(side=LEFT)

drinksFrame=LabelFrame(menuFrame,text='Drinks',font=('arial',19,'bold'),bd=10,relief=RIDGE,fg='red4')
drinksFrame.pack(side=LEFT)

cakesFrame=LabelFrame(menuFrame,text='Cakes',font=('arial',19,'bold'),bd=10,relief=RIDGE,fg='red4')
cakesFrame.pack(side=LEFT)

rightFrame=Frame(root,bd=15,relief=RIDGE,bg='red4')
rightFrame.pack(side=RIGHT)

calculatorFrame=Frame(rightFrame,bd=1,relief=RIDGE,bg='red4')
calculatorFrame.pack()

receiptFrame=Frame(rightFrame,bd=4,relief=RIDGE,bg='red4')
receiptFrame.pack()

buttonFrame=Frame(rightFrame,bd=3,relief=RIDGE,bg='red4')
buttonFrame.pack()

#variables
var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()
var9=IntVar()

var10=IntVar()
var11=IntVar()
var12=IntVar()
var13=IntVar()
var14=IntVar()
var15=IntVar()
var16=IntVar()
var17=IntVar()
var18=IntVar()

var19=IntVar()
var20=IntVar()
var21=IntVar()
var22=IntVar()
var23=IntVar()
var24=IntVar()
var25=IntVar()
var26=IntVar()
var27=IntVar()

e_roti=StringVar()
e_dosa=StringVar()
e_idly=StringVar()
e_chapathi=StringVar()
e_rice=StringVar()
e_chicken=StringVar()
e_mutton=StringVar()
e_curd=StringVar()
e_briyani=StringVar()

e_pepsi=StringVar()
e_coke=StringVar()
e_choco=StringVar()
e_redbull=StringVar()
e_iceCream=StringVar()
e_fanta=StringVar()
e_lime=StringVar()
e_water=StringVar()
e_juice=StringVar()

e_panCake=StringVar()
e_chocoCake=StringVar()
e_normalCake=StringVar()
e_vannila=StringVar()
e_strawberry=StringVar()
e_blueberry=StringVar()
e_iceCake=StringVar()
e_blackforest=StringVar()
e_whiteforest=StringVar()

costoffoodvar=StringVar()
subtotalvar=StringVar()
costofdrinkvar=StringVar()
servicetaxvar=StringVar()
costofcakevar=StringVar()
totalvar=StringVar()

#assume value 0
e_roti.set('0')
e_dosa.set('0')
e_idly.set('0')
e_chapathi.set('0')
e_rice.set('0')
e_chicken.set('0')
e_mutton.set('0')
e_curd.set('0')
e_briyani.set('0')

e_pepsi.set('0')
e_coke.set('0')
e_choco.set('0')
e_redbull.set('0')
e_iceCream.set('0')
e_fanta.set('0')
e_lime.set('0')
e_water.set('0')
e_juice.set('0')

e_panCake.set('0')
e_chocoCake.set('0')
e_normalCake.set('0')
e_vannila.set('0')
e_strawberry.set('0')
e_blueberry.set('0')
e_iceCake.set('0')
e_blackforest.set('0')
e_whiteforest.set('0')


#food
roti=Checkbutton(foodFrame,text='Roti',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var1,command=roti)
roti.grid(row=0,column=0,sticky=W)

dosa=Checkbutton(foodFrame,text='Dosa',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var2,command=dosa)
dosa.grid(row=1,column=0,sticky=W)

idly=Checkbutton(foodFrame,text='Idly',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var3,command=idly)
idly.grid(row=2,column=0,sticky=W)

chapathi=Checkbutton(foodFrame,text='Chapathi',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var4,command=chapathi)
chapathi.grid(row=3,column=0,sticky=W)

rice=Checkbutton(foodFrame,text='Rice',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var5,command=rice)
rice.grid(row=4,column=0,sticky=W)

chicken=Checkbutton(foodFrame,text='Chicken',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var6,command=chicken)
chicken.grid(row=5,column=0,sticky=W)

mutton=Checkbutton(foodFrame,text='Mutton',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var7,command=mutton)
mutton.grid(row=6,column=0,sticky=W)

curd=Checkbutton(foodFrame,text='Curd',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var8,command=curd)
curd.grid(row=7,column=0,sticky=W)

briyani=Checkbutton(foodFrame,text='Briyani',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var9,command=briyani)
briyani.grid(row=8,column=0,sticky=W)

#entry fields for food items
textroti=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_roti)
textroti.grid(row=0,column=1)

textdosa=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_dosa)
textdosa.grid(row=1,column=1)

textidly=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_idly)
textidly.grid(row=2,column=1)

textchapathi=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_chapathi)
textchapathi.grid(row=3,column=1)

textrice=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_rice)
textrice.grid(row=4,column=1)

textchicken=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_chicken)
textchicken.grid(row=5,column=1)

textmutton=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_mutton)
textmutton.grid(row=6,column=1)

textcurd=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_curd)
textcurd.grid(row=7,column=1)

textbriyani=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_briyani)
textbriyani.grid(row=8,column=1)


#drinks
pepsi=Checkbutton(drinksFrame,text='Pepsi',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var10,command=pepsi)
pepsi.grid(row=0,column=0,sticky=W)

coke=Checkbutton(drinksFrame,text='Coke',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var11,command=coke)
coke.grid(row=1,column=0,sticky=W)

choco=Checkbutton(drinksFrame,text='Choco',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var12,command=choco)
choco.grid(row=2,column=0,sticky=W)

redbull=Checkbutton(drinksFrame,text='Redbull',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var13,command=redbull)
redbull.grid(row=3,column=0,sticky=W)

iceCream=Checkbutton(drinksFrame,text='IceCream',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var14,command=icecream)
iceCream.grid(row=4,column=0,sticky=W)

fanta=Checkbutton(drinksFrame,text='Fanta',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var15,command=fanta)
fanta.grid(row=5,column=0,sticky=W)

lime=Checkbutton(drinksFrame,text='Lime',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var16,command=lime)
lime.grid(row=6,column=0,sticky=W)

water=Checkbutton(drinksFrame,text='Water',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var17,command=water)
water.grid(row=7,column=0,sticky=W)

juice=Checkbutton(drinksFrame,text='Juice',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var18,command=juice)
juice.grid(row=8,column=0,sticky=W)

#entry fields for drinks items
textpepsi=Entry(drinksFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_pepsi)
textpepsi.grid(row=0,column=1)

textcoke=Entry(drinksFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_coke)
textcoke.grid(row=1,column=1)

textchoco=Entry(drinksFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_choco)
textchoco.grid(row=2,column=1)

textredbull=Entry(drinksFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_redbull)
textredbull.grid(row=3,column=1)

texticeCream=Entry(drinksFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_iceCream)
texticeCream.grid(row=4,column=1)

textfanta=Entry(drinksFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_fanta)
textfanta.grid(row=5,column=1)

textlime=Entry(drinksFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_lime)
textlime.grid(row=6,column=1)

textwater=Entry(drinksFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_water)
textwater.grid(row=7,column=1)

textjuice=Entry(drinksFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_juice)
textjuice.grid(row=8,column=1)

#Cakes
panCake=Checkbutton(cakesFrame,text='PanCake',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var19,command=pancake)
panCake.grid(row=0,column=0,sticky=W)

chocoCake=Checkbutton(cakesFrame,text='ChocoCake',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var20,command=chococake)
chocoCake.grid(row=1,column=0,sticky=W)

normalCake=Checkbutton(cakesFrame,text='NormalCake',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var21,command=normalcake)
normalCake.grid(row=2,column=0,sticky=W)

vannila=Checkbutton(cakesFrame,text='Vannila',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var22,command=vannila)
vannila.grid(row=3,column=0,sticky=W)

strawberry=Checkbutton(cakesFrame,text='Strawberry',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var23,command=strawberry)
strawberry.grid(row=4,column=0,sticky=W)

blueberry=Checkbutton(cakesFrame,text='Blueberry',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var24,command=blueberry)
blueberry.grid(row=5,column=0,sticky=W)

iceCake=Checkbutton(cakesFrame,text='IceCake',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var25,command=icecake)
iceCake.grid(row=6,column=0,sticky=W)

blackforest=Checkbutton(cakesFrame,text='Blackforest',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var26,command=blackforest)
blackforest.grid(row=7,column=0,sticky=W)

whiteforest=Checkbutton(cakesFrame,text='Whiteforest',font=('arial',18,'bold'),onvalue=1,offvalue=0,variable=var27,command=whiteforest)
whiteforest.grid(row=8,column=0,sticky=W)

#entry fields for cakes items
textpanCake=Entry(cakesFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_panCake)
textpanCake.grid(row=0,column=1)

textchocoCake=Entry(cakesFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_chocoCake)
textchocoCake.grid(row=1,column=1)

textnormalCake=Entry(cakesFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_normalCake)
textnormalCake.grid(row=2,column=1)

textvannila=Entry(cakesFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_vannila)
textvannila.grid(row=3,column=1)

textstrawberry=Entry(cakesFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_strawberry)
textstrawberry.grid(row=4,column=1)

textblueberry=Entry(cakesFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_blueberry)
textblueberry.grid(row=5,column=1)

texticeCake=Entry(cakesFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_iceCake)
texticeCake.grid(row=6,column=1)

textblackforest=Entry(cakesFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_blackforest)
textblackforest.grid(row=7,column=1)

textwhiteforest=Entry(cakesFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_whiteforest)
textwhiteforest.grid(row=8,column=1)

#costlabels & entry feilds
labelCostofFoods=Label(costFrame,text='Cost of Foods',font=('arial',16,'bold'),fg='#0F9D58',bg='red4')
labelCostofFoods.grid(row=0,column=0)

textCostofFoods=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=costoffoodvar)
textCostofFoods.grid(row=0,column=1,padx=41)

labelSubTotal=Label(costFrame,text='Sub Total',font=('arial',16,'bold'),fg='#0F9D58',bg='red4')
labelSubTotal.grid(row=0,column=2)

textSubTotal=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=subtotalvar)
textSubTotal.grid(row=0,column=3,padx=41)


labelCostofDrinks=Label(costFrame,text='Cost of Drinks',font=('arial',16,'bold'),fg='#0F9D58',bg='red4')
labelCostofDrinks.grid(row=1,column=0)

textCostofDrinks=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=costofdrinkvar)
textCostofDrinks.grid(row=1,column=1,padx=41)

labelServiceTax=Label(costFrame,text='Service Tax',font=('arial',16,'bold'),fg='#0F9D58',bg='red4')
labelServiceTax.grid(row=1,column=2)

textServiceTax=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=servicetaxvar)
textServiceTax.grid(row=1,column=3,padx=41)


labelCostofCakes=Label(costFrame,text='Cost of Cakes',font=('arial',16,'bold'),fg='#0F9D58',bg='red4')
labelCostofCakes.grid(row=2,column=0)

textCostofCakes=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=costofcakevar)
textCostofCakes.grid(row=2,column=1,padx=41)

labelTotal=Label(costFrame,text='Total',font=('arial',16,'bold'),fg='#0F9D58',bg='red4')
labelTotal.grid(row=2,column=2)

textTotal=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=totalvar)
textTotal.grid(row=2,column=3,padx=41)

#Buttons
buttonTotal=Button(buttonFrame,text='Total',font=('arial',14,'bold'),fg='white',bg='red4',bd=3,padx=5,command=total)
buttonTotal.grid(row=0,column=0)

buttonReceipt=Button(buttonFrame,text='Receipt',font=('arial',14,'bold'),fg='white',bg='red4',bd=3,padx=5,command=receipt)
buttonReceipt.grid(row=0,column=1)

buttonSave=Button(buttonFrame,text='Save',font=('arial',14,'bold'),fg='white',bg='red4',bd=3,padx=5,command=save)
buttonSave.grid(row=0,column=2)

buttonSend=Button(buttonFrame,text='Send',font=('arial',14,'bold'),fg='white',bg='red4',bd=3,padx=5,command=send)
buttonSend.grid(row=0,column=3)

buttonReset=Button(buttonFrame,text='Reset',font=('arial',14,'bold'),fg='white',bg='red4',bd=3,padx=5,command=reset)
buttonReset.grid(row=0,column=4)

#textarea for receipt
textReceipt=Text(receiptFrame,font=('arial',12,'bold'),bd=3,width=42,height=14)
textReceipt.grid(row=0,column=0)

#calculator
operator=''
def buttonClick(numbers):
    global operator
    operator+=numbers
    calculatorField.delete(0,END)
    calculatorField.insert(END,operator)

def clear():
    global operator
    operator=''
    calculatorField.delete(0,END)

def answer():
    global operator
    result=str(eval(operator))
    calculatorField.delete(0,END)
    calculatorField.insert(0,result)
    operator=''

calculatorField=Entry(calculatorFrame,font=('arial',16,'bold'),width=32,bd=4)
calculatorField.grid(row=0,column=0,columnspan=4)

Button(calculatorFrame,text='7',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,command=lambda:buttonClick('7')).grid(row=1,column=0)
Button(calculatorFrame,text='8',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,command=lambda:buttonClick('8')).grid(row=1,column=1)
Button(calculatorFrame,text='9',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,command=lambda:buttonClick('9')).grid(row=1,column=2)
Button(calculatorFrame,text='+',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,command=lambda:buttonClick('+')).grid(row=1,column=3)

Button(calculatorFrame,text='4',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,command=lambda:buttonClick('4')).grid(row=2,column=0)
Button(calculatorFrame,text='5',font=('arial',16,'bold'),fg='red4',bg='white',bd=6,width=6,command=lambda:buttonClick('5')).grid(row=2,column=1)
Button(calculatorFrame,text='6',font=('arial',16,'bold'),fg='red4',bg='white',bd=6,width=6,command=lambda:buttonClick('6')).grid(row=2,column=2)
Button(calculatorFrame,text='-',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,command=lambda:buttonClick('-')).grid(row=2,column=3)

Button(calculatorFrame,text='1',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,command=lambda:buttonClick('1')).grid(row=3,column=0)
Button(calculatorFrame,text='2',font=('arial',16,'bold'),fg='red4',bg='white',bd=6,width=6,command=lambda:buttonClick('2')).grid(row=3,column=1)
Button(calculatorFrame,text='3',font=('arial',16,'bold'),fg='red4',bg='white',bd=6,width=6,command=lambda:buttonClick('3')).grid(row=3,column=2)
Button(calculatorFrame,text='*',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,command=lambda:buttonClick('*')).grid(row=3,column=3)

Button(calculatorFrame,text='Ans',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,command=answer).grid(row=4,column=0)
Button(calculatorFrame,text='Clear',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,command=clear).grid(row=4,column=1)
Button(calculatorFrame,text='0',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,command=lambda:buttonClick('0')).grid(row=4,column=2)
Button(calculatorFrame,text='/',font=('arial',16,'bold'),fg='yellow',bg='red4',bd=6,width=6,command=lambda:buttonClick('/')).grid(row=4,column=3)


root.mainloop()




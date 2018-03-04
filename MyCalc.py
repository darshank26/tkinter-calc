from tkinter import*
cal = Tk()

def onButtonClick(num):
    global operator
    operator = operator + str(num)
    text_ip.set(operator)

def onButtonClear():
    global operator
    operator = ""
    text_ip.set("")

def onButtonEq():
    global operator
    value = str(eval(operator))
    text_ip.set(value)
    operator=""
    
cal.title("Calculator")
operator = ""
text_ip = StringVar()

txtDisplay = Entry(cal,font=('arial',20,'bold'),textvar = text_ip, bd =10,
                   insertwidth=4, bg="powder blue", justify="right").grid(columnspan=4)

#=============== Row 1 ==========================
button7 = Button(cal,padx =16, bd=1, fg="black",font=('arial',20,'bold'),text='7', command=lambda:onButtonClick(7), bg="powder blue").grid(row=1,column=0)
button8 = Button(cal,padx =16, bd=1, fg="black",font=('arial',20,'bold'),text='8', command=lambda:onButtonClick(8), bg="powder blue").grid(row=1,column=1)
button9 = Button(cal,padx =16, bd=1, fg="black",font=('arial',20,'bold'),text='9', command=lambda:onButtonClick(9), bg="powder blue").grid(row=1,column=2)
addbutton = Button(cal,padx =16, bd=1, fg="black",font=('arial',20,'bold'),text='+', command=lambda:onButtonClick("+"), bg="powder blue").grid(row=1,column=3)

#=============== Row 2 ==========================
button4 = Button(cal,padx =16, bd=1, fg="black",font=('arial',20,'bold'),text='4', command=lambda:onButtonClick(4), bg="powder blue").grid(row=2,column=0)
button5 = Button(cal,padx =16, bd=1, fg="black",font=('arial',20,'bold'),text='5' ,command=lambda:onButtonClick(5), bg="powder blue").grid(row=2,column=1)
button6 = Button(cal,padx =16, bd=1, fg="black",font=('arial',20,'bold'),text='6', command=lambda:onButtonClick(6), bg="powder blue").grid(row=2,column=2)
subbutton = Button(cal,padx =16, bd=1, fg="black",font=('arial',20,'bold'),text='- ', command=lambda:onButtonClick("-"), bg="powder blue").grid(row=2,column=3)

#=============== Row 3 ==========================
button1 = Button(cal,padx =16, bd=1, fg="black",font=('arial',20,'bold'),text='1',command=lambda:onButtonClick(1), bg="powder blue").grid(row=3,column=0)
button2 = Button(cal,padx =16, bd=1, fg="black",font=('arial',20,'bold'),text='2',command=lambda:onButtonClick(2), bg="powder blue").grid(row=3,column=1)
button3 = Button(cal,padx =16, bd=1, fg="black",font=('arial',20,'bold'),text='3',command=lambda:onButtonClick(3), bg="powder blue").grid(row=3,column=2)
mulbutton = Button(cal,padx =16, bd=1, fg="black",font=('arial',20,'bold'),text='* ',command=lambda:onButtonClick("*"), bg="powder blue").grid(row=3,column=3)

#=============== Row 4 ==========================
button0 = Button(cal,padx =16, bd=1, fg="black",font=('arial',20,'bold'),text='0',command=lambda:onButtonClick(0), bg="powder blue").grid(row=4,column=0)
buttoneq = Button(cal,padx =16, bd=1, fg="black",font=('arial',20,'bold'),text='=',command=onButtonEq, bg="powder blue").grid(row=4,column=1)
divbutton = Button(cal,padx =16, bd=1, fg="black",font=('arial',20,'bold'),text='/ ',command=lambda:onButtonClick("/"), bg="powder blue").grid(row=4,column=2)
buttonC = Button(cal,padx =16, bd=1, fg="black", font=('arial',20,'bold'),text='C',command=onButtonClear, bg="powder blue").grid(row=4,column=3)




cal.mainloop()

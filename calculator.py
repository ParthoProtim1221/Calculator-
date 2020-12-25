from tkinter import *

def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    txt_input.set(operator)

def btnClear():
    global operator
    operator=""
    txt_input.set("")

def btnEqual():
    global operator
    res = str(eval(operator))
    txt_input.set(res)
    operator=""

cal = Tk()
cal.title("Partho's Calculator")
operator = ""
txt_input = StringVar()

txtDisplay = Entry(cal, font=('times new roman', 20, 'bold'), textvariable = txt_input, bd = 30,
                   insertwidth = 4, bg = 'light blue', justify ='right').grid(columnspan=8)

btn7 = Button(cal, padx=16, bd=8, fg='black',font=('times new roman', 20, 'bold'),text ="7",bg = 'light blue',command=lambda:btnClick(7)).grid(row=1,column=0)
btn8 = Button(cal, padx=16, bd=8, fg='black',font=('times new roman', 20, 'bold'),text ="8",bg = 'light blue',command=lambda:btnClick(8)).grid(row=1,column=1)
btn9 = Button(cal, padx=16, bd=8, fg='black',font=('times new roman', 20, 'bold'),text ="9",bg = 'light blue',command=lambda:btnClick(9)).grid(row=1,column=2)
add  = Button(cal, padx=16, bd=8, fg='black',font=('times new roman', 20, 'bold'),text ="+",bg = 'light blue',command=lambda:btnClick("+")).grid(row=1,column=4)

btn4 = Button(cal, padx=16, bd=8, fg='black',font=('times new roman', 20, 'bold'),text ="4",bg = 'light blue',command=lambda:btnClick(4)).grid(row=2,column=0)
btn5 = Button(cal, padx=16, bd=8, fg='black',font=('times new roman', 20, 'bold'),text ="5",bg = 'light blue',command=lambda:btnClick(5)).grid(row=2,column=1)
btn6 = Button(cal, padx=16, bd=8, fg='black',font=('times new roman', 20, 'bold'),text ="6",bg = 'light blue',command=lambda:btnClick(6)).grid(row=2,column=2)
min  = Button(cal, padx=16, bd=8, fg='black',font=('times new roman', 20, 'bold'),text ="-",bg = 'light blue',command=lambda:btnClick("-")).grid(row=2,column=4)

btn1 = Button(cal, padx=16, bd=8, fg='black',font=('times new roman', 20, 'bold'),text ="1",bg = 'light blue',command=lambda:btnClick(1)).grid(row=3,column=0)
btn2 = Button(cal, padx=16, bd=8, fg='black',font=('times new roman', 20, 'bold'),text ="2",bg = 'light blue',command=lambda:btnClick(2)).grid(row=3,column=1)
btn3 = Button(cal, padx=16, bd=8, fg='black',font=('times new roman', 20, 'bold'),text ="3",bg = 'light blue',command=lambda:btnClick(3)).grid(row=3,column=2)
mul  = Button(cal, padx=16, bd=8, fg='black',font=('times new roman', 20, 'bold'),text ="*",bg = 'light blue',command=lambda:btnClick("*")).grid(row=3,column=4)

btn0 = Button(cal, padx=16, pady=16, bd=8, fg='black',font=('times new roman', 20, 'bold'),text ="0",bg = 'light blue',command=lambda:btnClick(0)).grid(row=4,column=0)
cButton = Button(cal, padx=16, pady=16 ,bd=8, fg='black',font=('times new roman', 20, 'bold'),text ="C",bg = 'light blue',command=lambda:btnClear()).grid(row=4,column=1)
equal = Button(cal, padx=16, pady=16 ,bd=8, fg='black',font=('times new roman', 20, 'bold'),text ="=",bg = 'light blue',command=lambda:btnEqual()).grid(row=4,column=2)
div = Button(cal, padx=16, pady=16 ,bd=8, fg='black',font=('times new roman', 20, 'bold'),text ="/",bg = 'light blue',command=lambda:btnClick("/")).grid(row=4,column=4)

cal.mainloop()

from tkinter import *
from tkinter.messagebox import *
from PIL import Image,ImageTk
#some useful variable
font=('Verdana',22,'bold')

#Important functions
def click_button_function(event):
    text=event.widget['text']
    print(text)
    if(text!='<--' and text!='<<'):
        textfield.insert('end',text)

    if(text=='='):
        try:
            opt=textfield.get()
            sol=eval(opt[0:len(opt)-1])
            textfield.delete(0,'end')
            textfield.insert('end',sol)
        except Exception as e:
            showerror('Error',e)
            textfield.delete(0,END)
    if(text=='<<'):
        textfield.delete(0,END)
    if(text=='<--'):
        eg=textfield.get()
        eg1=eg[0:len(eg)-1]
        textfield.delete(0,'end')
        textfield.insert('end',eg1)

#Creating a window
window=Tk()
window.title("My Calculator")
window.geometry('450x600')

#Picture lable
pic= Image.open('calculator/calc1.png').resize((100,100))
img=ImageTk.PhotoImage(pic)

headingLable=Label(window, image=img)#lable ko add krna he main window me
headingLable.pack(side=TOP,pady=0)

heading=Label(window,text='My Calculator',font=font,underline=0)
heading.pack(side=TOP)

#textfield
textfield=Entry(window,font=font, justify="center")
textfield.pack(side=TOP, pady=5, fill='x',padx=10)

#Buttons
buttonframe= Frame(window)#frame is invisible
buttonframe.pack(side='top')
#adding button
temp=1
for i in range(3):
    for j in range(3):
        btn=Button(buttonframe,text=str(temp),font=font,width=4,relief='ridge',activebackground='lightgreen',activeforeground='white')
        btn.grid(row=i,column=j,padx=5,pady=5)
        temp=temp+1
        btn.bind('<Button-1>',click_button_function)
btnZero=Button(buttonframe,text='0',font=font,width=4,relief='ridge',activebackground='lightgreen')
btnZero.grid(row=3,column=0,padx=5,pady=5)
btnDot=Button(buttonframe,text='.',font=font,width=4,relief='ridge',activebackground='lightgreen')
btnDot.grid(row=3,column=1,padx=5,pady=5)
btnEqual=Button(buttonframe,text='=',font=font,width=4,relief='ridge',activebackground='lightgreen')
btnEqual.grid(row=3,column=2,padx=5,pady=5)
operations=['+','-','*','/']
temp2=0
for i in operations:
    btn2=Button(buttonframe,text=i,font=font,width=4,relief='ridge',activebackground='lightgreen')
    btn2.grid(row=temp2,column=3,padx=5,pady=5)
    temp2+=1
    btn2.bind('<Button-1>',click_button_function)
btnClear=Button(buttonframe,text='<--',font=font,width=8,relief='ridge')
btnClear.grid(row=4,column=0,columnspan=2,padx=5,pady=5)
btnAllClear=Button(buttonframe,text='<<',font=font,width=8,relief='ridge')
btnAllClear.grid(row=4,column=2,columnspan=2,padx=5,pady=5)

#Personal Info
label2=Label(window,font=('Verdana',15,'bold'),text='Developed by Pranjal Raghuvanshi')
label2.pack(side='bottom')

#Binding all buttons
btnZero.bind('<Button-1>',click_button_function)
btnDot.bind('<Button-1>',click_button_function)
btnEqual.bind('<Button-1>',click_button_function)
btnClear.bind('<Button-1>',click_button_function)
btnAllClear.bind('<Button-1>',click_button_function)

window.mainloop()
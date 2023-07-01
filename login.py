#import Part
from tkinter import *
from PIL import ImageTk
import socket
import mysql.connector
import os
from subprocess import call


#cheake internet connection 
def check_internet_connection():
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=3)
        return True
    except socket.error:
        return False
    

main_Function=check_internet_connection()


def software_Run(x):
    if x == True:
        #backend
        def on_enter(event):
            if userEntry.get()=='ENTER FACULTY ID':
                userEntry.delete(0,END)
        def on_passEnter(event):
            if passwordEntry.get()=='ENTER PASSWORD':
                passwordEntry.delete(0,END)
        def hide():
            open_eye.config(file='log_img/close_eye.png')
            passwordEntry.config(show='*')
            eyebtn.config(command=show)
        def show():
            open_eye.config(file='log_img/eye.png')
            passwordEntry.config(show='')
            eyebtn.config(command=hide)
        
        #MY SQL CONNECTION
        def onClick_login():
            conn = mysql.connector.connect(host="localhost",port="3306",user="root",password="",database="app_db")
            cursor=conn.cursor()
        
            selectQuery="select * from login_id"

            cursor.execute(selectQuery)

            records = cursor.fetchall()
            print(cursor.rowcount)
            user_value=userEntry.get()
            passwor_value=passwordEntry.get()
            for row in records:
                if row[1]==user_value and row[2]==passwor_value:
                    root.destroy()
                    call(['python','main.py'])
                else:
                    return False
            cursor.close()
            conn.close()
        
        #fontend
        root = Tk()
        root.geometry()
        root.title('Online Attendance System Login Page')

        bg_img=ImageTk.PhotoImage(file="log_img/bg.jpg")
        bgLable=Label(root,image=bg_img)
        bgLable.grid(row=0,column=0)

        spu_login_lable = Label(root,text="ONLINE ATTENDANCE SYSTEM",font=('Microsoft Yahsi UI Light',30,'bold'),bg='#011226',fg='#02c1fb')
        spu_login_lable.place(x=100,y=50)

        hading_lable = Label(root,text="FACULTY LOGIN PAGE",font=('Microsoft Yahsi UI Light',23,'bold'),bg='#011226',fg='#02c1fb')
        hading_lable.place(x=1045,y=100)

        userEntry=Entry(root,width=25,font=('Microsoft Yahsi UI Light',14,'bold'),bd=0,fg='#02c1fb',bg='#011226')
        userEntry.place(x=1050,y=220)
        userEntry.insert(0,"ENTER FACULTY ID")
        userEntry.bind('<FocusIn>',on_enter)


        frame1=Frame(root,width=277,height=2,bg='#28fafe')
        frame1.place(x=1050,y=242)



        passwordEntry=Entry(root,width=25,font=('Microsoft Yahsi UI Light',14,'bold'),bd=0,fg='#02c1fb',bg='#011226')
        passwordEntry.place(x=1050,y=300)
        passwordEntry.insert(0,"ENTER PASSWORD")
        passwordEntry.bind('<FocusIn>',on_passEnter)


        frame2=Frame(root,width=277,height=2,bg='#28fafe')
        frame2.place(x=1050,y=322)

        open_eye=PhotoImage(file='log_img/eye.png')
        eyebtn=Button(root,image=open_eye,height=20,bg='#011226',bd=0,activebackground='#011226',cursor='hand2',command=hide)

        eyebtn.place(x=1290,y=300)
        
        loinButton=Button(root,text="Login",font=('Open Sans',16,'bold'),fg='#011226',bg='#02c1fb',activebackground='#02c1fb',cursor='hand2',bd=0,width=21,command=onClick_login)
        loinButton.place(x=1050,y=370)
        
        root.mainloop()
        
        
    else:
        root = Tk()
        root.title('Network Error!')
        root.geometry("660x300")
        root.resizable(False,False)
        root.config(bg="white")
        lable_text=Label(root,text="NETWORK CONNECTION ERROR!",font=('Microsoft Yahsi UI Light',30,'bold'),bg='#011226',fg='#02c1fb')
        lable_text.place(x=0,y=0)
        lable_message=Label(root,text="can you check your internet connection!",font=('Microsoft Yahsi UI Light',22,'bold'),bg='white',fg='#02c1fb')
        lable_message.place(x=0,y=60)
        
        root.mainloop()
        

        
        

software_Run(main_Function)
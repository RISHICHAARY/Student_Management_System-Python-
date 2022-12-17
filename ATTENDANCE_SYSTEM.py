from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
from datetime import date
import random
from twilio.rest import Client
account_sid="AC2c7776ca460f5753af647a63f561c04c"
auth_token="e1e805c8b117b5707a48f0df8df9a05f"
con=sqlite3.connect('User.db')
curs=con.cursor()
curs.execute("create table if not exists Accounts(user_name varchar(25),password varchar(25),Mobno varchar(15))")
con.commit()
curs.execute("create table if not exists Setting(Srt varchar(30),Usr varchar(30),pss varchar(30),Sts varchar(10))")
curs.execute("select Srt from Setting")
i=curs.fetchall()
if(i==[]):
        curs.execute("insert into Setting (Srt) values('3')")
        con.commit()
else:
        pass
def Aut():
        b=curs.execute("select * from accounts")
        d=b.fetchall()
        def SIGN():
                def center_window(w=300, h=200):
                        ws = window1.winfo_screenwidth()
                        hs = window1.winfo_screenheight()
                        x = (ws/2) - (w/2)
                        y = (hs/2) - (h/2)
                        window1.geometry('%dx%d+%d+%d' % (w, h, x, y))
                window1=Tk()
                window1.configure(bg="#920057")
                window1.geometry("550x352")
                window1.overrideredirect(1)
                center_window(550,352)
                Main=Frame(window1,bg="#ffffce")
                Main.pack(padx=25,pady=10)
                Sub=Frame(window1,bg="#ffffce")
                Sub.pack()
                QB=Button(Sub,text="X",padx=10,pady=5,bd=0,bg="#d03636",command=lambda:[window1.destroy()]).pack(anchor="ne")
                User=Label(Sub,font=("vardana",15,'bold'),text="USERNAME:",bg='#ffffce').pack(padx=30,anchor="nw")
                UsN=Entry(Sub,font=("vardana",15),border=0,width="25")
                UsN.pack(padx=100,pady=10,anchor="ne")
                Pon=Label(Sub,font=("vardana",15,'bold'),text="MOBILE NO:",bg='#ffffce').pack(padx=30,anchor="nw")
                PoN=Entry(Sub,font=("vardana",15),border=0,width="25")
                PoN.pack(padx=100,pady=10,anchor='ne')
                Pass=Label(Sub,font=("vardana",15,'bold'),text="PASSWORD:",bg='#ffffce').pack(padx=30,anchor="nw")
                PaN=Entry(Sub,font=("vardana",15),border=0,width="25",show="*")
                PaN.pack(padx=100,pady=10,anchor='ne')
                SB=Button(Sub,font=("vardana",15,'bold'),text="CONFIRM",bg="#ffde59",bd=0,command=lambda:[fun(UsN,PaN,PoN)]).pack(pady=10)
                def fun(UsN,PaN,PoN):
                        a=UsN.get()
                        b1=PaN.get()
                        c1=PoN.get()
                        aa=str(a)
                        bb=str(b1)
                        try:
                                cc=int(c1)
                        except ValueError: messagebox.showinfo("ERROR","ENTER VALID MOBILE NUMBER")
                        if(len(d)==0):
                                rng=1
                        else:
                                rng=len(d)
                        for i in range(0,rng):
                                if(len(d)!=0):
                                        if(d[i][0]==a):
                                                messagebox.showinfo("ERROR","ACCOUNT EXIST")
                                                break
                                        elif(aa=="" or bb==""):
                                                messagebox.showinfo("ERROR","USERNAME OR PASSWORD CANNOT BE EMPTY")
                                                break
                                        else:
                                                curs.execute("insert into Accounts values('{}','{}','{}')".format(a,b1,c1))
                                                con.commit()
                                                messagebox.showinfo("SUCCESS","ACCOUNT CREATED")
                                                window1.destroy()
                                                break
                                else:
                                        if(aa=="" or bb==""):
                                                messagebox.showinfo("ERROR","USERNAME OR PASSWORD CANNOT BE EMPTY")
                                                break
                                        else:
                                                curs.execute("insert into Accounts values('{}','{}','{}')".format(a,b1,c1))
                                                con.commit()
                                                messagebox.showinfo("SUCCESS","ACCOUNT CREATED")
                                                window1.destroy()
                                                break
        def LOG(A,B):
                global a343
                a343=A.get()
                b=B.get()
                aa=a343
                bb=b
                b=curs.execute("select * from accounts")
                d=b.fetchall()
                for i in range(0,len(d)):
                        if(d[i][0]==aa and d[i][1]==bb):
                                window0.destroy()
                                Dashboard(aa)
                                break
                        elif(aa=="" or bb==""):
                                messagebox.showinfo("ERROR","USERNAME OR PASSWORD CANNOT BE EMPTY")
                                break
                        else:
                                if(i==len(d)-1):
                                        messagebox.showinfo("ERROR","INVALID USERNAME OR PASSWORD")
                                        break
        def Fpsw():
                curs.execute("Select User_Name,Mobno from Accounts")
                jil=curs.fetchall()
                def center_window(w=300, h=200):
                        ws = window1.winfo_screenwidth()
                        hs = window1.winfo_screenheight()
                        x = (ws/2) - (w/2)
                        y = (hs/2) - (h/2)
                        window1.geometry('%dx%d+%d+%d' % (w, h, x, y))
                window1=Tk()
                window1.configure(bg="#920057")
                window1.geometry("550x352")
                window1.overrideredirect(1)
                center_window(550,352)
                Main=Frame(window1,bg="#ffffce")
                Main.pack(padx=25,pady=28)
                Sub=Frame(window1,bg="#ffffce")
                Sub.pack()
                QB=Button(Sub,text="X",padx=10,pady=5,bd=0,bg="#d03636",command=lambda:[window1.destroy()]).pack(anchor="ne")
                User=Label(Sub,font=("vardana",15,'bold'),text="USERNAME:",bg='#ffffce').pack(padx=30,anchor="nw")
                UsN=Entry(Sub,font=("vardana",15),border=0,width="25")
                UsN.pack(padx=100,pady=10,anchor="ne")
                Pon=Label(Sub,font=("vardana",15,'bold'),text="MOBILE NO:",bg='#ffffce').pack(padx=30,anchor="nw")
                PoN=Entry(Sub,font=("vardana",15),border=0,width="25")
                PoN.pack(padx=100,pady=10,anchor='ne')
                SB=Button(Sub,font=("vardana",15,'bold'),text="SEND OTP",bg="#ffde59",bd=0,command=lambda:[OTP(UsN,PoN),window1.destroy()]).pack(pady=10)
                def OTP(UsN,PoN):
                        a=UsN.get()
                        c1=PoN.get()
                        aa=str(a)
                        bb=str(c1)
                        b=curs.execute("select User_Name,Mobno from accounts")
                        d=b.fetchall()
                        for i in range(0,len(d)):
                                if(d[i][0]==aa and d[i][1]==bb):
                                        def center_window(w=300, h=200):
                                                ws = window11.winfo_screenwidth()
                                                hs = window11.winfo_screenheight()
                                                x = (ws/2) - (w/2)
                                                y = (hs/2) - (h/2)
                                                window11.geometry('%dx%d+%d+%d' % (w, h, x, y))
                                        window11=Tk()
                                        window11.configure(bg="#920057")
                                        window11.geometry("550x250")
                                        window11.overrideredirect(1)
                                        center_window(550,250)
                                        Main=Frame(window11,bg="#ffffce")
                                        Main.pack(padx=25,pady=28)
                                        Sub=Frame(window11,bg="#ffffce").pack()
                                        QB=Button(Main,text="X",padx=10,pady=5,bd=0,bg="#d03636",command=lambda:[window11.destroy()]).pack(anchor="ne")
                                        User1=Label(Main,font=("vardana",15,'bold'),text="OTP sent to: "+bb,bg='#ffffce').pack(padx=30,anchor="nw")
                                        User=Label(Main,font=("vardana",15,'bold'),text="ENTER OTP:",bg='#ffffce').pack(padx=30,anchor="nw")
                                        UsN=Entry(Main,font=("vardana",15),border=0,width="25")
                                        UsN.pack(padx=100,pady=10,anchor="ne")
                                        Opt1=random.randint(1000,9999)
                                        SB=Button(Main,font=("vardana",15,'bold'),text="VERIFY",bg="#ffde59",bd=0,command=lambda:[Psc(Opt1,UsN),window11.destroy()]).pack(pady=10)
                                        client=Client(account_sid,auth_token)
                                        message=client.messages.create(body="Hi!! "+aa+" use "+str(Opt1)+" as your one time password.",from_="+13349662713",to="+91"+bb)
                                        def Psc(Z,S):
                                                sd=S.get()
                                                if(str(Z)==str(sd)):
                                                        def center_window(w=300, h=200):
                                                                ws = window112.winfo_screenwidth()
                                                                hs = window112.winfo_screenheight()
                                                                x = (ws/2) - (w/2)
                                                                y = (hs/2) - (h/2)
                                                                window112.geometry('%dx%d+%d+%d' % (w, h, x, y))
                                                        window112=Tk()
                                                        window112.configure(bg="#920057")
                                                        window112.geometry("550x250")
                                                        window112.overrideredirect(1)
                                                        center_window(550,250)
                                                        Main=Frame(window112,bg="#ffffce")
                                                        Main.pack(padx=25,pady=28)
                                                        Sub=Frame(window112,bg="#ffffce").pack()
                                                        QB=Button(Main,text="X",padx=10,pady=5,bd=0,bg="#d03636",command=lambda:[window11.destroy()]).pack(anchor="ne")
                                                        User1=Label(Main,font=("vardana",15,'bold'),text="USERNAME: "+aa,bg='#ffffce').pack(padx=30,anchor="nw")
                                                        User=Label(Main,font=("vardana",15,'bold'),text="NEW PASSWORD:",bg='#ffffce').pack(padx=30,anchor="nw")
                                                        UsN=Entry(Main,font=("vardana",15),border=0,width="25")
                                                        UsN.pack(padx=100,pady=10,anchor="ne")
                                                        def Ccp(D):
                                                                vi=D.get()
                                                                curs.execute("update Accounts set password ='{}'where user_name='{}' ".format(vi,aa))
                                                                con.commit()
                                                                messagebox.showinfo("Success","PASSWORD CHANGED")
                                                                window112.destroy()
                                                        SB=Button(Main,font=("vardana",15,'bold'),text="CONFIRM",bg="#ffde59",bd=0,command=lambda:[Ccp(UsN)]).pack(pady=10)
                                                else:
                                                        messagebox.showinfo("Error","INVALID OTP")
                                        break
                                elif(aa=="" or bb==""):
                                        messagebox.showinfo("ERROR","USERNAME OR MOBILE NO CANNOT BE EMPTY")
                                        window1.destroy()
                                        break
                                else:
                                        if(i==len(d)-1):
                                                messagebox.showinfo("ERROR","USERNAME AND MOBILE NO MISS MATCH")
                                                window1.destroy()
                                                break
        def center_window(w=300, h=200):
            # get screen width and height
            ws = window0.winfo_screenwidth()
            hs = window0.winfo_screenheight()
            # calculate position x, y
            x = (ws/2) - (w/2)    
            y = (hs/2) - (h/2)
            window0.geometry('%dx%d+%d+%d' % (w, h, x, y))
        b34=curs.execute("select Usr,pss from Setting")
        b32=b34.fetchall()
        window0=Tk()
        window0.title("TAKE IT EASY")
        window0.geometry("1535x865")
        window0.overrideredirect(1)
        center_window(1540,868)
        IT=PhotoImage(file="LoginBG.png")
        Cvas1=Canvas(window0)
        Cvas1.pack(fill="both",expand=True)
        Cvas1.create_image(0,0,image=IT,anchor="nw")
        User=Label(window0,font=("vardana",25,'bold'),text="USERNAME:",bg='#ffffce')
        User_window=Cvas1.create_window(920,350,anchor="nw",window=User)
        UsN=Entry(window0,font=("vardana",25),border=0,width="25")
        UsN_Window=Cvas1.create_window(920,400,anchor="nw",window=UsN)
        Pass=Label(window0,font=("vardana",25,'bold'),text="PASSWORD:",bg='#ffffce')
        Pass_window=Cvas1.create_window(920,450,anchor="nw",window=Pass)
        PaN=Entry(window0,font=("vardana",25),border=0,width="25",show="*")
        PaN_Window=Cvas1.create_window(920,500,anchor="nw",window=PaN)
        if(b32[0][0]!= None):
            UsN.insert(END,b32[0][0])
            PaN.insert(END,b32[0][1])
        else:
            pass
        SB=Button(window0,font=("vardana",15,'bold'),text="Not An User? Signup",bg="#ffffce",bd=0,command=lambda:[SIGN()])
        SB_Window=Cvas1.create_window(1030,640,anchor="nw",window=SB)
        FP=Button(window0,font=("vardana",15,'bold'),text="Forgot Password?",bg="#ffffce",bd=0,command=lambda:[Fpsw()])
        FP_Window=Cvas1.create_window(920,540,anchor="nw",window=FP)
        LB=Button(window0,font=("vardana",15,'bold'),text="LOGIN",bg="green2",padx=30,bd=0,command=lambda:[LOG(UsN,PaN)])
        LB_Window=Cvas1.create_window(1070,590,anchor="nw",window=LB)
        QB=Button(window0,text="X",padx=10,pady=5,bd=0,bg="#d03636",command=lambda:[window0.quit()])
        QB_Window=Cvas1.create_window(1538,0,anchor="ne",window=QB)
        window0.mainloop()
def Dashboard(Usr):
        def center_window(w=300, h=200):
            # get screen width and height
            ws = window.winfo_screenwidth()
            hs = window.winfo_screenheight()
            # calculate position x, y
            x = (ws/2) - (w/2)    
            y = (hs/2) - (h/2)
            window.geometry('%dx%d+%d+%d' % (w, h, x, y))
        con1=sqlite3.connect('{}.db'.format(Usr))
        curs1=con1.cursor()
        curs1.execute("create table if not exists Presdetl(Adno varchar(30),Name varchar(30),Dob varchar(25),"
                      "Gndr varchar(10),email varchar(30),adrs varchar(100),Fname varchar(30),Fpn varchar(15),"
                      "Focc varchar(25),Fanualinc varchar(15),Mname varchar(30),Mpn varchar(15),Mocc varchar(25),"
                      "Manualinc varchar(15))")
        curs1.execute("create table if not exists Att(Date varchar(15))")
        curs1.execute("create table if not exists Mrk(Name varchar(30))")
        con1.commit()
        window=Tk()
        window.title("TAKE IT EASY")
        window.geometry("1538x865")
        window.overrideredirect(1)
        center_window(1538,865)
        Main=Frame(window,bg="black")
        Main.pack(side=RIGHT)
        Menu=Frame(window,bg="#920057")
        Menu.pack(side=LEFT)
        IT=PhotoImage(file="Logo1.png")
        bc=PhotoImage(file="Bbg1.png")
        Cvas11=Canvas(Menu,bg="#920057",bd=0, highlightthickness=0,height=865,width=260)
        Cvas11.pack(fill="both",expand=True)
        Cvas11.create_image(30,10,image=IT,anchor="nw")
        Cvas11.create_image(10,310,image=bc,anchor="nw")
        User=Label(Menu,font=("vardana",21,'bold'),text="ATTENDANCE\nSYSTEM",bg='#920057')
        User_window=Cvas11.create_window(30,211,anchor="nw",window=User)
        Adcl=Button(Menu,font=("vardana",15,'bold'),text="ADD STUDENT",bg="#ffde59",border=0,padx=43,command=lambda:[adstud(window,Main1,Usr)])
        Adcl_window=Cvas11.create_window(10,395,anchor="nw",window=Adcl)
        Prof=Button(Menu,font=("vardana",15,'bold'),text="PROFILE",bg="#ffde59",border=0,padx=71,command=lambda:[prof(window,Main1,Usr)])
        Prof_window=Cvas11.create_window(10,495,anchor="nw",window=Prof)
        Att=Button(Menu,font=("vardana",15,'bold'),text="ATTENDANCE",bg="#ffde59",border=0,padx=47,command=lambda:[atd(window,Main1,Usr)])
        Att_window=Cvas11.create_window(10,445,anchor="nw",window=Att)
        Mrk=Button(Menu,font=("vardana",15,'bold'),text="MARK",bg="#ffde59",border=0,padx=85,command=lambda:[mrkreg(window,Main1,Usr)])
        Mrk_window=Cvas11.create_window(10,545,anchor="nw",window=Mrk)
        Ste=Button(Menu,font=("vardana",15,'bold'),text="SETTINGS",bg="#ffde59",border=0,padx=63,command=lambda:[Set()])
        Ste_window=Cvas11.create_window(10,595,anchor="nw",window=Ste)
        def Dbr(A,B,C):
                B.destroy()
                global Main1
                Main1=Frame(A,bg="#5ce1e6",pady=20,padx=20)
                Main1.pack(side=RIGHT)
                Qt=Button(Main1,text="X",bg="#d03636",border=0,padx=10,pady=5,command=lambda:[window.destroy()])
                Qt.pack(anchor="ne",pady=5,padx=5)
                Nmlst=Frame(Main1,bg="#ffffce")
                Nmlst.pack()
                Wlcm=Label(Nmlst,text="WELCOME!!",font=("vardana",25,'bold'),bg="#ffffce").pack(side=TOP,padx=520,pady=370)
        Dbr(window,Main,Usr)
        def Btdis():
                Prof.configure(state=DISABLED)
                Att.configure(state=DISABLED)
                Mrk.configure(state=DISABLED)
                Adcl.configure(state=DISABLED)
        def Btenb():
                Prof.configure(state=NORMAL)
                Att.configure(state=NORMAL)
                Mrk.configure(state=NORMAL)
                Adcl.configure(state=NORMAL)
        def prof(A,B,C):
                Btdis()
                B.destroy()
                Main=Frame(A,bg="#5ce1e6",pady=25,padx=20)
                Main.pack(side=RIGHT)
                Sub=Frame(Main,bg="#5ce1e6")
                Sub.pack()
                Nmlst=Frame(Sub,bg="#ffffce")
                Nmlst.pack(side=LEFT)
                Nmslt=Frame(Nmlst,bg="#ffffce",pady=10)
                Nmslt.pack(side=BOTTOM,pady=7)
                Dsp=Frame(Sub,bg="#ffffce")
                Dsp.pack(side=RIGHT)
                Dps=Frame(Dsp,bg="#ffffce",pady=5)
                Qt = Button(Dsp, text="<", bg="#d03636", padx=10, pady=5, bd=0,command=lambda: [Main.destroy(), Btenb(), Dbr(A, B, C)])
                Qt.pack(pady=5, padx=0, anchor="ne")
                Dps.pack(side=BOTTOM)
                H1=Label(Nmlst,text="NAME LIST",font=("Microsoft Sans Serif",20,'bold'),bg="#ffffce").pack(padx=130,pady=23)
                NMlst=Frame(Nmlst,bg="#ffffce")
                NMlst.pack(side=TOP,pady=20)
                H2=Label(Dsp,text="STUDENT PROFILE",font=("Microsoft Sans Serif",25,'bold'),bg="#ffffce").pack(side=TOP,padx=250,pady=3)
                Display=Text(Dps,font=('Microsoft Sans Serif',20),width=50,height=23,bg="#ffffce",border=0)
                Display.pack()
                def ret(evt):
                        Display.configure(state=NORMAL)
                        Display.delete(1.0,END)
                        curs1.execute("select Name from Presdetl")
                        iret=curs1.fetchall()
                        kret=[]
                        for ic in range(len(iret)):
                                lk=str(iret[ic][0])
                                pk=[lk]
                                kret=kret+pk
                        value=str(booklist.get(booklist.curselection()))
                        gf=value
                        for i in range(0,len(kret)):
                                if(gf==kret[i]):
                                        curs1.execute("select * from Presdetl where Name like '{}'".format(kret[i]))
                                        iret1=curs1.fetchall()
                                        kret1=[]
                        for ic in range(len(iret1)):
                                lk=str(iret1[ic][0])
                                lk1=str(iret1[ic][1])
                                lk2=str(iret1[ic][2])
                                lk3=str(iret1[ic][3])
                                lk4=str(iret1[ic][4])
                                lk5=str(iret1[ic][5])
                                lk6=str(iret1[ic][6])
                                lk7=str(iret1[ic][7])
                                lk8=str(iret1[ic][8])
                                lk9=str(iret1[ic][9])
                                lk10=str(iret1[ic][10])
                                lk11=str(iret1[ic][11])
                                lk12=str(iret1[ic][12])
                                lk13=str(iret1[ic][13])
                                pk=[lk,lk1,lk2,lk3,lk4,lk5,lk6,lk7,lk8,lk9,lk10,lk11,lk12,lk13]
                                kret1=kret1+pk
                        for jkl in range(len(kret1)):
                                if(jkl==(0)):
                                        Display.insert(END,"STUDENT DETAILS: \n\nADMISSION NO: "+kret1[0])
                                elif(jkl==1):
                                        Display.insert(END,"\nNAME: "+kret1[1])
                                elif(jkl==2):
                                    Display.insert(END,"\nDOB: "+kret1[2])
                                elif(jkl==3):
                                    Display.insert(END,"\nGENDER: "+kret1[3])
                                elif(jkl==4):
                                    Display.insert(END,"\nE-MAIL: "+kret1[4])
                                elif(jkl==5):
                                    Display.insert(END,"\nADDRESS: "+kret1[5])
                                elif(jkl==6):
                                    Display.insert(END,"\n\nFATHER'S DETAILS: \n\nFATHER'S NAME: "+kret1[6])
                                elif(jkl==7):
                                    Display.insert(END,"\nFATHER'S P.NO: "+kret1[7])
                                elif(jkl==8):
                                    Display.insert(END,"\nFATHER'S OCCUPATION: "+kret1[8])
                                elif(jkl==9):
                                    Display.insert(END,"\nFATHER'S ANUAL INCOME: "+kret1[9])
                                elif(jkl==10):
                                    Display.insert(END,"\n\nMOTHER'S DETAILS: \n\nMOTHER'S NAME: "+kret1[10])
                                elif(jkl==11):
                                    Display.insert(END,"\nMOTHER'S P.NO: "+kret1[11])
                                elif(jkl==12):
                                    Display.insert(END,"\nMOTHER'S OCCUPATION: "+kret1[12])
                                elif(jkl==13):
                                    Display.insert(END,"\nMOTHER'S ANUAL INCOME: "+kret1[13])
                        Display.configure(state=DISABLED)
                curs.execute("select Srt from Setting")
                i=curs.fetchall()
                if(i[0][0]=="1"):
                        curs1.execute("select Name from Presdetl order by Name asc")
                elif(i[0][0]=="2"):
                        curs1.execute("select Name from Presdetl order by Adno asc")
                else:
                        curs1.execute("select Name from Presdetl")
                i=curs1.fetchall()
                k=[]
                for ic in range(len(i)):
                    lk=str(i[ic][0])
                    pk=[lk]
                    k=k+pk
                ListOfBooks=k
                scrollbar=Scrollbar(NMlst)
                scrollbar.grid(row=0,column=1,st='ns')
                booklist=Listbox(NMlst,width=20,height=21,font=('Microsoft Sans Serif',20),bd=0,bg="#ffffce")
                booklist.bind('<<ListboxSelect>>',ret)
                booklist.grid(row=0,column=0,padx=8,pady=0)
                scrollbar.config(command=booklist.yview)
                for items in ListOfBooks:
                        booklist.insert(END,items)
        def atd(A,B,C):
                Btdis()
                B.destroy()
                de=date.today()
                fg=de.strftime("%Y-%m-%d")
                Main=Frame(A,bg="#5ce1e6",pady=22,padx=35)
                Main.pack(side=RIGHT)
                Nmlst=Frame(Main,bg="#ffffce",pady=5)
                Nmlst.pack(side=TOP)
                NmH1=Frame(Nmlst,bg="#ffffce")
                NmH1.pack(side=TOP,pady=10)
                Qt=Button(NmH1,text="<",bg="#d03636",padx=10,pady=5,bd=0,command=lambda:[Main.destroy(),Btenb(),Dbr(A,B,C)])
                Qt.pack(anchor="ne")
                NmH2=Frame(Nmlst,bg="#ffffce",padx=30)
                NmH2.pack(side=BOTTOM)
                NmSH1=Frame(NmH2,bg="#ffffce")
                NmSH1.pack(side=LEFT)
                NmSH2=Frame(NmH2,bg="#ffffce",padx=10)
                NmSH2.pack(side=RIGHT)
                NmSH21=Frame(NmSH2,bg="#ffffce")
                NmSH21.pack(side=TOP,padx=60)
                NmSH22=Frame(NmSH2,bg="#ffffce",padx=10)
                NmSH22.pack(side=BOTTOM,padx=50)
                Nmslt=Frame(Main,bg="#5ce1e6")
                Nmslt.pack(side=BOTTOM,pady=10)
                H1=Label(NmH1,text="ATTENDANCE REGISTER",font=("vardana",25,'bold'),bg="#ffffce").pack(padx=400,pady=0)
                Atd=Button(Nmslt,font=("vardana",15,'bold'),text="MARK ATTENDANCE",bg="#ffde59",padx=30,command=lambda:[Atd.configure(state=DISABLED),updt(A,B,C)])
                Atd.pack(side=LEFT,padx=5)
                Dt=Label(NmSH21,text="DATE:",font=("vardana",20,'bold'),bg="#ffffce").grid(row=0,column=0,sticky="ne")
                war1=Label(NmSH1,text="*SELECT ABSENTIES",font=("vardana",10),bg="#ffffce").grid(row=1,column=0)
                Nm_ent=Entry(NmSH21,font=("vardana",20,'bold'),border=0,bg="#ffffce",width=30)
                Nm_ent.grid(row=0,column=1,sticky="nw")
                Nm_ent.insert(END,fg)
                Display=Text(NmSH22,font=('Microsoft Sans Serif',20),width=40,height=19,border=1,bg="#ffffce")
                Display.pack()
                war2=Label(NmSH22,text="*BACKSPACE TO REMOVE ABSENTIES",font=("vardana",10),bg="#ffffce").pack()
                def ver(evt):
                        value=str(booklist.get(booklist.curselection()))
                        gf=value
                        df=gf.split("(")
                        Display.insert(END,"\n"+df[0])
                curs.execute("select Srt from Setting")
                i=curs.fetchall()
                if(i[0][0]=="1"):
                        curs1.execute("select Name from Presdetl order by Name asc")
                elif(i[0][0]=="2"):
                        curs1.execute("select Name from Presdetl order by Adno asc")
                else:
                        curs1.execute("select Name from Presdetl")
                i=curs1.fetchall()
                k=[]
                for ic in range(len(i)):
                    lk=str(i[ic][0])
                    curs1.execute("select count({}) from Att where {} like 'P'".format(i[ic][0].replace(" ",""),i[ic][0].replace(" ","")))
                    Presn=curs1.fetchall()
                    curs1.execute("select count(*) from Att")
                    Actl=curs1.fetchall()
                    if(Presn[0][0]==0):
                        prt=0
                    else:
                        prt=(Presn[0][0]/Actl[0][0])*100
                    prtf=lk+"("+str(prt)+")%"
                    pk=[prtf]
                    k=k+pk
                ListOfBooks=k
                scrollbar=Scrollbar(NmSH1)
                scrollbar.grid(row=0,column=1,st='nwns')
                booklist=Listbox(NmSH1,width=25,height=19,font=('Microsoft Sans Serif',20),border=0,bg="#ffffce")
                booklist.bind('<<ListboxSelect>>',ver)
                booklist.grid(row=0,column=0,padx=8,pady=0)
                scrollbar.config(command=booklist.yview)
                for items in ListOfBooks:
                        booklist.insert(END,items)
                def updt(A,B,S):
                        A1=Display.get(1.0,"end-1c")
                        B1=A1.split("\n")
                        C1=Nm_ent.get()
                        curs1.execute("select Date from Att")
                        Actl1=curs1.fetchall()
                        if(Actl1==[]):
                                Nb=1
                        else:
                                Nb=len(Actl1)
                        for ik in range(0,Nb):
                                if(Actl1==[]):
                                        curs1.execute("insert into Att (Date) values('{}')".format(C1))
                                        con1.commit()
                                elif(str(C1)==Actl1[ik][0]):
                                        break
                                else:
                                        if(ik==len(Actl1)-1):
                                                curs1.execute("insert into Att (Date) values('{}')".format(C1))
                                                con1.commit()
                        curs1.execute("select Name from Presdetl")
                        i=curs1.fetchall()
                        for j in range (0,len(i)):
                                if(i[j][0] in B1):
                                        curs1.execute("update Att set '{}'='A' where date like '{}'".format(i[j][0].replace(" ",""),C1))
                                        con1.commit()
                                else:
                                       curs1.execute("update Att set '{}'='P' where date like '{}'".format(i[j][0].replace(" ",""),C1))
                                       con1.commit()
                        messagebox.showinfo("SUCCESS","MARKED SUCCESSFULY")
                        A.destroy()
                        Dashboard(S)
        def mrkreg(A,B,C):
                Btdis()
                B.destroy()
                Main=Frame(A,bg="#5ce1e6",pady=22,padx=20)
                Main.pack(side=RIGHT)
                Nmlst=Frame(Main,bg="#ffffce",pady=5)
                Nmlst.pack(side=TOP)
                NmH1=Frame(Nmlst,bg="#ffffce")
                NmH1.pack(side=TOP,pady=10)
                Qt=Button(NmH1,text="<",bg="#d03636",padx=10,pady=5,bd=0,command=lambda:[Main.destroy(),Btenb(),Dbr(A,B,C)])
                Qt.pack(anchor="ne")
                NmH2=Frame(Nmlst,bg="#ffffce")
                NmH2.pack(side=BOTTOM)
                NmSH1=Frame(NmH2,bg="#ffffce")
                NmSH1.pack(side=LEFT)
                NmSH2=Frame(NmH2,bg="#ffffce")
                NmSH2.pack(side=LEFT)
                NmSH3=Frame(NmH2,bg="#ffffce")
                NmSH3.pack(side=RIGHT)
                Nmslt=Frame(Main,bg="#5ce1e6",pady=12)
                Nmslt.pack(side=BOTTOM,pady=5)
                H1=Label(NmH1,text="MARK REGISTER",font=("vardana",25,'bold'),bg="#ffffce").pack(padx=480,pady=1)
                Atd=Button(Nmslt,font=("vardana",15,'bold'),text="+ ADD MARK",bg="#ffde59",padx=30,command=lambda:[rec()])
                Atd.pack(side=LEFT,padx=5)
                H11=Label(NmSH2,text="SUBJECT",font=("vardana",25,'bold'),bg="#ffffce").grid(row=0,column=0,padx=20)
                H12=Label(NmSH2,text="MARK",font=("vardana",25,'bold'),bg="#ffffce").grid(row=0,column=1,padx=10)
                Sm1_ent=Entry(NmSH2,font=("Microsoft Sans Serif",15,'bold'),border=0,fg="black",bg="white",width=15)
                Sm1_ent.grid(row=1,column=0,pady=10)
                Sm2_ent=Entry(NmSH2,font=("Microsoft Sans Serif",15,'bold'),border=0,fg="black",bg="white",width=15)
                Sm2_ent.grid(row=2,column=0,pady=10)
                Sm3_ent=Entry(NmSH2,font=("Microsoft Sans Serif",15,'bold'),border=0,fg="black",bg="white",width=15)
                Sm3_ent.grid(row=3,column=0,pady=10)
                Sm4_ent=Entry(NmSH2,font=("Microsoft Sans Serif",15,'bold'),border=0,fg="black",bg="white",width=15)
                Sm4_ent.grid(row=4,column=0,pady=10)
                Sm5_ent=Entry(NmSH2,font=("Microsoft Sans Serif",15,'bold'),border=0,fg="black",bg="white",width=15)
                Sm5_ent.grid(row=5,column=0,pady=10)
                Sm6_ent=Entry(NmSH2,font=("Microsoft Sans Serif",15,'bold'),border=0,fg="black",bg="white",width=15)
                Sm6_ent.grid(row=6,column=0,pady=10)
                Sm7_ent=Entry(NmSH2,font=("Microsoft Sans Serif",15,'bold'),border=0,fg="black",bg="white",width=15)
                Sm7_ent.grid(row=7,column=0,pady=10)
                Smr1_ent=Entry(NmSH2,font=("Microsoft Sans Serif",15,'bold'),border=0,fg="black",bg="white",width=4)
                Smr1_ent.grid(row=1,column=1,pady=10)
                Smr2_ent=Entry(NmSH2,font=("Microsoft Sans Serif",15,'bold'),border=0,fg="black",bg="white",width=4)
                Smr2_ent.grid(row=2,column=1,pady=10)
                Smr3_ent=Entry(NmSH2,font=("Microsoft Sans Serif",15,'bold'),border=0,fg="black",bg="white",width=4)
                Smr3_ent.grid(row=3,column=1,pady=10)
                Smr4_ent=Entry(NmSH2,font=("Microsoft Sans Serif",15,'bold'),border=0,fg="black",bg="white",width=4)
                Smr4_ent.grid(row=4,column=1,pady=10)
                Smr5_ent=Entry(NmSH2,font=("Microsoft Sans Serif",15,'bold'),border=0,fg="black",bg="white",width=4)
                Smr5_ent.grid(row=5,column=1,pady=10)
                Smr6_ent=Entry(NmSH2,font=("Microsoft Sans Serif",15,'bold'),border=0,fg="black",bg="white",width=4)
                Smr6_ent.grid(row=6,column=1,pady=10)
                Smr7_ent=Entry(NmSH2,font=("Microsoft Sans Serif",15,'bold'),border=0,fg="black",bg="white",width=4)
                Smr7_ent.grid(row=7,column=1,pady=10)
                H13=Label(NmSH2,text="EXAM NAME",font=("vardana",25,'bold'),bg="#ffffce").grid(row=8,column=0)
                Sm11_ent=Entry(NmSH2,font=("Microsoft Sans Serif",15,'bold'),border=0,fg="black",bg="white",width=15)
                Sm11_ent.grid(row=9,column=0,pady=10)
                H14=Label(NmSH2,text="NAME",font=("vardana",25,'bold'),bg="#ffffce").grid(row=10,column=0)
                Sm12_ent=Entry(NmSH2,font=("Microsoft Sans Serif",15,'bold'),border=0,fg="black",bg="white",width=15)
                Sm12_ent.grid(row=11,column=0,pady=10)
                Display=Text(NmSH3,font=('Microsoft Sans Serif',20),width=35,bg="#ffffce",height=19,border=0)
                Display.pack()
                def rec():
                        A=Sm1_ent.get()
                        B=Sm2_ent.get()
                        C=Sm3_ent.get()
                        D=Sm4_ent.get()
                        E=Sm5_ent.get()
                        F=Sm6_ent.get()
                        G=Sm7_ent.get()
                        H=Smr1_ent.get()
                        I=Smr2_ent.get()
                        J=Smr3_ent.get()
                        K=Smr4_ent.get()
                        L=Smr5_ent.get()
                        M=Smr6_ent.get()
                        N=Smr7_ent.get()
                        O=Sm11_ent.get()
                        P=Sm12_ent.get()
                        curs1.execute("PRAGMA table_info(Mrk)")
                        e=curs1.fetchall()
                        Z=O+":"+","+A+":"+H+","+B+":"+I+","+C+":"+J+","+D+":"+K+","+E+":"+L+","+F+":"+M+","+G+":"+N
                        for ij in range(0,len(e)):
                                if (str(O.replace(" ","")) in e[ij]):
                                        curs1.execute("update Mrk set '{}'='{}' where Name like '{}'".format(O.replace(" ",""),Z,P))
                                        con1.commit()
                                        messagebox.showinfo("SUCCESS","SAVED SUCCESSFULY")
                                        Sm1_ent.delete(0, END)
                                        Sm2_ent.delete(0, END)
                                        Sm3_ent.delete(0, END)
                                        Sm4_ent.delete(0, END)
                                        Sm5_ent.delete(0, END)
                                        Sm6_ent.delete(0, END)
                                        Sm7_ent.delete(0, END)
                                        Smr1_ent.delete(0, END)
                                        Smr2_ent.delete(0, END)
                                        Smr3_ent.delete(0, END)
                                        Smr4_ent.delete(0, END)
                                        Smr5_ent.delete(0, END)
                                        Smr6_ent.delete(0, END)
                                        Smr7_ent.delete(0, END)
                                        Sm11_ent.delete(0, END)
                                        Sm12_ent.delete(0, END)
                                        break
                                else:
                                        if(ij==len(e)-1):
                                                curs1.execute("alter table Mrk add column '{}' varchar(100)".format(O.replace(" ","")))
                                                curs1.execute("insert into Mrk ('{}') values('A')".format(O.replace(" ","")))
                                                curs1.execute("update Mrk set '{}'='{}' where Name like '{}'".format(O.replace(" ",""),Z,P))
                                                con1.commit()
                                                messagebox.showinfo("SUCCESS","SAVED SUCCESSFULY")
                                                Sm1_ent.delete(0, END)
                                                Sm2_ent.delete(0, END)
                                                Sm3_ent.delete(0, END)
                                                Sm4_ent.delete(0, END)
                                                Sm5_ent.delete(0, END)
                                                Sm6_ent.delete(0, END)
                                                Sm7_ent.delete(0, END)
                                                Smr1_ent.delete(0, END)
                                                Smr2_ent.delete(0, END)
                                                Smr3_ent.delete(0, END)
                                                Smr4_ent.delete(0, END)
                                                Smr5_ent.delete(0, END)
                                                Smr6_ent.delete(0, END)
                                                Smr7_ent.delete(0, END)
                                                Sm11_ent.delete(0, END)
                                                Sm12_ent.delete(0, END)
                                                break
                def ret(evt):
                        Sm12_ent.delete(0, END)
                        Display.delete(1.0,END)
                        value=str(booklist.get(booklist.curselection()))
                        gf=value
                        Sm12_ent.insert(END,gf)
                        curs1.execute("select * from Mrk where Name like '{}'".format(gf))
                        f=curs1.fetchall()
                        for k in range(1,len(f[0])):
                                X=f[0][k].split(",")
                                for l in range(0,len(X)):
                                        if(X[l]!=":"):
                                                Display.insert(END,X[l]+"\n")
                                        else:
                                                pass
                                Display.insert(END,"\n")
                curs.execute("select Srt from Setting")
                i=curs.fetchall()
                if(i[0][0]=="1"):
                        curs1.execute("select Name from Presdetl order by Name asc")
                elif(i[0][0]=="2"):
                        curs1.execute("select Name from Presdetl order by Adno asc")
                else:
                        curs1.execute("select Name from Presdetl")
                i=curs1.fetchall()
                k=[]
                for ic in range(len(i)):
                    lk=str(i[ic][0])
                    pk=[lk]
                    k=k+pk
                ListOfBooks=k
                scrollbar=Scrollbar(NmSH1)
                scrollbar.grid(row=0,column=1,st='ns')
                booklist=Listbox(NmSH1,width=20,height=20,font=('Microsoft Sans Serif',20),border=0,bg="#ffffce")
                booklist.bind('<<ListboxSelect>>',ret)
                booklist.grid(row=0,column=0,padx=8,pady=0)
                scrollbar.config(command=booklist.yview)
                for items in ListOfBooks:
                        booklist.insert(END,items)
        def adstud(A,B,C):
                Btdis()
                B.destroy()
                Main=Frame(A,bg="#5ce1e6",pady=20,padx=22)
                Main.pack(side=RIGHT)
                Nmlst=Frame(Main,bg="#ffffce",pady=5)
                Nmlst.pack(side=TOP)
                NmH1=Frame(Nmlst,bg="#ffffce")
                NmH1.pack(side=TOP,pady=10)
                Qt=Button(NmH1,text="<",bg="#d03636",bd=0,padx=10,pady=5,command=lambda:[Main.destroy(),Btenb(),Dbr(A,B,C)])
                Qt.pack(anchor="ne")
                NmH2=Frame(Nmlst,bg="#ffffce")
                NmH2.pack(side=BOTTOM)
                Nmslt=Frame(Main,bg="#5ce1e6",pady=12)
                Nmslt.pack(side=BOTTOM,pady=5)
                H1=Label(NmH1,text="ADD STUDENT",font=("vardana",25,'bold'),bd=0,bg="#ffffce").pack(padx=500,pady=10)
                Qt=Button(Nmslt,font=("vardana",15,'bold'),text="+ ADD STUDENT",bg="#ffde59",padx=30,command=lambda:[save()])
                Qt.pack(side=RIGHT,padx=5)
                Lb1=Label(NmH2,text="STUDENT DETAILS:\n",font=("vardana",15,'bold'),bg="#ffffce").grid(row=0,column=0,sticky="ne")
                Adno=Label(NmH2,text="ADMISSION NO:",font=("vardana",15,'bold'),bg="#ffffce").grid(row=1,column=0,sticky="ne")
                Nm=Label(NmH2,text="NAME:",font=("vardana",15,'bold'),bg="#ffffce").grid(row=2,column=0,sticky="ne")
                Bd=Label(NmH2,text="DOB:",font=("vardana",15,'bold'),bg="#ffffce").grid(row=3,column=0,sticky="ne")
                Em=Label(NmH2,text="E-MAIL:",font=("vardana",15,'bold'),bg="#ffffce").grid(row=5,column=0,sticky="ne")
                Gd=Label(NmH2,text="GENDER:",font=("vardana",15,'bold'),bg="#ffffce").grid(row=4,column=0,sticky="ne")
                Ad=Label(NmH2,text="ADDRESS:",font=("vardana",15,'bold'),bg="#ffffce").grid(row=6,column=0,sticky="ne")
                Lb2=Label(NmH2,text="\nFATHER DETAILS:\n",font=("vardana",15,'bold'),bg="#ffffce").grid(row=7,column=0,sticky="ne")
                Fn=Label(NmH2,text="NAME:",font=("vardana",15,'bold'),bg="#ffffce").grid(row=8,column=0,sticky="ne")
                Fpn=Label(NmH2,text="MOBILE NO:",font=("vardana",15,'bold'),bg="#ffffce").grid(row=9,column=0,sticky="ne")
                Foc=Label(NmH2,text="OCCUPATION:",font=("vardana",15,'bold'),bg="#ffffce").grid(row=10,column=0,sticky="ne")
                Fai=Label(NmH2,text="ANUAL INCOME:",font=("vardana",15,'bold'),bg="#ffffce").grid(row=11,column=0,sticky="ne")
                Lb3=Label(NmH2,text="\nMOTHER DETAILS:\n",font=("vardana",15,'bold'),bg="#ffffce").grid(row=12,column=0,sticky="ne")
                Mn=Label(NmH2,text="NAME:",font=("vardana",15,'bold'),bg="#ffffce").grid(row=13,column=0,sticky="ne")
                Mpn=Label(NmH2,text="MOBILE NO:",font=("vardana",15,'bold'),bg="#ffffce").grid(row=14,column=0,sticky="ne")
                Moc=Label(NmH2,text="OCCUPATION:",font=("vardana",15,'bold'),bg="#ffffce").grid(row=15,column=0,sticky="ne")
                Mai=Label(NmH2,text="ANUAL INCOME:",font=("vardana",15,'bold'),bg="#ffffce").grid(row=16,column=0,sticky="ne")
                Adno_ent=Entry(NmH2,font=("vardana",15),border=0,width=30)
                Adno_ent.grid(row=1,column=1)
                Nm_ent=Entry(NmH2,font=("vardana",15),border=0,width=30)
                Nm_ent.grid(row=2,column=1)
                Bd_ent=Entry(NmH2,font=("vardana",15),border=0,width=30)
                Bd_ent.grid(row=3,column=1)
                Em_ent=Entry(NmH2,font=("vardana",15),border=0,width=30)
                Em_ent.grid(row=5,column=1)
                Gd_ent=Entry(NmH2,font=("vardana",15),border=0,width=30)
                Gd_ent.grid(row=4,column=1)
                Ad_ent=Entry(NmH2,font=("vardana",15),border=0,width=30)
                Ad_ent.grid(row=6,column=1)
                Fn_ent=Entry(NmH2,font=("vardana",15),border=0,width=30)
                Fn_ent.grid(row=8,column=1)
                Fpn_ent=Entry(NmH2,font=("vardana",15),border=0,width=30)
                Fpn_ent.grid(row=9,column=1)
                Foc_ent=Entry(NmH2,font=("vardana",15),border=0,width=30)
                Foc_ent.grid(row=10,column=1)
                Fai_ent=Entry(NmH2,font=("vardana",15),border=0,width=30)
                Fai_ent.grid(row=11,column=1)
                Mn_ent=Entry(NmH2,font=("vardana",15),border=0,width=30)
                Mn_ent.grid(row=13,column=1)
                Mpn_ent=Entry(NmH2,font=("vardana",15),border=0,width=30)
                Mpn_ent.grid(row=14,column=1)
                Moc_ent=Entry(NmH2,font=("vardana",15),border=0,width=30)
                Moc_ent.grid(row=15,column=1)
                Mai_ent=Entry(NmH2,font=("vardana",15),border=0,width=30)
                Mai_ent.grid(row=16,column=1)
                def save():
                        A=Adno_ent.get()
                        B=Nm_ent.get()
                        C=Bd_ent.get()
                        D=Gd_ent.get()
                        E=Em_ent.get()
                        F=Ad_ent.get()
                        G=Fn_ent.get()
                        H=Fpn_ent.get()
                        I=Foc_ent.get()
                        J=Fai_ent.get()
                        K=Mn_ent.get()
                        L=Mpn_ent.get()
                        M=Moc_ent.get()
                        N=Mai_ent.get()
                        curs1.execute("insert into Presdetl values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(A,B,C,D,E,F,G,H,I,J,K,L,M,N))
                        curs1.execute("alter table Att add column '{}' varchar(30)".format(B.replace(" ","")))
                        curs1.execute("insert into Mrk (Name) values('{}')".format(B))
                        con1.commit()
                        messagebox.showinfo("SUCCESS","STUDENT ADDED")
                        Adno_ent.delete(0, END)
                        Nm_ent.delete(0, END)
                        Bd_ent.delete(0, END)
                        Gd_ent.delete(0, END)
                        Em_ent.delete(0, END)
                        Ad_ent.delete(0, END)
                        Fn_ent.delete(0, END)
                        Fpn_ent.delete(0, END)
                        Foc_ent.delete(0, END)
                        Fai_ent.delete(0, END)
                        Mn_ent.delete(0, END)
                        Mpn_ent.delete(0, END)
                        Moc_ent.delete(0, END)
                        Mai_ent.delete(0, END)
        def Set():
                curs.execute("select Sts from Setting")
                Remacc=curs.fetchall()
                def center_window(w=300, h=200):
                        ws = window1.winfo_screenwidth()
                        hs = window1.winfo_screenheight()
                        x = (ws/2) - (w/2)
                        y = (hs/2) - (h/2)
                        window1.geometry('%dx%d+%d+%d' % (w, h, x, y))
                window1=Tk()
                window1.configure(bg="#920057")
                window1.geometry("560x345")
                window1.overrideredirect(1)
                center_window(560,345)
                Main=Frame(window1,bg="#ffffce")
                Main.pack(padx=25,pady=10)
                def Semn(A):
                        Sub=Frame(window1,bg="#ffffce")
                        Sub.pack(pady=35)
                        QB=Button(Sub,text="X",padx=10,pady=5,bd=0,bg="#d03636",command=lambda:[window1.destroy()]).pack(anchor="ne")
                        H1=Label(Sub,font=("vardana",20,'bold'),text="SETTINGS",bg='#ffffce').pack()
                        Sub1=Frame(Sub,bg="#ffffce",pady=10,padx=10)
                        Sub1.pack()
                        CP=Button(Sub1,font=("vardana",15,'bold'),text="CHANGE PASSWORD",bg="#ffde59",bd=0,command=lambda:[Cp(window1,Sub)]).grid(row=0,column=0,padx=5,pady=5)
                        if(Remacc[0][0]==None):
                                RM=Button(Sub1,font=("vardana",15,'bold'),text="REMENBER ME",bg="#ffde59",bd=0,command=lambda:[Rem(window1,Sub)]).grid(row=0,column=1,padx=5,pady=5)
                        else:
                                RM=Button(Sub1,font=("vardana",15,'bold'),text="CHANGE REMEBER ME",bg="#ffde59",bd=0,command=lambda:[Rem(window1,Sub)]).grid(row=0,column=1,padx=5,pady=5)
                                RM1=Button(Sub1,font=("vardana",15,'bold'),text="FORGET ME",padx=53,bg="#ffde59",bd=0,command=lambda:[Remcan(window1)]).grid(row=1,column=1,padx=5,pady=5)
                        SR=Button(Sub1,font=("vardana",15,'bold'),text="SORT BY",bg='#ffde59',bd=0,padx=60,command=lambda:[Srt(Cata1)]).grid(row=2,column=0,padx=5,pady=5)
                        RS=Button(Sub1,font=("vardana",15,'bold'),text="REMOVE STUDENT",bg='#ffde59',bd=0,padx=10,command=lambda:[dels(window1,Sub)]).grid(row=1,column=0,padx=5,pady=5)
                        Cata1=ttk.Combobox(Sub1,font=("vardana",15,'bold'),width="20",state="randomly")
                        Cata1['values']=["Alphabetical Order","Roll No","Added Time"]
                        Cata1.current(0)
                        Cata1.grid(row=2,column=1,padx=5,pady=5)
                Semn(window1)
                def Srt(Z):
                        A=Z.get()
                        if(A=="Alphabetical Order"):
                                curs.execute("update Setting set Srt ='1'")
                                con.commit()
                                messagebox.showinfo("SUCCESS","SORTED")
                        elif(A=="Roll No"):
                                curs.execute("update Setting set Srt ='2'")
                                con.commit()
                                messagebox.showinfo("SUCCESS","SORTED")
                        else:
                                curs.execute("update Setting set Srt ='3'")
                                con.commit()
                                messagebox.showinfo("SUCCESS","SORTED")
                def Rem(X,Y):
                        Y.destroy()
                        Main=Frame(X,bg="#920057")
                        Main.pack(pady=33)
                        Title=Frame(Main,bg="#ffffce")
                        Title.pack()
                        QB=Button(Title,text="<",padx=10,pady=5,bd=0,bg="#d03636",command=lambda:[Main.destroy(),Semn(X)]).pack(anchor="ne")
                        H1=Label(Title,font=("vardana",20,'bold'),text="REMEMBER ME",bg='#ffffce').pack(padx=10,pady=20)
                        Full=Frame(Title,bg="#ffffce",padx=40)
                        Full.pack()
                        user=Label(Full,font=("vardana",15,'bold'),text="USERNAME:",bg='#ffffce').grid(row=0,column=0,pady=5)
                        pas=Label(Full,font=("vardana",15,'bold'),text="PASSWORD:",bg='#ffffce').grid(row=1,column=0,pady=5)
                        user12=Entry(Full,font=("vardana",15,'bold'),width="25")
                        user12.grid(row=0,column=1)
                        pas12=Entry(Full,font=("vardana",15,'bold'),width="25",show="*")
                        pas12.grid(row=1,column=1)
                        lg=Button(Full,text="ADD",font=("vardana",15,'bold'),bd=0,bg="#ffde59",command=lambda:[Elsup(),X.destroy()])
                        lg.grid(row=2,column=1,sticky="e",padx=5,pady=5)
                        def Elsup():
                                A111=user12.get()
                                B111=pas12.get()
                                b=curs.execute("select * from Accounts")
                                d=b.fetchall()
                                kl='D'
                                for i in range(0,len(d)):
                                        if(d[i][0]==A111 and d[i][1]==B111):
                                                curs.execute("update Setting set (Usr,pss)=('{}','{}') where Srt='1' or Srt='2' or Srt='3'".format(A111,B111))
                                                con.commit()
                                                curs.execute("update Setting set Sts='D' where Srt='1' or Srt='2' or Srt='3'")
                                                con.commit()
                                                messagebox.showinfo("Success","Account Remembered Successfully")
                                                break
                                        elif(A111==""and B111==""):
                                                messagebox.showinfo("ERROR!!!","Please Enter A Valid Account")
                                                break
                                        else:
                                                if(i==len(d)-1):
                                                        messagebox.showinfo("ERROR!!!","Please Enter A Valid Account")
                def Remcan(X):
                        ins=messagebox.askyesno("WARNING","Do Want To Forget Your Default Login")
                        if(ins>0):
                                curs.execute("update setting set (Usr,pss,Sts)=(Null,Null,Null) where Sts='D'")
                                con.commit()
                                messagebox.showinfo("Success","Account Forgot Successfully")
                                X.destroy()
                def Cp(X,Y):
                        Y.destroy()
                        Main=Frame(X,bg="#920057",pady=33)
                        Main.pack()
                        Title=Frame(Main,bg="#ffffce")
                        Title.pack()
                        QB=Button(Title,text="<",padx=10,pady=5,bd=0,bg="#d03636",command=lambda:[Main.destroy(),Semn(X)]).pack(anchor="ne")
                        H1=Label(Title,font=("vardana",20,'bold'),text="CHANGE PASSWORD",bg='#ffffce').pack(padx=20,pady=20)
                        Full=Frame(Title,bg="#ffffce",padx=40)
                        Full.pack()
                        user=Label(Full,font=("vardana",15,'bold'),text="USERNAME:",bg='#ffffce').grid(row=0,column=0,pady=5)
                        pas=Label(Full,font=("vardana",15,'bold'),text="PASSWORD:",bg='#ffffce').grid(row=1,column=0,pady=5)
                        user12=Entry(Full,font=("vardana",15,'bold'),width="25")
                        user12.grid(row=0,column=1)
                        pas12=Entry(Full,font=("vardana",15,'bold'),width="25",show="*")
                        pas12.grid(row=1,column=1)
                        user12.insert(END,a343)
                        user12.configure(state=DISABLED)
                        lg=Button(Full,text="CHANGE",font=("vardana",15,'bold'),bd=0,bg="#ffde59",command=lambda:[Fcp(pas12),X.destroy()])
                        lg.grid(row=2,column=1,padx=5,pady=5,sticky="e")
                        def Fcp(Asd):
                                vi=Asd.get()
                                curs.execute("update Accounts set password ='{}'where user_name='{}' ".format(vi,a343))
                                con.commit()
                                messagebox.showinfo("Success","PASSWORD CHANGED")
                def Rs(X,Y):
                        Y.destroy()
                        Main = Frame(X, bg="#920057", pady=10)
                        Main.pack()
                        Title = Frame(Main, bg="#ffffce")
                        Title.pack()
                        QB = Button(Title, text="<", padx=10, pady=5, bd=0, bg="#d03636",command=lambda: [Main.destroy(), Semn(X)]).pack(anchor="ne")
                        H1 = Label(Title, font=("vardana", 20, 'bold'), text="REMOVE STUDENT", bg='#ffffce').pack(padx=20, pady=20)
                        Full = Frame(Title, bg="#ffffce", padx=100)
                        Full.pack()
                        Full1 = Frame(Title, bg="#ffffce", padx=40)
                        Full1.pack()
                        curs.execute("select Srt from Setting")
                        i = curs.fetchall()
                        if (i[0][0] == "1"):
                                curs1.execute("select Name from Presdetl order by Name asc")
                        elif (i[0][0] == "2"):
                                curs1.execute("select Name from Presdetl order by Adno asc")
                        else:
                                curs1.execute("select Name from Presdetl")
                        i = curs1.fetchall()
                        k = []
                        for ic in range(len(i)):
                                lk = str(i[ic][0])
                                pk = [lk]
                                k = k + pk
                        ListOfBooks = k
                        scrollbar = Scrollbar(Full)
                        scrollbar.grid(row=0, column=1, st='ns')
                        booklist = Listbox(Full, width=23, height=5, font=('Microsoft Sans Serif', 15), border=0,bg="#ffffce")
                        booklist.bind('<<ListboxSelect>>')
                        booklist.grid(row=0,column=0, padx=8, pady=0)
                        scrollbar.config(command=booklist.yview)
                        for items in ListOfBooks:
                                booklist.insert(END, items)
                        lg = Button(Full1, text="REMOVE", font=("vardana", 15, 'bold'), bd=0, bg="#ffde59",command=lambda: [Res(), X.destroy()])
                        lg.grid(row=0, column=1, sticky="e", padx=5, pady=5)
                        def Res():
                                value = str(booklist.get(booklist.curselection()))
                                curs1.execute("delete from Presdetl where Name like '{}'".format(value))
                                con1.commit()
                                messagebox.showinfo("Success", value+" REMOVED")
                                X.destroy()
                def dels(X,Y):
                        Y.destroy()
                        Main = Frame(X, bg="#920057", pady=33)
                        Main.pack()
                        Title = Frame(Main, bg="#ffffce")
                        Title.pack()
                        QB = Button(Title, text="<", padx=10, pady=5, bd=0, bg="#d03636",command=lambda: [Main.destroy(), Semn(X)]).pack(anchor="ne")
                        H1 = Label(Title, font=("vardana", 20, 'bold'), text="REMOVE STUDENT", bg='#ffffce').pack(padx=20, pady=20)
                        Full = Frame(Title, bg="#ffffce", padx=40)
                        Full.pack()
                        curs.execute("select Srt from Setting")
                        i = curs.fetchall()
                        if (i[0][0] == "1"):
                                curs1.execute("select Name from Presdetl order by Name asc")
                        elif (i[0][0] == "2"):
                                curs1.execute("select Name from Presdetl order by Adno asc")
                        else:
                                curs1.execute("select Name from Presdetl")
                        i = curs1.fetchall()
                        k = []
                        for ic in range(len(i)):
                                lk = str(i[ic][0])
                                pk = [lk]
                                k = k + pk
                        ListOfBooks = k
                        user = Label(Full, font=("vardana", 15, 'bold'), text="STUDENT:", bg='#ffffce').grid(row=0,column=0,pady=5)
                        pas = Label(Full, font=("vardana", 15, 'bold'), text="ROLLNO:", bg='#ffffce').grid(row=1,column=0,pady=5)
                        user12 =ttk.Combobox(Full,font=("vardana",15,"bold"),width=25,state="randomly")
                        user12.grid(row=0, column=1)
                        user12['values']=k
                        user12.current(0)
                        def Rlen(event):
                                global cv
                                cv=str(user12.get())
                                curs1.execute("select Adno from Presdetl where Name='{}'".format(cv))
                                i1=curs1.fetchone()
                                pas12.insert(END,i1[0])
                                global stu
                                stu= pas12.get()
                        user12.bind("<<ComboboxSelected>>",Rlen)
                        pas12 = Entry(Full, font=("vardana", 15, 'bold'), width="25")
                        pas12.grid(row=1, column=1)
                        def Fcp1(X):
                                print(X)
                                curs1.execute("delete from Presdetl where Adno='{}'".format(stu))
                                con1.commit()
                                messagebox.showinfo("Success", cv + " REMOVED")
                        lg = Button(Full, text="-REMOVE", font=("vardana", 15, 'bold'), bd=0, bg="#ffde59",command=lambda: [Fcp1(stu), X.destroy()])
                        lg.grid(row=2, column=1, padx=5, pady=5, sticky="e")
        window.mainloop()
Aut()
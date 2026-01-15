from tkinter import Tk,Label,Frame,Button,Entry,messagebox,simpledialog
import time
import sqlite3
import TableCreator
import Generator
import EmailHandler
import re
from datetime import datetime
from PIL import Image,ImageTk 


TableCreator.create()

def update_time():
    curdate=time.strftime("%d-%b-%Y⏰ %r")
    date.configure(text=curdate)
    date.after(1000,update_time)


def newuser_screen():
    def back():
        frm.destroy()
        main_screen()

    def reset_click():
        e_name.delete(0,"end")
        e_adhar.delete(0,"end")
        e_mobile.delete(0,"end")
        e_email.delete(0,"end")
        e_name.focus()

    def createacn_db():
        name=e_name.get()
        email=e_email.get()
        mobile=e_mobile.get()
        adhar=e_adhar.get()

        if len(name)==0 or len(email)==0 or len(mobile)==0 or len(adhar)==0:
            messagebox.showwarning("New User","Empty fields are not allowed")
            return
        
        match=re.fullmatch(r"[a-zA-Z0-9_.]+@[a-zA-Z]+\.[a-zA-Z]+",email)
        if match==None:
             messagebox.showwarning("New User","Enter Valid Email")

        match=re.fullmatchr("[6-9][0-9]{9}",mobile)
        if match==None:
             messagebox.showwarning("New User","Enter Valid Mobile")

        match=re.fullmatch("[0-9]{12}",adhar)
        if match==None:
             messagebox.showwarning("New User","Enter Valid Adhar")
        
        bal=0
        opendate=datetime.now()
        pwd=Generator.generate_pass()
        query="""insert into accounts values(?,?,?,?,?,?,?,?)"""
        conobj=sqlite3.connect(database="mybank.sqlite")
        curobj=conobj.cursor()
        curobj.execute(query,(None,name,pwd,mobile,email,adhar,bal,opendate))
        conobj.commit()

        conobj=sqlite3.connect(database="mybank.sqlite")
        curobj=conobj.cursor()
        query="""select max(acn) from accounts """
        curobj.execute(query)
        tup=curobj.fetchone()
        conobj.close()
        EmailHandler.send_credentials(email,name,tup[0],pwd)

        messagebox.showinfo("Account Creation","Your Account is opened \n we have mailed your creaditials to given email")

    

    frm=Frame(root,highlightbackground="black",highlightthickness=2)
    frm.configure(bg="Teal")
    frm.place(relx=0,rely=.16,relwidth=1,relheight=.73)

    back_btn=Button(frm,text="Back",
                       bg="Beige",
                       font=("arial",20,"bold"),
                       bd=5,
                       activebackground="Teal",
                       activeforeground="Beige",
                       command=back)
    back_btn.place(relx=0,rely=0)

    title=Label(frm,text="Welcome to ABC Bank🏦",
            font=("arial",40,"bold"),bg="Teal",foreground="Beige")
    title.pack()

    title=Label(frm,text="Dedicated support for your financial growth",
            font=("arial",20,"bold"),bg="Teal",foreground="Beige")
    title.pack()

    title=Label(frm,text="We are committed to helping you manage, grow, and protect your finances with confidence.",
            font=("arial",20,"bold"),bg="Teal",foreground="Beige")
    title.pack(side="bottom")


    lbl_name=Label(frm,text="Name",font=("arial",20,"bold"),
                   bg="Navy Blue",fg="Beige",width=9)
    lbl_name.place(relx=.19,rely=.2)

    e_name=Entry(frm,font=("arial",20,"bold"),bd=5)
    e_name.place(relx=.31,rely=.2)
    e_name.focus()



    lbl_email=Label(frm,text="Email",font=("arial",20,"bold"),
                   bg="Navy Blue",fg="Beige",width=9)
    lbl_email.place(relx=.54,rely=.2)

    e_email=Entry(frm,font=("arial",20,"bold"),bd=5)
    e_email.place(relx=.66,rely=.2)



    lbl_mobile=Label(frm,text="Mobile No.",font=("arial",20,"bold"),
                   bg="Navy Blue",fg="Beige",width=9)
    lbl_mobile.place(relx=.54,rely=.33)

    e_mobile=Entry(frm,font=("arial",20,"bold"),bd=5)
    e_mobile.place(relx=.66,rely=.33)



    lbl_adhar=Label(frm,text="Adhar No.",font=("arial",20,"bold"),
                   bg="Navy Blue",fg="Beige",width=9)
    lbl_adhar.place(relx=.19,rely=.33)

    e_adhar=Entry(frm,font=("arial",20,"bold"),bd=5)
    e_adhar.place(relx=.31,rely=.33)


    submit_btn=Button(frm,text="Submit",
                       bg="Beige",
                       font=("arial",20,"bold"),
                       bd=5,
                       width=6,
                       activebackground="Teal",
                       activeforeground="Beige",
                       command=createacn_db)
    submit_btn.place(relx=.43,rely=.5)


    reset_btn=Button(frm,text="Reset",
                       bg="Beige",
                       font=("arial",20,"bold"),
                       bd=5,
                       width=6,
                       activebackground="Teal",
                       activeforeground="Beige",
                       command=reset_click)
    reset_btn.place(relx=.53,rely=.5)

def welcome_screen(acn=None):
    def logout():
        frm.destroy()
        existinguser_screen()

    def check_screen():
        ifrm=Frame(root,highlightbackground="black",highlightthickness=2)
        ifrm.configure(bg="Beige")
        ifrm.place(relx=.2,rely=.39,relwidth=.7,relheight=.5)

        title_lbl=Label(ifrm,text="This is Check Details Screen",
                        font=("arial",25,"bold"),
                        bg="Beige")
        title_lbl.pack()

        conobj=sqlite3.connect(database="mybank.sqlite")
        curobj=conobj.cursor()
        query="""select acn,bal,adhar,email,opendate from accounts where acn=?"""
        curobj.execute(query,(acn,))
        tup=curobj.fetchone()
        conobj.close()

        details = f"""
{'Account No':<10} = {tup[0]}\n
{'Account Bal':<10} = {tup[1]}\n
{'Account Aadhar':<10} = {tup[2]}\n
{'Account Email':<10} = {tup[3]}\n
{'Account OpenDate':<10} = {tup[4]}\n
"""

        lbl_details=Label(ifrm,text=details,bg="Beige",fg="Black",font=("arial",15))
        lbl_details.place(relx=.2,rely=.2)


    def update_screen():
        def update_db():
            name=e_name.get()
            email=e_email.get()
            mobile=e_mobile.get()
            password=e_pass.get()

            conobj=sqlite3.connect(database="mybank.sqlite")
            curobj=conobj.cursor()
            query="""update accounts set name=?,email=?,mob=?,pass=? where acn=?"""
            curobj.execute(query,(name,email,mobile,password,acn))
            conobj.commit()
            conobj.close()
            messagebox.showinfo("Update Screen","Details updated successfully")
            welcome_screen(acn)

        conobj=sqlite3.connect(database="mybank.sqlite")
        curobj=conobj.cursor()
        query="""select name,email,mob,pass from accounts where acn=?"""
        curobj.execute(query,(acn,))
        tup=curobj.fetchone()
        conobj.close()

        ifrm=Frame(root,highlightbackground="black",highlightthickness=2)
        ifrm.configure(bg="Beige")
        ifrm.place(relx=.2,rely=.39,relwidth=.7,relheight=.5)

        title_lbl=Label(ifrm,text="This is Update Details Screen",
                        font=("arial",25,"bold"),
                        bg="Beige")
        title_lbl.pack()

        lbl_name=Label(ifrm,text="Name",font=("arial",20,"bold"),
                   bg="Navy Blue",fg="Beige",width=9)
        lbl_name.place(relx=.03,rely=.2)

        e_name=Entry(ifrm,font=("arial",20,"bold"),bd=5)
        e_name.place(relx=.2,rely=.2)
        e_name.focus()



        lbl_email=Label(ifrm,text="Email",font=("arial",20,"bold"),
                   bg="Navy Blue",fg="Beige",width=9)
        lbl_email.place(relx=.5,rely=.2)

        e_email=Entry(ifrm,font=("arial",20,"bold"),bd=5)
        e_email.place(relx=.66,rely=.2)



        lbl_mobile=Label(ifrm,text="Mobile No.",font=("arial",20,"bold"),
                   bg="Navy Blue",fg="Beige",width=9)
        lbl_mobile.place(relx=.5,rely=.39)

        e_mobile=Entry(ifrm,font=("arial",20,"bold"),bd=5)
        e_mobile.place(relx=.66,rely=.39)



        lbl_pass=Label(ifrm,text="Password",font=("arial",20,"bold"),
                   bg="Navy Blue",fg="Beige",width=9)
        lbl_pass.place(relx=.03,rely=.39)

        e_pass=Entry(ifrm,font=("arial",20,"bold"),bd=5)
        e_pass.place(relx=.2,rely=.39)

        e_name.insert(0,tup[0])
        e_email.insert(0,tup[1])
        e_mobile.insert(0,tup[2])
        e_pass.insert(0,tup[3])

        update_btn=Button(ifrm,text="Update",
                       bg="Navy Blue",fg="white",
                       font=("arial",20,"bold"),
                       bd=5,
                       width=6,
                       activebackground="Teal",
                       activeforeground="Beige",
                       command=update_db)
        update_btn.place(relx=.43,rely=.6)


    def deposit_screen():
        def deposit_db():
            amt=float(e_amt.get())
            conobj=sqlite3.connect(database="mybank.sqlite")
            curobj=conobj.cursor()
            query="""update accounts set bal=bal+? where acn=?"""
            curobj.execute(query,(amt,acn))
            conobj.commit()
            conobj.close()
            messagebox.showinfo("Deposit Screen",f"{amt}Deposited Successfully")
            e_amt.delete(0,"end")
            e_amt.focus()


        ifrm=Frame(root,highlightbackground="black",highlightthickness=2)
        ifrm.configure(bg="Beige")
        ifrm.place(relx=.2,rely=.39,relwidth=.7,relheight=.5)

        title_lbl=Label(ifrm,text="This is Deposit Amount Screen",
                        font=("arial",25,"bold"),
                        bg="Beige")
        title_lbl.pack()

        lbl_amt=Label(ifrm,text="Amount",font=("arial",20,"bold"),
                   bg="Navy Blue",fg="Beige",width=9)
        lbl_amt.place(relx=.27,rely=.39)

        e_amt=Entry(ifrm,font=("arial",20,"bold"),bd=5)
        e_amt.place(relx=.43,rely=.39)

        deposit_btn=Button(ifrm,text="Deposit",
                       bg="Navy Blue",fg="white",
                       font=("arial",20,"bold"),
                       bd=5,
                       width=6,
                       activebackground="Teal",
                       activeforeground="Beige",
                       command=deposit_db)
        deposit_btn.place(relx=.43,rely=.6)

    def withdraw_screen():
         def withdraw_db():
             amt=float(e_amt.get())
             conobj=sqlite3.connect(database="mybank.sqlite")
             curobj=conobj.cursor()
             query="""select bal,email,name from accounts where acn=?"""
             curobj.execute(query,(acn,))
             tup=curobj.fetchone()
             conobj.close()

             if tup[0]>=amt:
                 gen_otp=Generator.generate_otp()
                 EmailHandler.send_otp_withdraw(tup[1],tup[2],gen_otp,amt)
                 user_otp=simpledialog.askinteger("Withdraw OTP","OTP is Send on Your Email")
                 if gen_otp==user_otp:
                    conobj=sqlite3.connect(database="mybank.sqlite")
                    curobj=conobj.cursor()
                    query="""update accounts set bal=bal-? where acn=?"""
                    curobj.execute(query,(amt,acn))
                    conobj.commit()
                    conobj.close()
                    messagebox.showinfo("Withdraw Screen",f"{amt}Withdrawn Successfully")
                    e_amt.delete(0,"end")
                    e_amt.focus()
                 else:
                    messagebox.showerror("Withdraw Screen","Invalid OTP")
                    submit_btn.configure(text="Resend OTP")
             else:
                messagebox.showwarning("Withdraw Screen",f"Insufficient Bal:{tup[0]}")

         ifrm=Frame(root,highlightbackground="black",highlightthickness=2)
         ifrm.configure(bg="Beige")
         ifrm.place(relx=.2,rely=.39,relwidth=.7,relheight=.5)

         title_lbl=Label(ifrm,text="This is Withdraw Amount Screen",
                        font=("arial",25,"bold"),
                        bg="Beige")
         title_lbl.pack()

         lbl_amt=Label(ifrm,text="Amount",font=("arial",20,"bold"),
                   bg="Navy Blue",fg="Beige",width=9)
         lbl_amt.place(relx=.27,rely=.39)

         e_amt=Entry(ifrm,font=("arial",20,"bold"),bd=5)
         e_amt.place(relx=.43,rely=.39)

         submit_btn=Button(ifrm,text="Withdraw",
                       bg="Navy Blue",fg="white",
                       font=("arial",20,"bold"),
                       bd=5,
                       width=6,
                       activebackground="Teal",
                       activeforeground="Beige",
                       command=withdraw_db)
         submit_btn.place(relx=.43,rely=.6)

    def transfer_screen():

        def transfer_db():
             to_acn=int(e_to.get())
             amt=float(e_amt.get())

             conobj=sqlite3.connect(database="mybank.sqlite")
             curobj=conobj.cursor()
             query="""select * from accounts where acn=?"""
             curobj.execute(query,(to_acn,))
             tup=curobj.fetchone()
             conobj.close()

             if tup==None:
                 messagebox.showerror("Transfer Screen","Invalid To ACN")
                 return

             conobj=sqlite3.connect(database="mybank.sqlite")
             curobj=conobj.cursor()
             query="""select bal,email,name from accounts where acn=?"""
             curobj.execute(query,(acn,))
             tup=curobj.fetchone()
             conobj.close()

             if tup[0]>=amt:
                 gen_otp=Generator.generate_otp()
                 EmailHandler.send_otp_transfer(tup[1],tup[2],gen_otp,amt,to_acn)
                 user_otp=simpledialog.askinteger("Transfer OTP","OTP is Send on Your Email")
                 if gen_otp==user_otp:
                    conobj=sqlite3.connect(database="mybank.sqlite")
                    curobj=conobj.cursor()
                    query1="""update accounts set bal=bal-? where acn=?"""
                    query2="""update accounts set bal=bal+? where acn=?"""
                    curobj.execute(query1,(amt,acn))
                    curobj.execute(query2,(amt,to_acn))
                    conobj.commit()
                    conobj.close()
                    messagebox.showinfo("Transfer Screen",f"{amt}Transfer Successfully")
                    e_amt.delete(0,"end")
                    e_amt.focus()
                 else:
                    messagebox.showerror("Transfer Screen","Invalid OTP")
                    submit_btn.configure(text="Resend OTP")
             else:
                messagebox.showwarning("Transfer Screen",f"Insufficient Bal:{tup[0]}")



        ifrm=Frame(root,highlightbackground="black",highlightthickness=2)
        ifrm.configure(bg="Beige")
        ifrm.place(relx=.2,rely=.39,relwidth=.7,relheight=.5)

        title_lbl=Label(ifrm,text="This is Transfer Amount Screen",
                        font=("arial",25,"bold"),
                        bg="Beige")
        title_lbl.pack()

        lbl_to=Label(ifrm,text="To ACN",font=("arial",20,"bold"),
                   bg="Navy Blue",fg="Beige",width=9)
        lbl_to.place(relx=.27,rely=.3)

        e_to=Entry(ifrm,font=("arial",20,"bold"),bd=5)
        e_to.place(relx=.43,rely=.3)
        e_to.focus()


        lbl_amt=Label(ifrm,text="Amount",font=("arial",20,"bold"),
                   bg="Navy Blue",fg="Beige",width=9)
        lbl_amt.place(relx=.27,rely=.44)

        e_amt=Entry(ifrm,font=("arial",20,"bold"),bd=5)
        e_amt.place(relx=.43,rely=.44)

        submit_btn=Button(ifrm,text="Transfer",
                       bg="Navy Blue",fg="white",
                       font=("arial",20,"bold"),
                       bd=5,
                       width=6,
                       activebackground="Teal",
                       activeforeground="Beige",
                       command=transfer_db)
        submit_btn.place(relx=.43,rely=.65)

    conobj=sqlite3.connect(database="mybank.sqlite")
    curobj=conobj.cursor()
    query="""select name from accounts where acn=?"""
    curobj.execute(query,(acn,))
    tup=curobj.fetchone()
    conobj.close()   

    frm=Frame(root,highlightbackground="black",highlightthickness=2)
    frm.configure(bg="Teal")
    frm.place(relx=0,rely=.16,relwidth=1,relheight=.73)

    logout_btn=Button(frm,text="Logout",
                       bg="Beige",
                       font=("arial",20,"bold"),
                       bd=5,
                       activebackground="Teal",
                       activeforeground="Beige",
                       command=logout)
    logout_btn.place(relx=.92,rely=0)

    lbl_acn=Label(frm,text=f"Welcome🙏🏻{tup[0]}",font=("arial",20,"bold"),
                   bg="Navy Blue",fg="Beige")
    lbl_acn.place(relx=.001,rely=0)


    check_btn=Button(frm,text="Check Details",
                       bg="Yellow",
                       font=("arial",20,"bold"),
                       bd=5,
                       width=15,
                       activebackground="Teal",
                       activeforeground="Beige",command=check_screen)
    check_btn.place(relx=.001,rely=.31)

    update_btn=Button(frm,text="Update Details",
                       bg="Navy",fg="white",
                       font=("arial",20,"bold"),
                       bd=5,
                       width=15,
                       activebackground="Teal",
                       activeforeground="Beige",command=update_screen)
    update_btn.place(relx=.001,rely=.46)

    deposit_btn=Button(frm,text="Deposit Amount",
                       bg="Green",fg="White",
                       font=("arial",20,"bold"),
                       bd=5,
                       width=15,
                       activebackground="Teal",
                       activeforeground="Beige",command=deposit_screen)
    deposit_btn.place(relx=.001,rely=.61)

    withdraw_btn=Button(frm,text="Withdraw Amount",
                       bg="Red",fg="White",
                       font=("arial",20,"bold"),
                       bd=5,
                       width=15,
                       activebackground="Teal",
                       activeforeground="Beige",command=withdraw_screen)
    withdraw_btn.place(relx=.001,rely=.75)

    transfer_btn=Button(frm,text="Transfer Amount",
                       bg="Gold",
                       font=("arial",20,"bold"),
                       bd=5,
                       width=15,
                       activebackground="Teal",
                       activeforeground="Beige",command=transfer_screen)
    transfer_btn.place(relx=.001,rely=.9)




def existinguser_screen():
    def back():
        frm.destroy()
        main_screen()

    def fp_click():
        frm.destroy()
        forgot_screen()

    def reset_click():
        e_acn.delete(0,"end")
        e_pass.delete(0,"end")
        e_acn.focus()

    def submit_click():
        acn=e_acn.get()
        pwd=e_pass.get()

        conobj=sqlite3.connect(database="mybank.sqlite")
        curobj=conobj.cursor()
        query="""select * from accounts where acn=? and pass=?"""
        curobj.execute(query,(acn,pwd))
        tup=curobj.fetchone()
        conobj.close()
        if tup==None:
            messagebox.showerror("Login","Invalid Credentials")
        else:
            acn=tup[0]
            frm.destroy()
            welcome_screen(acn)


    frm=Frame(root,highlightbackground="black",highlightthickness=2)
    frm.configure(bg="Teal")
    frm.place(relx=0,rely=.16,relwidth=1,relheight=.73)

    back_btn=Button(frm,text="Back",
                       bg="Beige",
                       font=("arial",20,"bold"),
                       bd=5,
                       activebackground="Teal",
                       activeforeground="Beige",
                       command=back)
    back_btn.place(relx=0,rely=0)


    title=Label(frm,text="Welcome to ABC Bank🏦",
            font=("arial",40,"bold"),bg="Teal",foreground="Beige")
    title.pack()


    title=Label(frm,text="Smart digital solutions for easy money management",
            font=("arial",20,"bold"),bg="Teal",foreground="Beige")
    title.pack()

    title=Label(frm,text="Personalized financial solutions for individuals and businesses",
            font=("arial",20,"bold"),bg="Teal",foreground="Beige")
    title.pack(side="bottom")



    lbl_acn=Label(frm,text="Account No.",font=("arial",20,"bold"),
                   bg="Navy Blue",fg="Beige",width=10)
    lbl_acn.place(relx=.3,rely=.25)

    e_acn=Entry(frm,font=("arial",20,"bold"),bd=5)
    e_acn.place(relx=.43,rely=.25)
    e_acn.focus()



    lbl_pass=Label(frm,text="Password",font=("arial",20,"bold"),
                   bg="Navy Blue",fg="Beige",width=10)
    lbl_pass.place(relx=.3,rely=.4)

    e_pass=Entry(frm,font=("arial",20,"bold"),bd=5,show="*")
    e_pass.place(relx=.43,rely=.4)


    submit_btn=Button(frm,text="Submit",
                       bg="Beige",
                       font=("arial",20,"bold"),
                       bd=5,
                       width=6,
                       activebackground="Teal",
                       activeforeground="Beige",
                       command=submit_click)
    submit_btn.place(relx=.44,rely=.53)

    reset_btn=Button(frm,text="Reset",
                       bg="Beige",
                       font=("arial",20,"bold"),
                       bd=5,
                       width=6,
                       activebackground="Teal",
                       activeforeground="Beige",
                       command=reset_click)
    reset_btn.place(relx=.54,rely=.53)


    forgot_btn=Button(frm,text="Forgot Password",
                       bg="Beige",
                       font=("arial",20,"bold"),
                       bd=5,
                       width=15,
                       activebackground="Teal",
                       activeforeground="Beige",
                       command=fp_click)
    forgot_btn.place(relx=.44,rely=.66)


def forgot_screen():
    def back():
        frm.destroy()
        existinguser_screen()

    def reset_click():
        e_acn.delete(0,"end")
        e_adhar.delete(0,"end")
        e_acn.focus()

    def send_otp():
        gen_otp=Generator.generate_otp()
        acn=e_acn.get()
        adhar=e_adhar.get()

        conobj=sqlite3.connect(database="mybank.sqlite")
        curobj=conobj.cursor()
        query="""select name,email,pass from accounts where acn=? and adhar=?"""
        curobj.execute(query,(acn,adhar))
        tup=curobj.fetchone()
        conobj.close()
        if tup==None:
            messagebox.showerror("Forgot Password","Record not found")
        else:
            EmailHandler.send_otp(tup[1],tup[0],gen_otp)

            attempts = 3
            for i in range(attempts):
                user_otp = simpledialog.askinteger(
                    "Password Recovery",
                    f"Enter OTP (Attempt {i+1}/{attempts})")

                if user_otp == gen_otp:
                    messagebox.showinfo(
                        "Password Recovery",
                        f"Your Password = {tup[2]}"
                        )
                    break
                else:
                    messagebox.showerror(
                        "Password Recovery",
                        "Invalid OTP")
            else:
                messagebox.showwarning(
                    "Password Recovery",
                    "You have used all 3 attempts. Please resend OTP."
                )

                otp_btn.configure(text="Resend OTP")

                

    frm=Frame(root,highlightbackground="black",highlightthickness=2)
    frm.configure(bg="Teal")
    frm.place(relx=0,rely=.16,relwidth=1,relheight=.73)

    back_btn=Button(frm,text="Back", 
                       bg="Beige",
                       font=("arial",20,"bold"),
                       activebackground="Teal",
                       activeforeground="Beige",
                       bd=5,command=back)
    back_btn.place(relx=0,rely=0)

    title=Label(frm,text="Welcome to ABC Bank🏦",
            font=("arial",40,"bold"),bg="Teal",foreground="Beige")
    title.pack()

    lbl_acn=Label(frm,text="Account No.",font=("arial",20,"bold"),
                   bg="Navy Blue",fg="Beige",width=10)
    lbl_acn.place(relx=.3,rely=.25)

    e_acn=Entry(frm,font=("arial",20,"bold"),bd=5)
    e_acn.place(relx=.43,rely=.25)
    e_acn.focus()

    lbl_adhar=Label(frm,text="Adhar No.",font=("arial",20,"bold"),
                   bg="Navy Blue",fg="Beige",width=10)
    lbl_adhar.place(relx=.3,rely=.36)

    e_adhar=Entry(frm,font=("arial",20,"bold"),bd=5)
    e_adhar.place(relx=.43,rely=.36)


    otp_btn=Button(frm,text="Send OTP",
                       bg="Beige",
                       font=("arial",20,"bold"),
                       bd=5,
                       width=9,
                       activebackground="Teal",
                       activeforeground="Beige",
                       command=send_otp)
    otp_btn.place(relx=.41,rely=.53)

    reset_btn=Button(frm,text="Reset",
                       bg="Beige",
                       font=("arial",20,"bold"),
                       bd=5,
                       width=9,
                       activebackground="Teal",
                       activeforeground="Beige",
                       command=reset_click)
    reset_btn.place(relx=.54,rely=.53)




def main_screen():

    def newuser_click():
        frm.destroy()
        newuser_screen()

    def existinguser_click():
        frm.destroy()
        existinguser_screen()


    frm=Frame(root,highlightbackground="black",highlightthickness=2)
    frm.configure(bg="Teal")
    frm.place(relx=0,rely=.16,relwidth=1,relheight=.73)

    title=Label(frm,text="Welcome to ABC Bank🏦",
            font=("arial",40,"bold"),bg="Teal",foreground="Beige")
    title.pack()

    title=Label(frm,text="Where your trust meets secure, smart, and seamless banking.",
            font=("arial",20,"bold"),bg="Teal",foreground="Beige")
    title.pack()

    title=Label(frm,text="Thank you for choosing ABC Bank — Your partner in every financial step.",
            font=("arial",20,"bold"),bg="Teal",foreground="Beige")
    title.pack(side="bottom")

    newuser_btn=Button(frm,text="Create Account\n Sign Up",
                       bg="Beige",
                       bd=5,
                       width=13,
                       font=("arial",20,"bold"),
                       activebackground="Teal",
                       activeforeground="Beige",
                       command=newuser_click)
    newuser_btn.place(relx=.43,rely=.3)

    existuser_btn=Button(frm,text="Existing user\nSign In",
                       bg="Beige",
                       bd=5,
                       width=13,
                       font=("arial",20,"bold"),
                       activebackground="Teal",
                       activeforeground="Beige",command=existinguser_click)
    existuser_btn.place(relx=.43,rely=.58)



root=Tk()   #n to make full Screen Window 
root.state("zoomed") # to make fullscreen window
root.resizable(width=False,height=False)
root.configure(bg="powder blue") 

title=Label(root,text="Banking Simulation",
            font=("arial",50,"bold","underline"),bg="powder blue")
title.pack()


curdate=time.strftime("%d-%b-%Y⏰ %r")
date=Label(root,text=curdate,
            font=("arial",20,"bold"),bg="powder blue")
date.pack(pady=15)
update_time()

img=Image.open("bank2.png").resize((400,140))
imagetk=ImageTk.PhotoImage(img,master=root)

lbl_img=Label(root,image=imagetk)
lbl_img.place(relx=0,rely=0)

footer=Label(root,text="Developed By:Babu Rav Apte\n📱 9999999999",
            font=("arial",30,"bold",),bg="powder blue")
footer.pack(side="bottom")


main_screen()
root.mainloop() # to make window visible


from tkinter import*
from tkinter import ttk  
import random
import time
import datetime
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector


class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")
        
        #TEXT VARIABLES
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()
        
        #***************BACKGROUND IMG **********************
        
        self.bg=ImageTk.PhotoImage(file=r"D:\collage work\projects\HOSPITAL_MANAGEMENT_SYSTEM\Screenshot_20230127_133211.png")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)
        
        #***************left IMG **********************
        
        self.bg1=ImageTk.PhotoImage(file=r"D:\collage work\projects\HOSPITAL_MANAGEMENT_SYSTEM\Free Vector _ Hospital.jpg")
        left_lbl=Label(self.root,image=self.bg1)
        left_lbl.place(x=50,y=100,width=470,height=500)
        
        
        ##################### Main FRame ###################
        frame=Frame(self.root,bg="white")
        frame.place(x=520,y=100,width=865,height=500)
        
        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="darkgreen",bg="white")
        register_lbl .place(x=20,y=20)


         #        label and entry 
        
        #ROW1
        fname=Label(frame,text="First Name",font=("times new roman",16,"bold"),bg="white")
        fname.place(x=50,y=100)
        
        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("timews new roman",16,"bold"))
        fname_entry.place(x=50,y=130,width=250)
        
        lname=Label(frame,text="Last Name",font=("times new roman",16,"bold"),bg="white",fg="black")
        lname.place(x=370,y=100)
        
        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",16,"bold"))
        self.txt_lname.place(x=370,y=130,width=250 )
        
        #ROW2
        contact=Label(frame,text="Contact No",font=("times new roman",16,"bold"),bg="white")
        contact.place(x=50,y=170)
        
        contact_entry=ttk.Entry(frame,textvariable=self.var_contact,font=("timews new roman",16,"bold"))
        contact_entry.place(x=50,y=200,width=250)
        
        email=Label(frame,text="Email",font=("times new roman",16,"bold"),bg="white",fg="black")
        email.place(x=370,y=170)
        
        email_entry=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",16,"bold"))
        email_entry.place(x=370,y=200,width=250 )
        
        #ROW3
        sq=Label(frame,text="Select Security Question",font=("times new roman",16,"bold"),bg="white")
        sq.place(x=50,y=240)
        
        self.combo_sq=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("timews new roman",16,"bold"),state="readonly")
        self.combo_sq["values"]=("Select","Your Birth Place","Your Bestfriend Name","Your Nickname")
        self.combo_sq.place(x=50,y=270,width=250)
        self.combo_sq.current(0)
        
       
       
        sa=Label(frame,text="Security Answer",font=("times new roman",16,"bold"),bg="white",fg="black")
        sa.place(x=370,y=240)
        
        sa_entry=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",16,"bold"))
        sa_entry.place(x=370,y=270,width=250 )
    
        #ROW4
        pas=Label(frame,text="Password",font=("times new roman",16,"bold"),bg="white")
        pas.place(x=50,y=310)
        
        pas_entry=ttk.Entry(frame,textvariable=self.var_pass,font=("timews new roman",16,"bold"))
        pas_entry.place(x=50,y=340,width=250)
        
        cpas=Label(frame,text="Confirm password",font=("times new roman",16,"bold"),bg="white",fg="black")
        cpas.place(x=370,y=310)
        
        cpas_entry=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",16,"bold"))
        cpas_entry.place(x=370,y=340,width=250 )


        #BUTTONS
        
        #login button
        #img0=Image.open(r"E:\miniproject\l11.png")
        #img0=img0.resize((200,55))
        #self.photoimage=ImageTk.PhotoImage(img0)
        #b1=Button(frame,image=self.photoimage,borderwidth=0,cursor="hand2",font=("times new roman",16,"bold"),fg="white")
        #b1.place(x=50,y=410,width=200)
        
      
        
        #login button
        #img2=Image.open(r"E:\miniproject\l11.png")
        #img2=img2.resize((200,60),Image.ANTIALIAS)
        #self.photoimage=ImageTk.PhotoImage(img2)
        b1=Button(frame,text="LOGIN",command=self.return_login,borderwidth=0,cursor="hand2",font=("times new roman",16,"bold"),fg="blue",bd=10,relief=RIDGE)
        b1.place(x=50,y=410,width=200)
        
        

        #register button
        #img1=Image.open(r"E:\miniproject\12.jpg")
        #img1=img1.resize((200,60))
        #self.photoimage1=ImageTk.PhotoImage(img1) 
        b2=Button(frame,text="REGISTER",command=self.register_data,borderwidth=0,cursor="hand2",font=("times new roman",16,"bold"),fg="blue",bd=10,relief=RIDGE)
        b2.place(x=370,y=410,width=200)


         #FUNCTIONALITY
    def register_data(self):
        if self.var_fname.get()=="" or self.var_pass.get()=="" or self.var_securityA.get()=="":
            messagebox.showerror("ERROR","All feilds are required")
            
        
        elif  self.var_confpass.get()!=self.var_pass.get():
            messagebox.showerror("ERROR","Password must be same")
        
        else:
            #messagebox.showinfo("SUCCESS","SUCCESSFULLY REGISTERED")
            conn=mysql.connector.connect(host="localhost",username="root",password="Anamika@01",database="mydata")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("ERROR","User already exist!Try another email")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                self.var_fname.get(),
                self.var_lname.get(),
                self.var_contact.get(),
                self.var_email.get(),
                self.var_securityQ.get(),
                self.var_securityA.get(),
                self.var_pass.get()
               ))
            conn.commit()
            conn.close()
            messagebox.showinfo("SUCCESS","SUCCESSFULLY REGISTERED")
        
    
    
    
    def return_login(self):
        self.root.destroy()         

        




if __name__=="__main__":
    root=Tk()
    app=Register(root)
    root.mainloop()
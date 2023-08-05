from tkinter import*
from tkinter import ttk  
from tkinter import messagebox
import mysql.connector



class hospital:
    def __init__(self,root):
        self.root=root
        self.root.title("hospital management system")
        self.root.geometry("1550x900+0+0")



   


        #variables
        self.pname=StringVar() 
        self.book=StringVar()
        self.dob=StringVar()
        self.pa=StringVar()
   
        self.no=StringVar()
        self.refno=StringVar()
        self.dose=StringVar()
        self.notb=StringVar()
        self.id=StringVar()
        self.expdate=StringVar()
        self.dd=StringVar()
        self.se=StringVar() 

        lbltitle=Label(self.root,bd=20,relief=RIDGE,text="HOSPITAL MANAGEMENT SYSTEM",fg="blue",bg="lavender",font=("times new roman",50,"bold"))
        lbltitle.pack(side=TOP,fill=X)

        #dataframe
        Dataframe=Frame(self.root,bd=20,relief=RIDGE,bg="lavender")
        Dataframe.place(x=0,y=130,width=1530,height=400)

        DataframeLeft=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=20,font=("times new roman",12,"bold"),text="Patient Info",bg="white")
        DataframeLeft.place(x=30,y=5,width=980,height=350)
        
        DataframeRight=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=20,font=("times new roman",12,"bold"),text="Prescription",bg="white")
        DataframeRight.place(x=985,y=5,width=450,height=350)



        #buttons frame

        Buttonframe=Frame(self.root,bd=5,relief=RIDGE,bg="lavender")
        Buttonframe.place(x=0,y=530,width=1530,height=56)

        Detailsframe=Frame(self.root,bd=10,relief=RIDGE,bg="lavender")
        Detailsframe.place(x=0,y=580,width=1530,height=190)

       # DataframeLeft

        lblpatientname=Label(DataframeLeft,text="Patient Name",font=("times new roman",13,"bold"),padx=2,pady=4,bg="white")
        lblpatientname.grid(row=0,column=0,sticky=W)
        txtpname=Entry(DataframeLeft,textvariable=self.pname,font=("arial",13,"bold"),width=35)
        txtpname.grid(row=0,column=1)

        lbldob=Label(DataframeLeft,text="Date of birth",font=("times new roman",13,"bold"),padx=2,pady=4,bg="white")
        lbldob.grid(row=1,column=0)
        txtdob=Entry(DataframeLeft,textvariable=self.dob,font=("arial",13,"bold"),width=35)
        txtdob.grid(row=1,column=1)
        

        lbladdr=Label(DataframeLeft,text="Patient Address",font=("times new roman",13,"bold"),padx=2,pady=4,bg="white")
        lbladdr.grid(row=2,column=0)
        txtaddr=Entry(DataframeLeft,textvariable=self.pa,font=("arial",13,"bold"),width=35)
        txtaddr.grid(row=2,column=1)

        lblno=Label(DataframeLeft,text="Name of Tablet",font=("times new roman",13,"bold"),padx=2,pady=4,bg="white")
        lblno.grid(row=3,column=0)
        txtno=Entry(DataframeLeft,textvariable=self.no,font=("arial",13,"bold"),width=35)
        txtno.grid(row=3,column=1)

        lblrefno=Label(DataframeLeft,text="Reference no",font=("times new roman",13,"bold"),padx=2,pady=4,bg="white")
        lblrefno.grid(row=4,column=0)
        txtref=Entry(DataframeLeft,textvariable=self.refno,font=("arial",13,"bold"),width=35)
        txtref.grid(row=4,column=1)

        lbldosage=Label(DataframeLeft,text="Dosage",font=("times new roman",13,"bold"),padx=2,pady=4,bg="white")
        lbldosage.grid(row=5,column=0)
        txtdos=Entry(DataframeLeft,textvariable=self.dose,font=("arial",13,"bold"),width=35)
        txtdos.grid(row=5,column=1)

        lblslot=Label(DataframeLeft,text="BOOKING SLOT:",font=("times new roman",12,"bold"),pady=4,padx=2)
        lblslot.grid(row=6,column=0)
        comslot=ttk.Combobox(DataframeLeft,textvariable=self.book,state="readonly",font=("times new roman",12,"bold"),width=35)
        comslot["values"]=("A","B","C","D","E")
        comslot.grid(row=6,column=1)

        lblnumber=Label(DataframeLeft,text="No. of Tablets",font=("times new roman",13,"bold"),padx=2,pady=4,bg="white")
        lblnumber.grid(row=0,column=2)
        txtn=Entry(DataframeLeft,textvariable=self.notb,font=("arial",13,"bold"),width=35)
        txtn.grid(row=0,column=3)

        lblid=Label(DataframeLeft,text="Issue date",font=("times new roman",13,"bold"),padx=2,pady=4,bg="white")
        lblid.grid(row=1,column=2)
        txtid=Entry(DataframeLeft,textvariable=self.id,font=("arial",13,"bold"),width=35)
        txtid.grid(row=1,column=3)

        lblexp=Label(DataframeLeft,text="Expiry date",font=("times new roman",13,"bold"),padx=2,pady=4,bg="white")
        lblexp.grid(row=2,column=2)
        txtexp=Entry(DataframeLeft,textvariable=self.expdate,font=("arial",13,"bold"),width=35)
        txtexp.grid(row=2,column=3)

        lbldd=Label(DataframeLeft,text="daily dosage",font=("times new roman",13,"bold"),padx=2,pady=4,bg="white")
        lbldd.grid(row=3,column=2)
        txtdd=Entry(DataframeLeft,textvariable=self.dd,font=("arial",13,"bold"),width=35)
        txtdd.grid(row=3,column=3)

        lblse=Label(DataframeLeft,text="Side Effect",font=("times new roman",13,"bold"),padx=2,pady=4,bg="white")
        lblse.grid(row=4,column=2)
        txtse=Entry(DataframeLeft,textvariable=self.se,font=("arial",13,"bold"),width=35)
        txtse.grid(row=4,column=3)

        

        #dataframe right
        self.txtprescription=Text(DataframeRight,font=("Times new roman",13,"bold"),width=43,height=16,padx=2,pady=6,bg="beige")
        self.txtprescription.grid(row=0,column=0)

        #buttons

        btnprescription=Button(Buttonframe,text="Prescription",command=self.iprescription,bg="green",fg="white",font=("arial",12,"bold"),width=25,height=1,padx=2,pady=8)
        btnprescription.grid(row=0,column=0)

        btnprescriptiondata=Button(Buttonframe,text="Prescription Data",command=self.iprescriptionData,bg="green",fg="white",font=("arial",12,"bold"),width=25,height=1,padx=2,pady=8)
        btnprescriptiondata.grid(row=0,column=1)

        btnupdate=Button(Buttonframe,text="Update",command=self.update,bg="green",fg="white",font=("arial",12,"bold"),width=25,height=1,padx=2,pady=8)
        btnupdate.grid(row=0,column=2)

        btnDel=Button(Buttonframe,text="Delete",command=self.Delete,bg="green",fg="white",font=("arial",12,"bold"),width=24,height=1,padx=2,pady=8)
        btnDel.grid(row=0,column=3)

        btnclear=Button(Buttonframe,text="Clear",command=self.clear,bg="green",fg="white",font=("arial",12,"bold"),width=22,height=1,padx=2,pady=8)
        btnclear.grid(row=0,column=4)

        
        btnexit=Button(Buttonframe,text="Exit",command=self.exit,bg="green",fg="white",font=("arial",12,"bold"),width=23,height=1,padx=2,pady=8)
        btnexit.grid(row=0,column=5)


        scroll_x=ttk.Scrollbar(Detailsframe,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Detailsframe,orient=VERTICAL)
        self.hospital_table=ttk.Treeview(Detailsframe,column=("BOOKING SLOT","Patient Name","DOB","Patient Address","Name of Tablets","Reference No.","Dosage","No. of Tablets","Issue Date","Expiry Date","Daily Dose","Side Effect"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x=ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_y=ttk.Scrollbar(command=self.hospital_table.yview)


        self.hospital_table.heading("BOOKING SLOT",text="BOOKING SLOT")
        self.hospital_table.heading("Patient Name",text="Patient Name")
        self.hospital_table.heading("DOB",text="DOB")
        self.hospital_table.heading("Patient Address",text="Patient Address")
        self.hospital_table.heading("Name of Tablets",text="Name of Tablets")
        self.hospital_table.heading("Reference No.",text="Reference No.")
        self.hospital_table.heading("Dosage",text="Dosage")
        self.hospital_table.heading("No. of Tablets",text="No. of Tablets")
        self.hospital_table.heading("Issue Date",text="Issue Date")
        self.hospital_table.heading("Expiry Date",text="Expiry Date")
        self.hospital_table.heading("Daily Dose",text="Daily Dose")
        self.hospital_table.heading("Side Effect",text="Side Effect")

        self.hospital_table["show"]="headings"
  

        self.hospital_table.column("BOOKING SLOT",width=100)
        self.hospital_table.column("Patient Name",width=100)
        self.hospital_table.column("DOB",width=100)
        self.hospital_table.column("Patient Address",width=100)
        self.hospital_table.column("Name of Tablets",width=100)
        self.hospital_table.column("Reference No.",width=100)
        self.hospital_table.column("Dosage",width=100)
        self.hospital_table.column("No. of Tablets",width=100)
        self.hospital_table.column("Issue Date",width=100)
        self.hospital_table.column("Expiry Date",width=100)
        self.hospital_table.column("Daily Dose",width=100)
        self.hospital_table.column("Side Effect",width=100)

        self.hospital_table.pack(fill=BOTH,expand=1)
        self.hospital_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()






             #functionality
    def iprescriptionData(self):
        if self.notb.get()==" " or self.refno.get()==" ":
             messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Anamika@01",database="mydata")
            my_cursor=conn.cursor()
            my_cursor.execute("insert into hospital values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.book.get(),
                                                                                        self.pname.get(),
                                                                                        self.dob.get(), 
                                                                                        self.pa.get(),
                                                                                        self.no.get(),
                                                                                        self.refno.get(),
                                                                                        self.dose.get(),
                                                                                        self.notb.get(),
                                                                                        self.id.get(),
                                                                                        self.expdate.get(),
                                                                                        self.dd.get(),
                                                                                        self.se.get()
            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success","Record has been inserted",parent=self.root)


    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Anamika@01",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from hospital")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.hospital_table.delete(*self.hospital_table.get_children())
            for i in rows:
                self.hospital_table.insert("",END,values=i)
                conn.commit()
            conn.close()


    def get_cursor(self,event=""):
        cursor_row=self.hospital_table.focus()
        content=self.hospital_table.item(cursor_row)
        row=content["values"]
        self.book.set(row[0])
        self.pname.set(row[1])  
        self.dob.set(row[2])
        self.pa.set(row[3])
        self.no.set(row[4])
        self.refno.set(row[5])
        self.dose.set(row[6])
        self.notb.set(row[7])
        self.id.set(row[8])
        self.expdate.set(row[9])
        self.dd.set(row[10])
        self.se.set(row[11])    
        



    def update(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Anamika@01",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("update hospital set BOOKING_SLOT=%s,NameofTablets=%s,Dose=%s,NoofTablets=%s,IssueDate=%s,ExpDate=%s,DailyDose=%s,SideEffect=%s,PatientName=%s,DOB=%s,PatientAddress=%s where Reference=%s",(
                            self.book.get(),
                            self.no.get(),
                            self.dose.get(),
                            self.notb.get(),
                            self.id.get(),
                            self.expdate.get(),
                            self.dd.get(),
                            self.se.get(),
                            self.pname.get(),
                            self.dob.get(),
                            self.pa.get(),
                            self.refno.get(),
                ))
        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("update","record has been updated successfully",parent=self.root)

    def iprescription(self):
        self.txtprescription.insert(END,"BOOKING SLOT:\t\t\t"+self.book.get()+"\n")
        self.txtprescription.insert(END,"patient name:\t\t\t"+self.pname.get()+"\n")
        self.txtprescription.insert(END,"DOB:\t\t\t"+self.dob.get()+"\n")
        self.txtprescription.insert(END,"Patient Address:\t\t\t"+self.pa.get()+"\n")
        self.txtprescription.insert(END,"Name of Tablets:\t\t\t"+self.no.get()+"\n")
        self.txtprescription.insert(END,"Reference No:\t\t\t"+self.refno.get()+"\n")
        self.txtprescription.insert(END,"Dosage:\t\t\t"+self.dose.get()+"\n")
        self.txtprescription.insert(END,"No. of Tablets:\t\t\t"+self.notb.get()+"\n")
        self.txtprescription.insert(END,"Issue Date:\t\t\t"+self.id.get()+"\n")
        self.txtprescription.insert(END,"Expiry Date:\t\t\t"+self.expdate.get()+"\n")
        self.txtprescription.insert(END,"Daily Dose:\t\t\t"+self.dd.get()+"\n")
        self.txtprescription.insert(END,"Side Effect:\t\t\t"+self.se.get()+"\n")


    def Delete(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Anamika@01",database="mydata")
        my_cursor=conn.cursor()
        query="delete from hospital where Reference=%s"
        value=(self.refno.get(),)
        my_cursor.execute(query,value)
        conn.commit()
        conn.close()
        self.fetch_data()
        messagebox.showinfo("Delete","deleted successfully",parent=self.root)


    def clear(self):
        self.book.set('')
        self.pname.set('') 
        self.dob.set('') 
        self.pa.set('') 
        self.no.set('') 
        self.refno.set('') 
        self.dose.set('') 
        self.notb.set('') 
        self.id.set('') 
        self.expdate.set('') 
        self.dd.set('') 
        self.se.set('')
        self.txtprescription.delete("1.0",END)


    def exit(self):
        exit=messagebox.askyesno("hospital management system","Confirm your exit",parent=self.root)
        if(exit>0):
            self.root.destroy()
            return




root=Tk()
ob=hospital(root)
root.mainloop()
from tkinter import *
from turtle import onclick
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox


class PharmaSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Pharmacy Managment System")
        self.root.geometry("1550x800+0+0")

        # ############### AddMed Variable ############
        self.addmed_var = StringVar()
        self.refmed_var = StringVar()

        # ############### All Label input Variables #######################
        self.refvar = StringVar()
        self.cmpnamevar = StringVar()
        self.typemedvar = StringVar()
        self.mednamevar = StringVar()
        self.lotnovar = StringVar()
        self.issuedatevar = StringVar()
        self.expdatevar = StringVar()
        self.usesvar = StringVar()
        self.sideeffectvar = StringVar()
        self.warningvar = StringVar()
        self.dosagevar = StringVar()
        self.productqtvar = StringVar()
        self.pricevar = StringVar()

        lbltitle = Label(self.root, text="Pharmacy Managment System", bd=15, relief=RIDGE,
                         bg="white", fg="darkgreen", font=("times new roman", 50, "bold"), padx=8, pady=8)

        lbltitle.pack(side=TOP, fill=X)

        img1 = Image.open("farmalogo.png")
        img1 = img1.resize((80, 80), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        b1 = Button(self.root, image=self.photoimg1, borderwidth=0)
        b1.place(x=160, y=15)

        # ############################DataFrame########################
        DataFrame = Frame(self.root, bd=15, relief=RIDGE, padx=20)
        DataFrame.place(x=0, y=120, width=1360, height=400)

        DataFrameLeft = LabelFrame(DataFrame, bd=10, relief=RIDGE, padx=20,
                                   text="Medicine Information", fg="darkgreen", font=("arial", 12, "bold"))
        DataFrameLeft.place(x=0, y=5, width=790, height=350)

        # ##########################Button Frame######################
        ButtonFrame = Frame(self.root, bd=15, relief=RIDGE, padx=20)
        ButtonFrame.place(x=0, y=520, width=1360, height=65)

        # ########################## Main Frame ######################
        btnAddData = Button(ButtonFrame, text="Medicine Add", font=(
            "arial", 13, "bold"), width=11, bg="darkgreen", fg="white", activebackground='orange', command=self.add_data)
        btnAddData.grid(row=0, column=0)

        btnAddData = Button(ButtonFrame, text="UPDATE", font=(
            "arial", 13, "bold"), width=11, bg="darkgreen", fg="white", activebackground="orange", command=self.update)
        btnAddData.grid(row=0, column=1)

        btnAddData = Button(ButtonFrame, text="DELETE", font=(
            "arial", 13, "bold"), width=11, bg="red", fg="white", activebackground="orange", command=self.delete)
        btnAddData.grid(row=0, column=2)

        btnAddData = Button(ButtonFrame, text="RESET", font=(
            "arial", 13, "bold"), width=11, bg="darkgreen", fg="white", activebackground="orange",command=self.reset)
        btnAddData.grid(row=0, column=3)

        btnAddData = Button(ButtonFrame, text="EXIT", font=(
            "arial", 13, "bold"), width=11, bg="darkgreen", fg="white", activebackground="orange")
        btnAddData.grid(row=0, column=4)

        ############################# Search By ##################
        lblSearch = Label(ButtonFrame, font=('arial', 17, 'bold'),
                          text="Search By", padx=2, bg="red", fg='white')
        lblSearch.grid(row=0, column=5, sticky=W)
        
        ################## Search Variables ################
        self.search_var=StringVar()

        searchCom = ttk.Combobox(ButtonFrame, width=9, font=(
            'arial', 17, 'bold'), state="readonly",textvariable=self.search_var)
        searchCom["values"] = ("Ref_no", "MedName", "LotNo")
        searchCom.grid(row=0, column=6)
        searchCom.current(0)
        
        ##################Search Text Variable ###############
        self.searchText_var=StringVar()
        txtsearch = Entry(ButtonFrame, bd=3, relief=RIDGE,
                          width=15, font=("arial", 17, "bold"),textvariable=self.searchText_var)
        txtsearch.grid(row=0, column=7)

        searchButton = Button(ButtonFrame, text="SEARCH", font=(
            "arial", 13, "bold"), width=11, bg="darkgreen", fg="white", activebackground="orange",command=self.search_data)
        searchButton.grid(row=0, column=8)

        showAll = Button(ButtonFrame, text="SHOW ALL", font=(
            "arial", 13, "bold"), width=11, bg="darkgreen", fg="white", activebackground="orange",command=self.fetch_data)
        showAll.grid(row=0, column=9)

        # ########################### Table and Entry#########################
        lblrefno = Label(DataFrameLeft, font=(
            'arial', 12, 'bold'), text="Reference No:", padx=2)
        lblrefno.grid(row=0, column=0, sticky=W)

        conn = mysql.connector.connect(
            host='localhost', user='root', password="Sandesh@123", database='pharma_database')
        ref_cursor = conn.cursor()
        ref_cursor.execute("select Ref from pharma")
        refrow = ref_cursor.fetchall()

        refCom = ttk.Combobox(DataFrameLeft, width=22, font=(
            'arial', 12, 'bold'), state="readonly", textvariable=self.refvar)
        refCom["values"] = refrow
        refCom.grid(row=0, column=1)
        refCom.current(0)

        compName = Label(DataFrameLeft, font=(
            'arial', 12, 'bold'), text="Company Name:", padx=2, pady=6)
        compName.grid(row=1, column=0, sticky=W)

        compEntry = Entry(DataFrameLeft, font=("arial", 13, 'bold'), bg='white',
                          bd=2, relief=RIDGE, width=24, textvariable=self.cmpnamevar)
        compEntry.grid(row=1, column=1)

        typeMed = Label(DataFrameLeft, font=("arial", 12, 'bold'),
                        text="Type Of Medicine:", padx=2, pady=6)
        typeMed.grid(row=2, column=0)

        typeMedCom = ttk.Combobox(DataFrameLeft, width=22, font=(
            'arial', 12, 'bold'), state="readonly", textvariable=self.typemedvar)
        typeMedCom["values"] = ("Tablet", "Liquid", "Capsule",
                                "Topical Medicines", "Drops", "Inhaler", "Injection")
        typeMedCom.current(0)
        typeMedCom.grid(row=2, column=1)

        MedNameLbl = Label(DataFrameLeft, font=(
            "arial", 12, 'bold'), text="Medicine Name:", padx=2, pady=6)
        MedNameLbl.grid(row=3, column=0, sticky=W)

        # ################## Med Names Label Left Section ######################
        med_name_cursor = conn.cursor()
        med_name_cursor.execute("select MedName from pharma")
        med_name_Data = med_name_cursor.fetchall()

        MedNameIp = ttk.Combobox(DataFrameLeft, state="readonly", font=(
            'arial', 12, 'bold'), width=22, textvariable=self.mednamevar)
        MedNameIp['value'] =med_name_Data
        MedNameIp.current(0)
        MedNameIp.grid(row=3, column=1)

        lblLotNo = Label(DataFrameLeft, text="Lot No:",
                         font=('arial', 12, 'bold'), padx=2, pady=6)
        lblLotNo.grid(row=4, column=0, sticky=W)

        lblLotNoIp = Entry(DataFrameLeft, font=("arial", 13, 'bold'),
                           bg='white', relief=RIDGE, width=24, textvariable=self.lotnovar)
        lblLotNoIp.grid(row=4, column=1)

        lblIssueDate = Label(DataFrameLeft, text="Issue Date:", font=(
            'arial', 12, 'bold'), padx=2, pady=6)
        lblIssueDate.grid(column=0, row=5, sticky=W)

        lblIssueDateIp = Entry(DataFrameLeft, font=(
            'arial', 13, 'bold'), relief=RIDGE, width=24, textvariable=self.issuedatevar)
        lblIssueDateIp.grid(column=1, row=5)

        lblExpDate = Label(DataFrameLeft, font=(
            'arial', 12, 'bold'), text="Exp Date:", padx=2, pady=6)
        lblExpDate.grid(column=0, row=6, sticky=W)

        lblExpDateIp = Entry(DataFrameLeft, font=(
            'arial', 13, 'bold'), relief=RIDGE, width=24, textvariable=self.expdatevar)
        lblExpDateIp.grid(column=1, row=6)

        lblUses = Label(DataFrameLeft, font=(
            'arial', 12, 'bold'), text="Uses:", padx=2, pady=6)
        lblUses.grid(column=0, row=7, sticky=W)

        lblUsesIp = Entry(DataFrameLeft, font=('arial', 13, 'bold'),
                          relief=RIDGE, width=24, textvariable=self.usesvar)
        lblUsesIp.grid(column=1, row=7)

        lblSidEffect = Label(DataFrameLeft, font=(
            'arial', 12, 'bold'), text="Side Effect:", padx=2, pady=6)
        lblSidEffect.grid(column=0, row=8, sticky=W)

        lblSidEffectIp = Entry(DataFrameLeft, font=(
            'arial', 13, 'bold'), relief=RIDGE, width=24, textvariable=self.sideeffectvar)
        lblSidEffectIp.grid(column=1, row=8)

        # #######################DataFrame Left column 3 data#####################
        lblPrecWarning = Label(DataFrameLeft, font=(
            'arial', 12, 'bold'), text="Prec&Warning:", padx=15)
        lblPrecWarning.grid(row=0, column=2, sticky=W)

        lblPrecWarningIp = Entry(DataFrameLeft, font=(
            'arial', 13, 'bold'), relief=RIDGE, width=24, textvariable=self.warningvar)
        lblPrecWarningIp.grid(row=0, column=3)

        lblDosage = Label(DataFrameLeft, font=(
            'arial', 12, 'bold'), text="Dosage:", padx=15, pady=6)
        lblDosage.grid(row=1, column=2, sticky=W)

        lblDosageIp = Entry(DataFrameLeft, font=(
            'arial', 13, 'bold'), relief=RIDGE, width=24, textvariable=self.dosagevar)
        lblDosageIp.grid(row=1, column=3)

        lblTabPrice = Label(DataFrameLeft, font=(
            'arial', 12, 'bold'), text="Tablet Price:", padx=15, pady=6)
        lblTabPrice.grid(row=2, column=2, sticky=W)

        lblTabPriceIp = Entry(DataFrameLeft, font=(
            'arial', 13, 'bold'), relief=RIDGE, width=24, textvariable=self.pricevar)
        lblTabPriceIp.grid(row=2, column=3)

        lblProdQT = Label(DataFrameLeft, font=(
            'arial', 12, 'bold'), text="Product QT:", padx=15, pady=6)
        lblProdQT.grid(row=3, column=2, sticky=W)

        lblProdQTIp = Entry(DataFrameLeft, font=(
            'arial', 13, 'bold'), relief=RIDGE, width=24, textvariable=self.productqtvar)
        lblProdQTIp.grid(row=3, column=3)

        # ##########################Images Section##################
        slogan = Label(DataFrameLeft, font=('arial', 12, 'bold'),
                       text="Save Life !", padx=15, pady=6, foreground='red')
        slogan.place(x=475, y=300)
        img2 = Image.open("farma 4.jpg")
        img2 = img2.resize((353, 160), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        b2 = Button(self.root, image=self.photoimg2, borderwidth=0)
        b2.place(x=450, y=300)

        # ############################ Right Frame###################
        DataFrameRight = LabelFrame(DataFrame, bd=10, relief=RIDGE, padx=20,
                                    text="Medicine Add Department", fg="darkgreen", font=("arial", 12, "bold"))
        DataFrameRight.place(x=800, y=5, width=500, height=350)
        img3 = Image.open("farma1.jpg")
        img3 = img3.resize((200, 75), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        b1 = Button(self.root, image=self.photoimg3, borderwidth=0)
        b1.place(x=845, y=160)

        img4 = Image.open("farma2.jpg")
        img4 = img4.resize((150, 75), Image.Resampling.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        b1 = Button(self.root, image=self.photoimg4, borderwidth=0)
        b1.place(x=1045, y=160)

        img5 = Image.open("farma3.jpg")
        img5 = img5.resize((150, 140), Image.Resampling.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        b1 = Button(self.root, image=self.photoimg5, borderwidth=0)
        b1.place(x=1175, y=160)

        lblrefno = Label(DataFrameRight, text="Ref No:",
                         font=('arial', 12, 'bold'), padx=15, pady=6)
        lblrefno.place(x=0, y=80)
        lblrefnoIp = Entry(DataFrameRight, textvariable=self.refmed_var, font=(
            'arial', 15, 'bold'), bd=2, relief=RIDGE, width=18)
        lblrefnoIp.place(x=105, y=80)

        lblMedName = Label(DataFrameRight, text="Med Name:",
                           font=('arial', 12, 'bold'), padx=15, pady=6)
        lblMedName.place(x=0, y=120)
        lblMedIp = Entry(DataFrameRight, textvariable=self.addmed_var, font=(
            'arial', 15, 'bold'), bd=2, relief=RIDGE, width=18)
        lblMedIp.place(x=105, y=120)

        # ##################### Side Frame Right ######################
        sideFrameRight = Frame(DataFrameRight, bd=4, bg='white', relief=RIDGE)
        sideFrameRight.place(x=20, y=160, width=290, height=160)

        scr_h = ttk.Scrollbar(sideFrameRight, orient=HORIZONTAL)
        scr_h.pack(side=BOTTOM, fill=X)
        scr_v = ttk.Scrollbar(sideFrameRight, orient=VERTICAL)
        scr_v.pack(side=RIGHT, fill=Y)

        self.medicine_table = ttk.Treeview(sideFrameRight, column=(
            'ref', 'medname'), xscrollcommand=scr_h.set, yscrollcommand=scr_v.set)
        scr_h.config(command=self.medicine_table.xview)
        scr_v.config(command=self.medicine_table.yview)

        self.medicine_table.heading('ref', text="Ref")
        self.medicine_table.heading("medname", text="Medicine Name")

        self.medicine_table["show"] = "headings"
        self.medicine_table.pack(fill=BOTH, expand=1)

        self.medicine_table.column("ref", width=50)
        self.medicine_table.column("medname", width=50)

        self.medicine_table.bind("<ButtonRelease-1>", self.Medget_cursor)

        # ####################### Medicine Add Button #################
        down_frame = Frame(DataFrameRight, bd=4, bg="pink", relief=RIDGE)
        down_frame.place(x=320, y=160, width=135, height=160)

        btnAddmed = Button(down_frame, text="ADD", font=(
            'arial', 12, "bold"), bg="green", padx=5, pady=4, width=11, command=self.Addmed)
        btnAddmed.grid(row=0, column=0)

        btnAddmed = Button(down_frame, text="UPDATE", font=(
            'arial', 12, "bold"), bg="gold", padx=5, pady=4, width=11, command=self.UpdateMed)
        btnAddmed.grid(row=1, column=0)

        btnAddmed = Button(down_frame, text="DELETE", font=(
            'arial', 12, "bold"), bg="cyan", padx=5, pady=4, width=11, command=self.DeletMed)
        btnAddmed.grid(row=2, column=0)

        btnAddmed = Button(down_frame, text="CLEAR", font=(
            'arial', 12, "bold"), bg="red", padx=5, pady=4, width=11, command=self.clearData)
        btnAddmed.grid(row=3, column=0)

        # ####################### Frame Details ########################
        FrameDetails = Frame(self.root, relief=RIDGE)
        FrameDetails.place(x=0, y=580, width=1360, height=200)

        # ####################### Main Table & Scroll Bar ####################
        Table_frame = Frame(FrameDetails, relief=RIDGE)
        Table_frame.place(x=0, y=1, width=1360, height=115)

        scroll_x = ttk.Scrollbar(Table_frame, orient=HORIZONTAL)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y = ttk.Scrollbar(Table_frame, orient=VERTICAL)
        scroll_y.pack(side=RIGHT, fill=Y)

        self.pharmacy_table = ttk.Treeview(Table_frame, column=("reg", 'companyname', 'type', 'tabletname', 'lotno', 'issuedate', 'expdate',
                                           'uses', 'sideeffect', 'warning', 'dosage', 'price', 'productqt'), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.pharmacy_table.xview)
        scroll_y.config(command=self.pharmacy_table.yview)

        self.pharmacy_table['show'] = 'headings'

        self.pharmacy_table.heading('reg', text='Reference No')
        self.pharmacy_table.heading('companyname', text="Company Name")
        self.pharmacy_table.heading('type', text='Type Of Medicine')
        self.pharmacy_table.heading('tabletname', text='Tablet Name')
        self.pharmacy_table.heading('lotno', text='Lot No')
        self.pharmacy_table.heading('issuedate', text='Issue Date')
        self.pharmacy_table.heading('expdate', text='Expiry Date')
        self.pharmacy_table.heading('uses', text='Uses')
        self.pharmacy_table.heading('sideeffect', text='Side Effect')
        self.pharmacy_table.heading('warning', text='Warning')
        self.pharmacy_table.heading('dosage', text='Dosage')
        self.pharmacy_table.heading('price', text='Price')
        self.pharmacy_table.heading('productqt', text='Product QT')
        self.pharmacy_table.pack(fill=BOTH, expand=1)

        self.pharmacy_table.column('reg', width=100)
        self.pharmacy_table.column('companyname', width=100)
        self.pharmacy_table.column('type', width=100)
        self.pharmacy_table.column('tabletname', width=100)
        self.pharmacy_table.column('lotno', width=100)
        self.pharmacy_table.column('issuedate', width=100)
        self.pharmacy_table.column('expdate', width=100)
        self.pharmacy_table.column('uses', width=100)
        self.pharmacy_table.column('sideeffect', width=100)
        self.pharmacy_table.column('warning', width=100)
        self.pharmacy_table.column('dosage', width=100)
        self.pharmacy_table.column('price', width=100)
        self.pharmacy_table.column('productqt', width=100)
        self.fetchdata()
        self.fetch_data()
        self.pharmacy_table.bind("<ButtonRelease-1>", self.get_cursor)

        # ###################### Add Medicine Functionality Declaration #############

    def Addmed(self):
        conn = mysql.connector.connect(host='localhost', user='root', password="Sandesh@123", database='pharma_database')
        my_cursor = conn.cursor()
        my_cursor.execute("insert into pharma(Ref,MedName) values(%s,%s)",
                          (self.refmed_var.get(), self.addmed_var.get()))
        conn.commit()
        self.fetchdata()
        # self.Medget_cursor()
        conn.close()
        messagebox.showinfo("Success", "Medicine Added")

    def fetchdata(self):
        conn = mysql.connector.connect(
            host='localhost', user='root', password="Sandesh@123", database='pharma_database')
        my_cursor = conn.cursor()
        my_cursor.execute("select * from pharma")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.medicine_table.delete(*self.medicine_table.get_children())
            for i in rows:
                self.medicine_table.insert("", END, values=i)
            conn.commit()
        conn.close()

        # ################ MedGetCursor #########################
    def Medget_cursor(self, event=""):
        cursor_row = self.medicine_table.focus()
        content = self.medicine_table.item(cursor_row)
        
        row = content["values"]
        self.refmed_var.set(row[0])
        self.addmed_var.set(row[1])

    def UpdateMed(self):
        if self.refmed_var.get() == "" or self.addmed_var.get() == "":
            messagebox.showerror("Error", "All fields are Required")
        else:
            conn = mysql.connector.connect(
                host='localhost', user='root', password="Sandesh@123", database='pharma_database')
            my_cursor = conn.cursor()
            my_cursor.execute("update pharma set MedName=%s where Ref=%s",
                              (self.addmed_var.get(), self.refmed_var.get()))
            conn.commit()
            self.fetchdata()
            conn.close()

            messagebox.showinfo("Success", "Medicine has been Updated")

    def DeletMed(self):
        conn = mysql.connector.connect(
            host='localhost', user='root', password="Sandesh@123", database='pharma_database')
        my_cursor = conn.cursor()

        query = "delete from pharma where Ref=%s"
        val = (self.refmed_var.get(),)
        my_cursor.execute(query, val)
        conn.commit()
        self.fetchdata()
        conn.close()

    def clearData(self):
        conn = mysql.connector.connect(
            host='localhost', user='root', password="Sandesh@123", database='pharma_database')
        self.refmed_var.set("")
        self.addmed_var.set("")

    # ############## Main Table ###################

    def add_data(self):
        if self.refvar.get() == "" or self.lotnovar.get() == "":
            messagebox.showerror("Error", "All Fields are required!")
        else:
            conn = mysql.connector.connect(
                host='localhost', user='root', password="Sandesh@123", database='pharma_database')
            my_cursor = conn.cursor()
            my_cursor.execute("insert into pharmacy values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (self.refvar.get(), self.cmpnamevar.get(), self.typemedvar.get(), self.mednamevar.get(), self.lotnovar.get(
            ), self.issuedatevar.get(), self.expdatevar.get(), self.usesvar.get(), self.sideeffectvar.get(), self.warningvar.get(), self.dosagevar.get(), self.pricevar.get(), self.productqtvar.get()))
        self.fetch_data()
        conn.close()
        messagebox.showinfo("Success", "Data Inserted Successfully!")

    def fetch_data(self):
        conn = mysql.connector.connect(
            host='localhost', user='root', password="Sandesh@123", database='pharma_database')
        my_cursor = conn.cursor()
        my_cursor.execute("select * from pharmacy")
        row = my_cursor.fetchall()
        if len(row) != 0:
            self.pharmacy_table.delete(*self.pharmacy_table.get_children())
            for i in row:
                self.pharmacy_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    def get_cursor(self, event=""):
        cursorrow = self.pharmacy_table.focus()
        contents = self.pharmacy_table.item(cursorrow)
        row_data = contents["values"]
        self.refvar.set(row_data[0])
        self.cmpnamevar.set(row_data[1])
        self.typemedvar.set(row_data[2])
        self.mednamevar.set(row_data[3])
        self.lotnovar.set(row_data[4])
        self.issuedatevar.set(row_data[5])
        self.expdatevar.set(row_data[6])
        self.usesvar.set(row_data[7])
        self.sideeffectvar.set(row_data[8])
        self.warningvar.set(row_data[9])
        self.dosagevar.set(row_data[10])
        self.pricevar.set(row_data[11])
        self.productqtvar.set(row_data[12])

    def update(self):
        if self.refvar.get() == "" or self.lotnovar.get() == "":
            messagebox.showerror("Error", "All fields are Required")
        else:
            conn = mysql.connector.connect(
                host='localhost', user='root', password="Sandesh@123", database='pharma_database')
            my_cursor = conn.cursor()
            my_cursor.execute("update pharmacy set CmpName=%s,TypeMed=%s,MedName=%s,LotNo=%s,IssueDate=%s,ExpDate=%s,Uses=%s,SideEffect=%s,Warning=%s,Dosage=%s,Price=%s,ProductQT=%s where Ref_no=%s",
                              (self.cmpnamevar.get(), self.typemedvar.get(), self.mednamevar.get(), self.lotnovar.get(), self.issuedatevar.get(), self.expdatevar.get(), self.usesvar.get(), self.sideeffectvar.get(), self.warningvar.get(), self.dosagevar.get(), self.pricevar.get(), self.productqtvar.get(), self.refvar.get()))
            conn.commit()
            self.fetch_data()
            conn.close()

            messagebox.showinfo("Success", "Medicine has been Updated")

    def delete(self):
        conn = mysql.connector.connect(
            host='localhost', user='root', password="Sandesh@123", database='pharma_database')
        my_cursor = conn.cursor()

        query = "delete from pharmacy where Ref_no=%s"
        val = (self.refvar.get(),)
        my_cursor.execute(query, val)
        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("Delete", "Information Deleted Successfully !")

    def reset(self):
        self.cmpnamevar.set("")
        self.lotnovar.set("")
        self.issuedatevar.set("")
        self.expdatevar.set("")
        self.usesvar.set("")
        self.sideeffectvar.set("")
        self.warningvar.set("")
        self.productqtvar.set("")
        self.pricevar.set("")
        self.dosagevar.set("")
    
    def search_data(self):
        conn = mysql.connector.connect(
            host='localhost', user='root', password="Sandesh@123", database='pharma_database')
        my_cursor = conn.cursor()
        my_cursor.execute(("select * from pharmacy where {} like '{}%'").format(self.search_var.get(),self.searchText_var.get()))
        row=my_cursor.fetchall()
        if len(row)!=0:
            self.pharmacy_table.delete(*self.pharmacy_table.get_children())
            for i in row:
                self.pharmacy_table.insert("",END,values=i)
            conn.commit()
        conn.close()
        


if __name__ == "__main__":
    root = Tk()
    obj = PharmaSystem(root)
    root.mainloop()

from tkinter import*  
# Importing Tkinter for GUI
from tkinter import ttk 
# ttk helps to modify the GUI
from PIL import Image,ImageTk
# for importing images and adjusting the design
from tkinter import messagebox
from tkcalendar import DateEntry
import mysql.connector
import cv2
import re
import tkinter as tk
import os
# from cryptography.fernet import Fernet

class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition System")
        #NO MAXIMIZE SCREEN
        self.root.resizable(False, False)
        
        #=================================VARIABLES====================================================
        
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
          
                
        # BANNER IMAGE
        img = Image.open(r"D:\Face Recognition System code\Image\ban.jpg")
        img=img.resize((1366,130),Image.LANCZOS)
        self.photoimage = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimage)
        f_lbl.place(x=0,y=0,width=1366,height=130)
        
        
        
         # backgorund image 
        bg1=Image.open(r"D:\Face Recognition System code\Image\bg4.png")
        bg1=bg1.resize((1366,768),Image.LANCZOS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=130,width=1366,height=768)

        
        
        
        # TITLE LABEL
        title_lbl = Label(bg_img, text="Student Management Dashboard", font=("Bell Gothic Std Black", 30, "bold"), bg="white", fg="Black")
        title_lbl.place(x=0,y=0,width=1366,height=45)
        
        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=5,y=55,width=1355,height=510)

            
        #left Label Frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="STUDENT DETAILS",font=("Verdana",14,"bold"))
        Left_frame.place(x=10,y=10,width=660,height=480)
        
        
        # Current Course 
        current_course_frame = LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="",font=("verdana",12,"bold"),fg="black")
        current_course_frame.place(x=10,y=5,width=635,height=150)
        
        
        # BANNER IMAGE
        stimg = Image.open(r"D:\Face Recognition System code\Image\stbanner.jpg")
        stimg=stimg.resize((635,147),Image.LANCZOS)
        self.stphotoimage = ImageTk.PhotoImage(stimg)

        f_lbl = Label(current_course_frame, image=self.stphotoimage)
        f_lbl.place(x=0,y=0,width=635,height=147)
        
        
        
        #Class Student Information 
        class_student_frame = LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("verdana",13,"bold"),fg="Black")
        class_student_frame.place(x=10,y=160,width=635,height=230)
        
        #ROLL NO
        
        roll_no_div_label=Label(class_student_frame,text="Roll-No:",font=("verdana",11,"bold"),bg="white",fg="black")
        roll_no_div_label.grid(row=0,column=0,padx=5,pady=5,sticky=W)
        
        roll_no_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=15,font=("verdana",12,"bold"))
        roll_no_entry.grid(row=0,column=1,padx=5,pady=5,sticky=W)
        
        #STUDENT NAME
        
        studentName_label=Label(class_student_frame,text="Std-Name:",font=("verdana",11,"bold"),bg="white",fg="black")
        studentName_label.grid(row=0,column=2,padx=5,pady=5,sticky=W)
        
        studentName_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=15,font=("verdana",12,"bold"))
        studentName_entry.grid(row=0,column=3,padx=5,pady=5,sticky=W)
        
        
        #CLASS DIVISION
        
        student_div_label = Label(class_student_frame,text="Class Section:",font=("verdana",12,"bold"),fg="black",bg="white")
        student_div_label.grid(row=1,column=0,padx=5,pady=5,sticky=W)

        div_combo=ttk.Combobox(class_student_frame,textvariable=self.var_div,width=13,font=("verdana",12,"bold"),state="readonly")
        div_combo["values"]=("Section-A")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=5,pady=5,sticky=W)
            
        
        #GENDER
        
        gender_label=Label(class_student_frame,text="Gender:",font=("verdana",11,"bold"),bg="white",fg="black")
        gender_label.grid(row=1,column=2,padx=5,pady=5,sticky=W)
        
        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,width=13,font=("verdana",12,"bold"),state="readonly")
        gender_combo["values"]=("Male","Female","Others")
        gender_combo.current(0)
        gender_combo.grid(row=1,column=3,padx=5,pady=5,sticky=W)
        
        #DATE OF BIRTH
        
        dob_label=Label(class_student_frame,text="DOB:",font=("verdana",11,"bold"),bg="white",fg="black")
        dob_label.grid(row=2,column=0,padx=5,pady=5,sticky=W)
        
        dob_entry=DateEntry(class_student_frame,textvariable=self.var_dob,width=13,font=("verdana",12,"bold"),date_pattern='yyyy-mm-dd')
        dob_entry.grid(row=2,column=1,padx=5,pady=5,sticky=W)
        
        
        #EMAIL
        
        email_label=Label(class_student_frame,text="Parents Email:",font=("verdana",11,"bold"),bg="white",fg="black")
        email_label.grid(row=2,column=2,padx=5,pady=5,sticky=W)
        
        email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=15,font=("verdana",12,"bold"))
        email_entry.grid(row=2,column=3,padx=5,pady=5,sticky=W)
        
        #PHONE NUMBER
        
        phone_label=Label(class_student_frame,text="Parents No:",font=("verdana",11,"bold"),bg="white",fg="black")
        phone_label.grid(row=3,column=0,padx=5,pady=5,sticky=W)
        
        phone_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=15,font=("verdana",12,"bold"))
        phone_entry.grid(row=3,column=1,padx=5,pady=5,sticky=W)
        
        
        #ADDRESS
        
        address_label=Label(class_student_frame,text="Address:",font=("verdana",11,"bold"),bg="white",fg="black")
        address_label.grid(row=3,column=2,padx=5,pady=5,sticky=W)
        
        address_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,width=15,font=("verdana",12,"bold"))
        address_entry.grid(row=3,column=3,padx=5,pady=5,sticky=W)
        
        #TEACHER
        
        teacher_label=Label(class_student_frame,text="Class Teacher:",font=("verdana",11,"bold"),bg="white",fg="black")
        teacher_label.grid(row=4,column=0,padx=5,pady=5,sticky=W)
        
        teacher_entry=ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=15,font=("verdana",12,"bold"))
        teacher_entry.grid(row=4,column=1,padx=5,pady=5,sticky=W)
        
        
        
        #RADIO BUTTON
        self.var_radio1=StringVar()
        radiobtn1=ttk.Radiobutton(class_student_frame,text="Take Photo Sample",variable=self.var_radio1,value="Yes")
        radiobtn1.grid(row=5,column=0,padx=5,pady=5,sticky=W)

        radiobtn1=ttk.Radiobutton(class_student_frame,text="No Photo Sample",variable=self.var_radio1,value="No")
        radiobtn1.grid(row=5,column=1,padx=5,pady=5,sticky=W)
        
        
        #BUTTON FRAME
        
        btn_frame=Frame(Left_frame,bd=2,bg="white",relief=RIDGE)
        btn_frame.place(x=10,y=390,width=635,height=60)
        
        #save button
        
        save_btn=Button(btn_frame,command=self.add_data,text="Save",width=10,font=("Gibson",13,"bold"),fg="white",bg="black")
        save_btn.grid(row=0,column=0,padx=5,pady=10,sticky=W)
        
        #update button
        update_btn=Button(btn_frame,command=self.update_data,text="Update",width=10,font=("Gibson",13,"bold"),fg="white",bg="black")
        update_btn.grid(row=0,column=1,padx=5,pady=8,sticky=W)

        #delete button
        del_btn=Button(btn_frame,command=self.delete_data,text="Delete",width=10,font=("Gibson",13,"bold"),fg="white",bg="black")
        del_btn.grid(row=0,column=2,padx=5,pady=10,sticky=W)

        #reset button
        reset_btn=Button(btn_frame,command=self.reset_data,text="Reset",width=10,font=("Gibson",13,"bold"),fg="white",bg="black")
        reset_btn.grid(row=0,column=3,padx=5,pady=10,sticky=W)

        #take photo button
        take_photo_btn=Button(btn_frame,command=self.generate_dataset,text="Take Pic",width=10,font=("Gibson",13,"bold"),fg="white",bg="black")
        take_photo_btn.grid(row=0,column=4,padx=5,pady=10,sticky=W)
        
        # #update photo button
        # update_photo_btn=Button(btn_frame,text="Update Pic",width=10,font=("Gibson",12,"bold"),fg="white",bg="black")
        # update_photo_btn.grid(row=0,column=5,padx=5,pady=10,sticky=W)
        
        #-------------------------------------------------------------------------------------------------------------------------------
        
        #RIGHT Label Frame
        RIGHT_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="STUDENT DETAILS",font=("Verdana",13,"bold"))
        RIGHT_frame.place(x=680,y=10,width=660,height=480)
        
        
        #====================================Database====================================================#
        
        search_frame=LabelFrame(RIGHT_frame,bd=2,bg="white",relief=RIDGE,text="Database",font=("verdana",12,"bold"),fg="black")
        search_frame.place(x=10,y=5,width=635,height=80)
        
        #REFRESH button
        ref_btn=Button(search_frame,text="Refresh Data",command=self.refresh_data,width=12,font=("verdana",12,"bold"),fg="white",bg="black")
        ref_btn.grid(row=0,column=3,padx=5,pady=10,sticky=W)
        
        
        
        # search_label=Label(search_frame,text="Search:",font=("verdana",12,"bold"),fg="black",bg="white")
        # search_label.grid(row=0,column=0,padx=5,pady=5,sticky=W)
        
        # # SEARCH COMBO BOX 
        # search_combo=ttk.Combobox(search_frame,width=12,font=("verdana",12,"bold"),state="readonly")
        # search_combo["values"]=("Select","Roll-No","Phone No")
        # search_combo.current(0)
        # search_combo.grid(row=0,column=1,padx=5,pady=15,sticky=W)
        
        # search_entry = ttk.Entry(search_frame,width=12,font=("verdana",12,"bold"))
        # search_entry.grid(row=0,column=2,padx=5,pady=5,sticky=W)
        
        # #FIND BUTTON
        # search_btn=Button(search_frame,text="Find",width=8,font=("verdana",12,"bold"),fg="white",bg="black")
        # search_btn.grid(row=0,column=3,padx=5,pady=10,sticky=W)


        # #SHOW BUTTON
        # ShowAll_btn=Button(search_frame,text="Search",width=8,font=("verdana",12,"bold"),fg="white",bg="black")
        # ShowAll_btn.grid(row=0,column=4,padx=5,pady=10,sticky=W)
        
        
        
        
        
        #=================================TABLE FRAME===========================================================#
        
        table_frame = Frame(RIGHT_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=10,y=90,width=635,height=360)
        

        #SCROLL BAR
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        #TABLE CREATION 
        #DUMMY NAME SHOULD BE GIVEN IN  TUPLE SUCH AS "ID"#
        self.student_table = ttk.Treeview(table_frame,column=("Name","Div","Gender","DOB","Mob-No","Address","Roll-No","Email","Teacher","Photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        
        
        self.student_table.heading("Name", text="Name")
        self.student_table.heading("Div", text="Division")
        self.student_table.heading("Gender", text="Gender")
        self.student_table.heading("DOB", text="DOB")
        self.student_table.heading("Mob-No", text="Mob-No")
        self.student_table.heading("Address", text="Address")
        self.student_table.heading("Roll-No", text="Roll-No")
        self.student_table.heading("Email", text="Email")
        self.student_table.heading("Teacher", text="Teacher")
        self.student_table.heading("Photo", text="PhotoSample")

        self.student_table["show"]="headings"
        
        
        #SETTING WIDTH OF COLUMNS
        
        
        self.student_table.column("Name",width=100)
        self.student_table.column("Div",width=100)
        self.student_table.column("Gender",width=100)
        self.student_table.column("DOB",width=100)
        self.student_table.column("Mob-No",width=100)
        self.student_table.column("Address",width=100)
        self.student_table.column("Roll-No",width=100)
        self.student_table.column("Email",width=100)
        self.student_table.column("Teacher",width=100)
        self.student_table.column("Photo",width=100)

        
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
       
        #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
        #++++++++++++++++++++++++++++++++++++++++++++++FUNCTION DECLARATION++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
        
    def has_symbols(self, input_string):
    # Check if the input string contains any symbols
        return bool(re.search(r'[!@#$%^&*(),.?":{}|<>/]', input_string))  
      
        #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
        #+++++++++++++++++++++++++++++++++++++++++++++++++++++ADD DATA+ +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
        #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
        
    def add_data(self):
        if self.var_roll.get()==""  or self.var_std_name.get()=="" or self.var_div.get()=="" or self.var_roll.get()=="" or self.var_gender.get()=="" or self.var_dob.get()=="" or self.var_email.get()=="" or self.var_phone.get()=="" or self.var_address.get()=="" or self.var_teacher.get()=="":
            messagebox.showerror("Error","Please Fill All Fields are Required!",parent=self.root)
            
        elif (
            self.has_symbols(self.var_std_name.get())
            or self.has_symbols(self.var_div.get())
            or self.has_symbols(self.var_roll.get())
            or self.has_symbols(self.var_gender.get())
            or self.has_symbols(self.var_dob.get())
            or self.has_symbols(self.var_phone.get())
            or self.has_symbols(self.var_address.get())
            or self.has_symbols(self.var_teacher.get())
            
            
        ):
            messagebox.showerror("Error", "Fields should not contain symbols!", parent=self.root)
            
        elif len(self.var_phone.get()) > 10: # Check if phone number length exceeds 10 digits
            messagebox.showerror("Error", "Not a Valid length of number! Phone number should be 10 digits or less.", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(username='root', password='niraj',host='localhost',database='face_recognition',port=3306)
                mycursor = conn.cursor()
                mycursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                self.var_std_name.get(),
                self.var_div.get(),
                self.var_gender.get(),
                self.var_dob.get(),
                self.var_phone.get(),
                self.var_address.get(),
                self.var_roll.get(),
                self.var_email.get(),
                self.var_teacher.get(),
                self.var_radio1.get()
                ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","All Records are Saved!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)
                

            
      # ===========================FETCHING DATA FROM DATABASE TABLE ================================#
              
    def fetch_data(self):
        conn = mysql.connector.connect(username='root', password='niraj',host='localhost',database='face_recognition',port=3306)
        mycursor = conn.cursor()

        mycursor.execute("select * from student")
        data=mycursor.fetchall()

        if len(data)!= 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()  
        
        
        
        # =====================================================================================================# 
        # ======================================REFRESH DATA FROM SQL==========================================# 
        # =====================================================================================================#                 
                    
    def refresh_data(self):
        try:
            conn = mysql.connector.connect(username='root', password='niraj', host='localhost', database='face_recognition', port=3306)
            mycursor = conn.cursor()
            mycursor.execute("SELECT * FROM student")
            rows = mycursor.fetchall()  # Fetch all rows
            self.student_table.delete(*self.student_table.get_children())  # Clear existing data
            for row in rows:
                # Insert each row into the Treeview widget
                self.student_table.insert("", "end", values=row)
            conn.close()
            messagebox.showinfo("Success", "Data refreshed successfully!", parent=self.root)
        except Exception as es:
            messagebox.showerror("Error", f"Error while refreshing data: {str(es)}", parent=self.root)    
        
        
        # +++++++++++++++++++++++++++++++++++++GET CURSOR FUNCTION +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
        
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]
        
        self.var_std_name.set(data[0]),
        self.var_div.set(data[1]),
        self.var_gender.set(data[2]),
        self.var_dob.set(data[3]),
        self.var_phone.set(data[4]),
        self.var_address.set(data[5]),
        self.var_roll.set(data[6]),
        self.var_email.set(data[7]),
        self.var_teacher.set(data[8]),
        self.var_radio1.set(data[9])
        
        #+++++++++++++++++++++++++++++++++++++++++++++++================== ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
        #+++++++++++++++++++++++++++++++++++++++++++++++  UPDATE FUNCTION +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
        #+++++++++++++++++++++++++++++++++++++++++++++++================== ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
        
    def update_data(self):
        if self.var_roll.get() == ""  or self.var_std_name.get() == "" or self.var_div.get() == "" or self.var_roll.get() == "" or self.var_gender.get() == "" or self.var_dob.get() == "" or self.var_email.get() == "" or self.var_phone.get() == "" or self.var_address.get() == "" or self.var_teacher.get() == "":
            messagebox.showerror("Error", "Please Fill All Fields are Required!", parent=self.root)
        elif (
            self.has_symbols(self.var_std_name.get())
            or self.has_symbols(self.var_div.get())
            or self.has_symbols(self.var_roll.get())
            or self.has_symbols(self.var_gender.get())
            or self.has_symbols(self.var_dob.get())
            or self.has_symbols(self.var_phone.get())
            or self.has_symbols(self.var_address.get())
            or self.has_symbols(self.var_teacher.get())
            
        ):
            messagebox.showerror("Error", "Symbols are not allowed!", parent=self.root)
        elif len(self.var_phone.get()) > 10: # Check if phone number length exceeds 10 digits
            messagebox.showerror("Error", "Not a Valid length of number! Phone number should be 10 digits or less.", parent=self.root)
    
        else:
            try:
                Update = messagebox.askyesno("Update", "Do you want to Update this Student Details!", parent=self.root)
                if Update > 0:
                    conn = mysql.connector.connect(username='root', password='niraj', host='localhost', database='face_recognition', port=3306)
                    mycursor = conn.cursor()
                    mycursor.execute("update student set Name=%s,Division=%s,Gender=%s,DOB=%s,`Mob-No`=%s,Address=%s,Email=%s,Teacher=%s,PhotoSample=%s where `Roll-No`=%s", (
                    self.var_std_name.get(),
                    self.var_div.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_email.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get(),
                    self.var_roll.get(),
                ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success", "Successfully Updated!", parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

                
#===========================================================================================================================================================#
#=================================================================Delete Function===========================================================================#
#===========================================================================================================================================================#
                
    def delete_data(self):
        if self.var_roll.get()=="":
            messagebox.showerror("Error","Roll Number Must be Required!",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete","Do you want to Delete?",parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(username='root', password='niraj',host='localhost',database='face_recognition',port=3306)
                    mycursor = conn.cursor() 
                    sql="delete from student where `Roll-No`=%s"
                    val=(self.var_roll.get(),)
                    mycursor.execute(sql,val)
                else:
                    if not delete:
                        return

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully Deleted!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)   
                
#===========================================================================================================================================================#
#=================================================================RESET Function===========================================================================#
#===========================================================================================================================================================#
    
                       
    def reset_data(self):
        self.var_std_name.set(""),
        self.var_div.set(""),
        self.var_gender.set("Male"),
        self.var_dob.set(""),
        self.var_phone.set(""),
        self.var_address.set(""),
        self.var_roll.set(""),
        self.var_email.set(""),
        self.var_teacher.set(""),
        self.var_radio1.set("")
        
#===========================================================================================================================================================#
#=================================================================PHOTO SAMPLE===========================================================================#
#===========================================================================================================================================================#


    def generate_dataset(self):
        if self.var_roll.get() == ""  or self.var_std_name.get() == "" or self.var_div.get() == "" or self.var_roll.get() == "" or self.var_gender.get() == "" or self.var_dob.get() == "" or self.var_email.get() == "" or self.var_phone.get() == "" or self.var_address.get() == "" or self.var_teacher.get() == "":
            messagebox.showerror("Error", "Please Fill All Fields are Required!", parent=self.root)
        else:
            try:
                
                conn = mysql.connector.connect(username='root', password='niraj',host='localhost',database='face_recognition',port=3306)
                mycursor = conn.cursor()
                mycursor.execute("select * from student")
                myreslut = mycursor.fetchall()
                id=0
                for x in myreslut:
                    id+=1

                mycursor.execute("update student set Name=%s,Division=%s,Gender=%s,DOB=%s,`Mob-No`=%s,Address=%s,Email=%s,Teacher=%s,PhotoSample=%s where `Roll-No`=%s", (
                    self.var_std_name.get(),
                    self.var_div.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_email.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get(),
                    self.var_roll.get()==id+1,
                      
                    ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
            
                
#===========================================================================================================================================================#
#=================================================================OPEN CV===================================================================================#
#==============+============================================================================================================================================#
                
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml") 
                
                def face_croped(img):
                    # conver gary sacle
                    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray,1.3,5)
                    #Scaling factor 1.3
                    # Minimum naber 5
                    for (x,y,w,h) in faces:
                        face_croped=img[y:y+h,x:x+w]
                        return face_croped
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_croped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_croped(my_frame),(200,200))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_path="data/Roll."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)        
                        cv2.imshow("Capture Images",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating dataset completed!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root) 
        
    
#MAIN CLASS OBJECT       
if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()


from tkinter import*  
# Importing Tkinter for GUI
from tkinter import ttk 
# ttk helps to modify the GUI
from PIL import Image,ImageTk
# for importing images and adjusting the design
from tkinter import messagebox
from tkcalendar import DateEntry
from mysql.connector import IntegrityError
import mysql.connector
import cv2
import re
import tkinter as tk
import os
import csv
from tkinter import filedialog
from datetime import date




mydata=[]

class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition System")
        #NO MAXIMIZE SCREEN
        self.root.resizable(False, False)
        
#--------------------------------------------------#
        #-----------Variables--------------#
#--------------------------------------------------#
        self.var_roll=StringVar()
        self.var_name=StringVar()
        self.var_gender=StringVar()
        self.var_time=StringVar()
        self.var_date=StringVar()
        self.var_attend=StringVar()
        
        
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
        title_lbl = Label(bg_img, text="Attendance Management", font=("calibri", 30, "bold"), bg="white", fg="black")
        title_lbl.place(x=0,y=0,width=1366,height=45)
        
#=========================================================================================#
        #========================SECTION CREATION=================================#
#=========================================================================================#
        # Creating Frame 
        main_frame = Frame(bg_img,bd=2,bg="white") #bd mean border 
        main_frame.place(x=5,y=55,width=1355,height=510)

        # Left Label Frame 
        left_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Record Management",font=("verdana",14,"bold"),fg="dark blue")
        left_frame.place(x=10,y=10,width=660,height=480)
        
        
         #ROLL NO
        
        roll_no_div_label=Label(left_frame,text="Roll.No:",font=("verdana",11,"bold"),bg="white",fg="black")
        roll_no_div_label.grid(row=0,column=0,padx=5,pady=5,sticky=W)
        
        roll_no_entry=ttk.Entry(left_frame,textvariable=self.var_roll,width=15,font=("verdana",12,"bold"))
        roll_no_entry.grid(row=0,column=1,padx=5,pady=5,sticky=W)
        
        #STUDENT NAME
        
        studentName_label=Label(left_frame,text="Std-Name:",font=("verdana",11,"bold"),bg="white",fg="black")
        studentName_label.grid(row=0,column=2,padx=5,pady=5,sticky=W)
        
        studentName_entry=ttk.Entry(left_frame,textvariable=self.var_name,width=15,font=("verdana",12,"bold"))
        studentName_entry.grid(row=0,column=3,padx=5,pady=5,sticky=W)
        
         #GENDER
        
        gender_label=Label(left_frame,text="Gender:",font=("verdana",11,"bold"),bg="white",fg="black")
        gender_label.grid(row=1,column=0,padx=5,pady=5,sticky=W)
        
        gender_combo=ttk.Entry(left_frame,textvariable=self.var_gender,width=15,font=("verdana",12,"bold"))
        gender_combo.grid(row=1,column=1,padx=5,pady=5,sticky=W)
        
        #time
        time_label = Label(left_frame,text="Time:",font=("verdana",12,"bold"),fg="black",bg="white")
        time_label.grid(row=1,column=2,padx=5,pady=5,sticky=W)

        time_entry = ttk.Entry(left_frame,textvariable=self.var_time,width=15,font=("verdana",12,"bold"))
        time_entry.grid(row=1,column=3,padx=5,pady=5,sticky=W)

        #Date 
        date_label = Label(left_frame,text="Date:",font=("verdana",12,"bold"),fg="black",bg="white")
        date_label.grid(row=2,column=0,padx=5,pady=5,sticky=W)

        date_entry = ttk.Entry(left_frame,textvariable=self.var_date,width=15,font=("verdana",12,"bold"))
        date_entry.grid(row=2,column=1,padx=5,pady=5,sticky=W)

        #Attendance
        student_attend_label = Label(left_frame,text="Attend-status:",font=("verdana",12,"bold"),fg="black",bg="white")
        student_attend_label.grid(row=2,column=2,padx=5,pady=5,sticky=W)

        attend_combo=ttk.Combobox(left_frame,textvariable=self.var_attend,width=13,font=("verdana",12,"bold"),state="readonly")
        attend_combo["values"]=("Status","Present","Absent","Late")
        attend_combo.current(0)
        attend_combo.grid(row=2,column=3,padx=5,pady=5,sticky=W)
        
        
        # ===============================Table Sql Data View==========================
        table_frame = Frame(left_frame,bd=5,bg="white",relief=RIDGE)
        table_frame.place(x=10,y=100,width=635,height=310)

        #scroll bar 
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        #create table 
        self.attendanceReport_left = ttk.Treeview(table_frame,column=("Roll_No","Name","Gender","Time","Date","Attend"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.attendanceReport_left.xview)
        scroll_y.config(command=self.attendanceReport_left.yview)

        self.attendanceReport_left.heading("Roll_No",text="Roll.No")
        self.attendanceReport_left.heading("Name",text="Std-Name")
        self.attendanceReport_left.heading("Gender",text="Gender")
        self.attendanceReport_left.heading("Time",text="Time")
        self.attendanceReport_left.heading("Date",text="Date")
        self.attendanceReport_left.heading("Attend",text="Attend-status")
        self.attendanceReport_left["show"]="headings"


        # Set Width of Colums 
        self.attendanceReport_left.column("Roll_No",width=100)
        self.attendanceReport_left.column("Name",width=100)
        self.attendanceReport_left.column("Gender",width=100)
        self.attendanceReport_left.column("Time",width=100)
        self.attendanceReport_left.column("Date",width=100)
        self.attendanceReport_left.column("Attend",width=100)
        
        self.attendanceReport_left.pack(fill=BOTH,expand=1)
        self.attendanceReport_left.bind("<ButtonRelease>",self.get_cursorleft)
        
        # =========================button section========================

        #Button Frame
        btn_frame = Frame(left_frame,bd=5,bg="white",relief=RIDGE)
        btn_frame.place(x=10,y=390,width=635,height=60)

        #Import button
        imp_btn=Button(btn_frame,text="Import CSV",command=self.importCsv,width=12,font=("verdana",12,"bold"),fg="white",bg="black")
        imp_btn.grid(row=0,column=0,padx=6,pady=10,sticky=W)

        #Export button
        exp_btn=Button(btn_frame,text="Export CSV",command=self.exportCsv,width=12,font=("verdana",12,"bold"),fg="white",bg="black")
        exp_btn.grid(row=0,column=1,padx=6,pady=8,sticky=W)

        #Update button
        update_btn=Button(btn_frame,text="Insert Details",command=self.action,width=12,font=("verdana",12,"bold"),fg="white",bg="black")
        update_btn.grid(row=0,column=2,padx=6,pady=10,sticky=W)

        #reset button
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=12,font=("verdana",12,"bold"),fg="white",bg="black")
        reset_btn.grid(row=0,column=3,padx=6,pady=10,sticky=W)



        # Right section=======================================================

        # Right Label Frame 
        right_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Database Management",font=("verdana",14,"bold"),fg="dark blue")
        right_frame.place(x=680,y=10,width=660,height=480)
        
         # -----------------------------Table Frame-------------------------------------------------
        #Table Frame 
        #Searching System in Right Label Frame 
        table_frame = Frame(right_frame,bd=5,bg="white",relief=RIDGE)
        table_frame.place(x=10,y=90,width=635,height=360)

        #scroll bar 
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        #create table 
        self.attendanceReport = ttk.Treeview(table_frame,column=("Roll_No","Name","Gender","Time","Date","Attend"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.attendanceReport.xview)
        scroll_y.config(command=self.attendanceReport.yview)

        self.attendanceReport.heading("Roll_No",text="Roll.No")
        self.attendanceReport.heading("Name",text="Std-Name")
        self.attendanceReport.heading("Gender",text="Gender")
        self.attendanceReport.heading("Time",text="Time")
        self.attendanceReport.heading("Date",text="Date")
        self.attendanceReport.heading("Attend",text="Attend-status")
        self.attendanceReport["show"]="headings"


        # Set Width of Colums 
        self.attendanceReport.column("Roll_No",width=100)
        self.attendanceReport.column("Name",width=100)
        self.attendanceReport.column("Gender",width=100)
        self.attendanceReport.column("Time",width=100)
        self.attendanceReport.column("Date",width=100)
        self.attendanceReport.column("Attend",width=100)
        
        self.attendanceReport.pack(fill=BOTH,expand=1)
        self.attendanceReport.bind("<ButtonRelease>",self.get_cursorright)
        self.fetch_data()
        
        
        
    # =================================update for mysql button============================================#
    #Update button
        upd_btn=Button(right_frame,text="Update Data",command=self.update_data,width=12,font=("verdana",12,"bold"),fg="white",bg="black")
        upd_btn.grid(row=0,column=1,padx=6,pady=10,sticky=W)
    #DELETE button
        del_btn=Button(right_frame,text="Delete Data",command=self.delete_data,width=12,font=("verdana",12,"bold"),fg="white",bg="black")
        del_btn.grid(row=0,column=2,padx=6,pady=10,sticky=W)
        
    #REFRESH button
        ref_btn=Button(right_frame,text="Refresh Data",command=self.refresh_data,width=12,font=("verdana",12,"bold"),fg="white",bg="black")
        ref_btn.grid(row=0,column=3,padx=6,pady=10,sticky=W)
        
        
        
    # =====================================================================================================# 
    # ======================================FETCH DATA FROM MYSQL==========================================# 
    # =====================================================================================================# 
    

    def fetch_data(self):
        conn = mysql.connector.connect(username='root', password='niraj',host='localhost',database='face_recognition',port=3306)
        mycursor = conn.cursor()

        mycursor.execute("select * from stattendance")
        data=mycursor.fetchall()

        if len(data)!= 0:
            self.attendanceReport.delete(*self.attendanceReport.get_children())
            for i in data:
                self.attendanceReport.insert("",END,values=i)
            conn.commit()
        conn.close()              
        
    # =====================================================================================================# 
                                     # REFUNCTION FOR FORM VALIDATION #
    # =====================================================================================================# 
    
    def has_symbols(self, input_string):
    # Check if the input string contains any symbols
        return bool(re.search(r'[!@#$%^&*(),.?"{}|<>]', input_string)) 
    
    # =====================================================================================================# 
    # ======================================UPDATE IN MYSQL================================================# 
    # =====================================================================================================# 
    
    def update_data(self):
        if self.var_roll.get()=="" or self.var_name.get()=="" or self.var_gender.get()=="" or self.var_time.get()=="" or self.var_date.get()=="" or self.var_attend.get()=="Status":
            messagebox.showerror("Error","Please Fill All Fields are Required!",parent=self.root)
            
        elif (
            self.has_symbols(self.var_name.get())
            or self.has_symbols(self.var_date.get())
            or self.has_symbols(self.var_roll.get())
            or self.has_symbols(self.var_gender.get())
            or self.has_symbols(self.var_time.get())
    
        ):
            messagebox.showerror("Error", "Not a Valid Input", parent=self.root)    
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to Update this Student Attendance!",parent=self.root)
                if Update > 0:
                    conn = mysql.connector.connect(username='root', password='niraj',host='localhost',database='face_recognition',port=3306)
                    mycursor = conn.cursor()
                    mycursor.execute("update stattendance set Roll_No=%s,Name=%s,Gender=%s,Time=%s,Date=%s,Attend=%s where Roll_No=%s",( 
                    
                    self.var_roll.get(),
                    self.var_name.get(),
                    self.var_gender.get(),
                    self.var_time.get(),
                    self.var_date.get(),
                    self.var_attend.get(),
                    self.var_roll.get() 
                    ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Successfully Updated!",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)  
                
        # =====================================================================================================# 
        # ======================================DELETE FROM MYSQL==============================================# 
        # =====================================================================================================#     
        
    def delete_data(self):
            if self.var_roll.get()=="":
                messagebox.showerror("Error","Roll No Must be Required!",parent=self.root)
            else:
                try:
                    delete=messagebox.askyesno("Delete","Do you want to Delete?",parent=self.root)
                    if delete>0:
                        conn = mysql.connector.connect(username='root', password='niraj',host='localhost',database='face_recognition',port=3306)
                        mycursor = conn.cursor() 
                        sql="delete from stattendance where Roll_No=%s"
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
    
        # =====================================================================================================# 
        # ======================================REFRESH DATA FROM SQL==========================================# 
        # =====================================================================================================#                 
                    
    def refresh_data(self):
        try:
            conn = mysql.connector.connect(username='root', password='niraj', host='localhost', database='face_recognition', port=3306)
            mycursor = conn.cursor()
            mycursor.execute("SELECT * FROM stattendance")
            rows = mycursor.fetchall()  # Fetch all rows
            self.attendanceReport.delete(*self.attendanceReport.get_children())  # Clear existing data
            for row in rows:
                # Insert each row into the Treeview widget
                self.attendanceReport.insert("", "end", values=row)
            conn.close()
            messagebox.showinfo("Success", "Data refreshed successfully!", parent=self.root)
        except Exception as es:
            messagebox.showerror("Error", f"Error while refreshing data: {str(es)}", parent=self.root)

  

    # =========================Fetch Data Import data ======================#

    def fetchData(self,rows):
        global mydata
        mydata = rows
        self.attendanceReport_left.delete(*self.attendanceReport_left.get_children())
        for i in rows:
            self.attendanceReport_left.insert("",END,values=i)
            print(i)
        

    def importCsv(self):
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
        self.fetchData(mydata)
        
        #==================Export CSV================#
        
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("Error","No Data Found!",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Successfuly","Export Data Successfully!")
        except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)  
                
    #=============Cursor Function for CSV========================#

    def get_cursorleft(self,event=""):
        cursor_focus = self.attendanceReport_left.focus()
        content = self.attendanceReport_left.item(cursor_focus)
        data = content["values"]

        self.var_roll.set(data[0]),
        self.var_name.set(data[1]),
        self.var_gender.set(data[2])
        self.var_time.set(data[3]),
        self.var_date.set(data[4]),
        self.var_attend.set(data[5])              

   #=============Cursor Function for mysql========================

    def get_cursorright(self,event=""):
        cursor_focus = self.attendanceReport.focus()
        content = self.attendanceReport.item(cursor_focus)
        data = content["values"]

        self.var_roll.set(data[0]),
        self.var_name.set(data[1]),
        self.var_gender.set(data[2])
        self.var_time.set(data[3]),
        self.var_date.set(data[4]),
        self.var_attend.set(data[5]) 
        
    #============================Reset Data======================
    def reset_data(self):
        self.var_roll.set("")
        self.var_name.set("")
        self.var_gender.set("")
        self.var_time.set("")
        self.var_date.set("")
        self.var_attend.set("Status")    
        
        
        # =====================================================================================================# 
        # ======================================EXPORT UPDATE==================================================# 
        # =====================================================================================================#     
    
    def action(self):
        if self.var_roll.get()=="" or self.var_name.get=="" or self.var_gender.get()=="" or self.var_time.get()=="" or self.var_date.get()=="" or self.var_attend.get()=="Status":
            messagebox.showerror("Error","Please Fill All Fields are Required!",parent=self.root)
                
        elif (
            self.has_symbols(self.var_name.get())
            or self.has_symbols(self.var_date.get())
            or self.has_symbols(self.var_roll.get())
            or self.has_symbols(self.var_gender.get())
            or self.has_symbols(self.var_time.get())
    
        ):
            messagebox.showerror("Error", "Not a Valid Input", parent=self.root)     
        else:
            try:
                conn = mysql.connector.connect(username='root', password='niraj',host='localhost',database='face_recognition',port=3306)
                mycursor = conn.cursor()
                mycursor.execute("insert into stattendance values(%s,%s,%s,%s,%s,%s)",(
                self.var_roll.get(),
                self.var_name.get(),
                self.var_gender.get(),
                self.var_time.get(),
                self.var_date.get(),
                self.var_attend.get()
                ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","All Records are Saved in Database!",parent=self.root)
            except IntegrityError:
                messagebox.showerror("Error", "This record already exists in the database!", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)  

                
                
#MAIN CLASS OBJECT       
if __name__ == "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()
    
    
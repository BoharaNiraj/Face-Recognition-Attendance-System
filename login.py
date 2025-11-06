from tkinter import* 
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from Register import Register
import mysql.connector
import os
from train import Train
from student import Student
from train import Train
from face_recognition import Face_recognition
from attendance import Attendance
from Help import Helpsupport
from Developer import Developer
import bcrypt
from exit import Exit
import pytz
from datetime import datetime


class login:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1366x768+0+0")
        #NO MAXIMIZE SCREEN
        self.root.resizable(False, False)
        #==============================VARIBALES=====================================#
        self.var_sq=StringVar()
        self.var_sa=StringVar()
        self.var_pass=StringVar()
        #============================================================================# 

        self.bg=ImageTk.PhotoImage(file=r"D:\Face Recognition System code\Image\bg4.png")
        
        lb1_bg=Label(self.root,image=self.bg)
        lb1_bg.place(x=0,y=0, relwidth=1,relheight=1)

        frame1= Frame(self.root,bg="teal")
        frame1.place(x=560,y=170,width=340,height=450)

        img1=Image.open(r"D:\Face Recognition System code\Image\log2.png")
        img1=img1.resize((100,100),Image.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lb1img1 = Label(image=self.photoimage1,bg="teal")
        lb1img1.place(x=690,y=175, width=100,height=100)

        get_str = Label(frame1,text="Login",font=("times new roman",20,"bold"),fg="white",bg="teal")
        get_str.place(x=140,y=100)       
        
        #label1 
        username =lb1= Label(frame1,text="E-Mail:",font=("times new roman",15,"bold"),fg="white",bg="teal")
        username.place(x=30,y=160)

        #entry1 
        self.txtuser=ttk.Entry(frame1,font=("times new roman",15,"bold"))
        self.txtuser.place(x=33,y=190,width=270)


        #label2 
        pwd =lb1= Label(frame1,text="Password:",font=("times new roman",15,"bold"),fg="white",bg="teal")
        pwd.place(x=30,y=230)

        #entry2 
        self.txtpwd=ttk.Entry(frame1,font=("times new roman",15,"bold"),show="*")
        self.txtpwd.place(x=33,y=260,width=270)


        # Creating Button Login
        loginbtn=Button(frame1,text="Login",command=self.login,font=("times new roman",15,"bold"),bd=0,relief=RIDGE,fg="teal",bg="white",activeforeground="white",activebackground="#007ACC")
        loginbtn.place(x=33,y=320,width=270,height=35)


        # Creating Button Registration
        loginbtn=Button(frame1,command=self.reg,text="Register",font=("times new roman",10,"bold"),bd=3,relief=RIDGE,fg="white",bg="teal",activeforeground="orange",activebackground="#002B53")
        loginbtn.place(x=33,y=370,width=70,height=25)


        # Creating Button Forget
        loginbtn=Button(frame1,command=self.Forget_pass,text="Forget",font=("times new roman",10,"bold"),bd=3,relief=RIDGE,fg="white",bg="teal",activeforeground="orange",activebackground="#002B53")
        loginbtn.place(x=115,y=370,width=70,height=25)
        
          
        
    def reg(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)
#=======================================================================================================#
#============================================LOGIN FUNCTION=============================================#
#=======================================================================================================#

    def login(self):
        if (self.txtuser.get()=="" or self.txtpwd.get()==""):
            messagebox.showerror("Error","All Field Required!")
        
        else:
            # Connect to the database
            conn = mysql.connector.connect(username='root', password='niraj', host='localhost', database='face_recognition', port=3306)
            mycursor = conn.cursor()

            # Retrieve hashed password from the database based on email
            mycursor.execute("SELECT pass FROM register WHERE email = %s", (self.txtuser.get(),))
            row = mycursor.fetchone()

            if row is None:
                # User not found
                messagebox.showerror("Error", "Invalid Username or Password!")
            else:
                # Verify the provided password with the hashed password from the database
                stored_hashed_password = row[0]
                provided_password = self.txtpwd.get()

                if bcrypt.checkpw(provided_password.encode('utf-8'), stored_hashed_password.encode('utf-8')):
                    # Passwords match, allow login
                    open_min = messagebox.askyesno("YesNo", "Access the System")
                    if open_min:
                        self.new_window = Toplevel(self.root)
                        self.app = FaceRecognitionSystem(self.new_window)
                else:
                    # Passwords do not match
                    messagebox.showerror("Error", "Invalid Username and Password!")
            conn.commit()
            conn.close()    
        
        #==========================================================================================================#
        #============================================RESET PASSWORD FUNCTION=======================================#
        #==========================================================================================================# 

    def Reset_pass(self):
        if self.var_sq.get() == "Select":
            messagebox.showerror("Error", "Select the Security Question!", parent=self.root2)
        elif self.var_sa.get() == "":
            messagebox.showerror("Error", "Please Enter the Answer!", parent=self.root2)
        elif self.var_pass.get() == "":
            messagebox.showerror("Error", "Please Enter the New Password!", parent=self.root2)
        else:
            try:
                conn = mysql.connector.connect(username='root', password='niraj', host='localhost', database='face_recognition', port=3306)
                mycursor = conn.cursor()

                # Retrieve user details based on email, security question, and answer
                query = "SELECT * FROM register WHERE email = %s AND securityque = %s AND secanswer = %s"
                value = (self.txtuser.get(), self.var_sq.get(), self.var_sa.get())
                mycursor.execute(query, value)
                row = mycursor.fetchone()

                if row is None:
                    messagebox.showerror("Error", "Invalid Answer!", parent=self.root2)
                else:
                    # Hash the new password before updating it in the database
                    hashed_password = self.hash_password(self.var_pass.get())

                    # Update the password in the database
                    update_query = "UPDATE register SET pass = %s WHERE email = %s"
                    update_values = (hashed_password, self.txtuser.get())
                    mycursor.execute(update_query, update_values)

                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Info", "Successfully Your password has been reset, Please login with the new Password!", parent=self.root2)

            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root2)

    def hash_password(self, password):
        # Generate a salt and hash the password using bcrypt
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed_password
        
        #=======================================================================================#
        #===================================FORGOT PASSWORD FUNCTION============================#
        #=======================================================================================#
        
    def Forget_pass(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please Enter the Email ID to reset Password!")
        else:
            conn = mysql.connector.connect(username='root', password='niraj',host='localhost',database='face_recognition',port=3306)
            mycursor = conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            mycursor.execute(query,value)
            row=mycursor.fetchone()
            # print(row)

            if row==None:
                messagebox.showerror("Error","Please Enter the Valid Email ID!")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.configure(bg="teal")
                self.root2.title("Forget Password")
                self.root2.geometry("400x400+610+170")
                l=Label(self.root2,text="Forget Password",font=("times new roman",30,"bold"),fg="black",bg="teal")
                l.place(x=0,y=10,relwidth=1)
                # -------------------fields-------------------
                #label1 
                ssq =lb1= Label(self.root2,text="Select Security Question:",font=("times new roman",15,"bold"),fg="black",bg="teal")
                ssq.place(x=70,y=80)

                #Combo Box1
                self.combo_security = ttk.Combobox(self.root2,textvariable=self.var_sq,font=("times new roman",15,"bold"),state="readonly")
                self.combo_security["values"]=("Select","Your Date of Birth","Your Nick Name","Your Favorite Book")
                self.combo_security.current(0)
                self.combo_security.place(x=70,y=110,width=270)


                #label2 
                sa =lb1= Label(self.root2,text="Security Answer:",font=("times new roman",15,"bold"),fg="black",bg="teal")
                sa.place(x=70,y=150)

                #entry2 
                self.txtpwd=ttk.Entry(self.root2,textvariable=self.var_sa,font=("times new roman",15,"bold"))
                self.txtpwd.place(x=70,y=180,width=270)

                #label2 
                new_pwd =lb1= Label(self.root2,text="New-Password:",font=("times new roman",15,"bold"),fg="black",bg="teal")
                new_pwd.place(x=70,y=220)

                #entry2 
                self.new_pwd=ttk.Entry(self.root2,textvariable=self.var_pass,font=("times new roman",15,"bold"))
                self.new_pwd.place(x=70,y=250,width=270)

                # Creating Button New Password
                loginbtn=Button(self.root2,command=self.Reset_pass,text="Reset Password",font=("times new roman",15,"bold"),bd=0,relief=RIDGE,fg="#fff",bg="dark blue",activeforeground="white",activebackground="#007ACC")
                loginbtn.place(x=70,y=300,width=270,height=35)
                
                


#======================================================MAIN CLASS=======================================================#               
                
                
class FaceRecognitionSystem:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition System")
        
        #NO MAXIMIZE SCREEN
        self.root.resizable(False, False)


        # BANNER IMAGE
        img = Image.open(r"D:\Face Recognition System code\Image\ban.jpg")
        img=img.resize((1366,130),Image.LANCZOS)
        self.photoimage = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimage)
        f_lbl.place(x=0,y=0,width=1366,height=130)


        # BACKGROUND IMAGE
        img1 = Image.open(r"D:\Face Recognition System code\Image\bg4.png")
        img1=img1.resize((1366,768),Image.LANCZOS)
        self.photoimage1 = ImageTk.PhotoImage(img1)

        bg_img = Label(self.root, image=self.photoimage1)
        bg_img.place(x=0,y=130,width=1366,height=768)
        

        # TITLE LABEL
        title_lbl = Label(bg_img, text="Face Recognition Attendance Software", font=("Bell Gothic Std Black", 30, "bold"), bg="white", fg="black")
        title_lbl.place(x=0,y=0,width=1366,height=45)
        
        #STUDENT BUTTON
        img2 = Image.open(r"D:\Face Recognition System code\Image\std1.jpg")
        img2=img2.resize((180,180),Image.LANCZOS)
        self.photoimage2 = ImageTk.PhotoImage(img2)
        
        b1=Button(bg_img,image=self.photoimage2,command=self.student_details,cursor="hand2")
        b1.place(x=250,y=100,width=180,height=180)
        
        
        b1_1 = Button(bg_img, text="Student Detail",command=self.student_details, cursor="hand2", font=("times new roman", 15, "bold"), bg="black", fg="white")
        b1_1.place(x=250,y=280,width=180,height=45)
        
        #FACE DETECT BUTTON
        img3 = Image.open(r"D:\Face Recognition System code\Image\det1.jpg")
        img3=img3.resize((180,180),Image.LANCZOS)
        self.photoimage3 = ImageTk.PhotoImage(img3)
        
        b1=Button(bg_img,image=self.photoimage3,cursor="hand2",command=self.face_rec)
        b1.place(x=480,y=100,width=180,height=180)
        
        
        b1_1 = Button(bg_img, text="Face Detect",command=self.face_rec ,cursor="hand2", font=("times new roman", 15, "bold"), bg="black", fg="white")
        b1_1.place(x=480,y=280,width=180,height=45)
        
        
        #ATTENDACNE BUTTON
        img4 = Image.open(r"D:\Face Recognition System code\Image\at.png")
        img4=img4.resize((180,170),Image.LANCZOS)
        self.photoimage4 = ImageTk.PhotoImage(img4)
        
        b1=Button(bg_img,command=self.face_attendance,image=self.photoimage4,cursor="hand2")
        b1.place(x=710,y=100,width=180,height=180)
        
        
        b1_1 = Button(bg_img, text="Attendance", cursor="hand2",command=self.face_attendance, font=("times new roman", 15, "bold"), bg="black", fg="white")
        b1_1.place(x=710,y=280,width=180,height=45)
        
        
        
        #SUPPORT BUTTON
        img5 = Image.open(r"D:\Face Recognition System code\Image\hlp.jpg")
        img5=img5.resize((180,180),Image.LANCZOS)
        self.photoimage5 = ImageTk.PhotoImage(img5)
        
        b1=Button(bg_img,image=self.photoimage5,command=self.Help,cursor="hand2")
        b1.place(x=940,y=100,width=180,height=180)
        
        
        b1_1 = Button(bg_img, text="Tech Support", cursor="hand2",command=self.Help ,font=("times new roman", 15, "bold"), bg="black", fg="white")
        b1_1.place(x=940,y=280,width=180,height=45)
        
        
        #DATA TRAIN BUTTON
        img6 = Image.open(r"D:\Face Recognition System code\Image\tra.jpg")
        img6=img6.resize((200,200),Image.LANCZOS)
        self.photoimage6 = ImageTk.PhotoImage(img6)
        
        b1=Button(bg_img,image=self.photoimage6,command=self.train_data,cursor="hand2")
        b1.place(x=250,y=330,width=180,height=180)
        
        
        b1_1 = Button(bg_img, text="Train Data", cursor="hand2",command=self.train_data ,font=("times new roman", 15, "bold"), bg="black", fg="white")
        b1_1.place(x=250,y=510,width=180,height=45)
        
        
        #DATA SET BUTTON
        img7 = Image.open(r"D:\Face Recognition System code\Image\set.png")
        img7=img7.resize((180,180),Image.LANCZOS)
        self.photoimage7 = ImageTk.PhotoImage(img7)
        
        b1=Button(bg_img,image=self.photoimage7,cursor="hand2",command=self.open_img )
        b1.place(x=480,y=330,width=180,height=180)
        
        
        b1_1 = Button(bg_img, text="Data Set", cursor="hand2",command=self.open_img ,font=("times new roman", 15, "bold"), bg="black", fg="white")
        b1_1.place(x=480,y=510,width=180,height=45)
        
        
        #CREATOR BUTTON
        img8 = Image.open(r"D:\Face Recognition System code\Image\dev.jpg")
        img8=img8.resize((180,180),Image.LANCZOS)
        self.photoimage8 = ImageTk.PhotoImage(img8)
        
        b1=Button(bg_img,image=self.photoimage8,cursor="hand2",command=self.developer)
        b1.place(x=710,y=330,width=180,height=180)
        
        
        b1_1 = Button(bg_img, text="Creator",command=self.developer ,cursor="hand2", font=("times new roman", 15, "bold"), bg="black", fg="white")
        b1_1.place(x=710,y=510,width=180,height=45)
        
        
        
        
        #EXIT BUTTON
        img9 = Image.open(r"D:\Face Recognition System code\Image\exi.jpg")
        img9=img9.resize((180,180),Image.LANCZOS)
        self.photoimage9 = ImageTk.PhotoImage(img9)
        
        b1=Button(bg_img,image=self.photoimage9,cursor="hand2",command=self.Close)
        b1.place(x=940,y=330,width=180,height=180)
        
        
        b1_1 = Button(bg_img, text="Exit",command=self.Close,cursor="hand2", font=("times new roman", 15, "bold"), bg="black", fg="white")
        b1_1.place(x=940,y=510,width=180,height=45)
    
    
        
    def open_img(self):
        os.startfile("data")
        
    def Close(self):
        self.root.destroy()
        
        #==================================================FUNCTION====================================================================#
    

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
        
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
        
    def face_rec(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_recognition(self.new_window)
        
    def face_attendance(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)
        
    def developer(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)
        
    def Help(self):
        self.new_window=Toplevel(self.root)
        self.app=Helpsupport(self.new_window)
                
                
                
                
                
                
                
                
                
                
                
                
           
          
#MAIN CLASS OBJECT       
if __name__ == "__main__":
    root=Tk()
    obj=login(root)
    root.mainloop()
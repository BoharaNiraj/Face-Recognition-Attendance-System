from tkinter import*  
# Importing Tkinter for GUI
from tkinter import ttk 
# ttk helps to modify the GUI
from PIL import Image,ImageTk
# for importing images and adjusting the design
import os
import cv2
from student import Student
from train import Train
from face_recognition import Face_recognition
from attendance import Attendance
from exit import Exit
from Developer import Developer
from Help import Helpsupport
import sys


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
        
        #==================================================FUNCTION====================================================================

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
        
    
   
             
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 2 and sys.argv[1] == "login":
        root = Tk()
        obj = FaceRecognitionSystem(root)
        root.mainloop()
    else:
        print("Access denied. Please Login to access this Module .")




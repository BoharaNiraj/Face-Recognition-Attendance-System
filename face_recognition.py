from tkinter import*  
# Importing Tkinter for GUI
from tkinter import ttk 
# ttk helps to modify the GUI
from PIL import Image,ImageTk
# for importing images and adjusting the design
from tkinter import messagebox
from time import strftime
from datetime import datetime as dt
# from twilio import Client
import mysql.connector
import cv2
import os
import numpy as np
import datetime
import pytz
import csv


class Face_recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition System")
        #NO MAXIMIZE SCREEN
        self.root.resizable(False, False)
        # BANNER IMAGE
        img = Image.open(r"N:\Face Recognition System code\Image\ban.jpg")
        img=img.resize((1366,130),Image.LANCZOS)
        self.photoimage = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimage)
        f_lbl.place(x=0,y=0,width=1366,height=130)
        
        #Background Image
        bg1=Image.open(r"N:\Face Recognition System code\Image\bg4.png")
        bg1=bg1.resize((1366,768),Image.LANCZOS)
        self.photobg1=ImageTk.PhotoImage(bg1)
        
        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=130,width=1366,height=768)
        
        
        # TITLE LABEL
        title_lbl = Label(bg_img, text="Welcome To Face Recognition", font=("calibri", 30, "bold"), bg="gainsboro", fg="Black")
        title_lbl.place(x=0,y=0,width=1366,height=45)
        
        
        #STUDENT BUTTON
        img2 = Image.open(r"N:\Face Recognition System code\Image\facedet.png")
        img2=img2.resize((180,180),Image.LANCZOS)
        self.photoimage2 = ImageTk.PhotoImage(img2)
        
        b1=Button(bg_img,image=self.photoimage2,command=self.face_recog,cursor="hand2")
        b1.place(x=600,y=170,width=180,height=180)
        
        
        b1_1 = Button(bg_img, text="Detect Face",command=self.face_recog,cursor="hand2", font=("tahoma", 15, "bold"), bg="black", fg="gainsboro")
        b1_1.place(x=600,y=350,width=180,height=45)
        
        #========================================================================================================================================================#
        #=============================================================ATTENDANCE=================================================================================#
        #========================================================================================================================================================#
   
    def mark_attendance(self, n, r, i):
    # Get the current date
        now = dt.now()
        nepal_timezone = pytz.timezone('Asia/Kathmandu')
        now = now.astimezone(nepal_timezone)
        d1 = now.strftime("%d-%m-%Y")

        # Define the folder name
        folder_name = "Class 1 Attendance"

        # Create the folder if it doesn't exist
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        # Check if the attendance file for the current date exists
        file_name = os.path.join(folder_name, f"Attendance-{d1}.csv")
        if not os.path.isfile(file_name):
            # Create a new attendance file for the current date
            with open(file_name, "w", newline="\n") as new_file:
                pass

        # Check if the student's attendance already recorded for the current date
        with open(file_name, "r", newline="\n") as f:
            csv_reader = csv.reader(f)
            for row in csv_reader:
                if row and row[0] == n and row[1] == r and row[2] == i and row[4] == d1:
                    return  # Student's attendance already recorded, no need to add again

        # Append attendance to the file
        with open(file_name, "a", newline="\n") as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow([n, r, i, now.strftime("%I:%M %p"), d1, "Present"])
            
        #========================================================================================================================================================#
        #============================================================FACE RECOGNITION============================================================================#
        #========================================================================================================================================================#
        
    def face_recog(self):
        def draw_boundray(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]
            
            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])

                confidence=int((100*(1-predict/300)))

                conn = mysql.connector.connect(username='root', password='niraj',host='localhost',database='face_recognition',port=3306)
                mycursor = conn.cursor()

               
                mycursor.execute("select Name from student where `Roll-No`=" + str(id))
                n = str(mycursor.fetchone()[0])  # Convert to string directly

                mycursor.execute("select `Roll-No` from student where `Roll-No`=" + str(id))
                r = str(mycursor.fetchone()[0]) 

                mycursor.execute("select Gender from student where `Roll-No`=" + str(id))
                i = str(mycursor.fetchone()[0])


                if confidence > 77:
                    cv2.putText(img, f"Roll:{r}", (x, y - 80), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 0),2)
                    cv2.putText(img, f"Name:{n}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 0), 2)
                    cv2.putText(img, f"Gender:{i}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 0),2)
                    self.mark_attendance(r,n,i)
                    
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)    

                coord=[x,y,w,y]
            
            return coord    



        #========================IMAGE RECOGNIZE===================#
        
        def recognize(img,clf,faceCascade):
            coord=draw_boundray(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer.create()
        clf.read("clf.xml")

        videoCap=cv2.VideoCapture(0)

        while True:
            ret,img=videoCap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Attendence Marker",img)

            if cv2.waitKey(1) == 13:
                break
        videoCap.release()
        cv2.destroyAllWindows()
                          
        
if __name__ == "__main__":
    root = Tk()
    obj = Face_recognition(root)
    root.mainloop()

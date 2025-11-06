from tkinter import*
from tkinter import ttk
from train import Train
from PIL import Image,ImageTk
# from student import Student
# from train import Train
# from face_recognition import Face_Recognition
# from attendance import Attendance
# import os

class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition System")

# This part is image labels setting start 
        # first header image  
        img=Image.open(r"D:\Face Recognition System code\Image\ban.jpg")
        img=img.resize((1366,130),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        # set image as lable
        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=1366,height=130)

        # backgorund image 
        bg1=Image.open(r"D:\Face Recognition System code\Image\bg4.png")
        bg1=bg1.resize((1366,768),Image.LANCZOS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=130,width=1366,height=768)


        #title section
        title_lb1 = Label(bg_img,text="Developer ",font=("verdana",30,"bold"),bg="white",fg="Black")
        title_lb1.place(x=0,y=0,width=1366,height=45)

        # Create buttons below the section 
        # ------------------------------------------------------------------------------------------------------------------- 
        # student button 1
        # Creating Frame 
        main_frame = Frame(bg_img,bd=2,bg="gainsboro") #bd mean border 
        main_frame.place(x=400,y=55,width=600,height=510)

        
        # BANNER IMAGE
        stimg = Image.open(r"D:\Face Recognition System code\Image\devr.png")
        stimg=stimg.resize((300,300),Image.LANCZOS)
        self.stphotoimage = ImageTk.PhotoImage(stimg)

        f_lbl = Label(main_frame, image=self.stphotoimage,bd=2, relief="solid", highlightthickness=1, highlightbackground="black")
        f_lbl.place(x=150,y=10,width=300,height=300)
        
        
        # Developer Name
        dev_name_label = Label(main_frame, text="Developer name: Niraj Bohara", font=("times new roman", 15, "bold"), bg="gainsboro",fg="Darkblue",)
        dev_name_label.place(x=150, y=310)
        
        # Contact Information
        contact_label = Label(main_frame, text="Contact: nirazbohara8@gmail.com", font=("times new roman", 15,"bold"), bg="gainsboro",fg="Darkblue")
        contact_label.place(x=150, y=340)
        
        # Contact Information
        contact_label = Label(main_frame, text="Copyright © 2024 Sunrise Public Secondary School", font=("times new roman", 10,"bold",), bg="gainsboro",fg="red")
        contact_label.place(x=150, y=470)
        
        
        
        

         


if __name__ == "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()
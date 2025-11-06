from tkinter import*
from PIL import Image,ImageTk


class Helpsupport:
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
        title_lb1 = Label(bg_img,text="Help-Desk ",font=("calibri", 30, "bold"), bg="white", fg="black")
        title_lb1.place(x=0,y=0,width=1366,height=45)
        
        # Creating Frame 
        main_frame = Frame(bg_img,bd=2,bg="gainsboro") #bd mean border 
        main_frame.place(x=400,y=70,width=600,height=510)
        
        # HELP IMAGE
        stimg = Image.open(r"D:\Face Recognition System code\Image\hlpr.png")
        stimg=stimg.resize((600,300),Image.LANCZOS)
        self.stphotoimage = ImageTk.PhotoImage(stimg)

        f_lbl = Label(main_frame, image=self.stphotoimage)
        f_lbl.place(x=0,y=0,width=600,height=300)
        
        # Developer Name
        dev_name_label = Label(main_frame, text="For Any enquiry:", font=("times new roman", 20, "bold",), bg="gainsboro", fg="Darkblue")
        dev_name_label.place(x=15, y=310)
        
        # Contact
        dev_name_label = Label(main_frame, text="Phone:+977 9848886777", font=("times new roman", 15, "bold","underline"), bg="gainsboro", fg="Darkblue")
        dev_name_label.place(x=15, y=345)
        
        # Email
        dev_name_label = Label(main_frame, text="Email:nirazbohara8@gmail.com", font=("times new roman", 15, "bold","underline"), bg="gainsboro", fg="Darkblue")
        dev_name_label.place(x=15, y=380)


if __name__ == "__main__":
    root=Tk()
    obj=Helpsupport(root)
    root.mainloop()
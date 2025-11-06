from tkinter import*  
# Importing Tkinter for GUI
from tkinter import ttk 
# ttk helps to modify the GUI
from PIL import Image,ImageTk
# for importing images and adjusting the design
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Train:
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
        
         # backgorund image 
        bg1=Image.open(r"D:\Face Recognition System code\Image\bg4.png")
        bg1=bg1.resize((1366,768),Image.LANCZOS)
        self.photobg1=ImageTk.PhotoImage(bg1)
        
        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=130,width=1366,height=768)
         
        # TITLE LABEL
        title_lbl = Label(bg_img, text="Dataset Trainer ", font=("Bell Gothic Std Black", 30, "bold"), bg="gainsboro", fg="black")
        title_lbl.place(x=0,y=0,width=1366,height=45)
        #===============================================================================================================================================#  
        # BUTTON FOR TRAINING
        #====================================================================================================================================================#
        # BUTTON 1 FOR TRAINING 
        #==================================================================================================================================================#
      
  
        #STUDENT BUTTON
        img2 = Image.open(r"D:\Face Recognition System code\Image\trn.png")
        img2=img2.resize((180,180),Image.LANCZOS)
        self.photoimage2 = ImageTk.PhotoImage(img2)
        
        b1=Button(bg_img,image=self.photoimage2,cursor="hand2",command=self.train_classifier)
        b1.place(x=600,y=170,width=180,height=180)
        
        
        b1_1 = Button(bg_img, text="Train Data",command=self.train_classifier ,cursor="hand2", font=("tahoma", 15, "bold"), bg="black", fg="white")
        b1_1.place(x=600,y=350,width=180,height=45)
        
    
         #==========================================================#
         #==================FUNCTION FOR TRAINING===================#
         #==========================================================#
     
    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]
        
        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L') # convert in gray scale 
            imageNp = np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)

            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
            
        # Converting id into array
        ids=np.array(ids)
        
        
        #==============================================#
        #=================Train Classifier=============#
        #==============================================#
        
        clf = cv2.face.LBPHFaceRecognizer.create()
        clf.train(faces,ids)
        clf.write("clf.xml")

        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Data Trained Succesfully!")
      
if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()

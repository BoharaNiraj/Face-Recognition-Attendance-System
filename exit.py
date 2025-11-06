from tkinter import *
  
# Class for tkinter window
  
  
class Exit:
    
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition System")
        # Button for closing
        exit_button = Button(self.root, text="Exit", command=self.Close)
        exit_button.pack(pady=20)
  
      
    # Function for closing window
    def Close(self):
        self.root.destroy()
  
  
if __name__=="__main__":
    root=Tk()
    obj=Exit(root)
    root.mainloop()
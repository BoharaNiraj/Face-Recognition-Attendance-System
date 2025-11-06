from tkinter import* 
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import re
import bcrypt


class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1366x768+0+0")
        #NO MAXIMIZE SCREEN
        self.root.resizable(False, False)
        self.previous_window = None  # Initialize a variable to store the reference to the previous window

        # ============ Variables =================
        self.var_name=StringVar()
        self.var_surname=StringVar()
        self.var_snum=StringVar()
        self.var_email=StringVar()
        self.var_sq=StringVar()
        self.var_sa=StringVar()
        self.var_pass=StringVar()
        self.var_cpass=StringVar()
        self.var_check=IntVar()

        self.bg=ImageTk.PhotoImage(file=r"D:\Face Recognition System code\Image\bgreg.png")
        
        lb1_bg=Label(self.root,image=self.bg)
        lb1_bg.place(x=0,y=0, relwidth=1,relheight=1)

        frame= Frame(self.root,bg="teal")
        frame.place(x=100,y=80,width=900,height=580)
        
        get_str = Label(frame,text="Registration",font=("Verdena",30,"bold"),fg="black",bg="teal")
        get_str.place(x=350,y=130)
        
        # back_button = Button(frame, text="Back", command=self.go_back)
        # back_button.place(x=10, y=10)
        #=============================================================================================#
        #=============================================================================================#
        # def go_back(self):
        # # Close the current window and show the previous window
        #     if self.previous_window:
        #     self.root.destroy()  # Close the current window
        #     self.previous_window.lift()  # Show the previous window
        
    #=============================================================================================#
        #=============================================================================================#
        #label1 
        fname =lb1= Label(frame,text="First Name:",font=("times new roman",15,"bold"),fg="black",bg="teal")
        fname.place(x=100,y=200)

        #entry1 
        self.txtuser=ttk.Entry(frame,textvariable=self.var_name,font=("times new roman",15,"bold"))
        self.txtuser.place(x=103,y=225,width=270)


        #label2 
        lname =lb1= Label(frame,text="Last Name:",font=("times new roman",15,"bold"),fg="black",bg="teal")
        lname.place(x=100,y=270)

        #entry2 
        self.txtpwd=ttk.Entry(frame,textvariable=self.var_surname,font=("times new roman",15,"bold"))
        self.txtpwd.place(x=103,y=295,width=270)
        
        #=============================================================================================#
        
        #label1 
        contact =lb1= Label(frame,text="Contact No:",font=("times new roman",15,"bold"),fg="black",bg="teal")
        contact.place(x=530,y=200)

        #entry1 
        self.txtuser=ttk.Entry(frame,textvariable=self.var_snum,font=("times new roman",15,"bold"))
        self.txtuser.place(x=533,y=225,width=270)


        #label2 
        email =lb1= Label(frame,text="Email:",font=("times new roman",15,"bold"),fg="black",bg="teal")
        email.place(x=530,y=270)

        #entry2 
        self.txtpwd=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15,"bold"))
        self.txtpwd.place(x=533,y=295,width=270)
        
        #=============================================================================================#
        
        #label1 
        ssq =lb1= Label(frame,text="Select Security Question:",font=("times new roman",15,"bold"),fg="black",bg="teal")
        ssq.place(x=100,y=350)

        #Combo Box1
        self.combo_security = ttk.Combobox(frame,textvariable=self.var_sq,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security["values"]=("Select","Your Date of Birth","Your Nick Name","Your Favorite Book")
        self.combo_security.current(0)
        self.combo_security.place(x=103,y=375,width=270)


        #label2 
        sa =lb1= Label(frame,text="Security Answer:",font=("times new roman",15,"bold"),fg="black",bg="teal")
        sa.place(x=100,y=420)

        #entry2 
        self.txtpwd=ttk.Entry(frame,textvariable=self.var_sa,font=("times new roman",15,"bold"))
        self.txtpwd.place(x=103,y=445,width=270)
        
        #=============================================================================================#
        
         #label1 
        pwd =lb1= Label(frame,text="Password:",font=("times new roman",15,"bold"),fg="black",bg="teal")
        pwd.place(x=530,y=350)

        #entry1 
        self.txtuser=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15,"bold"),show="*")
        self.txtuser.place(x=533,y=375,width=270)

        #label2 
        cpwd =lb1= Label(frame,text="Confirm Password:",font=("times new roman",15,"bold"),fg="black",bg="teal")
        cpwd.place(x=530,y=420)

        #entry2 
        self.txtpwd=ttk.Entry(frame,textvariable=self.var_cpass,font=("times new roman",15,"bold"),show="*")
        self.txtpwd.place(x=533,y=445,width=270)

        # Checkbutton
        checkbtn = Checkbutton(frame,variable=self.var_check,text="I Agree the Terms & Conditions",font=("times new roman",13,"bold"),fg="black",bg="teal")
        checkbtn.place(x=100,y=480,width=270)


        # Creating Button Register
        loginbtn=Button(frame,text="Register",command=self.reg,font=("times new roman",15,"bold"),bd=0,relief=RIDGE,fg="#fff",bg="dark blue",activeforeground="white",activebackground="#007ACC")
        loginbtn.place(x=103,y=510,width=270,height=35)

        # # Creating Button Login
        # loginbtn=Button(frame,text="Login",font=("times new roman",15,"bold"),bd=0,relief=RIDGE,fg="#fff",bg="dark blue",activeforeground="white",activebackground="#007ACC")
        # loginbtn.place(x=533,y=510,width=270,height=35)
        
    
        
    # =====================================================================================================# 
                                     # REFUNCTION FOR FORM VALIDATION #
    # =====================================================================================================# 
    
    def has_symbols(self, input_string):
    # Check if the input string contains any symbols
        return bool(re.search(r'[!@#$%^&*(),.?"{}|<>]', input_string))        
        
 #===============================================================================================================#
 #===============================================REGISTER FUNCTION===============================================#  
 #===============================================================================================================#  
 
    def reg(self):
        if (
            self.var_name.get() == ""
            or self.var_surname.get() == ""
            or self.var_snum.get() == ""
            or self.var_email.get() == ""
            or self.var_sq.get() == "Select"
            or self.var_sa.get() == ""
            or self.var_pass.get() == ""
            or self.var_cpass.get() == ""
        ):
            messagebox.showerror("Error", "All Field Required!")

        elif self.var_pass.get() != self.var_cpass.get():
            messagebox.showerror("Error", "Please Insure both Password & Confirm Password are Same!")
        
        elif self.var_check.get() == 0:
            messagebox.showerror("Error", "Please Check the Agree Terms and Conditions!")
        
        elif self.has_symbols(self.var_name.get()) or self.has_symbols(self.var_surname.get()) or self.has_symbols(self.var_snum.get()):
            messagebox.showerror("Error", "Not a Valid Input", parent=self.root)
            
        elif not re.search(r"[!@#$%^&*()_+=\[{\]};:<>|./?,-]", self.var_pass.get()):
            messagebox.showerror("Error", "Password must contain at least one symbol")    
        
        else:
            try:
                conn = mysql.connector.connect(username='root', password='niraj', host='localhost', database='face_recognition', port=3306)
                mycursor = conn.cursor()
                
                # Check if the user already exists
                query = "SELECT * FROM register WHERE email = %s"
                value = (self.var_email.get(),)
                mycursor.execute(query, value)
                row = mycursor.fetchone()
                
                if row is not None:
                    messagebox.showerror("Error", "User already exists, please try another email")
                
                else:
                    # Hash the password before storing it in the database
                    hashed_password = self.hash_password(self.var_pass.get())

                    # Insert user details into the database
                    mycursor.execute("INSERT INTO register VALUES (%s,%s,%s,%s,%s,%s,%s)", (
                        self.var_name.get(),
                        self.var_surname.get(),
                        self.var_snum.get(),
                        self.var_email.get(),
                        self.var_sq.get(),
                        self.var_sa.get(),
                        hashed_password  # Store hashed password
                    ))

                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Success", "Successfully Registered!", parent=self.root)
                    
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

    def hash_password(self, password):
        # Generate a salt and hash the password using bcrypt
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed_password
        
#MAIN CLASS OBJECT       
if __name__ == "__main__":
    root=Tk()
    obj=Register(root)
    root.mainloop()
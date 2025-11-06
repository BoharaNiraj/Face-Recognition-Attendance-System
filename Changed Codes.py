                
                
                
                
                
                # Face Recognition  Data Showing Code
                
                
                # mycursor.execute("select Name from student where `Roll-No`="+str(id))
                # n=mycursor.fetchone()
                # n = str(n)

                # mycursor.execute("select `Roll-No` from student where `Roll-No`="+str(id))
                # r=mycursor.fetchone()
                # r = str(r)

                # mycursor.execute("select Gender from student where `Roll-No`="+str(id))
                # i=mycursor.fetchone()
                # i = str(i)
          
          
          
          
                
                
    
    # MARKING ATTENDANCE ORIGNAL 
                
                
    #     with open("attendance.csv","r+",newline="\n") as f:
    #         myDatalist=f.readlines()
    #         name_list=[]
    #         for line in myDatalist:
    #             entry=line.split((","))
    #             name_list.append(entry[0])

    #         if((r not in name_list) and (i not in name_list) and (n not in name_list)):
    #             now=dt.now()
    #             nepal_timezone = pytz.timezone('Asia/Kathmandu')
    #             now = datetime.datetime.now(nepal_timezone)
    #             d1=now.strftime("%d/%m/%Y")
    #             dtString=now.strftime("%I:%M %p")
    #             f.writelines(f"\n{n}, {r}, {i}, {dtString}, {d1}, Present")
    
    
    
    
    
    
    # CHANGED WITH AUTOMATIC CSV GENERATE
    
    
    # def mark_attendance(self, n, r, i):
    #     # Get the current date
    #     now = dt.now()
    #     nepal_timezone = pytz.timezone('Asia/Kathmandu')
    #     now = now.astimezone(nepal_timezone)
    #     d1 = now.strftime("%d-%m-%Y")

    #     # Check if the attendance file for the current date exists
    #     file_name = f"attendance_{d1}.csv"
    #     if not os.path.isfile(file_name):
    #         # Create a new attendance file for the current date
    #         with open(file_name, "w", newline="\n") as new_file:
    #             csv_writer = csv.writer(new_file)
    #             csv_writer.writerow(["Name", "Roll Number", "ID", "Time", "Date", "Status"])

    #     # Check if the student's attendance already recorded for the current date
    #     with open(file_name, "r", newline="\n") as f:
    #         csv_reader = csv.reader(f)
    #         for row in csv_reader:
    #             if row[0] == n and row[1] == r and row[2] == i and row[4] == d1:
    #                 return  # Student's attendance already recorded, no need to add again

    #     # Append attendance to the file
    #     with open(file_name, "a", newline="\n") as f:
    #         csv_writer = csv.writer(f)
    #         csv_writer.writerow([n, r, i, now.strftime("%I:%M %p"), d1, "Present"])
            
            
            
            
            
    #Update button
        # upd_btn=Button(right_frame,text="Update",command=self.update_data,width=12,font=("verdana",12,"bold"),fg="white",bg="black")
        # upd_btn.grid(row=0,column=1,padx=6,pady=10,sticky=W)
        
        
    #     #DELETE button
    #     del_btn=Button(right_frame,text="Delete",command=self.delete_data,width=12,font=("verdana",12,"bold"),fg="white",bg="black")
    #     del_btn.grid(row=0,column=2,padx=6,pady=10,sticky=W)
        
    # #REFRESH button
    #     ref_btn=Button(right_frame,text="Refresh",command=self.refresh_data,width=12,font=("verdana",12,"bold"),fg="white",bg="black")
    #     ref_btn.grid(row=0,column=3,padx=6,pady=10,sticky=W)
    
    
    
    
    
    
    
    # Automatic CSV Generator Code
    
    # now = dt.now()
    #     nepal_timezone = pytz.timezone('Asia/Kathmandu')
    #     now = now.astimezone(nepal_timezone)
    #     d1 = now.strftime("%d-%m-%Y")

    #     # Check if the attendance file for the current date exists
    #     file_name = f"Attendance-{d1}.csv"
    #     if not os.path.isfile(file_name):
    #         # Create a new attendance file for the current date
    #         with open(file_name, "w", newline="\n") as new_file:
    #             pass

    #     # Check if the student's attendance already recorded for the current date
    #     with open(file_name, "r", newline="\n") as f:
    #         csv_reader = csv.reader(f)
    #         for row in csv_reader:
    #             if row[0] == n and row[1] == r and row[2] == i and row[4] == d1:
    #                 return  # Student's attendance already recorded, no need to add again

    #     # Append attendance to the file
    #     with open(file_name, "a", newline="\n") as f:
    #         csv_writer = csv.writer(f)
    #         csv_writer.writerow([n, r, i, now.strftime("%I:%M %p"), d1, "Present"])
    
    
    
    
    
    
    
    
    # Insert function without Validation of already existing DeprecationWarning
    
    
    # def action(self):
    #     if self.var_roll.get()=="" or self.var_name.get=="" or self.var_gender.get()=="" or self.var_time.get()=="" or self.var_date.get()=="" or self.var_attend.get()=="Status":
    #         messagebox.showerror("Error","Please Fill All Fields are Required!",parent=self.root)
                
    #     elif (
    #         self.has_symbols(self.var_name.get())
    #         or self.has_symbols(self.var_date.get())
    #         or self.has_symbols(self.var_roll.get())
    #         or self.has_symbols(self.var_gender.get())
    #         or self.has_symbols(self.var_time.get())
    
    #     ):
    #         messagebox.showerror("Error", "Not a Valid Input", parent=self.root)     
    #     else:
    #         try:
    #             conn = mysql.connector.connect(username='root', password='niraj',host='localhost',database='face_recognition',port=3306)
    #             mycursor = conn.cursor()
    #             mycursor.execute("insert into stattendance values(%s,%s,%s,%s,%s,%s)",(
    #             self.var_roll.get(),
    #             self.var_name.get(),
    #             self.var_gender.get(),
    #             self.var_time.get(),
    #             self.var_date.get(),
    #             self.var_attend.get()
    #             ))

    #             conn.commit()
    #             self.fetch_data()
    #             conn.close()
    #             messagebox.showinfo("Success","All Records are Saved in Database!",parent=self.root)
    #         except Exception as es:
    #             messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)  
    
    
    
    # Changed to 
    
    
    # def action(self):
        
    #     if (
    #         self.var_roll.get() == ""
    #         or self.var_name.get() == ""
    #         or self.var_gender.get() == ""
    #         or self.var_time.get() == ""
    #         or self.var_date.get() == ""
    #         or self.var_attend.get() == "Status"
    #     ):
    #         messagebox.showerror("Error", "Please Fill All Fields are Required!", parent=self.root)

    #     elif (
    #         self.has_symbols(self.var_name.get())
    #         or self.has_symbols(self.var_date.get())
    #         or self.has_symbols(self.var_roll.get())
    #         or self.has_symbols(self.var_gender.get())
    #         or self.has_symbols(self.var_time.get())
    #     ):
    #         messagebox.showerror("Error", "Not a Valid Input", parent=self.root)
    #     else:
    #         try:
    #             conn = mysql.connector.connect(
    #                 username='root', password='niraj', host='localhost', database='face_recognition', port=3306
    #             )
    #             mycursor = conn.cursor()

    #             # Check if the record already exists
    #             query = "SELECT * FROM stattendance WHERE Roll_No = %s AND Name = %s AND Gender = %s AND Time = %s AND Date = %s AND Attend = %s"
    #             params = (
    #                 self.var_roll.get(),
    #                 self.var_name.get(),
    #                 self.var_gender.get(),
    #                 self.var_time.get(),
    #                 self.var_date.get(),
    #                 self.var_attend.get(),
    #             )
    #             mycursor.execute(query, params)
    #             existing_record = mycursor.fetchone()

    #             if existing_record:
    #                 messagebox.showerror("Error", "This Entry of the student already exists in the database",
    #                                     parent=self.root)
    #             else:
    #                 mycursor.execute(
    #                     "INSERT INTO stattendance VALUES (%s,%s,%s,%s,%s,%s)",
    #                     (
    #                         self.var_roll.get(),
    #                         self.var_name.get(),
    #                         self.var_gender.get(),
    #                         self.var_time.get(),
    #                         self.var_date.get(),
    #                         self.var_attend.get(),
    #                     ),
    #                 )

    #                 conn.commit()
    #                 self.fetch_data()
    #                 conn.close()
    #                 messagebox.showinfo("Success", "All Records are Saved in Database!", parent=self.root)
    #         except Exception as es:
    #             messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)
    
    
    
    
    
    
    
    
    
    # Again Used Integrity error library from _mysql.connector
    
    # from mysql.connector import IntegrityError
    # def action(self):
    #     if self.var_roll.get()=="" or self.var_name.get=="" or self.var_gender.get()=="" or self.var_time.get()=="" or self.var_date.get()=="" or self.var_attend.get()=="Status":
    #         messagebox.showerror("Error","Please Fill All Fields are Required!",parent=self.root)
                
    #     elif (
    #         self.has_symbols(self.var_name.get())
    #         or self.has_symbols(self.var_date.get())
    #         or self.has_symbols(self.var_roll.get())
    #         or self.has_symbols(self.var_gender.get())
    #         or self.has_symbols(self.var_time.get())
    
    #     ):
    #         messagebox.showerror("Error", "Not a Valid Input", parent=self.root)     
    #     else:
    #         try:
    #             conn = mysql.connector.connect(username='root', password='niraj',host='localhost',database='face_recognition',port=3306)
    #             mycursor = conn.cursor()
    #             mycursor.execute("insert into stattendance values(%s,%s,%s,%s,%s,%s)",(
    #             self.var_roll.get(),
    #             self.var_name.get(),
    #             self.var_gender.get(),
    #             self.var_time.get(),
    #             self.var_date.get(),
    #             self.var_attend.get()
    #             ))

    #             conn.commit()
    #             self.fetch_data()
    #             conn.close()
    #             messagebox.showinfo("Success","All Records are Saved in Database!",parent=self.root)
    #         except IntegrityError:
    #             messagebox.showerror("Error", "This record already exists in the database!", parent=self.root)
    #         except Exception as es:
    #             messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root) 
    
    
    
    
    
    
    
    
    # LOGIN Code
    
    #  def login(self):
    #     if (self.txtuser.get()=="" or self.txtpwd.get()==""):
    #         messagebox.showerror("Error","All Field Required!")
        
    #     else:
    #         # messagebox.showerror("Error","Please Check Username or Password !")
    #         conn = mysql.connector.connect(username='root', password='niraj',host='localhost',database='face_recognition',port=3306)
    #         mycursor = conn.cursor()
    #         mycursor.execute("select * from register where email=%s and pass=%s",(
    #             self.txtuser.get(),
    #             self.txtpwd.get()
    #         ))
    #         row=mycursor.fetchone()
    #         if row==None:
    #             messagebox.showerror("Error","Invalid Username and Password!")
    #         else:
    #             open_min=messagebox.askyesno("YesNo","Access the System")
    #             if open_min>0:
    #                 self.new_window=Toplevel(self.root)
    #                 self.app=FaceRecognitionSystem(self.new_window)
    #             else:
    #                 if not open_min:
    #                     return
    #         conn.commit()
    #         conn.close()    
    
    
    
    # Register code
    
    # def reg(self):
    #     if (self.var_name.get()=="" or self.var_surname.get()=="" or self.var_snum.get()=="" or self.var_email.get()=="" or self.var_sq.get()=="Select" or self.var_sa.get()=="" or self.var_pass.get()=="" or self.var_cpass.get()==""):
    #         messagebox.showerror("Error","All Field Required!")
    
    #     elif(self.var_pass.get() != self.var_cpass.get()):
    #         messagebox.showerror("Error","Please Insure both Password & Confirm Password are Same!")
    #     elif(self.var_check.get()==0):
    #         messagebox.showerror("Error","Please Check the Agree Terms and Conditons!")
    #     elif (
    #         self.has_symbols(self.var_name.get())
    #         or self.has_symbols(self.var_surname.get())
    #         or self.has_symbols(self.var_snum.get())
    
    #     ):
    #         messagebox.showerror("Error", "Not a Valid Input", parent=self.root)     
    #     else:
    #         # messagebox.showinfo("Successfully","Successfully Register!")
    #         try:
    #             conn = mysql.connector.connect(username='root', password='niraj',host='localhost',database='face_recognition',port=3306)
    #             mycursor = conn.cursor()
    #             query=("select * from register where email=%s")
    #             value=(self.var_email.get(),)
    #             mycursor.execute(query,value)
    #             row=mycursor.fetchone()
    #             if row!=None:
    #                 messagebox.showerror("Error","User already exist,please try another email")
    #             else:
    #                 mycursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
    #                 self.var_name.get(),
    #                 self.var_surname.get(),
    #                 self.var_snum.get(),
    #                 self.var_email.get(),
    #                 self.var_sq.get(),
    #                 self.var_sa.get(),
    #                 self.var_pass.get()
    #                 ))

    #                 conn.commit()
    #                 conn.close()
    #                 messagebox.showinfo("Success","Successfully Registerd!",parent=self.root)
    #         except Exception as es:
    #             messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)
    
    
    
    
    # Reset Password function
    
    # def Reset_pass(self):
    #     if self.var_sq.get()=="Select":
    #         messagebox.showerror("Error","Select the Security Question!",parent=self.root2)
    #     elif(self.var_sa.get()==""):
    #         messagebox.showerror("Error","Please Enter the Answer!",parent=self.root2)
    #     elif(self.var_pass.get()==""):
    #         messagebox.showerror("Error","Please Enter the New Password!",parent=self.root2)
    #     else:
    #         conn = mysql.connector.connect(username='root', password='niraj',host='localhost',database='face_recognition',port=3306)
    #         mycursor = conn.cursor()
    #         query=("select * from register where email=%s and securityque=%s and secanswer=%s")
    #         value=(self.txtuser.get(),self.var_sq.get(),self.var_sa.get())
    #         mycursor.execute(query,value)
    #         row=mycursor.fetchone()
    #         if row==None:
    #             messagebox.showerror("Error","Invalid Answer!",parent=self.root2)
    #         else:
    #             query=("update register set pass=%s where email=%s")
    #             value=(self.var_pass.get(),self.txtuser.get())
    #             mycursor.execute(query,value)

    #             conn.commit()
    #             conn.close()
    #             messagebox.showinfo("Info","Successfully Your password has been reset, Please login with new Password!",parent=self.root2)
    
    
    
    
    
    
    
    
    
    
    # Photo capture code from Student
    
    # face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml") 
                
    #             def face_croped(img):
    #                 # conver gary sacle
    #                 gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #                 faces = face_classifier.detectMultiScale(gray,1.3,5)
    #                 #Scaling factor 1.3
    #                 # Minimum naber 5
    #                 for (x,y,w,h) in faces:
    #                     face_croped=img[y:y+h,x:x+w]
    #                     return face_croped
    #             cap=cv2.VideoCapture(0)
    #             img_id=0
    #             while True:
    #                 ret,my_frame=cap.read()
    #                 if face_croped(my_frame) is not None:
    #                     img_id+=1
    #                     face=cv2.resize(face_croped(my_frame),(200,200))
    #                     face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
    #                     file_path="data/Roll."+str(id)+"."+str(img_id)+".jpg"
    #                     cv2.imwrite(file_path,face)
    #                     cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)        
    #                     cv2.imshow("Capture Images",face)

    #                 if cv2.waitKey(1)==13 or int(img_id)==100:
    #                     break
    #             cap.release()
    #             cv2.destroyAllWindows()
    #             messagebox.showinfo("Result","Generating dataset completed!",parent=self.root)
    #         except Exception as es:
    #             messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root) 
    
    
    
    # def reg(self):
    #     if (
    #         self.var_name.get() == ""
    #         or self.var_surname.get() == ""
    #         or self.var_snum.get() == ""
    #         or self.var_email.get() == ""
    #         or self.var_sq.get() == "Select"
    #         or self.var_sa.get() == ""
    #         or self.var_pass.get() == ""
    #         or self.var_cpass.get() == ""
    #     ):
    #         messagebox.showerror("Error", "All Field Required!")

    #     elif self.var_pass.get() != self.var_cpass.get():
    #         messagebox.showerror("Error", "Please Insure both Password & Confirm Password are Same!")
        
    #     elif self.var_check.get() == 0:
    #         messagebox.showerror("Error", "Please Check the Agree Terms and Conditions!")
        
    #     elif self.has_symbols(self.var_name.get()) or self.has_symbols(self.var_surname.get()) or self.has_symbols(self.var_snum.get()):
    #         messagebox.showerror("Error", "Not a Valid Input", parent=self.root)
            
    #     # elif not re.search(r"[!@#$%^&*()_+=\[{\]};:<>|./?,-]", self.var_pass.get()):
    #     #     messagebox.showerror("Error", "Password must contain at least one symbol")    
        
    #     else:
    #         try:
    #             conn = mysql.connector.connect(username='root', password='niraj', host='localhost', database='face_recognition', port=3306)
    #             mycursor = conn.cursor()
                
    #             # Check if the user already exists
    #             query = "SELECT * FROM register WHERE email = %s"
    #             value = (self.var_email.get(),)
    #             mycursor.execute(query, value)
    #             row = mycursor.fetchone()
                
    #             if row is not None:
    #                 messagebox.showerror("Error", "User already exists, please try another email")
                
    #             else:
    #                 # Hash the password before storing it in the database
    #                 hashed_password = self.hash_password(self.var_pass.get())

    #                 # Insert user details into the database
    #                 mycursor.execute("INSERT INTO register VALUES (%s,%s,%s,%s,%s,%s,%s)", (
    #                     self.var_name.get(),
    #                     self.var_surname.get(),
    #                     self.var_snum.get(),
    #                     self.var_email.get(),
    #                     self.var_sq.get(),
    #                     self.var_sa.get(),
    #                     hashed_password  # Store hashed password
    #                 ))

    #                 conn.commit()
    #                 conn.close()
    #                 messagebox.showinfo("Success", "Successfully Registered!", parent=self.root)
                    
    #         except Exception as es:
    #             messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

    # def hash_password(self, password):
    #     # Generate a salt and hash the password using bcrypt
    #     salt = bcrypt.gensalt()
    #     hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    #     return hashed_password
    
    
    # Form Validation
    
    # elif (
    #         self.has_symbols(self.var_std_name.get())
    #         or self.has_symbols(self.var_div.get())
    #         or self.has_symbols(self.var_roll.get())
    #         or self.has_symbols(self.var_gender.get())
    #         or self.has_symbols(self.var_dob.get())
    #         or self.has_symbols(self.var_phone.get())
    #         or self.has_symbols(self.var_address.get())
    #         or self.has_symbols(self.var_teacher.get())
            
    #     ):
    #         messagebox.showerror("Error", "Symbols are not allowed!", parent=self.root)
    #     elif len(self.var_phone.get()) > 10: # Check if phone number length exceeds 10 digits
    #         messagebox.showerror("Error", "Not a Valid length of number! Phone number should be 10 digits or less.", parent=self.root)
    
    
    # elif (
    #         self.has_symbols(self.var_std_name.get())
    #         or self.has_symbols(self.var_div.get())
    #         or self.has_symbols(self.var_roll.get())
    #         or self.has_symbols(self.var_gender.get())
    #         or self.has_symbols(self.var_dob.get())
    #         or self.has_symbols(self.var_phone.get())
    #         or self.has_symbols(self.var_address.get())
    #         or self.has_symbols(self.var_teacher.get())
            
            
    #     ):
    #         messagebox.showerror("Error", "Fields should not contain symbols!", parent=self.root)
            
    #     elif len(self.var_phone.get()) > 10: # Check if phone number length exceeds 10 digits
    #         messagebox.showerror("Error", "Not a Valid length of number! Phone number should be 10 digits or less.", parent=self.root)
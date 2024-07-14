from utils.helper_code import *  # Importing necessary functions from helper_code module

def change_psswd():
    """
    Function to change the password.
    """
    
    change = Tk()
    change.geometry("940x600+160+100")
    change.title("Change Password")
    change.wm_iconbitmap("media/password.ico")
    change.configure(background="snow")
    
    old_pass = tk.StringVar(change)
    new_pass = tk.StringVar(change)
    new_pass_cnf = tk.StringVar(change)
    
    bg_img = Image.open("media/add_back.jpg")
    bg = ImageTk.PhotoImage(bg_img, master=change)
    
    back = Label(change, image=bg)
    back.pack()

    def confirm():
        """
        Function to confirm the password change.
        """
        
        with open('credentials.json', 'r') as f:
            data = json.load(f)
            log_pass = data["log_pass"]
        
        if log_pass==old_pass.get():
            if new_pass.get()==new_pass_cnf.get():
                data = {"log_pass":new_pass.get(), "passwd": passwd, "dbname":dbname}

                with open('credentials.json', 'w') as f:
                    json.dump(data,f)

                messagebox.showinfo("Success","Password Changed Successfully")
                change.destroy()        
            else:  
                messagebox.showerror("Error","New Password does not match")
                change.tkraise()          
        else:
            messagebox.showerror("Error","Please Confirm your Old Password")
            change.tkraise()
    
    title = Label(change,text="Change Password", bg="lavender blush" , fg="#be2102", relief=SOLID,
                  font=("times new roman","25","bold")).place(x=0,y=0,relwidth=1)
    
    frame=Frame(change,bg="lavender blush",highlightbackground="black",highlightthickness=1)
    frame.place(x=280,y=150)
    
    old = Label(frame,text="Old Password", bg="lavender blush" , fg="#be2102",
                font=("times new roman","15","bold")).grid(row=10,column=10,padx=15,pady=15)
    enter_old = Entry(frame,show="*",width=30,textvariable=old_pass).grid(row=10,column=12,padx=15,pady=15)
    
    new = Label(frame,text="New Password", bg="lavender blush" , fg="#be2102",
                font=("times new roman","15","bold")).grid(row=12,column=10,padx=15,pady=15)
    enter_new = Entry(frame,show="*",width=30,textvariable=new_pass).grid(row=12,column=12,padx=15,pady=15)
    
    new_cnf = Label(frame,text="Confirm New Password", bg="lavender blush" , fg="#be2102",
                    font=("times new roman","15","bold")).grid(row=14,column=10,padx=15,pady=15)
    enter_new_cnf = Entry(frame,show="*",width=30,textvariable=new_pass_cnf).grid(row=14,column=12,padx=15,pady=15)
    
    verify = Button(frame,text="Confirm", bg="lavender blush" , fg="#be2102", relief=SOLID, command = confirm, font=("times new roman","13","bold"),width=10).grid(row=16,column=10,padx=15,pady=15)
    
    change.mainloop()

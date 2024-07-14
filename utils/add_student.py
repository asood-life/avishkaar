from utils.helper_code import *  # Importing necessary functions from helper_code module

def add_std():
    """
    Function to add student details to the database.
    """
    
    addStd = Tk()
    addStd.resizable(False,False)
    addStd.geometry("940x600+160+100")
    addStd.title("Add Students")
    addStd.wm_iconbitmap('media/add.ico')  # Setting window icon
    
    # Initializing StringVar for various entry fields
    roll_no = tk.StringVar(addStd)
    name = tk.StringVar(addStd)
    section = tk.StringVar(addStd)
    gender = tk.StringVar(addStd)
    contact = tk.StringVar(addStd)
    email = tk.StringVar(addStd)
    dob = tk.StringVar(addStd)
    division = tk.StringVar(addStd)
    
    def add_db():
        """
        Function to add student details to the database.
        """

        inputs = [roll_no, name, division, gender, dob]
        
        if any(input_field.get() == "" for input_field in inputs):
            messagebox.showerror("Error","Please complete Roll No, Name, Class, Gender and DOB")
            addStd.tkraise()

        else:
            if not validate_data(roll_no.get(), name.get(), division.get(), section.get(), contact.get(), email.get(), dob.get()):
                addStd.tkraise()
 
            else: 
                conn = mysql.connector.connect(host="127.0.0.1",user="root",password=passwd,database=dbname)
                cur = conn.cursor()
                cur.execute( "select * from "+dbname+" where " + "Roll_No" + " like '%" + roll_no.get() + "%'" )
                rows = cur.fetchall()
                
                if len(rows)==0: 
                    # Check if a student with the entered roll number is present in database or not
                    cur.execute("Insert into "+dbname+" values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                                (roll_no.get(),
                                name.get(),
                                division.get(),
                                section.get(),
                                gender.get(),
                                contact.get(),
                                email.get(),
                                dob.get(),
                                address_entry.get('1.0',END)
                                ))
                    messagebox.showinfo("Success" , "Recorded")
                    conn.commit()
                    conn.close()
                    addStd.destroy()
                    
                else:
                    messagebox.showerror("Error","Roll Number already present")  
                    addStd.tkraise() 
                
    addStd.configure(background="snow")
    
    # Labels and entry fields for student details
    add_head = Label(addStd , text="Enter Student Details" , bg="lavender blush" , fg="#be2102",
                     font=("times new roman" , 25 , "bold"),relief=SOLID)
    add_head.place(x=0,y=0,relwidth=1)
    
    dashboard_l = Frame(addStd ,bg="lavender blush", highlightbackground="black" , highlightthickness=1)
    dashboard_l.place(x=50,y=100)
    
    dashboard_r = Frame(addStd,bg="lavender blush", highlightbackground="black" , highlightthickness=1)
    dashboard_r.place(x=500,y=100)
    
    add_roll = Label(dashboard_l , text="Roll Number" , bg="lavender blush" , fg="#be2102",
                     font=("times new roman" , 15 , "bold"))
    add_roll.grid(row = 0 , column = 0 , pady=20 )
    roll_entry = tk.Entry(dashboard_l , width=20 , textvariable=roll_no)
    roll_entry.grid(row = 0 , column = 1 , pady=20 , padx=10 )

    add_name = Label(dashboard_l , text="Name" , bg="lavender blush" , fg="#be2102",
                     font=("times new roman" , 15 , "bold")).grid(row = 1 , column = 0 , pady=20 )
    name_entry = Entry(dashboard_l , width=40 , textvariable=name).grid(row = 1 , column = 1 , pady=20 , padx=10 )
    
    add_division = Label(dashboard_l , text="Class" , bg="lavender blush" , fg="#be2102",
                     font=("times new roman" , 15 , "bold")).grid(row = 2 , column = 0 , pady=20 )
    division_entry = Entry(dashboard_l , textvariable=division).grid(row = 2 , column = 1 , pady=20 , padx=10 )
    
    add_section = Label(dashboard_l , text="Section" , bg="lavender blush" , fg="#be2102",
                     font=("times new roman" , 15 , "bold")).grid(row = 3 , column = 0 , pady=20 )
    section_entry = Entry(dashboard_l , textvariable=section).grid(row = 3 , column = 1 , pady=20 , padx=10 )
    
    add_gender = Label(dashboard_r , text="Gender" , bg="lavender blush" , fg="#be2102",
                     font=("times new roman" , 15 , "bold")).grid(row = 0 , column = 0 , pady=20 )
    gender_entry = ttk.Combobox(dashboard_r , state="readonly" , textvariable=gender)
    gender_entry['values'] = ('Male' , 'Female' , 'Other')
    gender_entry.grid(row = 0 , column = 1 , pady=20 , padx=10 )
    
    add_contact = Label(dashboard_r , text="Contact Number" , bg="lavender blush" , fg="#be2102",
                     font=("times new roman" , 15 , "bold")).grid(row = 1 , column = 0 , pady=20 )
    contact_entry = Entry(dashboard_r , textvariable=contact).grid(row = 1 , column = 1 , pady=20 , padx=10 )
    
    add_dob = Label(dashboard_r , text="D.O.B" , bg="lavender blush" , fg="#be2102",
                     font=("times new roman" , 15 , "bold")).grid(row = 2 , column = 0 , pady=20 )
    dob_entry = Entry(dashboard_r , textvariable=dob).grid(row = 2 , column = 1 , pady=20 , padx=10 )
    
    add_email = Label(dashboard_r , text="Email" , bg="lavender blush" , fg="#be2102",
                     font=("times new roman" , 15 , "bold")).grid(row = 3 , column = 0 , pady=20 )
    email_entry = Entry(dashboard_r , width=35 , textvariable=email).grid(row = 3 , column = 1 , pady=20 , padx=10 )
    
    add_address = Label(dashboard_r , text="Address" , bg="lavender blush" , fg="#be2102",
                     font=("times new roman" , 15 , "bold")).grid(row = 4 , column = 0 , pady=20 )
    address_entry = Text(dashboard_r , width=30 , height=5)
    address_entry.grid(row = 4 , column = 1 , pady=10 , padx=10 )
            
    add_btn_frame = Frame(addStd)
    
    add_btn_frame.place(x=120,y=460)
    add_btn = Button(add_btn_frame,text="Add Student",command=add_db ,font=("times new roman","14","bold"), relief=SOLID, bg="lavender blush" , fg="#be2102" , width=20)
    add_btn.grid(row = 5 , column = 1 , pady=10 , padx=10 )
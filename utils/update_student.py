from utils.helper_code import *

"""
fetch_data() -> fetch data from database
clear() -> reset all fields
get_cursor() -> fill corresponding fields of the selected student
search_data() -> search for a student in the database
"""
    
def update_std():
    
    updStd = Tk()
    updStd.resizable(False,False)
    updStd.geometry("940x600+160+100")
    updStd.title("Update Students")
    updStd.configure(background="snow")
    updStd.wm_iconbitmap('media/update.ico')
    
    bg_img = Image.open("media/add_back.jpg")
    bg = ImageTk.PhotoImage(bg_img, master=updStd)
    back = Label(updStd, image=bg)
    back.pack()
    
    roll_no = tk.StringVar(updStd)
    name = tk.StringVar(updStd)
    division = tk.StringVar(updStd)
    section = tk.StringVar(updStd)
    gender = tk.StringVar(updStd)
    contact = tk.StringVar(updStd)
    email = tk.StringVar(updStd)
    dob = tk.StringVar(updStd)
    searchby = tk.StringVar(updStd)
    searchtext = tk.StringVar(updStd)
    
    def fetch_data():
        
        conn = mysql.connector.connect(host="127.0.0.1",user="root",password=passwd,database=dbname)
        cur = conn.cursor()
        cur.execute("select * from "+dbname)
        rows = cur.fetchall()
        
        if len(rows)!=0:
            stu_tab.delete(*stu_tab.get_children())
            
            for r in rows:
                stu_tab.insert('',END,values=r)
                
            conn.commit()
        conn.close()
        
    def clear():
        
        roll_no.set("")
        name.set("")
        division.set("")
        section.set("")
        gender.set("")
        contact.set("")
        email.set("")
        dob.set("")
        address_entry.delete('1.0',END)
    
    display = Frame(updStd , bg="lavender blush" , width = 280 , height = 600 ,
                    highlightbackground="black" , highlightthickness=1)
    display.place(x=10,y=30)
    
    right = Frame(updStd,bg="snow",width=640,height=570)
    right.place(x=420,y=10)
    
    add_roll = Label(display , text="Roll Number" ,  bg="lavender blush" , fg="#be2102",
                     font=("times new roman" , 15 ,"bold"))
    add_roll.grid(row = 0 , column = 0 , pady=20 )
    roll_entry = tk.Entry(display , width=20 , textvariable=roll_no)
    roll_entry.grid(row = 0 , column = 1 , pady=20 , padx=10 )

    add_name = Label(display , text="Name" , bg="lavender blush" , fg="#be2102",
                     font=("times new roman" , 15 , "bold")).grid(row = 1 , column = 0 , pady=10 )
    name_entry = Entry(display , width=35 , textvariable=name).grid(row = 1 , column = 1 , pady=12 , padx=5 )
    
    add_division = Label(display , text="Class" , bg="lavender blush" , fg="#be2102",
                     font=("times new roman" , 15 , "bold")).grid(row = 2 , column = 0 , pady=10 )
    division_entry = Entry(display , textvariable=division).grid(row = 2 , column = 1 , pady=12 , padx=5 )
    
    add_section = Label(display , text="Section" , bg="lavender blush" , fg="#be2102",
                     font=("times new roman" , 15 , "bold")).grid(row = 3 , column = 0 , pady=12 )
    section_entry = Entry(display , textvariable=section).grid(row = 3 , column = 1 , pady=12 , padx=5 )
    
    add_gender = Label(display , text="Gender" , bg="lavender blush" , fg="#be2102",
                     font=("times new roman" , 15 , "bold")).grid(row = 4 , column = 0 , pady=12 )
    gender_entry = ttk.Combobox(display , state="readonly" , textvariable=gender)
    gender_entry['values'] = ('Male' , 'Female' , 'Other')
    gender_entry.grid(row = 4 , column = 1 , pady=12 , padx = 5 )
    
    add_contact = Label(display , text="Contact Number" , bg="lavender blush" , fg="#be2102",
                     font=("times new roman" , 15 , "bold")).grid(row = 5 , column = 0 , pady=12 )
    contact_entry = Entry(display , textvariable=contact).grid(row = 5 , column = 1 , pady=12 , padx=5 )
    
    add_dob = Label(display , text="D.O.B" , bg="lavender blush" , fg="#be2102",
                     font=("times new roman" , 15 , "bold")).grid(row = 6 , column = 0 , pady=12 )
    dob_entry = Entry(display , textvariable=dob).grid(row = 6 , column = 1 , pady=12 , padx=5 )
    
    add_email = Label(display , text="Email" , bg="lavender blush" , fg="#be2102",
                     font=("times new roman" , 15 , "bold")).grid(row = 7 , column = 0 , pady=12 )
    email_entry = Entry(display , width=30 , textvariable=email).grid(row = 7 , column = 1 , pady=12 , padx=5 )
    
    add_address = Label(display , text="Address" , bg="lavender blush" , fg="#be2102",
                     font=("times new roman" , 15 , "bold")).grid(row = 8 , column = 0 , pady=12 )
    address_entry = Text(display , width=30 , height=4)
    address_entry.grid(row = 8 , column = 1 , pady=12 , padx=5 )
    
    table_frame = Frame(right)
    table_frame.place(x=20,y=120,height=400,width=500)
    
    scroll_x = Scrollbar(table_frame,orient=HORIZONTAL)
    scroll_y = Scrollbar(table_frame,orient=VERTICAL)
    stu_tab = ttk.Treeview(table_frame,columns=('roll' , 'name' , 'division' , 'section' , 'gender' ,'contact' , 'email' , 'dob' , "address"), xscrollcommand = scroll_x.set)
    scroll_x.pack(side=BOTTOM,fill=X)
    scroll_y.pack(side=RIGHT,fill=Y)
    scroll_x.config(command = stu_tab.xview)
    scroll_y.config(command = stu_tab.yview)
    
    stu_tab.heading("roll",text="Roll Number")
    stu_tab.heading("name",text="Name")
    stu_tab.heading("division",text="Class")
    stu_tab.heading("section",text="Section")
    stu_tab.heading("gender",text="Gender")
    stu_tab.heading("contact",text="Contact")
    stu_tab.heading("email",text="Email")
    stu_tab.heading("dob",text="DOB")
    stu_tab.heading("address",text="Address")
    stu_tab['show']=['headings']
        
    stu_tab.column("roll",width=100)
    stu_tab.column("name",width=200)
    stu_tab.column("division",width=100)
    stu_tab.column("section",width=100)
    stu_tab.column("gender",width=100)
    stu_tab.column("contact",width=100)
    stu_tab.column("email",width=200)
    stu_tab.column("dob",width=100)
    stu_tab.column("address",width=400)
        
    stu_tab.pack(fill=BOTH , expand = 1)
    fetch_data()
    
    def get_cursor(event):
        
        cursor_row = stu_tab.focus()
        contents = stu_tab.item(cursor_row)
        row = contents['values']
        roll_no.set(row[0])
        name.set(row[1])
        division.set(row[2])
        section.set(row[3])
        gender.set(row[4])
        contact.set(row[5])
        email.set(row[6])
        dob.set(row[7])
        address_entry.delete('1.0',END)
        address_entry.insert(END , row[8])
    
    stu_tab.pack(fill=BOTH , expand = 1)
    stu_tab.bind("<ButtonRelease-1>",get_cursor)
    
    def search_data():
    
        conn = mysql.connector.connect(host="127.0.0.1",user="root",password=passwd,database=dbname)
        cur = conn.cursor()
        one = str(searchby.get())
        two = str(searchtext.get())
        cur.execute( "select * from "+dbname+" where " + one + " like '%" + two + "%'" )
        rows = cur.fetchall()
        
        if len(rows)!=0:
            stu_tab.delete(*stu_tab.get_children())
            
            for r in rows:
                stu_tab.insert('',END,values=r)
        else:   
            messagebox.showerror("Error","No results found")
            updStd.tkraise()

        conn.commit()
        conn.close()
    
    search = Frame(right , bg="lavender blush" , width = 660 , height = 100 ,
                   highlightbackground="black" , highlightthickness=1)
    search.place(x=15 , y=20)
    
    search_by_lbl = Label(search,text="Search By" , bg="lavender blush" , fg="#be2102",
                         font=("times new roman","15","bold")).grid(row=0,column=0,padx=10)
    
    search_by = ttk.Combobox(search , state="readonly" , textvariable = searchby, width=10)
    search_by['values'] = ('Roll_No' , 'Name' , 'Contact' , 'Class' , 'Section' , 'Email')
    search_by.grid(row=0,column=2,padx=10,pady=5)
    
    search_text = Entry(search , textvariable = searchtext , width=23)
    search_text.grid(row=0,column=6,padx=10)
    search_btn = Button(search,text="Search" , command=search_data , bg="lavender blush" , fg="#be2102", relief = SOLID, font=("times new roman","15","bold")).grid(row=0,column=8,padx=20,pady=10)
    
    def update_data():
        
        conn = mysql.connector.connect(host="127.0.0.1",user="root",password=passwd,database=dbname)
        cur = conn.cursor()

        if not validate_data(roll_no.get(), name.get(), division.get(), section.get(), contact.get(), email.get(), dob.get()):
            updStd.tkraise()
        
        else:
            cur.execute("update "+dbname+ " set name=%s,class=%s,section=%s,gender=%s,contact=%s,email=%s,dob=%s,address=%s where                     roll_no=%s", ( name.get(),division.get(),section.get(), gender.get(),contact.get(), email.get(),   
                    dob.get(), address_entry.get('1.0',END),roll_no.get()))
        
            conn.commit()
            messagebox.showinfo("Success","Updated Successfully")
            
            updStd.destroy()
            conn.close()
            
            fetch_data()
            clear()
    
    btn_upd = Button(right,text="Update",command=update_data ,font=("times new roman","14","bold"),
                    relief=SOLID, bg="lavender blush" , fg="#be2102" , width=10)
    btn_upd.place(x=250,y=530)
    
    updStd.mainloop()
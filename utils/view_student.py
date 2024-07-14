from utils.helper_code import *

def view_std():
    
    viewStd = Tk() # creating window and setting necessary parameters
    
    viewStd.resizable(False,False) # window can't be resized
    viewStd.geometry("940x600+160+100") # window parameters
    viewStd.title("View Students") # window title
    viewStd.wm_iconbitmap('media/view.ico') # window icon
    
    roll_no = StringVar()  # declaring variables
    name = StringVar()
    section = StringVar()
    gender = StringVar()
    dob = StringVar()
    division = StringVar()
    contact = StringVar()
    email = StringVar()
    
    scroll_x = Scrollbar(viewStd, orient=HORIZONTAL)  # horizontal scrollbar
    scroll_y = Scrollbar(viewStd, orient=VERTICAL)  # vertical scrollbar
    
    stu_tab = ttk.Treeview(viewStd,columns=('roll' , 'name' , 'division' , 'section' , 'gender' ,'contact' , 'email' , 'dob' , "address"), xscrollcommand = scroll_x.set, height=25)
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
    stu_tab.heading("dob",text="D.O.B")
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
    
    conn = mysql.connector.connect(host="127.0.0.1",user="root",password=passwd,database=dbname)  # connecting to database
    cur = conn.cursor()
    cur.execute("select * from "+ dbname)
    rows = cur.fetchall()
    
    if len(rows)!=0:  # check if table is empty ot not
        stu_tab.delete(*stu_tab.get_children())
    
        for r in rows: 
            stu_tab.insert('',END,values=r)
            
    else:
        messagebox.showerror('No Students in Databse', "Please add Student Records to Database")
        
    conn.commit()
    conn.close()
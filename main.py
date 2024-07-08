import sys
sys.path.append("utils")

from add_student import add_std
from change_password import change_psswd
from delete_student import del_std
from update_student import update_std
from view_student import view_std
from dashboards import dashboards
from announcements import announcements
from helper_code import *

header, txt, cnt = "Student Data Management Portal", "", 0
"""
Main Portal

show_dt() -> display current date and time
exit_portal() -> exit the portal
animate() -> add animation to the main header
"""

def open_portal():

    def exit_portal():
        if portal.state()=="normal":  # check whether the portal is opened or not   
            portal.destroy()
            
    def show_dt():
        time_str = time.strftime("%H:%M:%S")  # get current date and time 
        date = time.strftime("%d:%m:%Y")   
        clock.config(text = " Date : "+ date + "\n" + "Time : " + time_str )
        clock.after(100, show_dt)
        
    def animate():
        
        global cnt, txt  
        if cnt >= len(header):  # reset all the parameters once the header is fully traversed
            cnt, txt = 0, ""
            title_2.config(text=txt)  
        else: 
            txt = txt+header[cnt]
            title_2.config(text=txt)
            cnt += 1
            
        title_2.after(150, animate)
    
    portal = Tk()  # creating tkinter window and setting the requi#be2102 parameters
    
    portal.title("Student Data Management Portal")
    portal.resizable(False,False)
    portal.wm_iconbitmap('media/user.ico')

    screen_width = portal.winfo_screenwidth()
    screen_height = portal.winfo_screenheight()
    portal.geometry(f"{screen_width-20}x{screen_height-20}+0+0")

    bg_2 = ImageTk.PhotoImage(Image.open("media/add_back.jpg"))
    view = ImageTk.PhotoImage((Image.open("media/view.png")).resize((135,135),Image.LANCZOS))
    add = ImageTk.PhotoImage((Image.open("media/add.png")).resize((135,135),Image.LANCZOS))
    update = ImageTk.PhotoImage((Image.open("media/update.png")).resize((135,135),Image.LANCZOS))
    delete = ImageTk.PhotoImage((Image.open("media/delete.png")).resize((135,135),Image.LANCZOS))
    face = ImageTk.PhotoImage((Image.open("media/face.png")).resize((135,135),Image.LANCZOS))
    train = ImageTk.PhotoImage((Image.open("media/announcements.png")).resize((135,135),Image.LANCZOS))
    password = ImageTk.PhotoImage((Image.open("media/password.png")).resize((135,135),Image.LANCZOS))
    exit = ImageTk.PhotoImage((Image.open("media/exit.png")).resize((135,135),Image.LANCZOS))
    add_back_img = Image.open("media/add_back.jpg")
    add_back = ImageTk.PhotoImage(add_back_img)
    
    bg_2_label = Label(portal , image=bg_2)
    bg_2_label.pack()
    
    title_2 = Label(portal , text="Student Data Management Portal" , font=("times new roman" , 36 , "bold") , bg="lavender blush", relief=SOLID , fg="#be2102")
    title_2.place(x=0,y=0,relwidth=1)
    
    # animate()
    
    clock = Label(portal,font=("Times New Roman",12,"bold"),bg="lavender blush")
    clock.place(x=100,y=10)
    
    show_dt()
    
    brand_img = ImageTk.PhotoImage((Image.open("media/brand.png")).resize((50,50),Image.LANCZOS))
    brand = Label(portal , image=brand_img).place(x=30,y=4)
    
    menu = Frame(portal , bg="lavender blush" , highlightbackground="black" , highlightthickness=1 , width=200 , height=680)
    menu.place(x=3,y=70)
    
    menu_r = Frame(portal , bg="lavender blush" , highlightbackground="black" , highlightthickness=1 , width=200 ,height=680)
    menu_r.place(x=1110,y=70)
    
    btn_view = Button(menu , text="View Students" , image=view , bg="lavender blush" , command = view_std ,compound=tk.TOP).grid(row=0,column=0)

    btn_add = Button(menu , text="Add Students" , image=add , bg="lavender blush" , command = add_std ,
    compound=tk.TOP).grid(row=1,column=0)

    btn_update = Button(menu , text="Update Students" , image=update , bg="lavender blush" , command = update_std ,compound=tk.TOP).grid(row=2,column=0)

    btn_delete = Button(menu , text="Delete Students" , image=delete , bg="lavender blush" , command = del_std ,compound=tk.TOP).grid(row=3,column=0)

    btn_face = Button(menu_r , text="Dashboards" ,image=face , bg="lavender blush" , command = dashboards,compound=tk.TOP).grid(row=4,column=0)

    btn_train = Button(menu_r , text="Announcements" ,image=train , bg="lavender blush" , command = announcements,compound=tk.TOP).grid(row=5,column=0)

    btn_change = Button(menu_r , text="Change Password", image=password , bg="lavender blush" , command = change_psswd ,compound=tk.TOP).grid(row=6,column=0)

    btn_exit = Button(menu_r , text="Exit" , image=exit , bg="lavender blush" , command = exit_portal ,
    compound=tk.TOP).grid(row=7,column=0)    
    
    portal.mainloop()
    
"""
Log-In Window
"""
    
login = Tk()

username = StringVar()
password = StringVar()

login.title("Login to Student Data Management Portal")
login.resizable(False,False)

screen_width = login.winfo_screenwidth()
screen_height = login.winfo_screenheight()
login.geometry(f"{screen_width-20}x{screen_height-20}+0+0")

def log_in():
    
    if username.get() == "" or password.get() == "":  # check for empty fields
        messagebox.showerror("Error","All fields are Required")
        
    elif username.get() == "admin" and password.get() == log_pass:
        login.destroy()  
        open_portal()     
        
    else:
        messagebox.showerror("Error","Invalid Username or Password")

bg_1 = ImageTk.PhotoImage(Image.open("media/add_back.jpg"))
add_back = ImageTk.PhotoImage(file="media/add_back.jpg")
user_1 = ImageTk.PhotoImage((Image.open("media/user_1.jpeg")).resize((150,150),Image.LANCZOS))
user_2 = ImageTk.PhotoImage(Image.open("media/user_2.png").resize((30,30),Image.LANCZOS))
psswd_1 = ImageTk.PhotoImage(Image.open("media/psswd_1.png").resize((30,30),Image.LANCZOS))

bg_1_label = Label(login , image=bg_1)
bg_1_label.pack()

title_1 = Label(login , text="" , font=("times new roman" , 40 , "bold") , bg="lavender blush" , 
                relief=SOLID , fg="#be2102")
title_1.place(x=0,y=0,relwidth=1)

login_frame = Frame(login , bg="lavender blush" , highlightbackground="black" , highlightthickness=3)
login_frame.place(x=420 , y=220)
login_user = Label(login_frame , image = user_1 , relief=SOLID).grid(row = 0 , columnspan = 2 , pady=20 )

login_user_logo = Label(login_frame , text = "Username" , image=user_2 , compound=LEFT , bg="lavender blush" , fg="#be2102" , font=("times new roman" , 15 , "bold"))
login_user_logo.grid(row=1 , column=0)

login_user_entry = Entry(login_frame , textvariable=username , width=40).grid(row=1,column=1,padx=15)

login_psswd_logo = Label(login_frame , text = "Password" , image=psswd_1 , bg="lavender blush" ,fg="#be2102" ,compound=LEFT , font=("times new roman" , 15 , "bold"))
login_psswd_logo.grid(row=2 , column=0)

login_psswd_entry = Entry(login_frame , show='*' ,textvariable = password , width=40).grid(row=2,column=1,padx=15)

login_button = Button(login_frame , text="Login" , command = log_in , width=15 , font=("times new roman" , 15 , "bold") , bg="lavender blush" , fg="#be2102" , relief=SOLID).grid(row=3,columnspan=2,pady=20)
        
login.mainloop()
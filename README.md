<h3>Table of Contents</h3>
<ul>
    <li><a href="#introduction">Introduction</a></li>
    <li><a href="#overview">Overview</a></li>
    <li><a href="#installation-and-setup">Installation and Setup</a></li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#future-work">Future Work</a></li>
</ul>

<h3 id="introduction">Introduction</h3>
<div>
   In the bustling corridors of educational institutions, administrators are constantly overwhelmed with the sheer volume of student data they must manage. From enrollment records and attendance logs to academic performance and personal details , the task is monumental. Recognizing this challenge, I set out to create Avishkaar, a Student Data Management Portal that transforms how educational institutions handle student data.
</div>

<h3 id="overview">Overview</h3>
<div>
   Avishkaar serves as a Student Data Management Portal, featuring a Tkinter-based Frontend integrated with MySQL as its Backend Database. The seamless connection and interaction with the database is facilitated by the <code>mysql-connector-python</code> package, empowering the Frontend to access and manipulate data stored in database. 
   <br><br>
   However Avishkaar is more than just a archive for student data. It embodies an ambitious vision for elevating data management and manipulation to new heights. At its current stage, the application caters to the administrative domain by providing essential functionalities for administering student data in a methodical manner.<br><br>
</div>

```
                +-------------------+
                |      Tkinter      |
                |   (Client Side)   |
                +--------+----------+
                         |
                         | User Input
                         v
            +------------+------------------+
            |    mysql-connector-python     |
            |      (Data Processing)        |
            +------------+------------------+
                         |
                         | SQL Queries
                         v
                +--------+----------+
                |     MySQL DB      |
                |  (Server Side)    |
                +-------------------+

```

<div>
   The following diagram depicts the schema of the MySQL database, encompassing crucial student information such as roll number, name, class, section, gender, contact number, email, date of birth, and address. The roll number is designated as PK (Primary Key) and UQ (Unique Index), ensuring each student is allocated a distinct identifier.<br><br>
   <img width="500" src="./screenshots/mysql-db.png"><br>
</div>

<h3 id="installation-and-setup">Installation and Setup</h3>
<blockquote>
   It is recommended to set up a virtual environment to avoid conflicts between package versions installed on your system and keep your workspace organized. To create a virtual environment and activate it, please follow the instructions detailed on <a href="https://docs.python.org/3/library/venv.html">python venv page</a>. The procedure to deactivate the environment is also provided here.
   <br>
</blockquote>
<br>
<blockquote>Please note that currently, the application may not be fully responsive on smaller screens, potentially leading to UI breakdowns. I am actively working on UI enhancements to ensure resposive behavior of the Portal.<br>
</blockquote>
<br>
<ul>
   <li>Clone the git repo using <code>git clone https://github.com/asood-life/avishkaar.git</code></li>
   <li>Install the required packages using <code>pip install -r requirements.txt</code></li>
   <li>Create a MySQL database following the schema described above. Ensure to specify the database name and required access password in the <code>credentials.json</code> file.</li>
</ul>

<h3 id="usage">Usage</h3>
<div>
   Navigate to the project folder and execute <code>python main.py</code> to run the application.
</div>
<br>
<div>
   Welcome to the Login Page! Please provide your Username and Password to access the Portal. The default credentials are both set to "admin." You can easily change the password later from the Portal.
</div>
<br>
<img src="screenshots/login-page.png"><br><br>

<div>After a successful login, the user is greeted with a window showcasing the Portal interface, which includes 8 Buttons (4 on each side). These buttons offer a range of functionalities:</div>
<br>
<img src="screenshots/home-page.png"><br><br>

<b>VIEW STUDENTS</b>: Enables user to access and view records of all students stored in the database in a tabular format.
<br><br>
<img src="screenshots/view-students.png"><br> 

<b>ADD STUDENTS</b>: Empowers the user to add student records to the database populating the following fields:
<br>
<ul>
   <li>Roll Number</li>
   <li>Name of Student</li>
   <li>Section</li>
   <li>Class</li>
   <li>Gender</li>
   <li>Contact Number</li>
   <li>Date of Birth</li>
   <li>Email</li>
   <li>Address</li>
</ul>
Please note that the Roll Number holds fundamental significance for each student and cannot be shared with others. Hence, the portal strictly prohibits the duplication of roll numbers for multiple students. Furthermore, it is crucial to fill at least the Roll Number and Name of the Student. Other details can be updated later thorugh the Portal.<br><br>
<img src="screenshots/add-students.png"><br><br>

<b>UPDATE STUDENTS</b>:  If you have entered incorrect details or missed some entries, don't fret! The portal allows you to update student records at your convenience. One of its most fascinating features for smooth operation is the Search functionality. User can easily search for a particular student using the following fields:
<ul>
   <li>Roll Number</li>
   <li>Name</li>
   <li>Contact Number</li>
   <li>Class</li>
   <li>Section</li>
   <li>Email</li>
</ul>
Leverage the search feature and get the results displayed in the table positioned on the right to locate the student for whom you wish to update details. Simply clicking on the student entry in the table will automatically populate the fields located on the left. From there, you can update any desired field. Once you are finished, use the <code>Update</code> button to apply the modifications and get them relfected in the database.<br><br> 
<img src="screenshots/update-students.png"><br><br>

<b>DELETE STUDENTS</b>:  If one of your students has recently left or transferred to another institution, it is crucial to promptly remove their relevant records from the database to prevent any confusion. The Search functionality mentioned above is also available for this purpose. Simply search for the concerned student, click on their entry in the table where the results are displayed, and then use the <code>Delete</code> button to remove them from the database.<br><br>
<img src="screenshots/delete-students.png"><br><br>

<b>CHANGE PASSWORD</b>:  If you have accidentally revealed your password to someone (well I have done at start :D) don't panic. You can change your password anytime you desire. However, before making the change, user must confirm their old password to ensure authentic access.<br><br>
The login password is retrieved from the <code>credentials.json</code> file. If the validation is successful during the password change process, the new password is written to the JSON, overwriting the previous value.
<br><br>
<img src="screenshots/change-password.png"><br><br>

<b>EXIT</b>:  Enables the user to exit the portal and close the portal window. Please note that this button can only be used to close the main portal window and not any other active windows.
</p>

<h3 id="future-work">Future Work</h3>
<ul>
   <li><b>Enhancing Responsiveness and Modularizing Codebase</b>: Ensure the application adjusts to various screen sizes while modularizing the codebase for better organization and easier maintainence in the future.</li>
   <li><b>Announcements</b>: Introduce a feature for publishing announcements in the application.</li>
   <li><b>Personalized Dashboards</b>: Incorporate a personalized dashboard for students, showcasing their attendance and grades, courses taken, and other pertinent personal information already recorded in the database.</li>
   <li><b>Bulk Operations</b>: Allow the use of an excel sheet to add or update student details in the database ensuring minimal manual intervention and streamlining of the overall procedure.</li>
</ul>

<hr>
<div>
    Thank you for taking the time to go through this project! If you find it valuable, please consider giving it a ⭐ star. Your support is appreciated and helps others in discovering the project. Should you have any enhancement requests or encounter a bug, please report it in the <a href="https://github.com/asood-life/avishkaar/issues">Issues</a> section. Your feedback is crucial in improving this project for all.
</div>

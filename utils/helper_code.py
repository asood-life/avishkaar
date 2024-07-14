# Importing necessary libraries
import numpy as np
from tkinter import *
from tkinter import ttk, messagebox
import tkinter as tk
import pandas as pd
import mysql.connector
from PIL import ImageTk, Image
import json
from datetime import datetime
import time, re

# Loading database credentials from JSON file
with open("credentials.json", "r") as file:
    creds = json.load(file)

# Extracting credentials from JSON
log_pass = creds["log_pass"]
passwd = creds["passwd"]
dbname = creds["dbname"]


def validate_data(roll_no, name, division, section, contact, email, dob):
        
        # Check if roll number is an integer
        try:
            int(roll_no)
        except ValueError:
            messagebox.showerror("Input Error", "Roll number must be an integer")
            return False
        
        # Check if name contains only alphabetic characters and is at least 3 characters long
        if not re.match(r'^[A-Za-z ]{3,}$', name):
            messagebox.showerror("Input Error", "Name must contain only alphabetic characters and be at least 3 characters long")
            return False
        
        # Check if division is an integer
        try:
            int(division)
        except ValueError:
            messagebox.showerror("Input Error", "Division must be an integer")
            return False
        
        # Check if section is a single character
        if section and len(section) != 1:
            messagebox.showerror("Input Error", "Section must be a single character")
            return False
        
        # Check if contact is a valid phone number (basic check)
        if contact and not re.match(r'^\+?1?\d{9,15}$', contact):
            messagebox.showerror("Input Error", "Contact must be a valid phone number")
            return False
        
        # Check if email is valid
        if email and not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
            messagebox.showerror("Input Error", "Email must be a valid email address")
            return False
        
        # Check if dob is in 'YYYY-MM-DD' format
        try:
            datetime.strptime(dob, '%Y-%m-%d')
        except ValueError:
            messagebox.showerror("Input Error", "Date of Birth must be in 'YYYY-MM-DD' format")
            return False
        
        return True
from blood_pressure import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import filedialog, messagebox
from tkinter import messagebox
from tkinter import messagebox, filedialog
from tkinter import messagebox, simpledialog
import customtkinter as ctk
import customtkinter as ctk  # Assuming you are using CTk widgets
import datetime
import json
import matplotlib.pyplot as plt
import os
import random
import tkinter as tk

def switch_to_register():
    login_window.withdraw()
    register_window.deiconify()

# Create main window
main_window = ctk.CTk()
main_window.title("Patient Profile Manager")
main_window.geometry("800x500")
main_window.withdraw()

# Left Panel: Profile Information
profile_frame = ctk.CTkFrame(main_window)
profile_frame.pack(side="left", fill="y", padx=20, pady=20)

label_profile_title = ctk.CTkLabel(profile_frame, text="Patient Profile", font=ctk.CTkFont(size=20, weight="bold"))
label_profile_title.pack(pady=10)

label_profile_name = ctk.CTkLabel(profile_frame, text="Name:")
label_profile_name.pack(pady=(10, 2))
label_profile_name_value = ctk.CTkLabel(profile_frame, text="")
label_profile_name_value.pack()

label_profile_id = ctk.CTkLabel(profile_frame, text="User ID:")
label_profile_id.pack(pady=(10, 2))
label_profile_id_value = ctk.CTkLabel(profile_frame, text="")
label_profile_id_value.pack()

label_add_category = ctk.CTkLabel(profile_frame, text="Add New Category")
label_add_category.pack(pady=(20, 5))

entry_category = ctk.CTkEntry(profile_frame, placeholder_text="Category Name (e.g., Diagnosis)")
entry_category.pack(pady=5)

entry_category_value = ctk.CTkEntry(profile_frame, placeholder_text="Category Value")
entry_category_value.pack(pady=5)

button_add_category = ctk.CTkButton(profile_frame, text="Add Category", command=add_category)
button_add_category.pack(pady=10)

# Right Panel: Categories Table
categories_frame = ctk.CTkFrame(main_window, border_color="gray", border_width=1)
categories_frame.pack(side="right", fill="both", expand=True, padx=20, pady=20)

label_table_header = ctk.CTkLabel(categories_frame, text="Cate  gories", font=ctk.CTkFont(size=16, weight="bold"))
label_table_header.pack(pady=10)

# Registration and Login Windows
register_window = ctk.CTkToplevel(main_window)
register_window.title("Register")
register_window.geometry("400x500")

login_window = ctk.CTkToplevel(main_window)
login_window.title("Sign In")
login_window.geometry("400x300")
login_window.withdraw()

# Registration Window UI
label_title = ctk.CTkLabel(register_window, text="Register", font=ctk.CTkFont(size=24, weight="bold"))
label_title.pack(pady=20)

label_name = ctk.CTkLabel(register_window, text="Name")
label_name.pack(pady=(10, 5))
entry_name = ctk.CTkEntry(register_window)
entry_name.pack(pady=5)

label_id = ctk.CTkLabel(register_window, text="National ID")
label_id.pack(pady=(10, 5))
entry_id = ctk.CTkEntry(register_window)
entry_id.pack(pady=5)

label_password = ctk.CTkLabel(register_window, text="Password")
label_password.pack(pady=(10, 5))
entry_password = ctk.CTkEntry(register_window, show="*")
entry_password.pack(pady=5)

label_confirm_password = ctk.CTkLabel(register_window, text="Confirm Password")
label_confirm_password.pack(pady=(10, 5))
entry_confirm_password = ctk.CTkEntry(register_window, show="*")
entry_confirm_password.pack(pady=5)

button_register = ctk.CTkButton(register_window, text="Register", command=register_user)
button_register.pack(pady=20)

button_switch_login = ctk.CTkButton(register_window, text="Switch to Login", command=lambda: (register_window.withdraw(), login_window.deiconify()))
button_switch_login.pack(pady=10)

# Login Window UI
label_login_title = ctk.CTkLabel(login_window, text="Login", font=ctk.CTkFont(size=24, weight="bold"))
label_login_title.pack(pady=20)

label_login_id = ctk.CTkLabel(login_window, text="User ID")
label_login_id.pack(pady=(10, 5))
entry_login_id = ctk.CTkEntry(login_window)
entry_login_id.pack(pady=5)

label_login_password = ctk.CTkLabel(login_window, text="Password")
label_login_password.pack(pady=(10, 5))
entry_login_password = ctk.CTkEntry(login_window, show="*")
entry_login_password.pack(pady=5)

button_login = ctk.CTkButton(login_window, text="Login", command=login_user)
button_login.pack(pady=20)

button_switch_register = ctk.CTkButton(login_window, text="Switch to Register", command=lambda: (login_window.withdraw(), register_window.deiconify()))
button_switch_register.pack(pady=10)

import customtkinter as ctk
from tkinter import messagebox, simpledialog
import json
import os
import random

# Directory to store user data
USER_DATA_DIR = "user_data"

if not os.path.exists(USER_DATA_DIR):
    os.makedirs(USER_DATA_DIR)

# Global variables
logged_in_user = {}

# Function to generate a unique randomized patient ID

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

def login_user():
    global logged_in_user
    patient_id = entry_login_id.get()  # Now using Patient ID for login
    password = entry_login_password.get()

    user_files = [f for f in os.listdir(USER_DATA_DIR) if f.endswith('.json')]

    for user_file in user_files:
        with open(os.path.join(USER_DATA_DIR, user_file), "r") as file:
            user_data = json.load(file)
            if str(user_data["patient_id"]) == patient_id and user_data["password"] == password:
                logged_in_user = user_data
                messagebox.showinfo("Success", f"Welcome back, {logged_in_user['name']}!")
                switch_to_main(logged_in_user)
                return

    messagebox.showerror("Error", "Invalid Patient ID or Password!")


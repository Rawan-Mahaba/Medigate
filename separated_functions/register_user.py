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

def register_user():
    global logged_in_user
    name = entry_name.get()
    user_id = entry_id.get()  # This is the National ID
    password = entry_password.get()
    confirm_password = entry_confirm_password.get()

    if not name or not user_id or not password or not confirm_password:
        messagebox.showerror("Error", "All fields are required!")
        return

    if len(password) < 8:
        messagebox.showerror("Error", "Password must be at least 8 characters long!")
        return

    special_characters = "@$&"
    if not any(char in special_characters for char in password):
        messagebox.showerror("Error", "Password must contain at least one special character (@, $, &).")
        return

    if not user_id.isdigit():
        messagebox.showerror("Error", "National ID must be numeric!")
        return

    if password != confirm_password:
        messagebox.showerror("Error", "Passwords do not match!")
        return

    user_file_path = os.path.join(USER_DATA_DIR, f"{user_id}.json")
    if os.path.exists(user_file_path):
        messagebox.showinfo("Notice", "User ID already exists! Redirecting to login.")
        switch_to_login()
        return

    # Generate a randomized patient ID
    patient_id = generate_patient_id()

    user_data = {
        "name": name,
        "national_id": user_id,
        "patient_id": patient_id,
        "password": password,
        "categories": [],
        "diabetes": [],
        "blood pressure": []
    }

    with open(user_file_path, "w") as user_file:
        json.dump(user_data, user_file, indent=4)

    messagebox.showinfo("Success", f"Registration Successful! Your Patient ID is: {patient_id}")
    clear_register_form()
    switch_to_main(user_data)
import customtkinter as ctk
import json

# Function to calculate and display average blood pressure
# Other helper functions (login_user, save_user_data, etc.) remain unchanged...

# Update the main window to include the Diabetes feature

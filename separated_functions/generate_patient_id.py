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

def generate_patient_id():
    """Generates a unique 8-digit patient ID."""
    return random.randint(10000000, 99999999)

# Function to handle the blood pressure feature
    def upload_measure():
        new = simpledialog.askinteger("Blood Pressure", "You did not upload any measurements. Please enter your latest blood pressure level:")
        if new is not None:
            blood_pressure_levels.append(new)

    def add_measure():
        while messagebox.askyesno("Blood Pressure", "Want to add another measure?"):
            new = simpledialog.askinteger("Blood Pressure", "Enter your new blood pressure level:")
            if new is not None:
                blood_pressure_levels.append(new)

    def check_previous_measures():
        if messagebox.askyesno("Blood Pressure", "Want to check the previous measures?"):
            if not blood_pressure_levels:
                messagebox.showinfo("No Data", "No previous blood pressure data found.")
            else:
                messagebox.showinfo("Previous Measures", "\n".join(map(str, blood_pressure_levels)))

    def save_to_file():
        logged_in_user["blood_pressure"] = blood_pressure_levels
        save_user_data()

    if len(blood_pressure_levels) == 0:
        upload_measure()

    add_measure()
    save_to_file()
    check_previous_measures()

    messagebox.showinfo("Blood Pressure", "Thank you!")



# Function for the Diabetes feature

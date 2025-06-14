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

def diabetes():
    glucose_levels = logged_in_user.get("diabetes", [])

    def upload_measure():
        new = simpledialog.askinteger("Diabetes", "You did not upload any measurements. Please enter your latest blood glucose level:")
        if new is not None:
            glucose_levels.append(new)

    def add_measure():
        while messagebox.askyesno("Diabetes", "Want to add another measure?"):
            new = simpledialog.askinteger("Diabetes", "Enter your new blood glucose level:")
            if new is not None:
                glucose_levels.append(new)

    def check_previous_measures():
        if messagebox.askyesno("Diabetes", "Want to check the previous measures?"):
            previous_measures = "\n".join(map(str, glucose_levels)) or "No previous data available."
            messagebox.showinfo("Previous Measures", previous_measures)

    def save_to_user_data():
        logged_in_user["diabetes"] = glucose_levels
        save_user_data()

    if len(glucose_levels) == 0:
        upload_measure()

    add_measure()
    save_to_user_data()
    check_previous_measures()

    messagebox.showinfo("Diabetes", "Thank you!")

# Function to handle registration

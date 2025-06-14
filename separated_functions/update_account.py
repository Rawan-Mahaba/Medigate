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

def update_account():
    """Logs doctor updates into a file."""
    # Ask the user for the doctor's name and the edit date
    doctor_name = ctk.CTkInputDialog(
        title="Update Account", text="Enter the doctor's name who made these edits:"
    ).get_input()

    if not doctor_name:
        messagebox.showwarning("Warning", "Doctor's name cannot be empty.")
        return

    edit_date = ctk.CTkInputDialog(
        title="Update Account",
        text="Enter the date of the edits (YYYY-MM-DD) or leave blank for today's date:",
    ).get_input()

    if not edit_date:
        edit_date = datetime.datetime.now().strftime('%Y-%m-%d')
    else:
        try:
            # Validate the entered date
            datetime.datetime.strptime(edit_date, '%Y-%m-%d')
        except ValueError:
            messagebox.showerror("Error", "Invalid date format. Please use YYYY-MM-DD.")
            return

    # Append the update information to the `updates.txt` file
    try:
        with open('updates.txt', 'a') as file:
            file.write(f"Doctor: {doctor_name}, Date: {edit_date}\n")
        messagebox.showinfo("Success", "The update has been logged successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to log the update. Error: {e}")


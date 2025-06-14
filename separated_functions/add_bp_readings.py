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

def add_bp_readings():
    global bp_readings, bp_readings_added, show_graph_button

    # Prompt the user to select a JSON file
    file_path = filedialog.askopenfilename(title="Select JSON File", filetypes=[("JSON Files", "*.json")])
    if not file_path:
        return

    try:
        with open(file_path, 'r') as file:
            data = json.load(file)

        # Ensure the JSON has the correct structure
        if "blood_pressure" in data and isinstance(data["blood_pressure"], list):
            bp_readings = data["blood_pressure"]
            if not all(isinstance(x, (int, float)) for x in bp_readings):
                raise ValueError("The 'blood_pressure' list contains non-numeric values.")

            bp_readings_added = True
            show_graph_button.pack(pady=20)  # Show the "Show Graph" button
            messagebox.showinfo("Success", "Blood pressure readings loaded successfully!")
        else:
            messagebox.showerror("Error", "Invalid JSON format. Ensure 'blood_pressure' key contains a list of numbers.")
    except json.JSONDecodeError:
        messagebox.showerror("Error", "Failed to decode JSON. Please select a valid JSON file.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")


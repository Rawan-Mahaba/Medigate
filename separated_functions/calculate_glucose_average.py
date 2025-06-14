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

def calculate_glucose_average():
    try:
        # Retrieve inputs from the glucose entry fields
        reading1 = float(glucose_entry1.get())
        reading2 = float(glucose_entry2.get())
        reading3 = float(glucose_entry3.get())

        # Calculate the average
        average_glucose = (reading1 + reading2 + reading3) / 3

        # Display the average in the glucose result label
        glucose_result_label.configure(text=f"Average Glucose Reading: {average_glucose:.2f}")

    except ValueError:
        glucose_result_label.configure(text="Error: Please enter valid numbers.")
    except Exception as e:
        glucose_result_label.configure(text=f"An unexpected error occurred: {e}")


# Main Window
root = ctk.CTk()  # Initialize the CustomTkinter root window
root.geometry("500x600")
root.title("SOS")

# Blood Pressure Section
bp_title_label = ctk.CTkLabel(root, text="Blood Pressure Readings", font=("Arial", 16))
bp_title_label.pack(pady=(20, 10))

bp_entry1 = ctk.CTkEntry(root, placeholder_text="Blood Pressure Reading 1")
bp_entry1.pack(pady=(5, 5))

bp_entry2 = ctk.CTkEntry(root, placeholder_text="Blood Pressure Reading 2")
bp_entry2.pack(pady=(5, 5))

bp_entry3 = ctk.CTkEntry(root, placeholder_text="Blood Pressure Reading 3")
bp_entry3.pack(pady=(5, 20))

bp_button = ctk.CTkButton(
    root,
    text="Calculate BP Average",
    command=SOS,
    fg_color="red",
    text_color="white"
)
bp_button.pack(pady=(10, 10))

bp_result_label = ctk.CTkLabel(root, text="", font=("Arial", 14))
bp_result_label.pack(pady=(10, 20))

# Glucose Section
glucose_title_label = ctk.CTkLabel(root, text="Glucose Readings", font=("Arial", 16))
glucose_title_label.pack(pady=(20, 10))

glucose_entry1 = ctk.CTkEntry(root, placeholder_text="Glucose Reading 1")
glucose_entry1.pack(pady=(5, 5))

glucose_entry2 = ctk.CTkEntry(root, placeholder_text="Glucose Reading 2")
glucose_entry2.pack(pady=(5, 5))

glucose_entry3 = ctk.CTkEntry(root, placeholder_text="Glucose Reading 3")
glucose_entry3.pack(pady=(5, 20))

glucose_button = ctk.CTkButton(
    root,
    text="Calculate Glucose Average",
    command=calculate_glucose_average,
    fg_color="blue",
    text_color="white"
)
glucose_button.pack(pady=(10, 10))

glucose_result_label = ctk.CTkLabel(root, text="", font=("Arial", 14))
glucose_result_label.pack(pady=(10, 20))

root.mainloop()  # Start the GUI loop

import tkinter as tk
from tkinter import messagebox, filedialog
import json
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Global variable to track whether blood pressure readings are added
bp_readings_added = False


# Function to load blood pressure readings from the JSON file
import tkinter as tk
from tkinter import filedialog, messagebox
import json
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Global variables
bp_readings = []  # Store loaded blood pressure readings
bp_readings_added = False


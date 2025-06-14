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

def plot_graph():
    global bp_readings, bp_readings_added

    if not bp_readings_added:
        messagebox.showerror("Error", "No blood pressure readings available. Please load readings first.")
        return

    try:
        if not bp_readings:
            messagebox.showerror("Error", "No readings found in the 'blood_pressure' list.")
            return

        # Create the plot
        fig, ax = plt.subplots()
        ax.plot(range(1, len(bp_readings) + 1), bp_readings, marker='o', linestyle='-', color='blue')
        ax.set_title("Blood Pressure Readings")
        ax.set_xlabel("Reading Index")
        ax.set_ylabel("BP Value")
        ax.grid(True)

        # Embed the plot into the GUI
        canvas = FigureCanvasTkAgg(fig, master=root)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Create the main window
root = tk.Tk()
root.title("BP Readings Viewer")
root.geometry("800x600")

# Add a button to load blood pressure readings
load_bp_button = tk.Button(root, text="Load Blood Pressure Readings", command=add_bp_readings)
load_bp_button.pack(pady=20)

# Add a button to show the graph (hidden initially)
show_graph_button = tk.Button(root, text="Show Graph", command=plot_graph)
show_graph_button.pack_forget()  # Initially hidden

# Run the application
root.mainloop()

import tkinter as tk
from tkinter import messagebox
import datetime
import customtkinter as ctk  # Assuming you are using CTk widgets


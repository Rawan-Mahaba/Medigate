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

def on_close():
    """Handles the main window close event."""
    if messagebox.askyesno("Confirm Exit", "Do you want to close the application?"):
        # Optional: Ask if the user wants to log an update
        if messagebox.askyesno("Log Update", "Would you like to log an update before exiting?"):
            update_account()
        main_window.destroy()  # Close the main window

# Create the main window
main_window = ctk.CTk()
main_window.title("Application")
main_window.geometry("400x300")

# Bind the `on_close` function to the main window's close event
main_window.protocol("WM_DELETE_WINDOW", on_close)

# Start the application
main_window.mainloop()

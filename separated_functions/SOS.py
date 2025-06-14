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

def SOS():
    try:
        # Retrieve inputs from the blood pressure entry fields
        reading1 = float(bp_entry1.get())
        reading2 = float(bp_entry2.get())
        reading3 = float(bp_entry3.get())

        # Calculate the average
        average_bp = (reading1 + reading2 + reading3) / 3

        # Display the average in the blood pressure result label
        bp_result_label.configure(text=f"Average Blood Pressure: {average_bp:.2f}")

    except ValueError:
        bp_result_label.configure(text="Error: Please enter valid numbers.")
    except Exception as e:
        bp_result_label.configure(text=f"An unexpected error occurred: {e}")


# Function to calculate the average glucose readings

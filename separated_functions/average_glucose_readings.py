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

def average_glucose_readings():
    try:
        # Open and load the data from the 'user-data' file
        with open('user-data', 'r') as file:
            data = json.load(file)

        # Extract the blood pressure list from the dictionary
        blood_pressure = data.get('blood presuure', [])

        # Check if the list is empty
        if not blood_pressure:
            print("No blood pressure data available.")
            return

        # Calculate the average
        average_bp = sum(blood_pressure) / len(blood_pressure)

        # Print the average in the console
        print(f"Average Blood Pressure: {average_bp}")

    except FileNotFoundError:
        print("Error: The file 'user-data' was not found.")
    except json.JSONDecodeError:
        print("Error: The file 'user-data' is not a valid JSON file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")



import customtkinter as ctk

# Define the SOS function
import customtkinter as ctk

# Define the SOS function
import customtkinter as ctk

# Function to calculate the average blood pressure

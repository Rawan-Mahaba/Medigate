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

def switch_to_main(user_data):
    global logged_in_user
    logged_in_user = user_data
    update_profile_info()
    load_categories()
    main_window.deiconify()
    register_window.withdraw()
    login_window.withdraw()

    # Add a button for the Diabetes feature
    blood_pressure_button = ctk.CTkButton(profile_frame, text="Blood pressure", command=blood_pressure, fg_color="pink", text_color="black")
    blood_pressure_button.pack(pady=(20, 5))

    # Add a button for the Diabetes feature
    diabetes_button = ctk.CTkButton(profile_frame, text="Diabetes", command=diabetes, fg_color="pink", text_color="black")
    diabetes_button.pack(pady=(20, 5))
import customtkinter as ctk
import json

# Function to calculate and display average blood pressure

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

def save_user_data():
    user_file_path = os.path.join(USER_DATA_DIR, f"{logged_in_user['national_id']}.json")
    with open(user_file_path, "w") as user_file:
        json.dump(logged_in_user, user_file, indent=4)


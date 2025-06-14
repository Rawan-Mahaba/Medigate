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

def add_category():
    category_name = entry_category.get()
    category_value = entry_category_value.get()

    if not category_name or not category_value:
        messagebox.showerror("Error", "Both category name and value are required!")
        return

    new_category = {"name": category_name, "value": category_value}
    logged_in_user["categories"].append(new_category)
    save_user_data()
    add_category_to_table(category_name, category_value)

    entry_category.delete(0, ctk.END)
    entry_category_value.delete(0, ctk.END)


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

def edit_category(category_name):
    for category in logged_in_user["categories"]:
        if category["name"] == category_name:
            entry_category.delete(0, ctk.END)
            entry_category_value.delete(0, ctk.END)
            entry_category.insert(0, category["name"])
            entry_category_value.insert(0, category["value"])
            logged_in_user["categories"].remove(category)
            break
    save_user_data()
    load_categories()


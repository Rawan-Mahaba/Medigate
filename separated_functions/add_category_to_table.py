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

def add_category_to_table(category_name, category_value):
    row_frame = ctk.CTkFrame(categories_frame)
    row_frame.pack(fill="x", pady=2)

    label_category_name = ctk.CTkLabel(row_frame, text=category_name, anchor="w")
    label_category_name.pack(side="left", padx=5)

    label_category_value = ctk.CTkLabel(row_frame, text=category_value, anchor="w")
    label_category_value.pack(side="left", padx=5)

    button_edit = ctk.CTkButton(row_frame, text="Edit", command=lambda: edit_category(category_name))
    button_edit.pack(side="left", padx=5)

    button_delete = ctk.CTkButton(row_frame, text="Delete", command=lambda: delete_category(category_name))
    button_delete.pack(side="left", padx=5)


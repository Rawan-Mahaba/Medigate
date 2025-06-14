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

def clear_register_form():
    entry_name.delete(0, ctk.END)
    entry_id.delete(0, ctk.END)
    entry_password.delete(0, ctk.END)
    entry_confirm_password.delete(0, ctk.END)

# Function to handle login

# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 13:05:57 2023

@author: Admin
"""

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry  # Assuming you have tkcalendar installed
from datetime import timedelta
from PIL import Image, ImageTk
root = tk.Tk()
root.title("Pink App")

# Set the background color to pink (hexadecimal color code for pink: #FFC0CB)
root.configure(bg='#FFC0CB')

# Create a label to demonstrate the pink background
label = tk.Label(root, text="Welcome to Flo", font=("Arial", 18), bg='#FFC0CB')
label.pack(padx=20, pady=40)


def log_cycle_dates():
    start_date = cycle_start_date_entry.get()
    end_date = cycle_end_date_entry.get()
    print("Start Date:", start_date)
    print("End Date:", end_date)
    messagebox.showinfo("Cycle Tracking", "Cycle dates logged successfully")

def log_symptoms():
    selected_symptoms = [symptom for symptom, var in symptom_vars.items() if var.get()]
    print("Selected Symptoms:", selected_symptoms)
    if len(selected_symptoms) > 4:
        messagebox.showwarning("Symptom Tracking", "Please select up to 4 symptoms.")
    else:
        messagebox.showinfo("Symptom Tracking", f"Symptoms logged successfully: {selected_symptoms}")

def on_symptoms_tab_selected(event):
    symptoms_frame.pack(fill='both', expand=True)  # Show only when Symptoms tab is selected

root = tk.Tk()
root.title("Pink App")
root.configure(bg='#FFC0CB')  # Set the background color to pink

label = tk.Label(root, text="Welcome to Flo", font=("Arial", 18), bg='#FFC0CB')
label.pack(padx=20, pady=40)

root.title("Symptom Tracker")
notebook = ttk.Notebook(root)
notebook.pack(fill='both', expand=True)

symptoms_tab = ttk.Frame(notebook)
notebook.add(symptoms_tab, text='Symptoms')

notebook.bind('<<NotebookTabChanged>>', on_symptoms_tab_selected)

style = ttk.Style()
style.configure('Symptoms.TFrame', background='#FFC0CB')

symptoms_frame = ttk.Frame(symptoms_tab, style='Symptoms.TFrame')
symptoms_frame.pack(fill='both', expand=True)

symptoms_list = ["Headache", "Cramps", "Vomiting", "Mood Swings", "Fatigue", "Nausea"]
symptom_vars = {symptom: tk.BooleanVar() for symptom in symptoms_list}

for idx, symptom in enumerate(symptoms_list):
    checkbox = tk.Checkbutton(symptoms_frame, text=symptom, variable=symptom_vars[symptom])
    checkbox.pack(anchor=tk.W)

log_symptoms_btn = tk.Button(symptoms_frame, text="Log Symptoms", command=log_symptoms)
log_symptoms_btn.pack()


def calculate_next_menstruation(current_cycle_end):
    next_menstruation = current_cycle_end + timedelta(days=28)
    return next_menstruation

def submit_data():
    cycle_start_date = cycle_start_date_entry.get_date()
    cycle_end_date = cycle_end_date_entry.get_date()
    symptoms = symptoms_entry.get("1.0", tk.END)

    next_menstruation = calculate_next_menstruation(cycle_end_date)

    confirmation_message = f"Data submitted successfully.\nNext menstruation starts on: {next_menstruation}"
    messagebox.showinfo("Submission", confirmation_message)

# Create main application window
root = tk.Tk()
root.title("Menstrual Cycle Tracking App")

# Create tabs for different functionalities
notebook = ttk.Notebook(root)
notebook.pack(fill='both', expand=True)

cycle_tab = ttk.Frame(notebook)
symptoms_tab = ttk.Frame(notebook)
health_insights_tab = ttk.Frame(notebook)
community_tab = ttk.Frame(notebook)
settings_tab = ttk.Frame(notebook)

notebook.add(cycle_tab, text='Cycle Tracking')
notebook.add(symptoms_tab, text='Symptoms')
notebook.add(health_insights_tab, text='Health Insights')
info_text = """
It Really Is Okay To Skip Your Period: You're not alone if you occasionally use your birth control to avoid your period. And fortunately, it's safe.
The Pill Isn't the Only Option for Heavy Periods: Menstrual Cups and Period Panties Are Eco-Friendly Options.
Your Periods May Be Variable During Perimenopause.
You Can Get Pregnant if You Have Sex During Your Period.
"""

info_label = tk.Label(health_insights_tab, text=info_text, justify=tk.LEFT)
info_label.pack()


notebook.add(community_tab, text='Community')
notebook.add(settings_tab, text='Settings')

# UI elements for Cycle Tracking tab
cycle_start_date_label = tk.Label(cycle_tab, text="Cycle Start Date:")
cycle_start_date_label.grid(row=0, column=0)
cycle_start_date_entry = DateEntry(cycle_tab)
cycle_start_date_entry.grid(row=0, column=1)

cycle_end_date_label = tk.Label(cycle_tab, text="Cycle End Date:")
cycle_end_date_label.grid(row=1, column=0)
cycle_end_date_entry = DateEntry(cycle_tab)
cycle_end_date_entry.grid(row=1, column=1)

log_cycle_dates_btn = tk.Button(cycle_tab, text="Log Cycle Dates", command=log_cycle_dates)
log_cycle_dates_btn.grid(row=2, columnspan=2)


# UI elements and functionality for other tabs can be added similarly

root.mainloop()

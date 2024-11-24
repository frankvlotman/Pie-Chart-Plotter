import tkinter as tk
from tkinter import messagebox
from tkinter import ttk  # Import ttk for themed widgets

from matplotlib import pyplot as plt

def plot_pie_chart():
    try:
        slices = [int(x) for x in slices_entry.get().split(',')]
        labels = labels_entry.get().split(',')
        explode = [float(x) for x in explode_entry.get().split(',')]

        if len(slices) != len(labels) or len(slices) != len(explode):
            raise ValueError("All input lists must have the same length.")

        plt.style.use("fivethirtyeight")
        plt.pie(slices, labels=labels, explode=explode, shadow=True,
                startangle=90, autopct='%1.1f%%',
                wedgeprops={'edgecolor': 'black'})

        plt.title(title_entry.get())
        plt.tight_layout()
        plt.show()
    except Exception as e:
        messagebox.showerror("Input Error", str(e))

def show_info():
    info_window = tk.Toplevel(root)
    info_window.title("Pie Chart Info")
    
    info_text = (
        "Input Instructions:\n\n"
        "- Slices: Enter comma-separated integers representing the "
        "sizes of the slices. These will be converted to percentages automatically.\n\n"
        "- Labels: Enter comma-separated labels corresponding to each slice.\n\n"
        "- Explode: Enter comma-separated float values to offset slices from the center. "
        "Use values like 0.1 or 0.2 for a slight offset. If no offset is desired, "
        "you can use 0 for the slices.\n\n"
        "Example:\n"
        "Slices: 50, 30, 20\n"
        "Labels: A, B, C\n"
        "Explode: 0, 0.1, 0\n"
        "This will create a pie chart with three slices labeled A, B, and C, "
        "with B slightly offset from the center."
    )
    
    tk.Label(info_window, text=info_text, justify=tk.LEFT, padx=10, pady=10).pack()

# Create the main window
root = tk.Tk()
root.title("Pie Chart Input")

# Initialize ttk.Style
style = ttk.Style()
style.theme_use("clam")  # Use 'clam' theme for better customization

# Define custom style for buttons
style.configure("Custom.TButton",
                background="#d0e8f1",
                foreground="black",
                borderwidth=1,
                focusthickness=3,
                focuscolor='none')

# Define style map for hover (active) state
style.map("Custom.TButton",
          background=[('active', '#87CEFA')],
          foreground=[('active', 'black')])

# Slices input
tk.Label(root, text="Slices (comma-separated):").grid(row=0, column=0, padx=10, pady=5, sticky='e')
slices_entry = tk.Entry(root, width=50)
slices_entry.grid(row=0, column=1, padx=10, pady=5)

# Labels input
tk.Label(root, text="Labels (comma-separated):").grid(row=1, column=0, padx=10, pady=5, sticky='e')
labels_entry = tk.Entry(root, width=50)
labels_entry.grid(row=1, column=1, padx=10, pady=5)

# Explode input
tk.Label(root, text="Explode (comma-separated):").grid(row=2, column=0, padx=10, pady=5, sticky='e')
explode_entry = tk.Entry(root, width=50)
explode_entry.grid(row=2, column=1, padx=10, pady=5)

# Title input
tk.Label(root, text="Chart Title:").grid(row=3, column=0, padx=10, pady=5, sticky='e')
title_entry = tk.Entry(root, width=50)
title_entry.grid(row=3, column=1, padx=10, pady=5)

# Plot button
plot_button = ttk.Button(root, text="Plot Pie Chart", command=plot_pie_chart, style="Custom.TButton")
plot_button.grid(row=4, columnspan=2, pady=10)

# Info button
info_button = ttk.Button(root, text="Info", command=show_info, style="Custom.TButton")
info_button.grid(row=5, columnspan=2, pady=10)

# Optional: Adjust padding and alignment for a better layout
for child in root.winfo_children():
    child.grid_configure(padx=5, pady=5)

# Start the GUI loop
root.mainloop()

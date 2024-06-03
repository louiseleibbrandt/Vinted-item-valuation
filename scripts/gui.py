import tkinter as tk
from scraper import scrape_and_calculate


def start_scraping():
    query = entry_query.get()
    condition = condition_var.get()
    output = scrape_and_calculate(query, condition) + "\n"
    result_label.config(text=output)

# Set up the tkinter GUI
root = tk.Tk()
root.title("Vinted Pricer")

# Search query input
tk.Label(root, text="Search Query:").grid(row=0, column=0, padx=10, pady=10)
entry_query = tk.Entry(root, width=50)
entry_query.grid(row=0, column=1, padx=10, pady=10)
entry_query.insert(0, "Gucci Jackie Bag")  # Set the default value

# Condition input
tk.Label(root, text="Condition:").grid(row=1, column=0, padx=10, pady=10)
condition_var = tk.StringVar()
condition_options = ["All", "New with tags", "New without tags", "Very good", "Good", "Satisfactory"]
condition_var.set(condition_options[0])  # Set the default value
condition_menu = tk.OptionMenu(root, condition_var, *condition_options)
condition_menu.grid(row=1, column=1, padx=10, pady=10)

# Start button
start_button = tk.Button(root, text="Start Scraping", command=start_scraping)
start_button.grid(row=2, column=1, padx=10, pady=10)

# Result label
result_label = tk.Label(root, text="", wraplength=400)
result_label.grid(row=3, column=0, columnspan=2, pady=10)

def run():
    root.mainloop()

from datetime import date, datetime
import tkinter as tk
from tkinter import messagebox

def calculate_gap():
    date_format = '%d:%m:%Y'
    try:
        d1 = datetime.strptime(start_entry.get(), date_format)
        d2 = datetime.strptime(end_entry.get(), date_format)

        days = abs((d2 - d1).days)
        years = round(days / 365.25, 1)
        months = round(days / 30.44, 1)
        weeks = round(days / 7, 1)

        result = (
            f"Total Gap: {days} days\n"
            f"Weeks: {weeks}\n"
            f"Months: {months}\n"
            f"Years: {years}"
        )

        messagebox.showinfo("Results", result)

    except ValueError:
        messagebox.showerror("Error", "Use Proper Format: DD:MM:YYYY")

# ---------------- GUI ----------------
root = tk.Tk()
root.title("Days Calculator")
root.geometry("300x200")        # 👈 BOX SIZE HERE
root.resizable(False, False)    # Lock resizing

tk.Label(root, text="StartDate DD:MM:YYYY", font=("Cascadia Code", 10)).pack(pady=5)
start_entry = tk.Entry(root, width=25, font=("Cascadia Code", 9))  # 👈 INPUT BOX SIZE
start_entry.pack(pady=5)

tk.Label(root, text="End Date DD:MM:YYYY", font=("Cascadia Code", 10)).pack(pady=5)
end_entry = tk.Entry(root, width=25, font=("Cascadia Code", 9))    # 👈 INPUT BOX SIZE
end_entry.pack(pady=5)

tk.Button(root, text="Calculate", width=15, command=calculate_gap).pack(pady=15)

root.mainloop()

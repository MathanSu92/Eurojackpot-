import random
import tkinter as tk
from tkinter import ttk

MAIN_NUMBERS = range(1, 51)
EURO_NUMBERS = range(1, 13)

def generate_ticket():
    """Generate one valid Eurojackpot-style ticket: 5 main + 2 Euro numbers."""
    main = sorted(random.sample(MAIN_NUMBERS, 5))
    euro = sorted(random.sample(EURO_NUMBERS, 2))
    return main, euro

def generate():
    main, euro = generate_ticket()
    result_var.set(
        "Hauptzahlen:  " + "  ".join(f"{n:02d}" for n in main) +
        "\nEurozahlen:   " + "  ".join(f"{n:02d}" for n in euro)
    )

root = tk.Tk()
root.title("Eurojackpot Tippgenerator")
root.geometry("440x270")
root.resizable(False, False)

frame = ttk.Frame(root, padding=24)
frame.pack(fill="both", expand=True)

ttk.Label(frame, text="Eurojackpot Tippgenerator",
          font=("Arial", 18, "bold")).pack(pady=(0, 10))
ttk.Label(frame,
          text="Erzeugt zufällige, gültige Tipps. Vergangene Ziehungen\n"
               "können künftige Zahlen nicht vorhersagen.",
          justify="center").pack(pady=(0, 20))

result_var = tk.StringVar(value="Klicke auf „Tipp generieren“")
ttk.Label(frame, textvariable=result_var, font=("Courier New", 14),
          justify="center").pack(pady=12)

ttk.Button(frame, text="Tipp generieren", command=generate).pack(pady=14)
ttk.Label(frame, text="5 aus 50 + 2 aus 12", foreground="gray").pack()

root.mainloop()

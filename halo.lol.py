import tkinter as tk
from tkinter import ttk, messagebox
import itertools
import threading
import time
import random
from playsound import playsound # type: ignore
import os

# Fake mod log window
def log_to_console(text):
    log_box.insert(tk.END, f"{time.strftime('%H:%M:%S')} - {text}\n")
    log_box.see(tk.END)

# RGB animation for title
def animate_title(label):
    colors = itertools.cycle(["red", "orange", "yellow", "lime", "cyan", "magenta"])
    while True:
        color = next(colors)
        try:
            label.config(fg=color)
        except:
            break
        time.sleep(0.2)

# Fake FPS counter
def simulate_fps(label):
    while True:
        fps = random.randint(58, 144)
        try:
            label.config(text=f"{fps} FPS")
        except:
            break
        time.sleep(1)

# Background music
def play_music():
    while True:
        try:
            playsound('music.mp3')
        except:
            break

# Drag window
def start_move(event):
    root.x = event.x
    root.y = event.y

def do_move(event):
    x = event.x_root - root.x
    y = event.y_root - root.y
    root.geometry(f"+{x}+{y}")

def fake_toggle(mod_name):
    messagebox.showinfo("Mod Activated", f"{mod_name} enabled (visual only 😎)")
    log_to_console(f"{mod_name} toggled.")

def fake_setting_change(*args):
    log_to_console(f"Visual setting changed to: {visual_setting.get()}")

# Launch GUI
root = tk.Tk()
root.title("halo.lol")
root.geometry("500x650")
root.configure(bg="#0f0f0f")
root.attributes("-topmost", True)

# Enable drag
root.bind("<Button-1>", start_move)
root.bind("<B1-Motion>", do_move)

# Title
title = tk.Label(root, text="💀 halo.lol 💀", font=("Consolas", 20, "bold"), bg="#0f0f0f")
title.pack(pady=10)

threading.Thread(target=animate_title, args=(title,), daemon=True).start()
threading.Thread(target=play_music, daemon=True).start()

# FPS counter
fps_label = tk.Label(root, text="60 FPS", fg="lime", bg="#0f0f0f", font=("Consolas", 10))
fps_label.place(x=10, y=10)
threading.Thread(target=simulate_fps, args=(fps_label,), daemon=True).start()

# Mod Checkboxes
tk.Label(root, text="MODS", fg="lime", bg="#0f0f0f", font=("Consolas", 14)).pack()

mods = [
    "God Mode",
    "Aimbot Overlay",
    "ESP Boxes",
    "RTX Visuals",
    "Skin Unlocker",
    "V-Bucks Injector",
    "Shader Glow FX"
]

for mod in mods:
    tk.Checkbutton(root, text=f"{mod} (Visual)", bg="#0f0f0f", fg="white",
                   selectcolor="#202020", activebackground="#0f0f0f",
                   font=("Consolas", 10),
                   command=lambda m=mod: fake_toggle(m)).pack(anchor='w', padx=30)

# Settings
tk.Label(root, text="\nVISUAL SETTINGS", fg="cyan", bg="#0f0f0f", font=("Consolas", 14)).pack()
visual_setting = tk.StringVar()
visual_setting.set("Ultra")
ttk.Combobox(root, textvariable=visual_setting,
             values=["Low", "Medium", "High", "Ultra", "RTX ON (Fake)"]
             ).pack()
visual_setting.trace("w", fake_setting_change)

tk.Label(root, text="Shader Intensity:", fg="white", bg="#0f0f0f").pack()
tk.Scale(root, from_=0, to=100, orient="horizontal", bg="#0f0f0f", fg="white",
         troughcolor="#404040", highlightthickness=0).pack()

tk.Button(root, text="Apply Visuals", command=lambda: fake_toggle("All Visual Mods"),
          bg="#00ff88", fg="black", font=("Consolas", 12)).pack(pady=10)

# Console Log
tk.Label(root, text="Mod Console", fg="gray", bg="#0f0f0f", font=("Consolas", 10)).pack()
log_box = tk.Text(root, height=8, bg="#101010", fg="lime", font=("Consolas", 9))
log_box.pack(fill="x", padx=10)

# Footer
tk.Label(root,
         text="⚠️ Visual-only menu. Nothing here is real.\nThis is purely for entertainment (or trolling).",
         fg="gray", bg="#0f0f0f", font=("Arial", 8), wraplength=450, justify="center").pack(pady=5)

root.mainloop()

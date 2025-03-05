import tkinter as tk
import json
import requests

phil_name = ""

def philosopher_name():
  phil_name = entry.get()
  phil_name = phil_name.lower().strip()
  return phil_name

def get_philosopher_death():
  name = philosopher_name()
  with open("philos.json") as f:
    data = json.load(f)
    death_date = data[name]
    label_output.config(text=f"{death_date}")
    entry.delete(0, tk.END)


root = tk.Tk()
root.title("===Philosopher Death Age Finder===")
root.geometry("745x700")

label_prompt = tk.Label(root, text="Enter your philosopher:", font=('Times New Roman',12, 'bold'))
label_prompt.pack()


entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Get Death Date", command=get_philosopher_death)
button.pack()

label_output = tk.Label(root, text=phil_name)
label_output.pack()

root.mainloop()

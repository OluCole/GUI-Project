import tkinter as tk
import json
import requests

phil_name = ""

def philosopher_name():
  phil_name = entry.get()
  phil_name = phil_name.lower().strip().title()
  return phil_name

def get_philosopher_death():
  name = philosopher_name()
  with open("philoso.json") as f:
    data = json.load(f)
    death_date = data[name]
    death_listbox.insert(tk.END, death_date)
    entry.delete(0, tk.END)
    # label_output.config(text=f"{death_date}")


root = tk.Tk()
root.title("            ========Philosopher Death Date Finder========")
root.geometry("745x700")

label_prompt = tk.Label(root, text="Enter your philosopher:", font=('Times New Roman',12, 'bold'))
label_prompt.pack()


entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Get Death Date", command=get_philosopher_death)
button.pack()

# label_output = tk.Label(root, text = phil_name)
# label_output.pack()

death_listbox = tk.Listbox(root, width=50, height=10)
death_listbox.pack()

def add_task():
  task = print(entry.get())
  if task:
    task_listbox.insert(tk.END, task)
    entry.delete(0, tk.END)
    return add_task

# task_listbox = tk.Listbox(root, width=50, height=10)
# task_listbox.pack()

root.mainloop()

import tkinter as tk

def Philosopher_Name():

    name = entry.get()

    label_output.config(text=f"Hello, {name}!")

    label_output.place(x=325, y=300)


root = tk.Tk()

root.title("   =============== Philosopher Death Age Finder =================")

root.geometry("745x700")

label_prompt = tk.Label(root, text="Enter your philosopher:", font=('Times New Roman',12, 'bold'))

label_prompt.place(x=250, y=200)


entry = tk.Entry(root)

entry.place(x=275, y=240)

button = tk.Button(root, text="Greet Me!", command=Philosopher_Name)

button.place(x=315, y=265)

label_output = tk.Label(root, text="")

label_output.pack()

root.mainloop()


# Create the main application window

# root = tk.Tk()

# # Set window title

# root.title("My First Tkinter App")

# # Set window size

# root.geometry("400x300")

# # Run the application

# label = tk.Label(root, text="Hello, Tkinter!")
# label.pack()


# def on_click():

#     print("Button Clicked!")

# button = tk.Button(root, text="Click Me", command=on_click)
# button.pack()
# entry = tk.Entry(root)
# entry.pack()

# root.mainloop()

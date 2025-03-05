import tkinter as tk
import json


def philosopher_name():
    philosopher_name = entry.get().upper().strip().lower
    label_output.config(text=f"It seems they passed {philosopher_name}!")
    label_output.place(x=325, y=380)
    return philosopher_name



    
# def philosopher_deaths(philoso.json):
#     philosopher_deaths = [philoso.json]
#     pass





# with open('philoso.json') as file:
#     data = json.load(file)
#     print (data['philoso.json'])
    
    
    



root = tk.Tk()

root.title("     =============== Philosopher Death Finder =================")

root.geometry("745x700")

label_prompt = tk.Label(root, text="Enter your philosopher:", font=('Times New Roman',12, 'bold'))


label_prompt.place(x=250, y=200)

label_prompt_philo = tk.Label(root, text=" Philosopher's Death Date:", font=('Times New Roman',12, 'bold'))

label_prompt_philo.place(x=235, y=350)

text_box = tk.Text(root, height=5, width=30)


entry = tk.Entry(root)

entry.place(x=270, y=240)

button = tk.Button(root, text="When?", command= "philosopher_name")

button.place(x=315, y=265)

label_output = tk.Label(root, text="")

label_output.pack()

text_box = tk.Text(root, height=5, width=30)
text_box.pack()
text_box.place(x=250, y=380)

root.mainloop()



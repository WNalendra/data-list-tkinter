import tkinter as tk

window = tk.Tk()
window.geometry('500x500')

listvar = []

def sumbitbutton():
    newdata = int(entry_input.get())
    listvar.append(newdata)
    list_txt.configure(text=f"Data Number:\n{listvar}")
    print(listvar)
def averagebutton():
    average = sum(listvar)/len(listvar)
    data_output.configure(text=f"average number: {average}")

Label_header = tk.Label(text="DATA LIST", font=('Arial', 24))
Label_header.pack()

text_label = tk.Label(text="Input Data :")
text_label.pack(pady=10)

entry_input = tk.Entry(width=30)
entry_input.pack()

submit_button = tk.Button(text="Submit", width=25,command=sumbitbutton)
submit_button.pack(pady=5)

list_txt = tk.Message(text="")
list_txt.pack(pady=12)

average_button = tk.Button(text="Average",command=averagebutton)
average_button.pack()

data_output = tk.Label(text="-[Output]-")
data_output.place(x=1,y=400)


window.mainloop()
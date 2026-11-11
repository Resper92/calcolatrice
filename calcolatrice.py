import tkinter as tk

box = tk.Tk()
box.title("Calculator")

display = tk.Entry(
    box,
    width=20,
    borderwidth=10
)
# Occupa 4 colonne (columnspan=4) per coprire tutti i bottoni
display.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky="we")

def print_key(valore):
    if valore == "c" :
        display.delete(0, tk.END)
    elif valore == "=":
        try:
            expression = display.get()
            result = eval(expression)
            display.delete(0, tk.END)
            display.insert(tk.END, result)
        except Exception as e:
            display.delete(0, tk.END)
            display.insert(tk.END, "Error")
    else:
        display.insert(tk.END, valore)

bottoni= [["c","%","(",")"],
    ["7","8","9","/"],
    ["4","5","6","*"],
    ["1","2","3","-"],
    [".","0","=","+"]
    ]
for riga, riga_bottoni in enumerate(bottoni):
    for colonna,testo in enumerate(riga_bottoni):
        btn=tk.Button(box,text=testo,width=5,height=2,command=lambda testo=testo: print_key(testo))
        btn.grid(row=riga +1,column=colonna)
        
        

        
if __name__ == "__main__":
    box.mainloop()
from tkinter import *
from tkinter import ttk

#create the window
root = Tk()

#example text i chanchet with function 
texts = ["Be","the","change","that","you","wish","to","see","in","the","world","."]
translate = ["Бъди", "за", "промяната", "която", "ти", "искаш", "да", "видиш", "в", "за", "свeта", "."]

textsbg = ["Бъди","промяната",",","която","искаш","да","видиш","в","света","."]

#modify root window
root.title("Multy Line Translete")
root.geometry("600x100")

master =  ttk.Entry(root)
master.grid()

#class row:
    
class tape:
    def __init__(self,first_row,sorce):
        self.widget = ttk.Frame(master, padding="3 3 12 12")
        self.widget.grid(column=0, row=0+first_row, sticky=(N, W, E, S))
        self.widget.columnconfigure(0, weight=1)
        self.widget.rowconfigure(0, weight=1)

        self.WordBoxes = [[],[],[]]
        for i in range(len(texts)):
            self.WordBoxes[0].append(ttk.Label(self.widget, text = sorce[i]).grid(column = i, row = 0+first_row, sticky = W))
            self.WordBoxes[1].append(ttk.Label(self.widget, text = translate[i]).grid(column = i, row = 1+first_row, sticky = W))
            
english = tape(0,texts)
bulgarian = tape(2,textsbg)


#for child in app.winfo_children(): child.grid_configure(padx=5, pady=5)

#kick off the event loop
root.mainloop()

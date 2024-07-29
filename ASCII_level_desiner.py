 ### main window is canvas
### left panel
###     -tools
###     -Tool options
### bottom left 
###       -Character/Tile
### Right Panel
###     - Meta Data of tile
###     - list of levels

import tkinter as tk 
import ttkbootstrap as ttk

def Button_Response(text: str = "None"):
    print(text)

def ToolSelect(master):
    tool_selected = tk.StringVar()
    
    colision = ttk.Radiobutton(master=master,text="Colision", value="COL", variable=tool_selected, command= lambda: Button_Response("colision"))
    colision.pack(anchor="w",side="top")
    
    containers = ttk.Radiobutton(master=master,text="Container", value="CON", variable=tool_selected,command= lambda: Button_Response("containers"))
    containers.pack(anchor="w",side="top")
    
    portals = ttk.Radiobutton(master=master,text="Portals", value="PRl", variable=tool_selected, command= lambda: Button_Response("portals"))
    portals.pack(anchor="w",side="top")
    
    entities = ttk.Radiobutton(master=master,text="Entities", value="ENT", variable=tool_selected, command= lambda: Button_Response("entities"))
    entities.pack(anchor="w",side="top")
    
    player = ttk.Radiobutton(master=master,text="Player", value="PYR", variable=tool_selected, command= lambda: Button_Response("player"))
    player.pack(anchor="w",side="top")
    
    items = ttk.Radiobutton(master=master, text="Items", value="ITM", variable=tool_selected, command= lambda: Button_Response("items"))
    items.pack(anchor="w",side="top")

    


def Main():
    win_width = 800
    win_height = 650

    #initTo create radio buttons, you use the Radiobutton widget. The following shows how to create radio buttons using the tk.Radiobutton constructor:

    root_win = tk.Tk()
    root_win.title("Level Desiner")
    root_win.geometry((str(win_width) +"x" +str(win_height)))
    
    left_panel = tk.Frame(root_win, padx= 10,pady=5, width=100,borderwidth=2,relief="ridge", bg="#d2dde0")

    left_panel.pack(side="left",anchor="nw",fill='y',expand=1)
    ToolSelect(left_panel)
    root_win.mainloop()


if __name__ == "__main__":
    Main()

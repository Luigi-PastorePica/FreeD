# Tk root / app bootstrap.
import tkinter as tk

BASE_WIDTH = 800
BASE_HEIGHT = 600
ASPECT_RATIO = BASE_WIDTH / BASE_HEIGHT

def maintain_aspect_ratio(event):
    if event.widget.master is not None:
        return

    new_width = event.width
    desired_height = int(new_width / ASPECT_RATIO)

    if abs(event.width - new_width) > 1 or abs(event.height - desired_height) > 1:
        event.widget.geometry(f"{new_width}x{desired_height}")
        return "break"

window = tk.Tk()
window.title("FreeD")
window.update_idletasks() # Awaits for geometry manager to finish rendering the window.
window.geometry(f"{BASE_WIDTH}x{BASE_HEIGHT}")
window.bind("<Configure>", maintain_aspect_ratio)
window.rowconfigure(0, weight=1)
window.columnconfigure([0], weight=1, minsize=BASE_WIDTH*0.75)
window.columnconfigure([1], weight=0, minsize=BASE_WIDTH*0.25)

# Graph container
graph_frame = tk.Frame(master=window, width=BASE_WIDTH * 0.75, height=BASE_HEIGHT, bd=2, relief="sunken")
graph_frame.grid(row=0, column=0, sticky="nsew")

# Input container
input_frame = tk.Frame(master=window, width=BASE_WIDTH*0.5, height=BASE_HEIGHT*0.9)
input_frame.grid(row=0, column=1, sticky="ns")
input_frame.columnconfigure([0,1], weight=1, minsize=BASE_WIDTH*0.20)
input_frame.rowconfigure([0,1,2], weight=1, minsize=BASE_HEIGHT*0.30)

frame_current_debt = tk.Frame(master=input_frame)
frame_current_debt.grid(row=0, column=0, sticky="ew")
lbl_current_debt = tk.Label(master=frame_current_debt, text="Current Debt")
lbl_current_debt.grid(row=0, column=0, sticky="w")
ent_current_debt = tk.Entry(master=frame_current_debt)
ent_current_debt.grid(row=1, column=0, sticky="ew")

frame_principal = tk.Frame(master=input_frame)
frame_principal.grid(row=1, column=0, sticky="ew")
lbl_principal = tk.Label(master=frame_principal, text="Principal")
lbl_principal.grid(row=0, column=0, sticky="w")
ent_principal = tk.Entry(master=frame_principal)
ent_principal.grid(row=1, column=0, sticky="ew")

frame_apr = tk.Frame(master=input_frame)
frame_apr.grid(row=2, column=0, sticky="ew")
lbl_apr = tk.Label(master=frame_apr, text="APR")
lbl_apr.grid(row=0, column=0, sticky="w")
ent_apr = tk.Entry(master=frame_apr)
ent_apr.grid(row=1, column=0, sticky="ew")

window.mainloop()

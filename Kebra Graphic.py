import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *
from tkinter import filedialog
import numpy as np

resX = []
resY = []

def new_file():
	inp.delete(0, 'end')
	a.clear()
	canvas.draw()

def save_file():
	try:
		filename = filedialog.asksaveasfilename(defaultextension=".png")
		f.savefig(filename)
	except:
		pass

def close():
	root.destroy()

def update():
	global resX, resY
	inpWords = inp.get().split(" ")

	if inpWords[0] == "plot":
		autolbl.config(text="[plot] <y1>,<y2>,...")
		del inpWords[0]
		a.clear()
		try:
			a.plot(eval(inpWords[0]), marker='o')
			canvas.draw()
		except:
			pass
	elif inpWords[0] == "sin":
		autolbl.config(text="[sin] <start x> <end x> <number of points>")
		del inpWords[0]
		a.clear()
		try:
			xs = np.linspace(float(inpWords[0]), float(inpWords[1]), int(inpWords[2]))
			ys = np.sin(xs)
			a.plot(xs, ys)
			canvas.draw()
		except:
			pass
	elif inpWords[0] == "cos":
		autolbl.config(text="[cos] <start x> <end x> <number of points>")
		del inpWords[0]
		a.clear()
		try:
			xs = np.linspace(float(inpWords[0]), float(inpWords[1]), int(inpWords[2]))
			ys = np.cos(xs)
			a.plot(xs, ys)
			canvas.draw()
		except:
			pass
	elif inpWords[0] == "f(x)":
		autolbl.config(text="[f(x)] <equation> <start x> <end x>")
		del inpWords[0]
		a.clear()
		resX = []
		resY = []
		try:
			for i in range(int(inpWords[1]), int(inpWords[2]) + 1):
				resX.append(i)
				resY.append(float(eval(inpWords[0].replace("x", str(i)))))
			a.plot(resX, resY)
			canvas.draw()
		except:
			pass
	else:
		autolbl.config(text="[plot] [sin] [cos] [f(x)]")
		a.clear()
		canvas.draw()
	root.after(1000, update)

def add_previous(event):
	if inp.get().lower().islower():
		previous.insert(END, inp.get())
		inp.select_range(0, 'end')

def get_previous(event):
	try:
		inp.delete(0, 'end')
		widget = event.widget
		selection = widget.curselection()
		value = widget.get(selection[0])
		inp.insert(0, value)
	except:
		pass

root = Tk()
root.title("Kebra <Graphic>")
root.geometry("900x700")
root.minsize(900, 700)
root.iconbitmap('Data/Graphiclogo.ico')

menubar = Menu(root)
root.config(menu=menubar)
submenu1 = Menu(menubar,tearoff=0)

menubar.add_cascade(label="File", menu=submenu1)
submenu1.add_command(label="New", command=new_file)
submenu1.add_command(label="Save", command=save_file)
submenu1.add_separator()
submenu1.add_command(label="Exit", command=close)

f = Figure(figsize=(5, 5), dpi=100)
a = f.add_subplot(111)
a.plot(resX)
a.set_facecolor("#2e2e2e")

f.patch.set_facecolor('#1e1e1e')
COLOR = 'white'
plt.rcParams['text.color'] = COLOR
plt.rcParams['axes.labelcolor'] = COLOR
plt.rcParams['xtick.color'] = COLOR
plt.rcParams['ytick.color'] = COLOR

inp = Entry(root, font=('Consolas', 14), bg="#2e2e2e", fg="white", insertbackground='white', bd=0)
inp.pack(side=BOTTOM, fill=BOTH)

inp.bind("<Return>", add_previous)

autolbl = Label(root, bg="#1e1e1e", font=('Consolas', 12), fg="white", text="[plot] [sin] [cos] [f(x)]")
autolbl.pack(side=BOTTOM, fill=BOTH)

fra = Frame(root, highlightbackground="#646464", highlightthickness=2)
fra.pack(side=LEFT, fill=Y)

previous = Listbox(fra, borderwidth=0, highlightthickness=0, activestyle="none", bg="#1e1e1e", fg="white", font=('Consolas', 12))
previous.pack(side=LEFT, fill=Y)

previous.bind("<Double-Button-1>", get_previous)

canvas = FigureCanvasTkAgg(f, master=root)
canvas.draw()
canvas.get_tk_widget().pack(fill=BOTH, expand=True)

update()

root.mainloop()
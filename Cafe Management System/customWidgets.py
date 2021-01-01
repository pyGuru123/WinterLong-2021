import tkinter as tk

class CustomFrame(tk.LabelFrame):
	def __init__(self, parent, **kwargs):
		tk.LabelFrame.__init__(self, parent, **kwargs)

		width = kwargs.get('width', 10)
		height = kwargs.get('height', 10)
		bg = kwargs.get('bg', 'white')
		fg = kwargs.get('fg', "#248aa2")
		bd = kwargs.get('borderwidth', "3")
		self.configure(width=width, height=height, font=('verdana',10,'bold'),
			borderwidth=bd, relief=tk.RIDGE, highlightthickness=4, bg=bg, fg=fg,
			highlightcolor="white", highlightbackground="white")

class CustomLabel(tk.Label):
	def __init__(self, parent, **kwargs):
		tk.Label.__init__(self, parent, **kwargs)

		width = kwargs.get('width', 10)
		bg = kwargs.get('bg', 'white')
		fg = kwargs.get('fg', 'black')
		self.configure(width=width, bg=bg, fg=fg, anchor='w',
						font=('Verdana', 10, 'bold'))
class CustomEntry(tk.Entry):
	def __init__(self, parent, **kwargs):
		tk.Entry.__init__(self, parent, **kwargs)

		width = kwargs.get('width', 8)
		self.configure(width=width,borderwidth=2,relief=tk.SUNKEN,bg="#248aa2",
					fg='white')

class CustomButton(tk.Button):
	def __init__(self, parent, **kwargs):
		tk.Button.__init__(self, parent, **kwargs)

		self.configure(width=7, borderwidth=2, font=('Arial',8, 'bold'),
			bg='#248aa2', fg="white", relief=tk.RAISED)

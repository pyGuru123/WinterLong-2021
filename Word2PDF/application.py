import os
import time
import threading
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import PhotoImage
from tkinter import filedialog
from tkinter import messagebox

# python -m pip install pywin32
import win32com.client

cwd = os.getcwd()

class Application(tk.Frame):
	def __init__(self, master=None):
		super().__init__(master=master)
		self.master = master
		self.grid()

		self.draw_title_frame()
		self.draw_body_frame()

		self.filepath = ''
		self.isFileSelected = False

	def draw_title_frame(self):
		self.title_frame = tk.Frame(self, width=400, height=50, bg='#E8175D')
		self.title_frame.grid(row=0, column=0)
		self.title_frame.grid_propagate(False)

		self.title = tk.Label(self.title_frame, width=24, height=1, bg='white',
				text='Document Converter',font=('verdana',18,'bold'),
				fg='#E8175D')
		self.title.grid(row=0, column=0, ipady=4)

#45ADA8
	def draw_body_frame(self):
		self.body_frame = tk.Frame(self, width=400, height=250, bg='#363636')
		self.body_frame.grid(row=1, column=0)
		self.body_frame.grid_propagate(False)

		self.w2p = tk.Button(self.body_frame, width=140, height=140,
					relief=tk.RAISED, image=image1, cursor = 'hand2',
					command=lambda : self.conversion_widgets(word2pdf=True)) 
		self.p2w = tk.Button(self.body_frame, width=140, height=140,
					relief=tk.RAISED, image=image2, cursor = 'hand2',
					command=lambda : self.conversion_widgets(word2pdf=False))

		self.w2p.grid(row=0, column=1, pady=(50,45), padx=(10,0))
		self.p2w.grid(row=0, column=2, pady=(50,45), padx=(10,0))

		self.lbl = tk.Label(self.body_frame, width=58, height=2, bg='#E8175D')
		self.lbl.grid(row=1, column=0, columnspan=4)

	def draw_converter_frame(self):
		for widget in self.body_frame.winfo_children():
			widget.destroy()
		self.body_frame.destroy()

		self.cvt_frame = tk.Frame(self, width=400, height=250, bg='#363636')
		self.cvt_frame.grid(row=1, column=0)
		self.cvt_frame.grid_propagate(False)

		self.top_frame = tk.Frame(self.cvt_frame, width=400, height=200, bg='#363636')
		self.top_frame.grid(row=0, column=0)
		self.top_frame.grid_propagate(False)

		self.bottom_frame = tk.Frame(self.cvt_frame, width=400, height=50, bg='#E8175D')
		self.bottom_frame.grid(row=1, column=0)
		self.bottom_frame.grid_propagate(False)

	def conversion_widgets(self, word2pdf=False):
		self.draw_converter_frame()

		# Top Frame Widgets
		if word2pdf:
			lbl_text = 'Convert Word 2 PDF'  
			select_lbl_text = 'Select a Word file'
			convert_btn_command = lambda : self.start_process(toPDF=True)
			select_file_command = lambda : self.select_file(selectPDF=False)
		else:
			lbl_text = 'Convert PDF 2 Word'
			select_lbl_text = 'Select a PDF file'
			convert_btn_command = lambda : self.start_process(toPDF=False)
			select_file_command = lambda : self.select_file(selectPDF=True)

		self.lbl = tk.Label(self.top_frame, text=lbl_text, bg='red',
					fg='white', font=('verdana', 12, 'bold'), width=20)
		self.lbl.grid(row=0, column=1, padx=10, columnspan=3, pady=10)
  
		self.select_lbl = tk.Label(self.top_frame, text=select_lbl_text,
						bg='#363636', fg='white', font=('verdana', 10))
		self.select_lbl.grid(row=1, column=0, columnspan=2, padx=15)

		self.select_button = tk.Button(self.top_frame, image = attach_icon,
					bg='#363636', relief=tk.FLAT, cursor='hand2',
					command=select_file_command)
		self.select_button.grid(row=1, column=3, padx=(20,0))

		self.abstract = tk.Label(self.top_frame, image=image3, bg='#363636')
		self.abstract.grid(row=1, column=4, rowspan=3)

		self.filepath_specifier = tk.Label(self.top_frame, width=30, height=3,
					bg='#363636', wraplength=180, fg='white',
					font=('verdana', 8))
		self.filepath_specifier.grid(row=3, column=0, columnspan=4)


		# Bottom Frame Widgets
		self.convert_btn = ttk.Button(self.bottom_frame, text='Convert', 
					command = convert_btn_command, cursor='hand2')
		self.convert_btn.grid(row=0, column=0, padx=25, pady=10)

		self.back_btn = ttk.Button(self.bottom_frame, text='Home',
					command=self.go_to_home, cursor='hand2')
		self.back_btn.grid(row=0, column=1, padx=180, pady=10)

		if self.filepath:
			self.convert_btn.config(state=tk.NORMAL)
		else:
			self.convert_btn.config(state=tk.DISABLED)

	def go_to_home(self):
		self.cvt_frame.destroy()
		self.filepath = ''
		self.draw_body_frame()

	def select_file(self, selectPDF=True):
		if selectPDF:
			filetypes = (("PDF","*.pdf"),)
		else:
			filetypes = (("Word","*.doc"),("Word","*.docx"),)

		path = filedialog.askopenfilename(initialdir=cwd, filetypes=filetypes)
		if path:
			self.filepath = path
			self.convert_btn.config(state=tk.NORMAL)
			self.filepath_specifier['text'] = self.filepath

	def start_process(self, toPDF=False):
		self.convert_btn.config(state=tk.DISABLED)
		self.back_btn.config(state=tk.DISABLED)

		if toPDF:
			target = self.convert_to_pdf
		else:
			target = self.convert_to_word
		thread = threading.Thread(target=target)
		thread.start()
		self.pool_thread(thread)

	def pool_thread(self, thread):
		if thread.is_alive():
			self.after(100, lambda : self.pool_thread(thread))
		else:
			self.convert_btn.config(state=tk.NORMAL)
			self.back_btn.config(state=tk.NORMAL)

	def convert_to_pdf(self):
		path = filedialog.asksaveasfilename(initialdir=cwd, 
				filetypes=(("PDF","*.pdf"),))
		if path:
			word = win32com.client.Dispatch("Word.Application")
			word.visible = False

			file = os.path.normpath(self.filepath)
			path = os.path.normpath(path)
			doc = word.Documents.Open(file)
			doc.SaveAs2(path, FileFormat=17)
			doc.Close()
			word.Quit()
			messagebox.showinfo('DocConverter', 'File Conversion Completed')

	def convert_to_word(self):
		path = filedialog.asksaveasfilename(initialdir=cwd, 
				filetypes=(("Word","*.doc"),("Word","*.docx"),))
		if path:
			word = win32com.client.Dispatch("Word.Application")
			word.visible = False

			file = os.path.normpath(self.filepath)
			doc = word.Documents.Open(file)
			doc.SaveAs2(path, FileFormat=16)
			doc.Close()
			word.Quit()
			messagebox.showinfo('DocConverter', 'File Conversion Completed')

if __name__ == '__main__':
	root = tk.Tk()
	root.geometry('400x300+400+220')
	root.title('Word 2 PDF')
	root.resizable(0,0)

	image1 = PhotoImage(file='images/image1.png')
	image2 = PhotoImage(file='images/image2.png')
	image3 = PhotoImage(file='images/image3.png')

	attach_icon = PhotoImage(file='icons/attach.png')

	app = Application(master=root)
	app.mainloop()
import os
import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
import datetime

from customWidgets import CustomLabel, CustomFrame, CustomEntry, CustomButton

if not os.path.exists('receipts/'):
	os.mkdir('receipts/')
	with open('receipts/orders.txt', 'w') as file:
		file.write('OrderN12121')

class Application(tk.Frame):
	def __init__(self, master=None):
		super().__init__(master=master)
		self.master = master
		self.grid()

		self.draw_frames()
		self.draw_title_widgets()
		self.draw_body_widgets()

		self.itemCost = {
			'Tea' : 10,
			'Coffee' : 15,
			'Pastery' : 80,
			'Pizza' : 199,
			'Fries' : 60,
			'Burger' : 49,
			'Pepsi' : 14,
			'Cookies' : 4
		}

		self.discount_dict = {
		0:0, 100 : 1, 300 : 2, 500 : 3, 1000 : 5, 2000 : 8, 5000 : 15
		}

		self.itemList = [item for item in self.itemCost.keys()]
		self.entryValues = [tk.StringVar() for item in self.itemList]
		self.expression = ''


		self.draw_item_frame_widgets()
		self.draw_bill_frame_widgets()
		self.draw_controller_frame_widgets()
		self.draw_calculator_frame_widgets()

	def draw_frames(self):
		self.title_frame = tk.Frame(self, width=800, height=105, bg='white')
		self.main_frame = tk.LabelFrame(self, width=800, height=280, bg='white')

		self.title_frame.grid(row=0, column=0)
		self.main_frame.grid(row=1, column=0, pady=5)

		self.title_frame.grid_propagate(False)
		self.main_frame.grid_propagate(False)

	def draw_title_widgets(self):
		self.icon = tk.Label(self.title_frame, image=coffee_icon1, bg='white')
		self.icon.grid(row=0, column=0, rowspan=2, padx=(10,3))

		self.title = tk.Label(self.title_frame, width=24, height=2,
					text='Honest Bistro Cafe', font=('verdana',22,'bold'), fg="#248aa2", bg="white")
		self.title.grid(row=0, column=1, columnspan=3)

		self.l1 = tk.Label(self.title_frame, bg='#248aa2', width=25)
		self.l2 = tk.Label(self.title_frame, bg='#248aa2', width=5)
		self.l1.grid(row=1, column=1)
		self.l2.grid(row=1, column=3)

		self.date_time = tk.Label(self.title_frame, text=self.get_current_datetime(),
					fg='#fe4a49', font=('verdana', 12, 'bold'))
		self.date_time.after(1000, self.update_datetime_label)
		self.date_time.grid(row=1, column=2, padx=5)

	def draw_body_widgets(self):
		self.items_frame = CustomFrame(self.main_frame, text='Cafe Items', height=240, width=170)
		self.items_frame.grid(row=0, column=0, padx=(15,10), pady=15, rowspan=2, sticky='NW')

		self.bill_frame = CustomFrame(self.main_frame, text='Items Bill', height=200, width=192)
		self.bill_frame.grid(row=0, column=1, padx=10, pady=(15,0))

		self.controller = CustomFrame(self.main_frame, width=192, height=30, borderwidth=0)
		self.controller.grid(row=1, column=1, padx=10, sticky='N')

		self.calculator = CustomFrame(self.main_frame, text='Calculator', height=200, width=168)
		self.calculator.grid(row=0, column=2, padx=5, pady=15, sticky='NW')

		self.contact = CustomFrame(self.main_frame, width=192, height=30, borderwidth=0)
		self.contact.grid(row=1, column=2, padx=10, sticky='N')

		l1 = tk.Label(self.contact, bg='#248aa2', width=25, height=2,
				 text='    Opens 09:00 to 08:30 \n   Contact : 876655444',
				font=('Verdana', 8, 'bold'), fg='white', anchor='w')
		l1.grid(row=0, column=0)

		self.items_frame.grid_propagate(False)
		self.bill_frame.grid_propagate(False)
		self.controller.grid_propagate(False)
		self.calculator.grid_propagate(False)

	def draw_item_frame_widgets(self):
		for row, item in enumerate(self.itemList):			
			label = CustomLabel(self.items_frame, text=(' ' + item))
			label.grid(row=row, column=0, pady=(4,0))

			entry = CustomEntry(self.items_frame, textvariable=self.entryValues[row])
			entry.grid(row=row, column=1, pady=(4,0))

	def draw_bill_frame_widgets(self):
		self.chargeList = ['Items Cost', 'Service Charge', 'GST Charges','Discount', 'Total']
		self.chargeValues = [tk.StringVar() for item in self.chargeList]

		for row, item in enumerate(self.chargeList):			
			label = CustomLabel(self.bill_frame, text=item, width=12)
			label.grid(row=row, column=0, pady=(3,0))

			entry = CustomEntry(self.bill_frame, textvariable=self.chargeValues[row])
			entry.grid(row=row, column=1, pady=(3,0))

		self.name_frame = tk.LabelFrame(self.bill_frame)
		self.name_frame.grid(row=5, column=0, columnspan=2, pady=(15,0), padx=3)

		self.customer_name = tk.StringVar()
		self.name = CustomLabel(self.name_frame, text='Name', width=7)
		self.name_entry = CustomEntry(self.name_frame, width=15, textvariable=self.customer_name)
		self.name.grid(row=0, column=0, pady=2, padx=1)
		self.name_entry.grid(row=0, column=1, pady=2, padx=1)

	def draw_controller_frame_widgets(self):
		self.total = CustomButton(self.controller, text='Calculate',
					command=self.calculate_payment)
		self.total.grid(row=0, column=0, padx=(2,0))

		self.clear = CustomButton(self.controller, text='Clear', command=self.clear_all)
		self.clear.grid(row=0, column=1, padx=(2,0))

		self.receipt = CustomButton(self.controller, text='Receipt', command=self.get_receipt)
		self.receipt.grid(row=0, column=2, padx=(2,0))

	def draw_calculator_frame_widgets(self):
		self.input_string = tk.StringVar()
		self.calc_entry = CustomEntry(self.calculator, width=23, textvariable=self.input_string)
		self.calc_entry.grid(row=0, column=0, columnspan=4, pady=(5,3), padx=4)

		self.seven = self.create_button(self.calculator, '7', '#248aa2', "white",
					lambda : self.get('7'), 1, 0)
		self.eight = self.create_button(self.calculator, '8', '#248aa2', "white",
					lambda : self.get('8'), 1, 1)
		self.nine = self.create_button(self.calculator, '9', '#248aa2', "white",
					lambda : self.get('9'), 1, 2)
		self.plus = self.create_button(self.calculator, '+', 'white', "black",
					lambda : self.get('+'), 1, 3)
		self.four = self.create_button(self.calculator, '4', '#248aa2', "white",
					lambda : self.get('4'), 2, 0)
		self.five = self.create_button(self.calculator, '5', '#248aa2', "white",
					lambda : self.get('5'), 2, 1)
		self.six = self.create_button(self.calculator, '6', '#248aa2', "white",
					lambda : self.get('6'), 2, 2)
		self.minus = self.create_button(self.calculator, '-', 'white', "black",
					lambda : self.get('-'), 2, 3)
		self.one = self.create_button(self.calculator, '1', '#248aa2', "white",
					lambda : self.get('1'), 3, 0)
		self.two = self.create_button(self.calculator, '2', '#248aa2', "white",
					lambda : self.get('2'), 3, 1)
		self.three = self.create_button(self.calculator, '3', '#248aa2', "white",
					lambda : self.get('3'), 3, 2)
		self.mult = self.create_button(self.calculator, '*', 'white', "black",
					lambda : self.get('*'), 3, 3)
		self.clear = self.create_button(self.calculator, 'C', '#248aa2', "white",
					self.delete_calc_text, 4, 0)
		self.zero = self.create_button(self.calculator, '0', '#248aa2', "white",
					lambda : self.get('0'), 4, 1)
		self.equal = self.create_button(self.calculator, '=', '#248aa2', "white",
					self.evaluate_expression, 4, 2)
		self.div = self.create_button(self.calculator, '/', 'white', "black",
					lambda : self.get('/'), 4, 3)

	def create_button(self, parent, text, bg, fg, command, r, c):
		self.button = tk.Button(parent, bg=bg, fg=fg, font=('Arial',10, 'bold'))
		self.button['text'] = text
		self.button['command'] = command
		self.button.config(height=1, width=3)
		self.button.grid(row=r, column=c, pady=4)

		return self.button

	def get(self, value):
		ops = ['+', '-', '*', '/']

		if self.expression == 'error':
			self.expression = ''

		if len(self.expression) == 0:
			if value in ['+', '-']:
				self.expression += value
			elif value in ['*', '/']:
				pass
			else:
				self.expression += value
		elif len(self.expression) > 0:
			if value in ops and self.expression[-1] in ops:
				self.expression = self.expression[:-1] + value
			else:
				self.expression += value

		self.input_string.set(self.expression)

	def evaluate_expression(self):
		if len(self.expression) > 0:
			try:
				self.expression = str(round(eval(self.expression), 2))
			except:
				self.expression = 'error'

			self.input_string.set(self.expression)

	def delete_calc_text(self):
		self.expression = ''
		self.calc_entry.delete(0,'end')

	def get_current_datetime(self):
		dt = datetime.datetime.now()
		return dt.strftime('%b %d ,%Y   %I:%M:%S %p')

	def update_datetime_label(self):
		dt = self.get_current_datetime()
		self.date_time['text'] = dt
		self.date_time.after(1000, self.update_datetime_label)

	def get_order_details(self):
		total_cost = 0

		for index, item in enumerate(self.itemList):
			qty = self.entryValues[index].get()
			if qty:
				self.hasBought = True
				cost = int(qty) * self.itemCost[item]
				total_cost += cost

		if self.hasBought:
			service_charge = round(0.04 * total_cost, 2)
			gst = round(0.05 * total_cost, 2)

			total = total_cost + service_charge + gst
			disc = 0
			for d in self.discount_dict.keys():
				if total >= d:
					disc = d

			cut = self.discount_dict[disc]
			discount = round((cut / 100) * total_cost, 2)
			total = round(total - discount, 2)
		else:
			total_cost, service_charge, gst, discount, total = [0 for i in range(5)]

		return total_cost, service_charge, gst, discount, total

	def calculate_payment(self):
		self.hasBought = False
		total_cost, service_charge, gst, discount, total = self.get_order_details()
		 
		if self.hasBought:
			self.chargeValues[0].set(str(total_cost))
			self.chargeValues[1].set(str(service_charge))
			self.chargeValues[2].set(str(gst))
			self.chargeValues[3].set(str(discount))
			self.chargeValues[4].set(str(total))

	def get_receipt(self):
		if self.chargeValues[4].get() != '':
			total_cost, service_charge, gst, discount, total = [self.chargeValues[i].get()
															for i in range(5)]
			name = self.customer_name.get()
			if name:
				current = self.make_entry()
				with open(f'receipts/order_receipt_{current}.txt', 'w') as file:
					file.write('Order Summary\n')
					file.write(f'Customer Name : {name}\n')
					file.write(f'Order date time : {self.get_current_datetime()}\n\n')
					i, q, p, t = 'item', 'quantity', 'price', 'total cost'
					file.write(f' {i:<12} | {q:<8} | {p:<8} | {t:<12}\n')
					for index, item in enumerate(self.itemList):
						qty = self.entryValues[index].get()
						if qty:
							self.hasBought = True
							c = self.itemCost[item]
							cost = int(qty) * c

							file.write(f' {item.lower():<12}| {qty:<8} | {c:<8} | {cost:<12}\n')

					file.write('\n')
					file.write(f'SubCost : {total_cost}\n')
					file.write(f'Service Charge : {service_charge}\n')
					file.write(f'GST : {gst}\n')
					file.write(f'Discount : {discount}\n')
					file.write(f'Total Cost : {total}\n')

				messagebox.showinfo('Honest Bistro', 'Receipt Generated')
			else:
				messagebox.showerror('Honest Bistro', 'Customer Name is required.')
		else:
			messagebox.showerror('Honest Bistro', 'No items Bought')

	def make_entry(self):
		with open('receipts/orders.txt') as file:
			current = file.readline()

		current = int(current[6:]) + 1
		with open('receipts/orders.txt', 'w') as file:
			file.write(('OrderN'+str(current)))

		return current

	def clear_all(self):
		for index, item in enumerate(self.itemList):
			self.entryValues[index].set('')

		for index, item in enumerate(self.chargeList):
			self.chargeValues[index].set('')

		self.customer_name.set('')
		self.hasBought = False

if __name__ == '__main__':
	root = tk.Tk()
	root.geometry('600x390')
	root.title('Honest Bistro')
	root.resizable(0,0)

	coffee_icon1 = PhotoImage(file='icons/coffee.png')

	app = Application(master=root)
	app.mainloop()
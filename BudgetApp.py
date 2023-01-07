import tkinter as tk

# Initialize variables for income, expenses, and savings
income = 0
expenses = 0
savings = 0

# Function to add income
def add_income(amount):
  global income
  income += amount

# Function to add expenses
def add_expense(amount):
  global expenses
  expenses += amount

# Function to calculate savings
def calculate_savings():
  global income, expenses, savings
  savings = income - expenses

# Function to display budget summary
def display_budget():
  global income, expenses, savings
  budget_text.config(state="normal")
  budget_text.delete("1.0", "end")
  budget_text.insert("end", "Income: $" + str(income) + "\n")
  budget_text.insert("end", "Expenses: $" + str(expenses) + "\n")
  budget_text.insert("end", "Savings: $" + str(savings) + "\n")
  budget_text.config(state="disabled")

# Function to handle button clicks
def button_click(event):
  global income_input, expenses_input
  income_amount = income_input.get()
  expenses_amount = expenses_input.get()
  if income_amount:
    add_income(int(income_amount))
  if expenses_amount:
    add_expense(int(expenses_amount))
  calculate_savings()
  display_budget()

# Create main window
window = tk.Tk()
window.title("Budget Calculator")

# Create widgets
income_label = tk.Label(window, text="Income:")
income_input = tk.Entry(window)
expenses_label = tk.Label(window, text="Expenses:")
expenses_input = tk.Entry(window)
add_button = tk.Button(window, text="Add")
budget_text = tk.Text(window, state="disabled", width=30, height=10)

# Add button click event
add_button.bind("<Button-1>", button_click)

# Add widgets to window
income_label.pack()
income_input.pack()
expenses_label.pack()
expenses_input.pack()
add_button.pack()
budget_text.pack()

# Run the main loop
window.mainloop()

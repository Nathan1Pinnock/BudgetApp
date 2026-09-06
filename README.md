# BudgetApp

A budget calculator with a Tkinter GUI. Two boxes, Income and Expenses, an Add button, and a read-only text box that shows the running totals and what's left.

I wrote it in January 2023, on the same day as ToDoList, while learning Tkinter. Both are one file with no classes: module-level totals, a handler bound to the button, and a function that clears and rewrites the text box.

## Run it

    python BudgetApp.py

## Rough edges

- The boxes aren't cleared after Add, so a second click adds the same amounts again.
- Whole numbers only. Anything else, 12.50 included, raises ValueError inside the callback. Tkinter prints the traceback and the window carries on.
- The totals are shown in dollars.
- Nothing is saved between runs, and there's no way to take an entry back.

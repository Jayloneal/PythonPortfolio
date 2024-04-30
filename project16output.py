import tkinter as tk
from tkinter import ttk

def convert_currency():
    amount = float(amount_entry.get())
    from_currency = from_currency_combobox.get()
    to_currency = to_currency_combobox.get()
    
    exchange_rates = {
        "USD": 1,
        "EUR": 0.85,
        "GBP": 0.72,
        "JPY": 110.15,
        "AUD": 1.31,
        "CAD": 1.25,
        "CHF": 0.92,
        "CNY": 6.36
    }
    
    if from_currency in exchange_rates and to_currency in exchange_rates:
        converted_amount = amount * (exchange_rates[to_currency] / exchange_rates[from_currency])
        result_label.config(text=f"{amount:.2f} {from_currency} = {converted_amount:.2f} {to_currency}")
    else:
        result_label.config(text="You selected the wrong currency.")

root = tk.Tk()
root.title("Currency Converter")

amount_label = ttk.Label(root, text="What's the amount?")
amount_label.grid(row=0, column=0, padx=10, pady=10)

amount_entry = ttk.Entry(root)
amount_entry.grid(row=0, column=1, padx=10, pady=10)

from_currency_label = ttk.Label(root, text="From your currency:")
from_currency_label.grid(row=1, column=0, padx=10, pady=10)

from_currency_combobox = ttk.Combobox(root, values=["USD", "EUR", "GBP", "JPY", "AUD", "CAD", "CHF", "CNY"])
from_currency_combobox.grid(row=1, column=1, padx=10, pady=10)

to_currency_label = ttk.Label(root, text="To your target currency:")
to_currency_label.grid(row=2, column=0, padx=10, pady=10)

to_currency_combobox = ttk.Combobox(root, values=["USD", "EUR", "GBP", "JPY", "AUD", "CAD", "CHF", "CNY"])
to_currency_combobox.grid(row=2, column=1, padx=10, pady=10)

convert_button = ttk.Button(root, text="Convert", command=convert_currency)
convert_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

result_label = ttk.Label(root, text="")
result_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()

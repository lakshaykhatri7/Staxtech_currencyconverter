import tkinter as tk
import requests

# Function to get exchange rates from API
def get_exchange_rates():
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    response = requests.get(url)
    data = response.json()
    return data["rates"]

# Function to convert currency
def convert_currency():
    amount = entry_amount.get()
    from_currency = dropdown_from.get()
    to_currency = dropdown_to.get()

    if amount == "":
        result_label.config(text="Please enter an amount")
        return

    try:
        amount = float(amount)
    except ValueError:
        result_label.config(text="Enter a valid number")
        return

    # Calculate conversion
    rate_from = rates[from_currency]
    rate_to = rates[to_currency]
    converted_amount = amount * rate_to / rate_from

    # Show result
    result = f"{amount:.2f} {from_currency} = {converted_amount:.2f} {to_currency}"
    result_label.config(text=result)

# Fetch all exchange rates
rates = get_exchange_rates()
currency_list = list(rates.keys())

# Create main window
window = tk.Tk()
window.title("Currency Converter")
window.geometry("350x300")

# Heading
heading = tk.Label(window, text="Currency Converter", font=("Arial", 16))
heading.pack(pady=10)

# Amount input
entry_amount = tk.Entry(window, font=("Arial", 14), justify="center")
entry_amount.pack(pady=5)
entry_amount.insert(0, "1")

# From currency dropdown
dropdown_from = tk.StringVar()
from_menu = tk.OptionMenu(window, dropdown_from, *currency_list)
dropdown_from.set("USD")
from_menu.pack(pady=5)

# To currency dropdown
dropdown_to = tk.StringVar()
to_menu = tk.OptionMenu(window, dropdown_to, *currency_list)
dropdown_to.set("INR")
to_menu.pack(pady=5)

# Convert button
convert_button = tk.Button(window, text="Convert", command=convert_currency)
convert_button.pack(pady=10)

# Result label
result_label = tk.Label(window, text="", font=("Arial", 14))
result_label.pack(pady=10)

# Run the GUI
window.mainloop()

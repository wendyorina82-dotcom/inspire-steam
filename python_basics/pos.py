import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("POS System - KSH")
root.geometry("600x500")
root.configure(bg="lightgray")

total_amount = 0

# -------- FUNCTIONS --------
def add_to_cart():
    global total_amount
    
    product = product_entry.get()
    price = price_entry.get()
    quantity = quantity_entry.get()
    
    if product == "" or price == "" or quantity == "":
        messagebox.showerror("Error", "Please fill all fields")
        return
    
    try:
        price = float(price)
        quantity = int(quantity)
    except ValueError:
        messagebox.showerror("Error", "Enter valid numbers")
        return
    
    subtotal = price * quantity
    total_amount += subtotal
    
    cart_list.insert(tk.END, f"{product}  x{quantity}  =  KSH {subtotal:.2f}")
    total_label.config(text=f"Total: KSH {total_amount:.2f}")
    
    product_entry.delete(0, tk.END)
    price_entry.delete(0, tk.END)
    quantity_entry.delete(0, tk.END)

def clear_cart():
    global total_amount
    cart_list.delete(0, tk.END)
    total_amount = 0
    total_label.config(text="Total: KSH 0.00")

# -------- LABELS & ENTRIES --------
tk.Label(root, text="Product Name", bg="lightgray").grid(row=0, column=0, padx=10, pady=10)
product_entry = tk.Entry(root)
product_entry.grid(row=0, column=1)

tk.Label(root, text="Price (KSH)", bg="lightgray").grid(row=1, column=0)
price_entry = tk.Entry(root)
price_entry.grid(row=1, column=1)

tk.Label(root, text="Quantity", bg="lightgray").grid(row=2, column=0)
quantity_entry = tk.Entry(root)
quantity_entry.grid(row=2, column=1)

# -------- BUTTONS --------
tk.Button(root, text="Add to Cart", bg="green", fg="white", command=add_to_cart)\
    .grid(row=3, column=0, pady=10)

tk.Button(root, text="Clear Cart", bg="red", fg="white", command=clear_cart)\
    .grid(row=3, column=1)

# -------- CART DISPLAY --------
cart_list = tk.Listbox(root, width=60)
cart_list.grid(row=4, column=0, columnspan=2, pady=20)

total_label = tk.Label(root, text="Total: KSH 0.00", font=("Arial", 14, "bold"), bg="lightgray")
total_label.grid(row=5, column=0, columnspan=2)

root.mainloop()
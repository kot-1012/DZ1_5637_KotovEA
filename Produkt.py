import tkinter as tk
from tkinter import messagebox

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - {self.price:.2f} руб."

class HotDrink(Product):
    def __init__(self, name, price, temperature):
        super().__init__(name, price)
        self.temperature = temperature

    def __str__(self):
        return f"{super().__str__()} ({self.temperature}°C)"

class VendingMachineGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Аппарат")
        self.master.geometry("300x300") 

        self.products = [HotDrink("Кофе", 250, 95),
                         HotDrink("Чай", 80, 80),
                         HotDrink("Горячий шоколад", 140, 65)]

        self.product_listbox = tk.Listbox(self.master)
        for product in self.products:
            self.product_listbox.insert(tk.END, product)
        self.product_listbox.pack(fill=tk.BOTH, expand=True)

        tk.Label(self.master, text="Введите сумму:").pack()
        self.amount_entry = tk.Entry(self.master)
        self.amount_entry.pack()

        self.buy_button = tk.Button(self.master, text="Купить", command=self.buy_product)
        self.buy_button.pack()

    def buy_product(self):
        try:
            selected_index = self.product_listbox.curselection()[0]
            selected_product = self.products[selected_index]
            amount = float(self.amount_entry.get())
            if amount < selected_product.price:
                messagebox.showerror("Требуется Ваше внимание", "Недостаточно средств.")
            else:
             if isinstance(selected_product, HotDrink):
                messagebox.showinfo("Покупка", f"Спасибо за покупку {selected_product.name}!")
             else:
                messagebox.showinfo("Покупка", f"Спасибо за покупку {selected_product.name}!")
        except IndexError:
            messagebox.showerror("Требуется Ваше внимание", "Пожалуйста, выберите продукт.")
        except ValueError:
            messagebox.showerror("Требуется Ваше внимание", "Введите сумму")

def main():
    root = tk.Tk()
    vending_machine_gui = VendingMachineGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()

from customtkinter import *

root = CTk()
root.title("Test - CustomTkinter")
root.geometry("1024x568")
root.resizable(False, False)

#PIZZA

anz_pizza = 0
anz_pizzafunghi = 0
anz_pizzasalami = 0
anz_pizzatuhnfisch = 0
anz_pizzahawai = 0

pr_pizza = 3.5
pr_pizzafunghi = 3.75
pr_pizzasalamai= 3.75
pr_pizzatuhnfisch = 3.75
pr_pizzahawai = 4.00

total_price = 0

l1 = CTkLabel(root, text="A&C", font=("Arial", 60, "bold"))
l1.place(x=15, y=15)

#Choosing your items
pizza_title = CTkLabel(root, text="Pizza", font=("Arial", 30, "bold"))
pizza_title.place(x=15, y=100)

#-->MAIN FUNCTION
def buttonFunction_addPizza():
    global anz_pizza

    anzahl = CTk()
    anzahl.title("Anzahl")
    anzahl.geometry("550x450")
    anzahl.resizable(False, False)

    anzahl_input = CTkEntry(anzahl, width=275)
    anzahl_input.insert(0, "Anzahl die sie kaufen wollen")
    anzahl_input.pack()

    def buttonFunction_anzpizza():
        global anz_pizza, total_price
        try:
            quantity = int(anzahl_input.get())
            anz_pizza = anz_pizza + quantity
            total_price = total_price + quantity * pr_pizza  
            print("Quantity:", anz_pizza)
            print("Total Price: €", total_price)
            total_price_label.configure(text=f"Total Price: {total_price:.2f}€")
            anzahl.destroy()
        except ValueError:
            print("Bitte geben Sie eine gültige Anzahl ein.")

    anzahl_btn = CTkButton(anzahl, text="Apply", command=buttonFunction_anzpizza)
    anzahl_btn.pack()

    anzahl.mainloop()
#-->End of MAIN FUNCTION
add_pizza = CTkButton(root, text="Pizza", command=buttonFunction_addPizza)
add_pizza.place(x=15, y=150)

def buttonFunction_addPizzafunghi():
    global anz_pizzafunghi

    anzahl = CTk()
    anzahl.title("Anzahl")
    anzahl.geometry("550x450")
    anzahl.resizable(False, False)

    anzahl_input = CTkEntry(anzahl, width=275)
    anzahl_input.insert(0, "Anzahl die sie kaufen wollen")
    anzahl_input.pack()

    def buttonFunction_anzpizza():
        global anz_pizzafunghi, total_price
        try:
            quantity = int(anzahl_input.get())
            anz_pizza = anz_pizzafunghi + quantity
            total_price = total_price + quantity * pr_pizzafunghi  
            print("Quantity:", anz_pizza)
            print("Total Price: €", total_price)
            total_price_label.configure(text=f"Total Price: {total_price:.2f}€")
            anzahl.destroy()
        except ValueError:
            print("Bitte geben Sie eine gültige Anzahl ein.")

    anzahl_btn = CTkButton(anzahl, text="Apply", command=buttonFunction_anzpizza)
    anzahl_btn.pack()

    anzahl.mainloop()

add_pizzafunghi = CTkButton(root, text="Pizza Funghi", command=buttonFunction_addPizzafunghi)
add_pizzafunghi.place(x=175, y=150)

def buttonFunction_addPizzasalami():
    global anz_pizzasalami

    anzahl = CTk()
    anzahl.title("Anzahl")
    anzahl.geometry("550x450")
    anzahl.resizable(False, False)

    anzahl_input = CTkEntry(anzahl, width=275)
    anzahl_input.insert(0, "Anzahl die sie kaufen wollen")
    anzahl_input.pack()

    def buttonFunction_anzpizza():
        global anz_pizzasalami, total_price
        try:
            quantity = int(anzahl_input.get())
            anz_pizza = anz_pizzasalami + quantity
            total_price = total_price + quantity * pr_pizzasalamai 
            print("Quantity:", anz_pizza)
            print("Total Price: €", total_price)
            total_price_label.configure(text=f"Total Price: {total_price:.2f}€")
            anzahl.destroy()
        except ValueError:
            print("Bitte geben Sie eine gültige Anzahl ein.")

    anzahl_btn = CTkButton(anzahl, text="Apply", command=buttonFunction_anzpizza)
    anzahl_btn.pack()

    anzahl.mainloop()

add_pizzasalamai = CTkButton(root, text="Pizza Salami", command=buttonFunction_addPizzasalami)
add_pizzasalamai.place(x=335, y=150)



def buttonFunction_addPizzahawai():
    global anz_pizzahawai

    anzahl = CTk()
    anzahl.title("Anzahl")
    anzahl.geometry("550x450")
    anzahl.resizable(False, False)

    anzahl_input = CTkEntry(anzahl, width=275)
    anzahl_input.insert(0, "Anzahl die sie kaufen wollen")
    anzahl_input.pack()

    def buttonFunction_anzpizza():
        global anz_pizza, total_price
        try:
            quantity = int(anzahl_input.get())
            anz_pizza = anz_pizzahawai + quantity
            total_price = total_price + quantity * pr_pizzahawai
            print("Quantity:", anz_pizza)
            print("Total Price: €", total_price)
            total_price_label.configure(text=f"Total Price: {total_price:.2f}€")
            anzahl.destroy()
        except ValueError:
            print("Bitte geben Sie eine gültige Anzahl ein.")

    anzahl_btn = CTkButton(anzahl, text="Apply", command=buttonFunction_anzpizza)
    anzahl_btn.pack()

    anzahl.mainloop()

add_pizzasalamai = CTkButton(root, text="Pizza Tuhnfisch", command=buttonFunction_addPizzatuhnfisch)
add_pizzasalamai.place(x=500, y=150)

def buttonFunction_addPizzatuhnfisch():
    global anz_pizza

    anzahl = CTk()
    anzahl.title("Anzahl")
    anzahl.geometry("550x450")
    anzahl.resizable(False, False)

    anzahl_input = CTkEntry(anzahl, width=275)
    anzahl_input.insert(0, "Anzahl die sie kaufen wollen")
    anzahl_input.pack()

    def buttonFunction_anzpizza():
        global anz_pizza, total_price
        try:
            quantity = int(anzahl_input.get())
            anz_pizza = anz_pizzatuhnfisch + quantity
            total_price = total_price + quantity * pr_pizzatuhnfisch
            print("Quantity:", anz_pizza)
            print("Total Price: €", total_price)
            total_price_label.configure(text=f"Total Price: {total_price:.2f}€")
            anzahl.destroy()
        except ValueError:
            print("Bitte geben Sie eine gültige Anzahl ein.")

    anzahl_btn = CTkButton(anzahl, text="Apply", command=buttonFunction_anzpizza)
    anzahl_btn.pack()

    anzahl.mainloop()

add_pizzasalamai = CTkButton(root, text="Pizza Hawai", command=buttonFunction_addPizzahawai)
add_pizzasalamai.place(x=500, y=150)




total_price_label = CTkLabel(root, text=f"Total Price: {total_price:.2f}€")
total_price_label.place(x=15, y=500)

# END PROCESS --> Buy BTN
def buttonFunction_buy():
    global total_price
    print("Total Price: ", total_price, "€.")
        
    buy = CTk()
    buy.title("Buy Items")
    buy.geometry("1024x568")
    buy.resizable(False, False)
    root.destroy()

    title = CTkLabel(buy, text="Buy your Items",font=("Arial", 45, "bold"))
    title.place(x=15, y=15)

    buy.mainloop()

buy_btn = CTkButton(root, text="Buy", width=990, command=buttonFunction_buy)
buy_btn.place(x=17.5, y=525)

root.mainloop()

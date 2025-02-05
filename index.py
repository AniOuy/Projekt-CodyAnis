from customtkinter import *

root = CTk()
root.title("Test - CustomTkinter")
root.geometry("1024x568")
root.resizable(False, False)

anz_pizza = 0
pr_pizza = 3.5

total_price = 0

l1 = CTkLabel(root, text="A&C", font=("Arial", 60, "bold"))
l1.place(x=15, y=15)


'''
-->MAIN FUNCTION
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

add_pizza = CTkButton(root, text="Buy Pizza", command=buttonFunction_addPizza)
add_pizza.pack()
'''

#Choosing your items
pizza_title = CTkLabel(root, text="Pizza", font=("Arial", 35, "bold"))
pizza_title.place(x=15, y=100)

total_price_label = CTkLabel(root, text=f"Total Price: {total_price:.2f}€")
total_price_label.place(x=15, y=500)

# END PROCESS --> Buy BTN
def buttonFunction_buy():
    global total_price
    print("Total Price: ", total_price, "€.")

buy_btn = CTkButton(root, text="Buy", width=990, command=buttonFunction_buy)
buy_btn.place(x=17.5, y=525)

root.mainloop()

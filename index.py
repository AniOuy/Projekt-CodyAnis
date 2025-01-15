from customtkinter import *

root = CTk()
root.title("Test - CustomTkinter")
root.geometry("1024x568")
root.resizable(False, False)

anz_pizza = 0
pr_pizza = 3.5

l1 = CTkLabel(root, text="A&C", font=("Arial", 65))
l1.place(x=25, y=15)

f1 = CTkFrame(root, width=990, bg_color="red")
f1.place(x=15, y=100)

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
        global anz_pizza
        try:
            quantity = int(anzahl_input.get())
            anz_pizza += quantity
            total_price = anz_pizza * pr_pizza
            print("Quantity:", anz_pizza)
            print("Total Price: €", total_price)
        except ValueError:
            print("Bitte geben Sie eine gültige Anzahl ein.")
        anzahl.destroy()

    anzahl_btn = CTkButton(anzahl, text="Apply", command=buttonFunction_anzpizza)
    anzahl_btn.pack()

    anzahl.mainloop()

add_pizza = CTkButton(f1, text="Buy Pizza", command=buttonFunction_addPizza)
add_pizza.pack()

buy_btn = CTkButton(root, text="Buy", width=990, command=lambda: print("Buy button clicked"))
buy_btn.place(x=17.5, y=525)

root.mainloop()
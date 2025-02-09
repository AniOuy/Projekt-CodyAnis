'''BE68539007547034'''

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

pr_pizza = 13.90
pr_pizzafunghi = 15.50
pr_pizzasalamai= 15.50
pr_pizzatuhnfisch = 15.50
pr_pizzahawai = 16.90

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
            total_price_label.configure(text=f"Total Price: {total_price:.2f}€")
            anzahl.destroy()
        except ValueError:
            print("Bitte geben Sie eine gültige Anzahl ein.")

    anzahl_btn = CTkButton(anzahl, text="Apply", command=buttonFunction_anzpizza)
    anzahl_btn.pack()

    anzahl.mainloop()

add_pizzasalamai = CTkButton(root, text="Pizza Salami", command=buttonFunction_addPizzasalami)
add_pizzasalamai.place(x=335, y=150)

def buttonFunction_addPizzatuhnfisch():
    global anz_pizzatuhnfisch

    anzahl = CTk()
    anzahl.title("Anzahl")
    anzahl.geometry("550x450")
    anzahl.resizable(False, False)

    anzahl_input = CTkEntry(anzahl, width=275)
    anzahl_input.insert(0, "Anzahl die sie kaufen wollen")
    anzahl_input.pack()

    def buttonFunction_anzpizza():
        global anz_pizzatuhnfisch, total_price
        try:
            quantity = int(anzahl_input.get())
            anz_pizza = anz_pizzatuhnfisch + quantity
            total_price = total_price + quantity * pr_pizzatuhnfisch
            total_price_label.configure(text=f"Total Price: {total_price:.2f}€")
            anzahl.destroy()
        except ValueError:
            print("Bitte geben Sie eine gültige Anzahl ein.")

    anzahl_btn = CTkButton(anzahl, text="Apply", command=buttonFunction_anzpizza)
    anzahl_btn.pack()

    anzahl.mainloop()

add_pizzatuhnfisch = CTkButton(root, text="Pizza Tuhnfisch", command=buttonFunction_addPizzatuhnfisch)
add_pizzatuhnfisch.place(x=500, y=150)

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
        global anz_pizzahawai, total_price
        try:
            quantity = int(anzahl_input.get())
            anz_pizza = anz_pizzahawai + quantity
            total_price = total_price + quantity * pr_pizzahawai
            total_price_label.configure(text=f"Total Price: {total_price:.2f}€")
            anzahl.destroy()
        except ValueError:
            print("Bitte geben Sie eine gültige Anzahl ein.")

    anzahl_btn = CTkButton(anzahl, text="Apply", command=buttonFunction_anzpizza)
    anzahl_btn.pack()

    anzahl.mainloop()

add_pizzahawai = CTkButton(root, text="Pizza Hawai", command=buttonFunction_addPizzahawai)
add_pizzahawai.place(x=660, y=150)

#SALAT
salat_title = CTkLabel(root, text="Salat", font=("Arial", 30, "bold"))
salat_title.place(x=15, y=215)

anz_hirtensalat = 0
anz_salatbeef = 0
anz_tuhnfischsteaksalat = 0
anz_ananassalat = 0
anz_garnelensalat = 0

pr_hirtensalat = 13.90
pr_salatbeef = 24.90
pr_tuhnfischsteaksalat= 23.90
pr_ananassalat = 16.90
pr_garnelensalat = 19.90

def buttonFunction_addhirtensalat():
    global anz_hirtensalat

    anzahl = CTk()
    anzahl.title("Anzahl")
    anzahl.geometry("550x450")
    anzahl.resizable(False, False)

    anzahl_input = CTkEntry(anzahl, width=275)
    anzahl_input.insert(0, "Anzahl die sie kaufen wollen")
    anzahl_input.pack()

    def buttonFunction_anzpizza():
        global anz_hirtensalat, total_price
        try:
            quantity = int(anzahl_input.get())
            anz_pizza = anz_hirtensalat + quantity
            total_price = total_price + quantity * pr_hirtensalat
            total_price_label.configure(text=f"Total Price: {total_price:.2f}€")
            anzahl.destroy()
        except ValueError:
            print("Bitte geben Sie eine gültige Anzahl ein.")

    anzahl_btn = CTkButton(anzahl, text="Apply", command=buttonFunction_anzpizza)
    anzahl_btn.pack()

    anzahl.mainloop()

add_hirtensalat = CTkButton(root, text="Hirtensalat", command=buttonFunction_addhirtensalat)
add_hirtensalat.place(x=15, y=275)

def buttonFunction_addsalatbeef():
    global anz_salatbeef

    anzahl = CTk()
    anzahl.title("Anzahl")
    anzahl.geometry("550x450")
    anzahl.resizable(False, False)

    anzahl_input = CTkEntry(anzahl, width=275)
    anzahl_input.insert(0, "Anzahl die sie kaufen wollen")
    anzahl_input.pack()

    def buttonFunction_anzpizza():
        global anz_salatbeef, total_price
        try:
            quantity = int(anzahl_input.get())
            anz_pizza = anz_salatbeef + quantity
            total_price = total_price + quantity * pr_salatbeef
            total_price_label.configure(text=f"Total Price: {total_price:.2f}€")
            anzahl.destroy()
        except ValueError:
            print("Bitte geben Sie eine gültige Anzahl ein.")

    anzahl_btn = CTkButton(anzahl, text="Apply", command=buttonFunction_anzpizza)
    anzahl_btn.pack()

    anzahl.mainloop()

add_salatbeef = CTkButton(root, text="Salatbeef", command=buttonFunction_addsalatbeef)
add_salatbeef.place(x=175, y=275)

def buttonFunction_addtuhnfischsteaksalat():
    global anz_tuhnfischsteaksalat

    anzahl = CTk()
    anzahl.title("Anzahl")
    anzahl.geometry("550x450")
    anzahl.resizable(False, False)

    anzahl_input = CTkEntry(anzahl, width=275)
    anzahl_input.insert(0, "Anzahl die sie kaufen wollen")
    anzahl_input.pack()

    def buttonFunction_anzpizza():
        global anz_tuhnfischsteaksalat, total_price
        try:
            quantity = int(anzahl_input.get())
            anz_pizza = anz_tuhnfischsteaksalat + quantity
            total_price = total_price + quantity * pr_tuhnfischsteaksalat
            total_price_label.configure(text=f"Total Price: {total_price:.2f}€")
            anzahl.destroy()
        except ValueError:
            print("Bitte geben Sie eine gültige Anzahl ein.")

    anzahl_btn = CTkButton(anzahl, text="Apply", command=buttonFunction_anzpizza)
    anzahl_btn.pack()

    anzahl.mainloop()

add_tuhnfischsteaksalat = CTkButton(root, text="Pizza Salami", command=buttonFunction_addtuhnfischsteaksalat)
add_tuhnfischsteaksalat.place(x=335, y=275)

def buttonFunction_addananassalat():
    global anz_ananassalat

    anzahl = CTk()
    anzahl.title("Anzahl")
    anzahl.geometry("550x450")
    anzahl.resizable(False, False)

    anzahl_input = CTkEntry(anzahl, width=275)
    anzahl_input.insert(0, "Anzahl die sie kaufen wollen")
    anzahl_input.pack()

    def buttonFunction_anzpizza():
        global anz_ananassalat, total_price
        try:
            quantity = int(anzahl_input.get())
            anz_pizza = anz_ananassalat + quantity
            total_price = total_price + quantity * pr_ananassalat
            total_price_label.configure(text=f"Total Price: {total_price:.2f}€")
            anzahl.destroy()
        except ValueError:
            print("Bitte geben Sie eine gültige Anzahl ein.")

    anzahl_btn = CTkButton(anzahl, text="Apply", command=buttonFunction_anzpizza)
    anzahl_btn.pack()

    anzahl.mainloop()

add_ananassalat = CTkButton(root, text="Ananas Salat", command=buttonFunction_addananassalat)
add_ananassalat.place(x=500, y=275)

def buttonFunction_addgarnelensalat():
    global anz_garnelensalat

    anzahl = CTk()
    anzahl.title("Anzahl")
    anzahl.geometry("550x450")
    anzahl.resizable(False, False)

    anzahl_input = CTkEntry(anzahl, width=275)
    anzahl_input.insert(0, "Anzahl die sie kaufen wollen")
    anzahl_input.pack()

    def buttonFunction_anzpizza():
        global anz_garnelensalat, total_price
        try:
            quantity = int(anzahl_input.get())
            anz_pizza = anz_garnelensalat + quantity
            total_price = total_price + quantity * pr_garnelensalat
            total_price_label.configure(text=f"Total Price: {total_price:.2f}€")
            anzahl.destroy()
        except ValueError:
            print("Bitte geben Sie eine gültige Anzahl ein.")

    anzahl_btn = CTkButton(anzahl, text="Apply", command=buttonFunction_anzpizza)
    anzahl_btn.pack()

    anzahl.mainloop()

add_garnelensalat = CTkButton(root, text="Garnelen Salat", command=buttonFunction_addgarnelensalat)
add_garnelensalat.place(x=660, y=275)

#pasta
salatpasta_title = CTkLabel(root, text="Pasta", font=("Arial", 30, "bold"))
salatpasta_title.place(x=15, y=330)

anz_tagliatellegarnellen = 0
anz_pennechampignons = 0
anz_tagliatellepesto = 0
anz_penneallarrabiata = 0
anz_tagliatellegyros = 0

pr_tagliatellegarnellen = 21.90
pr_pennechampignons = 15.90
pr_tagliatellepesto= 15.90
pr_penneallarrabiata = 15.90
pr_tagliatellegyros = 15.90

def buttonFunction_addtagliatellegarnellen():
    global anz_tagliatellegarnellen

    anzahl = CTk()
    anzahl.title("Anzahl")
    anzahl.geometry("550x450")
    anzahl.resizable(False, False)

    anzahl_input = CTkEntry(anzahl, width=275)
    anzahl_input.insert(0, "Anzahl die sie kaufen wollen")
    anzahl_input.pack()

    def buttonFunction_anzpizza():
        global anz_tagliatellegarnellen, total_price
        try:
            quantity = int(anzahl_input.get())
            anz_pizza = anz_tagliatellegarnellen + quantity
            total_price = total_price + quantity * pr_tagliatellegarnellen
            total_price_label.configure(text=f"Total Price: {total_price:.2f}€")
            anzahl.destroy()
        except ValueError:
            print("Bitte geben Sie eine gültige Anzahl ein.")

    anzahl_btn = CTkButton(anzahl, text="Apply", command=buttonFunction_anzpizza)
    anzahl_btn.pack()

    anzahl.mainloop()

add_tagliatellegarnellen = CTkButton(root, text="Tagliatellegarnellen", command=buttonFunction_addtagliatellegarnellen)
add_tagliatellegarnellen.place(x=15, y=385)

def buttonFunction_addpennechampignons():
    global anz_pennechampignons

    anzahl = CTk()
    anzahl.title("Anzahl")
    anzahl.geometry("550x450")
    anzahl.resizable(False, False)

    anzahl_input = CTkEntry(anzahl, width=275)
    anzahl_input.insert(0, "Anzahl die sie kaufen wollen")
    anzahl_input.pack()

    def buttonFunction_anzpizza():
        global anz_pennechampignons, total_price
        try:
            quantity = int(anzahl_input.get())
            anz_pizza = anz_pennechampignons + quantity
            total_price = total_price + quantity * pr_pennechampignons
            total_price_label.configure(text=f"Total Price: {total_price:.2f}€")
            anzahl.destroy()
        except ValueError:
            print("Bitte geben Sie eine gültige Anzahl ein.")

    anzahl_btn = CTkButton(anzahl, text="Apply", command=buttonFunction_anzpizza)
    anzahl_btn.pack()

    anzahl.mainloop()

add_pennechampignons = CTkButton(root, text="Pennechampignons", command=buttonFunction_addpennechampignons)
add_pennechampignons.place(x=175, y=385)

def buttonFunction_addtagliatellepesto():
    global tagliatellepesto

    anzahl = CTk()
    anzahl.title("Anzahl")
    anzahl.geometry("550x450")
    anzahl.resizable(False, False)

    anzahl_input = CTkEntry(anzahl, width=275)
    anzahl_input.insert(0, "Anzahl die sie kaufen wollen")
    anzahl_input.pack()

    def buttonFunction_anzpizza():
        global anz_tagliatellepesto, total_price
        try:
            quantity = int(anzahl_input.get())
            anz_pizza = anz_tagliatellepesto + quantity
            total_price = total_price + quantity * pr_tagliatellepesto
            total_price_label.configure(text=f"Total Price: {total_price:.2f}€")
            anzahl.destroy()
        except ValueError:
            print("Bitte geben Sie eine gültige Anzahl ein.")

    anzahl_btn = CTkButton(anzahl, text="Apply", command=buttonFunction_anzpizza)
    anzahl_btn.pack()

    anzahl.mainloop()

add_tagliatellepesto = CTkButton(root, text="Tagliatelle Pesto", command=buttonFunction_addtagliatellepesto)
add_tagliatellepesto.place(x=335, y=385)

def buttonFunction_addpenneallarrabiata():
    global anz_penneallarrabiata

    anzahl = CTk()
    anzahl.title("Anzahl")
    anzahl.geometry("550x450")
    anzahl.resizable(False, False)

    anzahl_input = CTkEntry(anzahl, width=275)
    anzahl_input.insert(0, "Anzahl die sie kaufen wollen")
    anzahl_input.pack()

    def buttonFunction_anzpizza():
        global anz_penneallarrabiata, total_price
        try:
            quantity = int(anzahl_input.get())
            anz_pizza = anz_penneallarrabiata + quantity
            total_price = total_price + quantity * pr_penneallarrabiata
            total_price_label.configure(text=f"Total Price: {total_price:.2f}€")
            anzahl.destroy()
        except ValueError:
            print("Bitte geben Sie eine gültige Anzahl ein.")

    anzahl_btn = CTkButton(anzahl, text="Apply", command=buttonFunction_anzpizza)
    anzahl_btn.pack()

    anzahl.mainloop()

add_penneallarrabiata = CTkButton(root, text="Penne All'Arrabiata", command=buttonFunction_addpenneallarrabiata)
add_penneallarrabiata.place(x=500, y=385)

def buttonFunction_addtagliatellegyros():
    global anz_tagliatellegyros

    anzahl = CTk()
    anzahl.title("Anzahl")
    anzahl.geometry("550x450")
    anzahl.resizable(False, False)

    anzahl_input = CTkEntry(anzahl, width=275)
    anzahl_input.insert(0, "Anzahl die sie kaufen wollen")
    anzahl_input.pack()

    def buttonFunction_anzpizza():
        global anz_tagliatellegyros, total_price
        try:
            quantity = int(anzahl_input.get())
            anz_pizza = anz_tagliatellegyros + quantity
            total_price = total_price + quantity * pr_tagliatellegyros
            total_price_label.configure(text=f"Total Price: {total_price:.2f}€")
            anzahl.destroy()
        except ValueError:
            print("Bitte geben Sie eine gültige Anzahl ein.")

    anzahl_btn = CTkButton(anzahl, text="Apply", command=buttonFunction_anzpizza)
    anzahl_btn.pack()

    anzahl.mainloop()

add_tagliatellegyros = CTkButton(root, text="Tagliatelle Gyros", command=buttonFunction_addtagliatellegyros)
add_tagliatellegyros.place(x=660, y=385)

total_price_label = CTkLabel(root, text=f"Total Price: {total_price:.2f}€")
total_price_label.place(x=15, y=500)

# END PROCESS --> Buy BTN
def buttonFunction_buy():
    global total_price
    print("Total Price: ", total_price, "€.")
        
    pay = CTk()
    pay.title("Pay Items")
    pay.geometry("1024x568")
    pay.resizable(False, False)

    title = CTkLabel(pay, text="Buy your Items", font=("Arial", 35, "bold"))
    title.pack(pady=30)

    amount = CTkLabel(pay, text="", font=("Arial", 65, "bold"))
    amount.pack(pady=15)
    amount.configure(text=f"{total_price:.2f}€")  # Formatierung auf zwei Dezimalstellen

    e_name = CTkEntry(pay, width=275)
    e_name.pack(pady=15)
    e_name.insert(0, "Name")

    e_vorname = CTkEntry(pay, width=275)
    e_vorname.pack(pady=15)
    e_vorname.insert(0, "Vorname")

    e_nummer = CTkEntry(pay, width=275)
    e_nummer.pack(pady=15)
    e_nummer.insert(0, "Telefonnummer")

    e_bank = CTkEntry(pay, width=275)
    e_bank.pack(pady=15)
    e_bank.insert(0, "BEXXXXXXXXXXXXXX")

    def buttonFunction_pay():
        end = CTk()
        end.title("END")
        end.geometry("1024x568")
        end.resizable(False, False)

        frame = CTkFrame(end)
        frame.pack(expand=True)

        l1 = CTkLabel(frame, text="Deine Bezahlung ist erfolgreich \n abgeschlossen worden!!!", 
                   text_color="lightgreen", font=("Arial", 60, "bold"))
        l1.pack(pady=45)

        pay.destroy()
        end.mainloop()

    pay_button = CTkButton(pay, width=275, text="Pay", command=buttonFunction_pay)
    pay_button.pack(pady=15)
    root.destroy()
    pay.mainloop()

buy_btn = CTkButton(root, text="Buy", width=990, command=buttonFunction_buy)
buy_btn.place(x=17.5, y=525)

root.mainloop()

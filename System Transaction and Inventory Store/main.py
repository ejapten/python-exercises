# create inventory
inventory = {
    "ID001": {"Name": "Pencil", "Price (Rp)": 1000, "Stock": 20},
    "ID002": {"Name": "Pen", "Price (Rp)": 1000, "Stock": 25},
    "ID003": {"Name": "Book", "Price (Rp)": 3500, "Stock": 100},
    "ID004": {"Name": "Ruler", "Price (Rp)": 2000, "Stock": 5},
    "ID005": {"Name": "Toefl Book", "Price (Rp)": 100000, "Stock": 10},
    "ID006": {"Name": "CSAT Book", "Price (Rp)": 150000, "Stock": 0},
    "ID007": {"Name": "Pencil 2B", "Price (Rp)": 3000, "Stock": 100},
}


# Function for users to put items into the shopping cart
def shopping_cart(inventory_store):
    cart = []  # empty shopping cart

    # create an input that can be entered by the user when shopping
    while True:
        # Enter an item
        name_of_goods = input("Enter the item name : ").strip()
        if name_of_goods.lower() == "end":
            break

        #  search for item ID when inputting item name
        id_item = None
        for key, detail in inventory_store.items():
            if detail["Name"] == name_of_goods:
                id_item = key
                break

        if id_item is None:
            print(f"Sorry, item '{name_of_goods}' wa not found in inventory")
            continue  # in this section, if a item does not exist, then immediately ask for input again

        # enter the quantity of items
        while True:
            try:
                quantity = int(input(f"quantity '{inventory_store[id_item]['Name']}: "))
                if quantity > 0:
                    break
                else:
                    print("Quantity of item must be more than 0")
            except ValueError:
                print("The input it's not valid. Enter a number")

        # add item to the cart
        cart.append({"id_item": id_item, "quantity": quantity})

        print(
            f"{inventory_store[id_item]['Name']} as much {quantity} unit added to cart"
        )

    return cart


print("\n===================== WELCOME TO BOOK STORE =====================")
print("=" * 65)

#  1. Print the data in the inventory
print("\n-----------------------Current Inventory-------------------------\n")
for id_brg, detail in inventory.items():
    print(
        f"{detail['Name']:<12} | Price (Rp): {detail['Price (Rp)']:<12} | Stock : {detail['Stock']:<12}"
    )

# 2. The user will put the item into the shopping cart
cart_user = shopping_cart(inventory)

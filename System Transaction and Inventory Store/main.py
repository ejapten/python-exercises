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
        name_of_goods = input("\nEnter the item name : ").strip()
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
                quantity = int(input(f"quantity '{inventory_store[id_item]['Name']}': "))
                if quantity > 0:
                    break
                else:
                    print("Quantity of item must be more than 0")
            except ValueError:
                print("The input it's not valid. Enter a number")

        # add item to the cart
        cart.append({"id_item": id_item, "quantity": quantity})

        print(f"--> {inventory_store[id_item]['Name']} as much {quantity} unit added to cart")

    return cart


# Function for transaction process
def transaction_process(cart_user, inventory_store):

    # check stock item in inventory
    for item in cart_user:  # check items purchased by the user (example : {"id_item": "ID001", "quantity": 3})
        id_item = item["id_item"]  # items purchased by the user
        quantity_of_items_purchased = item["quantity"]  # items purchased by the user

        print("\n-->Starting the transaction process...")

        if (inventory_store[id_item]["Stock"] >= quantity_of_items_purchased):  
            continue
        else:
            print(f"...Check Failed : '{inventory_store[id_item]['Name']}' Stock ({inventory_store[id_item]['Stock']} remaining) is not enough purchase of {quantity_of_items_purchased} units <--\n")
            return False
        
    print(f"...Goods check successful <--\n")

        # Sum the total shopping price
    total_price = 0

    print("=" * 20 + "SubTotal" + "=" * 20)

    for item in cart_user: # search item in cart when user purchased
        id_item = item["id_item"]  # get id_item from cart_user to find information (example : {"id_item": "ID001", "quantity": 3})
        quantity_of_items_purchased = item["quantity"]

        item_at_store = inventory_store[id_item] # id item in inventory  store
        name_item = item_at_store["Name"]
        price_item = item_at_store["Price (Rp)"]
        subtotal = quantity_of_items_purchased * price_item

        total_price += subtotal

        # reduce stock in inventory
        inventory_store[id_item]["Stock"] -= quantity_of_items_purchased
        # remaining stock
        remaining_stock = inventory_store[id_item]["Stock"]

        # Print purchased item
        print(f"+ {name_item:<10} | {quantity_of_items_purchased:<10} units | Rp {subtotal:<10}")
            

    # print Total Item
    print("-"*48)
    print(f"Total Spending : Rp {total_price}")
    print("="*48)

    # Informatioon about Inventory
    print("\n" + "="*20 + "Inventory After Transaction" + "="*20 + "\n")
    for id_item, detail in inventory_store.items():
        print(f"{id_item} : {detail}")
    print("\n"+"="*67 +"\n")

    return True

print("=" * 65) 
print("===================== WELCOME TO BOOK STORE =====================")
print("=" * 65)

#  1. Print the data in the inventory
print("\n-----------------------Current Inventory-------------------------\n")
for id_brg, detail in inventory.items():
    print(f"{detail['Name']:<12} | Price (Rp): {detail['Price (Rp)']:<12} | Stock : {detail['Stock']:<12}")
print("-----------------------------------------------------------------")
# 2. The user will put the item into the shopping cart
user_shopping_cart = shopping_cart(inventory)

# 3. transaction process when the cart not empty
if user_shopping_cart:
    print("\n" + "-" * 48)
    print("*"*11 + "THIS IS YOUR SHOPPING CART" + "*"*11)
    print("-" * 48)

    for item in user_shopping_cart:
        # id_item = item["id_item"]
        name = inventory[item["id_item"]]["Name"]
        quantity = item["quantity"]
        print(f"- {name} {quantity} units")

    transaction_process(user_shopping_cart, inventory)
else:
    print("There are no items in the Cart")
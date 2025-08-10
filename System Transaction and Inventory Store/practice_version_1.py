inventory = {'ID001' : {'Name' : 'Pen', 'Price' : 2000, 'Stock': 200},
            'ID002' : {'Name' : 'Pencil', 'Price' : 1000, 'Stock' : 50},
            'ID003' : {'Name' : 'Book', 'Price' : 5000, 'Stock' : 20}}
            
# Function for Interaction User when Shopping
def shopping_cart(inventory_store):
  cart_user = []
  while True:

    cart_item = input("Enter Name of Item : ")
    if cart_item.lower() == 'end':
      break
    
    for key, detail in inventory_store.items():
      if detail["Name"] == cart_item:
        id_item = key
        break

    quantity = int(input("Enter Quantity of Item : "))

    # cart shopping
    cart_user.append({"id_item": id_item, "cart_item": cart_item, "quantity": quantity})


  return cart_user

# Function for Transaction
def process_transaction(cart_user, inventory_store):

  total_harga = 0

  print("\n==== Subtotal ====")

  for item in cart_user:
    id_item = item["id_item"]
    quantity = item["quantity"]

    price_in_inventory = inventory_store[id_item]["Price"]
    item_name = inventory_store[id_item]["Name"]
    subtotal = quantity * price_in_inventory
    total_harga += subtotal

    print(f"= {item_name} | {quantity} Units | Rp {subtotal}")
  
  
  print(f"\nThe total price of the goods purchased is Rp {total_harga}")

  



cart_for_shopping = shopping_cart(inventory)

print("\nThis is Your Shopping Cart\n")
for item in cart_for_shopping:
  print(f"+ {item['cart_item']} {item['quantity']} units")
 
process_transaction(cart_for_shopping, inventory)


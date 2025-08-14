inventory = {'ID001' : {'Name' : 'Pen', 'Price' : 2000, 'Stock': 200},
            'ID002' : {'Name' : 'Pencil', 'Price' : 1000, 'Stock' : 50},
            'ID003' : {'Name' : 'Book', 'Price' : 5000, 'Stock' : 20}}

#Function for inputting item names so that they are not case sensitive
def input_cs(name_item_cart, inventory_store):
  for key, detail in inventory_store.items():
    if detail['Name'].lower() == name_item_cart.lower():
      return key
  return None

# Function for Interaction User when Shopping
def shopping_cart(inventory_store):
  cart_user = []
  while True:

    cart_item = input("--> Enter Name of Item : ").strip()
    if cart_item == "":
      print("Name Can't be Empty")
      continue
    if cart_item.isnumeric():
      print("Name Can't be Numeric")
      continue
    if cart_item.lower() == 'end':
      break

    id_item = input_cs(cart_item, inventory_store)
    if id_item is None:
      print(f"Sorry, item {cart_item} not found")
      continue
      
    for key, detail in inventory_store.items():
      if detail["Name"] == cart_item:
        id_item = key
        break

    while True:
      try:
        quantity = int(input("++> Enter Quantity of Item : "))
        if quantity > 0:
          break
        else:
          print("\n--> The number of items must be more than 0\n")
      except ValueError:
        print("\n--> The Input is not valid. Please enter a number\n")

    # cart shopping
    cart_user.append({"id_item": id_item, "cart_item": cart_item, "quantity": quantity})


  return cart_user

# Function for discount
def discount_and_total_spending(cart_user, inventory_store):

  total_spending = 0
  for item in cart_user:
    id_item = item['id_item']
    name = inventory_store[id_item]["Name"] 
    quantity = item['quantity']
    price_in_inventory = inventory_store[id_item]["Price"]
    subtotal = quantity * price_in_inventory

    if quantity > 10:
      discount = 0.1
      payment = subtotal - (discount * subtotal)
      print(f"id : {id_item}  | Name : {name} | quantity : {quantity} | Subtotal : {subtotal} | discount : {discount} | Total : {payment:.0f}")
    else:
      payment = subtotal
      print(f"Name : {name} | quantity : {quantity} | Subtotal : {subtotal} | discount : 0 | Total : {payment:.0f}")

    total_spending += payment

  return total_spending

# Function for Transaction
def payment_system(cart_user, inventory_store):

  if not cart_user:
   print("No items in cart. Exiting program.")
   return

  #subtotal
  print("\n"+ "-"*25 + "Subtotal" + "-"*25)
  total_spending = discount_and_total_spending(cart_user, inventory_store)
  print("-"*60)
  
  # total spending
  print(f"-->> The total price of the goods purchased is Rp {total_spending:.0f} <<--")
  print("="*85+"\n")
  
  # System Payment
  print("\n"+ "="*85)
  print("Payment".center(80))
  print("="*85)

  while True:
    pay = input("->Enter the amount of money : ")

    if not pay.isdigit():
      print("Please enter a valid number!")
      continue
    
    pay = int(pay)

    if pay >= total_spending:
      change_money = pay - total_spending
      print(f"\n->This Your Change : {change_money:.0f}")

      # stock
      for item in cart_user:
        id_item = item['id_item']
        quantity = item['quantity']
        # reduce stock
        inventory_store[id_item]['Stock'] -= quantity
        sisa_stock = inventory_store[id_item]['Stock']
      break
    else:
      print("\n->Sorry, your money is not enough to make the payment.")
      break
      
 
  print("\n"+ "="*35+"Inventory Store"+ "="*35)
  for key, detail in inventory_store.items():
    print(f"ID : {key:<7} | Product Name : {detail['Name']:<7} | Product Price : {detail['Price']:<7} | Stock Product : {detail['Stock']}")
  print("="*85+"\n")


# Interface
print("\n"+ "="*35+"Inventory Store"+ "="*35)
for key, detail in inventory.items():
  print(f"ID : {key:<7} | Product Name : {detail['Name']:<7} | Product Price : {detail['Price']:<7} | Stock Product : {detail['Stock']:<7}")
print("="*85+"\n")

#1. The user will put the item into the shopping cart
cart_for_shopping = shopping_cart(inventory)

# 2. Shopping list
print("\n"+ "="*85)
print("This is Your Shopping Cart".center(80))
print("="*85)

for item in cart_for_shopping:
  print(f"+ {item['cart_item']} {item['quantity']} units")

# 3. Payment Process
payment_system(cart_for_shopping, inventory)


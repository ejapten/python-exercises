inventory = {'ID001' : {'Name' : 'Pen', 'Price' : 2000, 'Stock': 200},
            ' ID002' : {'Name' : 'Pencil', 'Price' : 1000, 'Stock' : 50},
            'ID001' : {'Name' : 'Book', 'Price' : 5000, 'Stock' : 20}}
            
# Function for Interaction User when Shopping
def shopping_cart(inventory_store):
  cart_user = []
  while True:

    cart_item = input("Enter Name of Item : ")
    if cart_item.lower() == 'end':
      break

    quantity = int(input("Enter Quantity of Item : "))

    # cart shopping

    cart_user.append({"cart_item" : cart_item, "quantity" : quantity})

  return cart_user

cart_for_shopping = shopping_cart(inventory)

for detail in cart_for_shopping:
  print(f"+ Item : {detail['cart_item']}, Quantity of Item : {detail['quantity']}")


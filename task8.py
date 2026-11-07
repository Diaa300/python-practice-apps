import time
import json

admins = {
    "Diaa"   : "562010",
    "Eyad"   : "652101",
    "Ahmed"  : "952127",
    "Omar"   : "659814",
    "Yousef" : "984562"
}


def admin_required(func):
    def wrapper():
        print("--- Admin Authentication Required ---")

        name = input("Enter Admin Name: ").strip().capitalize()
        id = input("Enter Admin ID: ").strip()
        
        while not id.isdigit():

            print("Please Enter Numbers Only!")

            id = input("Enter Admin ID: ").strip()

            time.sleep(.4)
            print("Data analysis..""\n")

            time.sleep(1.5)

      
        if name in admins and admins[name] == id:

            print(f"Welcome Admin {name}!""\n")

            return func()
        else:

            print("Access Denied! You are not an admin.")
            
    return wrapper


def add_new_product():

        print("\n--- Add New Product ---")
        
        
        name = input("Enter product name: ").strip().capitalize()
        category = input("Enter category: ").strip().capitalize()
        price = float(input("Enter price: "))
        stock = int(input("Enter stock quantity: "))
        
    
        with open("product.json", "r", encoding="utf-8") as file:
            data = json.load(file)
        
    
        if data["products"]:
            last_product_id = data["products"][-1]["product_id"]
            new_id = last_product_id + 1
        else: 
            new_id = 1001
            
        
        new_product = {
            "product_id": new_id,
            "product_name": name,
            "category": category,
            "price": price,
            "stock": stock
        }
        
        data["products"].append(new_product)
        
        with open("product.json", "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
            
        print(f"Product '{name}' added successfully with ID: {new_id}!")

@admin_required
def admin_dashboard():

    while True:
        print("\n--- Admin Control Panel ---")
        print("1. Add New Product")
        print("2. Logout / Exit Dashboard")
        
        admin_choice = input("Choose an option: ").strip()
        
        if admin_choice == '1':
            add_new_product()  
        elif admin_choice == '2':
            print("Logging out from Admin Panel...")
            break
        else:
            print("Invalid choice, try again.")

    print("Welcome to the Admin Control Panel! You can manage products here.")



def product_generator():
  
    with open("product.json", "r", encoding="utf-8") as file:
        data = json.load(file)
        
 
    for product in data["products"]:
        yield product


def filter_products(max_price, category):

    gen = product_generator()

    for product in gen:

        if product["price"] <= max_price and product["category"] == category:

            yield product

def update_json_stock(product_id, new_stock):

    with open("product.json", "r", encoding="utf-8") as file:
        data = json.load(file)
        
    for product in data["products"]:
        if product["product_id"] == product_id:
            product["stock"] = new_stock
            break
            
    with open("product.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

while True:
    print("\n--- Welcome to Smart Store ---")
    print("1. Admin Login")
    print("2. Browse & Search Products")
    print("3. Exit")
    
    choice = input("Choose an option (1/2/3): ").strip()
    
    if choice == '1':
      
        admin_dashboard()
        
    elif choice == '2':
        try:
        
            price_input = input("Enter Maximum Price: ").strip()

            while not price_input.isdigit():

                print("Please enter numbers only for the price!")

                time.sleep(1)

                price_input = input("Enter Maximum Price: ").strip()

            max_price = float(price_input)

            category = input("Enter Category (e.g., Electronics, Accessories): ").strip().capitalize()
       
            print("\n--- Search Results ---")

            found = False

            for product in filter_products(max_price, category):
                found = True

                print(f"ID: {product['product_id']} | Name: {product['product_name']} | Price: {product['price']} | Stock: {product['stock']}")
            
            if not found:
                print("No products found matching your criteria.")
                
        except ValueError as e:
            print(f"DEBUG ERROR: {e}")
            print("Please enter a valid number for the price!")

    elif choice == '3':
        print("Thank you for using Smart Store. Goodbye!")

        break

    else:

        print("Invalid choice, please try again.")  
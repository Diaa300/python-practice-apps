from functools import wraps

def check_admin(func):

    @wraps(func)

    def wrapper(*args, **kwargs):

        user_role = input("Enter User Role (admin / user): ").strip().lower()

        if user_role == "admin":

            print("[Access granted]: Welcome, System Administrator.")

            return func(*args, **kwargs)
        
        else:

            print("[Rejected]: Prohibited, this procedure is for supervisors only!")

            return None

    return wrapper

@check_admin

def delete_product(product_id):

    print(f"Product ID {product_id} has been successfully deleted!")

    return {"status": "success"}

if __name__ == "__main__":
    delete_product(105)
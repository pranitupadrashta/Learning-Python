class Product:
    def __init__(self, product_id, name, category_id, price):
        self.product_id = product_id
        self.name = name
        self.category_id = category_id
        self.price = price

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.cart = []

class Admin:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class ShoppingCartApp:
    def __init__(self):
        self.products = []
        self.users = []
        self.admins = []
        self.logged_in_user = None
        self.logged_in_admin = None
        self.next_product_id = 1

    def add_product(self, name, category_id, price):
        product = Product(self.next_product_id, name, category_id, price)
        self.products.append(product)
        self.next_product_id += 1

    def add_user(self, username, password):
        user = User(username, password)
        self.users.append(user)

    def add_admin(self, username, password):
        admin = Admin(username, password)
        self.admins.append(admin)

    def login(self, username, password, role):
        if role == 'user':
            for user in self.users:
                if user.username == username and user.password == password:
                    self.logged_in_user = user
                    return True
        elif role == 'admin':
            for admin in self.admins:
                if admin.username == username and admin.password == password:
                    self.logged_in_admin = admin
                    return True
        return False

    def add_to_cart(self, product_id, quantity):
        if not self.logged_in_user:
            return "Please log in first."
        
        product = next((p for p in self.products if p.product_id == product_id), None)
        if product:
            self.logged_in_user.cart.append((product, quantity))
            return f"Added {quantity} {product.name}(s) to cart."
        return "Product not found."

    def remove_from_cart(self, product_id):
        if not self.logged_in_user:
            return "Please log in first."
        
        item_to_remove = None
        for item in self.logged_in_user.cart:
            if item[0].product_id == product_id:
                item_to_remove = item
                break
        
        if item_to_remove:
            self.logged_in_user.cart.remove(item_to_remove)
            return f"Removed {item_to_remove[0].name} from cart."
        return "Product not found in cart."

# Initialize the app
app = ShoppingCartApp()

# Add some products
app.add_product("Boots", "Footwear", 100)
app.add_product("Coat", "Clothing", 200)
app.add_product("Jacket", "Clothing", 150)
app.add_product("Cap", "Accessories", 50)

# Add user and admin
app.add_user("user1", "password1")
app.add_admin("admin", "adminpassword")

# Login as user
app.login("user1", "password1", "user")

# Add products to the user's cart
app.add_to_cart(1, 2)
app.add_to_cart(3, 1)

# Display user's cart
print(app.logged_in_user.cart)

# Login as admin
app.login("admin", "adminpassword", "admin")

# Try to add products (admins cannot add to cart)
app.add_to_cart(1, 1)  # This should fail

# Remove product from user's cart
app.remove_from_cart(1)

# Display updated cart
print(app.logged_in_user.cart)

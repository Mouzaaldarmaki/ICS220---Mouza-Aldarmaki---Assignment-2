class EBookStore: # EBookStore Class
    """Class representing the EBookStore."""

    def __init__(self, name: str, address: str, contact_number: str):
        # Initializes the store with name, address, and contact number
        self.__name = name  # Store name
        self.__address = address  # Store address
        self.__contact_number = contact_number  # Store contact number
        self.__ebook_list = []  # List to hold EBooks

    def add_ebook(self, ebook):
        # Adds an EBook to the store's catalog
        self.__ebook_list.append(ebook) # Append the EBook to the list

    def remove_ebook(self, ebook):
        # Removes an EBook from the store's catalog
        self.__ebook_list.remove(ebook) # Remove the specified EBook from the list

    def get_ebook_list(self):
        # Returns the list of EBooks in the store
        return self.__ebook_list # Return the list of EBooks

    def get_name(self):
        # Returns the name of the store
        return self.__name # Return the name of the store

    def get_address(self):
        # Returns the address of the store
        return self.__address # Return the address of the store

    def get_contact_number(self):
        # Returns the contact number of the store
        return self.__contact_number # Return the contact number of the store

    def __str__(self):
        # String representation of the EBookStore
        return f"EBookStore(name={self.__name}, ebooks={len(self.__ebook_list)})" # Return store details


# EBook Class
class EBook:
    """Class representing an EBook."""

    def __init__(self, title: str, author: str, publication_date: str, genre: str, price: float):
        # Initializes the EBook with title, author, publication date, genre, and price
        self.__title = title  # EBook title
        self.__author = author  # EBook author
        self.__publication_date = publication_date  # Publication date of the EBook
        self.__genre = genre  # Genre of the EBook
        self.__price = price  # Price of the EBook

    def get_title(self):
        # Returns the title of the EBook
        return self.__title # Return the title of the EBook

    def set_title(self, title: str):
        # Sets the title of the EBook
        self.__title = title # Update the title of the EBook

    def get_author(self):
        # Returns the author of the EBook
        return self.__author # Return the author of the EBook

    def set_author(self, author: str):
        # Sets the author of the EBook
        self.__author = author # Update the author of the EBook

    def get_publication_date(self):
        # Returns the publication date of the EBook
        return self.__publication_date # Return the publication date of the EBook

    def set_publication_date(self, date: str):
        # Sets the publication date of the EBook
        self.__publication_date = date # Update the publication date of the EBook

    def get_genre(self):
        # Returns the genre of the EBook
        return self.__genre # Return the genre of the EBook

    def set_genre(self, genre: str):
        # Sets the genre of the EBook
        self.__genre = genre # Update the genre of the EBook

    def get_price(self):
        # Returns the price of the EBook
        return self.__price # Return the price of the EBook

    def set_price(self, price: float):
        # Sets the price of the EBook
        self.__price = price # Update the price of the EBook

    def __str__(self):
        # String representation of the EBook
        return "EBook(title=" + self.__title + ", author=" + self.__author + ", price=" + str(self.__price) + ")" # Return details of the EBook


# SubscriptionEBook Class (inherits from EBook)
class SubscriptionEBook(EBook):
    """Class representing a Subscription EBook, inheriting from EBook."""

    def __init__(self, title: str, author: str, publication_date: str, genre: str, price: float,
                 subscription_fee: float, access_duration: int, subscription_level: str, is_active: bool):
        # Initializes the SubscriptionEBook with additional subscription details
        super().__init__(title, author, publication_date, genre, price)  # Call parent constructor to initialize inherited attributes
        self.__subscription_fee = subscription_fee  # Subscription fee for the EBook
        self.__access_duration = access_duration  # Access duration in days
        self.__subscription_level = subscription_level  # Subscription level
        self.__is_active = is_active  # Subscription status

    def get_subscription_fee(self):
        # Returns the subscription fee for the EBook
        return self.__subscription_fee # Return the subscription fee

    def set_subscription_fee(self, subscription_fee: float):
        # Sets the subscription fee for the EBook
        self.__subscription_fee = subscription_fee # Update the subscription fee

    def get_access_duration(self):
        # Returns the access duration for the EBook
        return self.__access_duration # Return the access duration

    def set_access_duration(self, access_duration: int):
        # Sets the access duration for the EBook
        self.__access_duration = access_duration # Update the access duration

    def get_subscription_level(self):
        # Returns the subscription level for the EBook
        return self.__subscription_level # Return the subscription level

    def set_subscription_level(self, subscription_level: str):
        # Sets the subscription level for the EBook
        self.__subscription_level = subscription_level # Update the subscription level

    def is_subscription_active(self):
        # Returns the active status of the subscription
        return self.__is_active # Return subscription active status

    def activate_subscription(self):
        # Activates the subscription
        self.__is_active = True # Set subscription status to active


    def __str__(self):
        # String representation of the Subscription EBook
        return "SubscriptionEBook(title=" + self.get_title() + ", subscription_fee=" + str(self.__subscription_fee) + ")" # Return details of the Subscription EBook


# Discount Class
class Discount:
    """Class representing a Discount."""

    def __init__(self, discount_type: str, value: float, is_percentage: bool = True, is_active: bool = True):
        # Initializes the Discount with type, value, and status
        self.__type = discount_type  # Type of discount (for instance, loyalty, bulk)
        self.__value = value  # Value of the discount
        self.__is_percentage = is_percentage  # Indicates if the discount is a percentage
        self.__is_active = is_active  # Status of the discount

    def apply(self, amount: float) -> float:
        # Applies the discount to a given amount and returns the discounted total
        if self.__is_percentage:
            return amount * (1 - self.__value)  # Apply percentage discount
        else:
            return amount - self.__value  # Apply fixed amount discount

    def activate(self):
        # Activates the discount
        self.__is_active = True # Set discount status to active

    def deactivate(self):
        # Deactivates the discount
        self.__is_active = False # Set discount status to inactive

    def __str__(self):
        # String representation of the Discount
        return f"Discount(type={self.__type}, value={self.__value}, is_percentage={self.__is_percentage}, is_active={self.__is_active})" # Return discount details


# ShoppingCart Class
class ShoppingCart:
    """Class representing a ShoppingCart."""

    def __init__(self, customer):
        # Initializes the ShoppingCart with an associated customer
        self.__customer = customer  # Customer associated with the cart
        self.__items = {}  # Dictionary to hold EBook items and their quantities
        self.__cart_total = 0.0  # Total cost of items in the cart

    def add_item(self, ebook, quantity):
        # Adds an EBook to the shopping cart with a specified quantity
        if ebook in self.__items:
            self.__items[ebook] += quantity  # Update quantity if EBook already in cart
        else:
            self.__items[ebook] = quantity  # Add new EBook to cart
        self.__cart_total += ebook.get_price() * quantity  # Update cart total

    def remove_item(self, ebook):
        # Removes an EBook from the shopping cart
        if ebook in self.__items:
            self.__cart_total -= ebook.get_price() * self.__items[ebook]  # Deduct from total
            del self.__items[ebook]  # Remove EBook from cart

    def update_quantity(self, ebook, quantity):
        # Updates the quantity of an EBook in the shopping cart
        if ebook in self.__items:
            self.__cart_total -= ebook.get_price() * self.__items[ebook]  # Deduct old quantity from total
            self.__items[ebook] = quantity  # Update to new quantity
            self.__cart_total += ebook.get_price() * quantity  # Update cart total

    def get_items(self):
        # Returns the list of items in the shopping cart
        return self.__items # Return the dictionary of items

    def get_customer(self):
        # Returns the customer associated with the shopping cart
        return self.__customer # Return the associated customer

    def calculate_total(self):
        # Calculates and returns the total cost of items in the cart
        return self.__cart_total # Return the total cost

    def __str__(self):
        # String representation of the ShoppingCart
        return f"ShoppingCart(customer={self.__customer}, total={self.__cart_total})" # Return shopping cart details


# Customer Class
class Customer:
    """Class representing a Customer."""

    def __init__(self, name: str, contact_info: str, loyalty_member: bool, account_balance: float):
        # Initializes the Customer with name, contact info, loyalty status, and account balance
        self.__name = name  # Customer name
        self.__contact_info = contact_info  # Customer contact information
        self.__loyalty_member = loyalty_member  # Loyalty membership status
        self.__account_balance = account_balance  # Customer account balance

    def get_name(self):
        # Returns the name of the customer
        return self.__name # Return the name of the customer

    def set_name(self, name: str):
        # Sets the name of the customer
        self.__name = name # Update the name of the customer

    def get_contact_info(self):
        # Returns the contact information of the customer
        return self.__contact_info # Return the contact information

    def set_contact_info(self, contact_info: str):
        # Sets the contact information of the customer
        self.__contact_info = contact_info # Update the contact information

    def is_loyalty_member(self):
        # Returns if the customer is a loyalty member
        return self.__loyalty_member # Return loyalty membership status

    def set_loyalty_member(self, loyalty_member: bool):
        # Sets the loyalty membership status of the customer
        self.__loyalty_member = loyalty_member # Update loyalty membership status

    def __str__(self):
        # String representation of the Customer
        return "Customer(name=" + self.__name + ", loyalty_member=" + str(self.__loyalty_member) + ")" # Return customer details


# Order Class
class Order:
    """Class representing an Order."""

    def __init__(self, customer, order_id: str, order_date: str):
        # Initializes the Order with customer, order ID, and order date
        self.__customer = customer  # Customer placing the order
        self.__order_id = order_id  # Unique order ID
        self.__order_date = order_date  # Date of the order
        self.__items = {}  # Dictionary to hold EBook items and their quantities
        self.__discounts = []  # List to hold applied discounts
        self.__total_amount = 0.0  # Total amount of the order

    def add_item(self, ebook, quantity: int = 1):
        # Adds an EBook to the order with the specified quantity
        if ebook in self.__items:
            self.__items[ebook] += quantity  # Update quantity if EBook already in order
        else:
            self.__items[ebook] = quantity  # Add new EBook to order
        self.__total_amount += ebook.get_price() * quantity  # Update total amount

    def add_discount(self, discount):
        # Adds a discount to the order
        self.__discounts.append(discount)  # Append discount to list

    def apply_discounts(self):
        # Applies all discounts to the total amount and returns the discounted total
        for discount in self.__discounts:
            self.__total_amount = discount.apply(self.__total_amount)  # Apply each discount
        return self.__total_amount # Return the total after discounts

    def calculate_total(self):
        # Calculates the total after applying any discounts
        return self.__total_amount # Return the total amount

    def get_order_id(self):
        # Returns the unique order ID
        return self.__order_id # Return the order ID

    def get_customer(self):
        # Returns the customer associated with the order
        return self.__customer # Return the associated customer

    def get_items(self):
        # Returns the items in the order
        return self.__items # Return the dictionary of items

    def __str__(self):
        # String representation of the Order
        return f"Order(id={self.__order_id}, customer={self.__customer.get_name()}, total={self.calculate_total()})" # Return order details


# Payment Class
class Payment:
    """Class representing a Payment."""

    def __init__(self, order, amount: float, payment_date: str, payment_method: str):
        # Initializes the Payment with the order, amount, date, and method
        self.__order = order  # Associated order
        self.__amount = amount  # Payment amount
        self.__payment_date = payment_date  # Date of payment
        self.__payment_method = payment_method  # Payment method used

    def process_payment(self):
        # Processes the payment (mock implementation)
        return True  # Indicates successful payment processing

    def __str__(self):
        # String representation of the payment details in the specified format
        return (
            f"Payment details:\n"
            f"order_id: {self.__order.get_order_id()}\n"
            f"customer: {self.__order.get_customer().get_name()}\n"
            f"total: {self.__order.calculate_total():.3f}\n"
            f"amount: {self.__amount:.5f}\n"
            f"payment method: {self.__payment_method}" # Return payment details
        )


# Invoice Class
class Invoice:
    """Class representing an Invoice."""

    def __init__(self, order, store, vat: float = 0.08):
        # Initializes the Invoice with the order, store, and VAT rate
        self.__order = order  # Associated order
        self.__store = store  # EBookStore information
        self.__customer_name = order.get_customer().get_name()  # Customer name from the order
        self.__customer_contact = order.get_customer().get_contact_info()  # Customer contact from the order
        self.__vat = vat  # VAT rate
        self.__total_with_vat = self.calculate_total_with_vat()  # Total amount including VAT

    def calculate_total_with_vat(self):
        # Calculates the total amount with VAT applied
        base_total = self.__order.calculate_total()  # Get base total
        return base_total * (1 + self.__vat)  # Calculate total with VAT

    def __str__(self):
        # Detailed string representation of the Invoice
        greeting = f"Hello from {self.__store.get_name()}!"  # Greeting from the store
        address = f"Address: {self.__store.get_address()}"  # Store address
        contact = f"Contact: {self.__store.get_contact_number()}"  # Store contact

        # Customer information
        customer_info = f"Customer Name: {self.__customer_name}\nContact: {self.__customer_contact}"

        # Order details
        order_details = "Order Summary:\n"
        for ebook, quantity in self.__order.get_items().items():
            item_total = ebook.get_price() * quantity  # Calculate item total
            order_details += f" - {ebook.get_title()} (x{quantity}): ${item_total:.2f}\n"  # Add item details

        # Total cost with discounts and VAT
        subtotal = f"Subtotal after discounts: ${self.__order.calculate_total():.2f}"  # Subtotal
        vat_amount = f"VAT (8%): ${(self.__total_with_vat - self.__order.calculate_total()):.2f}"  # VAT amount
        total = f"Total with VAT: ${self.__total_with_vat:.2f}"  # Total amount with VAT

        return (
            f"{greeting}\n{address}\n{contact}\n\n"
            f"{customer_info}\n\n{order_details}\n"
            f"{subtotal}\n{vat_amount}\n{total}\n"
        ) # Return formatted invoice details

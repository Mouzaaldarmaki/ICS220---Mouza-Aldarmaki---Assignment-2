from Ebook_Store import * # Import all classes and functions from the Ebook_Store module

# Test script to demonstrate the functionality of the EBookStore system
if __name__ == "__main__": # Check if this script is being run directly
    # Create an instance of EBookStore with a name, address, and contact number
    store = EBookStore("The Great E-books Store", "123 Book St", "123-456-7890")

    # Create some EBooks with title, author, publication date, genre, and price
    ebook1 = EBook("To Kill a Mockingbird", "Harper Lee", "1960", "Southern Gothic", 15.99)
    ebook2 = EBook("1984", "George Orwell", "1949", "Dystopian Fiction", 10.99)
    ebook3 = EBook("Get Good with Money", "Tiffany Aliche", "2021", "Self-Help", 18.99)
    ebook4 = EBook("Atomic Habits", "James Clear", "2018", "Self-Help", 29.99)
    ebook5 = EBook("The Silent Patient", "Alex Michaelides", "2019", "Psychological Thriller", 49.99)

    # Create some Subscription EBooks with additional details such as subscription fee and duration
    subscription_ebook1 = SubscriptionEBook("The 7 Habits of Highly Effective People", "Stephen Covey", "1989",
                                            "Self-Help", 20.99, 4.99, 30, "Basic", True)
    subscription_ebook2 = SubscriptionEBook("Thinking, Fast and Slow", "Daniel Kahneman", "2011", "Psychology", 29.99,
                                            5.99, 60, "Premium", False)

    # Add EBooks and Subscription EBooks to the store's catalog
    store.add_ebook(ebook1) # Add the first EBook
    store.add_ebook(ebook2) # Add the second EBook
    store.add_ebook(ebook3) # Add the third EBook
    store.add_ebook(ebook4) # Add the fourth EBook
    store.add_ebook(ebook5) # Add the fifth EBook
    store.add_ebook(subscription_ebook1) # Add the first Subscription EBook
    store.add_ebook(subscription_ebook2) # Add the second Subscription EBook

    # Display EBookStore information and available EBooks
    print(f"\n=== Welcome to {store.get_name()} ===") # Print the store's name
    print(f"Address: {store.get_address()}") # Print the store's address
    print(f"Contact: {store.get_contact_number()}") # Print the store's contact number
    print("\nAvailable EBooks:") # Header for available EBooks
    for ebook in store.get_ebook_list(): # Iterate through the list of EBooks
        print(f"Title: '{ebook.get_title()}', Author: {ebook.get_author()}, Price: ${ebook.get_price():.2f}") # Print details of each EBook

    # Create a list of customers with name, email, loyalty status, and account balance
    customers = [
        Customer("Mouza Aldarmaki", "202215015@zu.ac.ae", True, 100.00),
        Customer("Alyazia Mohamed", "202217371@zu.ac.ae", False, 50.00),
        Customer("Sara", "202124567@zu.ac.ae", False, 30.00),
        Customer("Shaikha", "202333001@zu.ac.ae", True, 75.00)
    ]

    # Initialize Shopping Cart for each customer using dictionary comprehension
    carts = {customer.get_name(): ShoppingCart(customer) for customer in customers}

    # Actions for Mouza Aldarmaki
    print(f"\n=== Actions ===") # Header for actions
    print(f"Customer Name: {customers[0].get_name()}") # Print the customer's name

    # Add items to Mouza's shopping cart
    carts["Mouza Aldarmaki"].add_item(ebook2, 2)  # Add 2 copies of '1984'
    carts["Mouza Aldarmaki"].add_item(ebook3, 1)  # Add 1 copy of 'Get Good with Money'
    carts["Mouza Aldarmaki"].add_item(subscription_ebook1, 1)  # Add 1 Subscription EBook
    print("Shopping Cart Items after adding:") # Header for added items
    for ebook, quantity in carts["Mouza Aldarmaki"].get_items().items(): # Iterate through items in the cart
        print(f"{ebook.get_title()} - Quantity: {quantity}") # Print each item's title and quantity

    carts["Mouza Aldarmaki"].remove_item(ebook2)  # Remove one copy of '1984'
    print("\nShopping Cart Items after removing one copy of '1984':") # Header for items after removal
    for ebook, quantity in carts["Mouza Aldarmaki"].get_items().items(): # Iterate through remaining items in the cart
        print(f"{ebook.get_title()} - Quantity: {quantity}") # Print each item's title and quantity


    # Modify customer account
    customers[0].set_contact_info("mouza.newemail@zu.ac.ae")  # Change email address
    print(f"\nCustomer account: ") # Header for customer account details
    print(f"Updated Email: {customers[0].get_contact_info()}") # Print updated email
    customers[0].set_loyalty_member(False)  # Change loyalty member status
    print(f"Updated Loyalty Status: {'Loyalty Member' if customers[0].is_loyalty_member() else 'Not a Loyalty Member'}") # Print updated loyalty status

    # Prepare and print the order summary for Mouza
    order1 = Order(customers[0], "ORD001", "2024-11-06") # Create an order for Mouza
    for ebook, quantity in carts["Mouza Aldarmaki"].get_items().items(): # Iterate through items in the cart
        order1.add_item(ebook, quantity) # Add each item to the order

    print("\n=== Order Summary ===") # Header for order summary
    print(f"Customer Name: {customers[0].get_name()}") # Print customer name in the order summary
    for ebook, quantity in order1.get_items().items(): # Iterate through items in the order
        print(f"{ebook.get_title()} - Quantity: {quantity}") # Print each item's title and quantity

    total_after_discounts = order1.apply_discounts()  # Apply discounts to the order
    print(f"Total after discounts: ${total_after_discounts:.2f}") # Print total after discounts

    # Generate and print invoice for Mouza
    invoice1 = Invoice(order1, store) # Create an invoice for the order
    print(f"\n=== Invoice ===") # Header for invoice
    print(invoice1) # Print invoice details

    # Process payment for Mouza's order
    payment1 = Payment(order1, total_after_discounts, "2024-11-06", "Credit Card") # Create a payment for the order
    payment1.process_payment()  # Process the payment (mock implementation)
    print(f"Payment processed successfully using Credit Card.") # Confirm payment success

    # Actions for Alyazia Mohamed
    print(f"\n=== Actions ===") # Header for actions
    print(f"Customer Name: {customers[1].get_name()}") # Print the customer's name

    # Add items to Alyazia's shopping cart
    carts["Alyazia Mohamed"].add_item(ebook3, 1)  # Add 1 copy of 'Get Good with Money'
    carts["Alyazia Mohamed"].add_item(ebook4, 1)  # Add 1 copy of 'Atomic Habits'
    carts["Alyazia Mohamed"].add_item(subscription_ebook2, 1)  # Add 1 Subscription EBook
    print("Shopping Cart Items after adding:") # Header for added items
    for ebook, quantity in carts["Alyazia Mohamed"].get_items().items(): # Iterate through items in the cart
        print(f"{ebook.get_title()} - Quantity: {quantity}") # Print each item's title and quantity

    # Remove an item from Alyazia's cart
    carts["Alyazia Mohamed"].remove_item(ebook3)  # Remove 'Get Good with Money'
    print("\nShopping Cart Items after removing 'Get Good with Money':") # Header for items after removal
    for ebook, quantity in carts["Alyazia Mohamed"].get_items().items(): # Iterate through remaining items in the cart
        print(f"{ebook.get_title()} - Quantity: {quantity}") # Print each item's title and quantity

    # Modify customer account details
    customers[1].set_contact_info("alyazia.aladawi@zu.ac.ae")  # Change email address
    print(f"\nCustomer account: ") # Header for customer account details
    print(f"Updated Email: {customers[1].get_contact_info()}") # Print updated email
    customers[1].set_loyalty_member(True)  # Change loyalty member status
    print(f"Updated Loyalty Status: {'Loyalty Member' if customers[1].is_loyalty_member() else 'Not a Loyalty Member'}") # Print updated loyalty status

    # Prepare and print the order summary for Alyazia
    order2 = Order(customers[1], "ORD002", "2024-11-06") # Create an order for Alyazia
    for ebook, quantity in carts["Alyazia Mohamed"].get_items().items():# Iterate through items in the cart
        order2.add_item(ebook, quantity) # Add each item to the order

    print("\n=== Order Summary ===") # Header for order summary
    print(f"Customer Name: {customers[1].get_name()}") # Print customer name in the order summary
    for ebook, quantity in order2.get_items().items(): # Iterate through items in the order
        print(f"{ebook.get_title()} - Quantity: {quantity}") # Print each item's title and quantity

    total_after_discounts = order2.apply_discounts()  # No loyalty discount for Alyazia
    print(f"Total after discounts for Alyazia Mohamed: ${total_after_discounts:.2f}") # Print total after discounts

    # Generate and print invoice for Alyazia
    invoice2 = Invoice(order2, store) # Create an invoice for the order
    print(f"\n=== Invoice ===") # Header for invoice
    print(invoice2) # Print invoice details

    # Process payment for Alyazia's order
    payment2 = Payment(order2, total_after_discounts, "2024-11-06", "Apple Pay") # Create a payment for the order
    payment2.process_payment()  # Process the payment (mock implementation)
    print(f"Payment processed successfully using Apple Pay.") # Confirm payment success

    # Actions for Sara
    print(f"\n=== Actions ===") # Header for actions
    print(f"Customer Name: {customers[2].get_name()}") # Print the customer's name

    # Add items to Sara's shopping cart
    carts["Sara"].add_item(ebook4, 1)  # Add 1 copy of 'Atomic Habits'
    carts["Sara"].add_item(ebook5, 1)  # Add 1 copy of 'The Silent Patient'
    print("Shopping Cart Items after adding:") # Header for added items
    for ebook, quantity in carts["Sara"].get_items().items(): # Iterate through items in the cart
        print(f"{ebook.get_title()} - Quantity: {quantity}") # Print each item's title and quantity

    # Remove an item from Sara's cart
    carts["Sara"].remove_item(ebook4)  # Remove 'Atomic Habits'
    print("\nShopping Cart Items after removing 'Atomic Habits':") # Header for items after removal
    for ebook, quantity in carts["Sara"].get_items().items(): # Iterate through remaining items in the cart
        print(f"{ebook.get_title()} - Quantity: {quantity}") # Print each item's title and quantity

    # Modify customer account details
    customers[2].set_contact_info("sara.mohammed@zu.ac.ae")  # Change email address
    print(f"\nCustomer account: ") # Header for customer account details
    print(f"Updated Email: {customers[2].get_contact_info()}") # Print updated email
    customers[2].set_loyalty_member(True)  # Change loyalty member status
    print(f"Updated Loyalty Status: {'Loyalty Member' if customers[2].is_loyalty_member() else 'Not a Loyalty Member'}") # Print updated loyalty status

    # Prepare and print the order summary for Sara
    order3 = Order(customers[2], "ORD003", "2024-11-06") # Create an order for Sara
    for ebook, quantity in carts["Sara"].get_items().items(): # Iterate through items in the cart
        order3.add_item(ebook, quantity) # Add each item to the order

    print("\n=== Order Summary ===") # Header for order summary
    print(f"Customer Name: {customers[2].get_name()}") # Print customer name in the order summary
    for ebook, quantity in order3.get_items().items(): # Iterate through items in the order
        print(f"{ebook.get_title()} - Quantity: {quantity}") # Print each item's title and quantity

    total_after_discounts = order3.apply_discounts()  # No loyalty discount for Sara
    print(f"Total after discounts: ${total_after_discounts:.2f}") # Print total after discounts

    # Generate and print invoice for Sara
    invoice3 = Invoice(order3, store) # Create an invoice for the order
    print(f"\n=== Invoice ===") # Header for invoice
    print(invoice3) # Print invoice details

    # Process payment for Sara's order
    payment3 = Payment(order3, total_after_discounts, "2024-11-06", "Apple Pay") # Create a payment for the order
    payment3.process_payment()  # Process the payment (mock implementation)
    print(f"Payment processed successfully using Apple Pay.") # Confirm payment success

    # Actions for Shaikha
    print(f"\n=== Actions ===") # Header for actions
    print(f"Customer Name: {customers[3].get_name()}") # Print the customer's name

    # Add items to Shaikha's shopping cart
    carts["Shaikha"].add_item(ebook1, 1)  # Add 1 copy of 'To Kill a Mockingbird'
    carts["Shaikha"].add_item(ebook2, 1)  # Add 1 copy of '1984'
    print("Shopping Cart Items after adding:") # Header for added items
    for ebook, quantity in carts["Shaikha"].get_items().items(): # Iterate through items in the cart
        print(f"{ebook.get_title()} - Quantity: {quantity}") # Print each item's title and quantity

    # Remove an item from Shaikha's cart
    carts["Shaikha"].remove_item(ebook1)  # Remove 'To Kill a Mockingbird'
    print("\nShopping Cart Items after removing 'To Kill a Mockingbird':") # Header for items after removal
    for ebook, quantity in carts["Shaikha"].get_items().items(): # Iterate through remaining items in the cart
        print(f"{ebook.get_title()} - Quantity: {quantity}") # Print each item's title and quantity

    # Modify customer account to activate subscription
    subscription_ebook1.activate_subscription() # Activate subscription for the specified EBook
    print(f"Subscription for {subscription_ebook1.get_title()} has been activated for {customers[3].get_name()}.") # Confirm subscription activation

    customers[3].set_contact_info("shaikha.newemail@zu.ac.ae")  # Change email address
    print(f"\nCustomer account: ") # Header for customer account details
    print(f"Updated Email: {customers[3].get_contact_info()}") # Print updated email
    customers[3].set_loyalty_member(False)  # Change loyalty member status
    print(f"Updated Loyalty Status: {'Loyalty Member' if customers[3].is_loyalty_member() else 'Not a Loyalty Member'}") # Print updated loyalty status

    # Prepare and print the order summary for Shaikha
    order4 = Order(customers[3], "ORD004", "2024-11-06") # Create an order for Shaikha
    for ebook, quantity in carts["Shaikha"].get_items().items(): # Iterate through items in the cart
        order4.add_item(ebook, quantity) # Add each item to the order

    print("\n=== Order Summary ===") # Header for order summary
    print(f"Customer Name: {customers[3].get_name()}") # Print customer name in the order summary
    for ebook, quantity in order4.get_items().items(): # Iterate through items in the order
        print(f"{ebook.get_title()} - Quantity: {quantity}") # Print each item's title and quantity

    total_after_discounts = order4.apply_discounts()  # No loyalty discount for Shaikha
    print(f"Total after discounts: ${total_after_discounts:.2f}") # Print total after discounts

    # Generate and print invoice for Shaikha
    invoice4 = Invoice(order4, store) # Create an invoice for the order
    print(f"\n=== Invoice ===") # Header for invoice
    print(invoice4) # Print invoice details

    # Process payment for Shaikha's order
    payment4 = Payment(order4, total_after_discounts, "2024-11-06", "Credit Card") # Create a payment for the order
    payment4.process_payment()  # Process the payment (mock implementation)
    print(f"Payment processed successfully using Credit Card.") # Confirm payment success

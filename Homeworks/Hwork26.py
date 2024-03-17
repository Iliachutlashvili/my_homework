# # დავალება 1

# class User:
#     def __init__(self, name):
#         self.name = name

#     def get_name(self):
#         return self.name


# class Storage:
#     def save(self, data):
#         print("Saving data to storage:", data)
#         pass


# class HttpConnection:
#     def send(self, data):
#         print("Sending data to HTTP connection:", data)
#         pass


# class Logger:
#     def log(self, message):
#         print("Logging message:", message)
#         pass


# user = User("John")
# storage = Storage()
# http_connection = HttpConnection()
# logger = Logger()

# user_name = user.get_name()
# storage.save(user_name)
# http_connection.send(user_name)
# logger.log("User data sent successfully.")


# # ----------------------------------------------------------------------------------------------------

# # დავალება 2 

class Discount:
    def __init__(self, customer, price):
        self.customer = customer
        self.price = price

    def give_discount(self):
        if self.customer == 'favourite':
            return self.price * 0.2
        elif self.customer == 'vip':
            return self.price * 0.4
        else:
            return 0 


class VIPDiscount(Discount):
    def give_discount(self):
        if self.customer == 'vip':
            return self.price * 0.4  
        else:
            return super().give_discount()


# Example usage
regular_customer_discount = Discount('regular', 100)
print("Regular Customer Discount:", regular_customer_discount.give_discount())

favorite_customer_discount = Discount('favourite', 100)
print("Favorite Customer Discount:", favorite_customer_discount.give_discount())

vip_customer_discount = VIPDiscount('vip', 100)
print("VIP Customer Discount:", vip_customer_discount.give_discount())
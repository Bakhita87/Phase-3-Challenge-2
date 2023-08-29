from Restaurant.customer import Customer
from Restaurant.restaurant import Restaurant
from Restaurant.review import Review


customer = Customer("Bakhita", "Otieno")
customer2= Customer("Wendy", "Otieno")
restaurant=Restaurant("Honey and Dough")
restaurant2=Restaurant("Bambino")

review = Review(customer, restaurant, 5)
review2 = Review (customer2 ,restaurant2,4.5)



restaurant = Restaurant()
# rating = Review(5)



# print (customer.name + ' ' + customer.familyname)
print (customer.get_name())
print (customer.get_familyname())
print (customer.get_fullname())
print (customer2.get_name())
print (customer2.get_familyname())
print (customer2.get_fullname())
print(restaurant.name)
print(restaurant2.name)
print(review.get_rating())
print(review2.get_rating())


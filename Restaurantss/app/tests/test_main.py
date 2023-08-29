from typing import Self
from Restaurant.customer import Customer
from Restaurant.restaurant import Restaurant
from Restaurant.review import Review

import unittest 

class CustomerTest(unittest.TestCase):
    customer= Customer("Bakhita", "Otieno")
    customer2=Customer("Wendy" , "Otieno")
    Self.assertEqual(customer.name,"Bakhita")
    Self.assertEqual(customer.familyname,"Otieno")
    Self.assertEqual(customer2.name,"Wendy")
    Self.assertEqual(customer2.familyname,"Otieno")

def test_given_name(self):
    customer =Customer("Bakhita", "Otieno")
    customer2=Customer("Wendy", "Otieno")
    self.assertEqual(customer.name, "Bakhita")
    customer2.name = "Wendy"
    self.assertEqual(customer2.name, "Otieno")

def test_familyname(self):
        customer = Customer("Bakhita", "Otieno")
        customer2=Customer("Wendy","Otieno")
        self.assertEqual(customer.familyname, "Otieno")
        customer2.familyname = "Otieno"
        self.assertEqual(customer2.familyname, "Otieno")

def test_full_name(self):
        customer = Customer("Bakhita", "Otieno")
        customer2=Customer("Wendy","Otieno")
        self.assertEqual(customer.fullname(), "Bakhita Otieno")
        customer2.name = "Wendy"
        self.assertEqual(customer2.fullname(), "Wendy Otieno")
      
def test_all(self):
        customer = Customer("Bakhita", "Otieno")
        customer2 = Customer("Wendy", "Otieno")
        customers = Customer.all()
        self.assertEqual(customers, [customer, customer2])


class ReviewTest(unittest.TestCase):

    def test_init(self):
        customer= Customer("Bakhita", "Otieno")
        restaurant = Restaurant("Honey and Dough")
        review = Review(customer, restaurant, 5)
        self.assertEqual(review.rating, 5)
        customer2=Customer("Wendy", "Otieno")
        restaurant2=Restaurant("Bakhita Otieno")
        review2=Review(customer2, restaurant2,4.5)
        self.assertEqual(review2.rating,4.5)

class RestaurantTest(unittest.TestCase):

    def test_init(self):
        restaurant = Restaurant("Honey and Dough")
        self.assertEqual(restaurant.name, "Honey and Dough")

    def test_name(self):
        restaurant = Restaurant("Honey and Dough")
        restaurant2= Restaurant("Bambino")
        self.assertEqual(restaurant.name, "Honey and Dough")
        restaurant2.name = "Bambino"
        self.assertEqual(restaurant2.name, "Bambino")



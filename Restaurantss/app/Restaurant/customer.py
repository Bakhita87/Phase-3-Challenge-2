

class Customer:
    all_customers = []


    def __init__(self, name , familyname):
        self.name = name
        self.familyname = familyname
        self.reviews = []
        self.restaurant = []

    def get_name(self):
        return self.name
    
    def get_familyname(self):
        return self.familyname
    
    def get_fullname(self):
        return f"{self.name} {self.familyname}"
    
    def add_reviews(self, reviews, restaurant):
        return self.add_reviews(reviews, restaurant)
    
    def restaurant(self):
        return set(self.restaurant)
    
   
    @classmethod
    def all(self):
        return self.all_customers

    
        
customer = Customer("","")
customer2 = Customer("","")

def num_reviews(self):
    return len(self.reviews)


@classmethod
def find_by_name(self, name):
    for customer in self.all_customers:
        if customer.fullname() == name:
            return customer
    return None

@classmethod
def find_all_by_name(self, name):
    return [customer for customer in self.all_customers if customer.name == name]








class Restaurant:

    def __init__(self, name = "Honey and Dough" ):
        self.name = name
        self.customer = []
        self.reviews = []

    def name(self):
        return self.name

    def add_review(self, reviews, customer) :
        return self.add_review(reviews,customer)
    
    


restaurant = Restaurant()
restaurant2 = Restaurant()
print(restaurant.name)

# def average_star_rating(self):
#     total_reviews = sum([review.rating for review in self.reviews()])
#     num_reviews = len(self.reviews())
#     if num_reviews == 0:
#         return 0
#     return total_reviews / num_reviews


class Review:
    all_reviews = []

   
    def __init__(self,customer , restaurant , rating = 5 ):
       self.customer = customer
       self.restaurant = restaurant
       self.rating = rating
       Review.all_reviews.append(self)
      
    def get_rating(self):
        return self.rating
    
   
    @classmethod
    def all(self):
        return self.all_reviews



def customer(self):
    return self.customer

def restaurant(self):
    return self.restaurant



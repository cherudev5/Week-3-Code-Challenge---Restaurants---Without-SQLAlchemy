import sqlite3


# Connect to SQLite database
CONN = sqlite3.connect('Reviews.db')
CUR = CONN.cursor()
# Restaurant class
class Restaurant:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def reviews(self):
        CUR.execute("SELECT * FROM reviews WHERE restaurant_id = ?", (self.id,))
        return CUR.fetchall()

    def customers(self):
        CUR.execute("SELECT DISTINCT customers.* FROM customers JOIN reviews ON customers.id = reviews.customer_id WHERE reviews.restaurant_id = ?", (self.id,))
        return CUR.fetchall()

    @classmethod
    def fanciest(cls):
        CUR.execute("SELECT * FROM restaurants ORDER BY price DESC LIMIT 1")
        result = CUR.fetchone()
        return cls(result[1], result[2])

    def all_reviews(self):
        CUR.execute("SELECT reviews.star_rating, customers.first_name, customers.last_name FROM reviews JOIN customers ON reviews.customer_id = customers.id WHERE reviews.restaurant_id = ?", (self.id,))
        reviews = CUR.fetchall()
        formatted_reviews = [f"Review for {self.name} by {review[1]} {review[2]}: {review[0]} stars." for review in reviews]
        return formatted_reviews
# Customer class
class Customer:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def reviews(self):
        CUR.execute("SELECT * FROM reviews WHERE customer_id = ?", (self.id,))
        return CUR.fetchall()

    def restaurants(self):
        CUR.execute("SELECT DISTINCT restaurants.* FROM restaurants JOIN reviews ON restaurants.id = reviews.restaurant_id WHERE reviews.customer_id = ?", (self.id,))
        return CUR.fetchall()

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def favorite_restaurant(self):
        CUR.execute("SELECT restaurants.*, MAX(reviews.star_rating) FROM restaurants JOIN reviews ON restaurants.id = reviews.restaurant_id WHERE reviews.customer_id = ?", (self.id,))
        result = CUR.fetchone()
        return Restaurant(result[1], result[2])

    def add_review(self, restaurant, rating):
        CUR.execute("INSERT INTO reviews (restaurant_id, customer_id, star_rating) VALUES (?, ?, ?)", (restaurant.id, self.id, rating))
        CONN.commit()

    def delete_reviews(self, restaurant):
        CUR.execute("DELETE FROM reviews WHERE customer_id = ? AND restaurant_id = ?", (self.id, restaurant.id))
        CONN.commit()
# Review class
class Review:
    def __init__(self, restaurant, customer, star_rating):
        self.restaurant = restaurant
        self.customer = customer
        self.star_rating = star_rating

    def customer(self):
        return self.customer

    def restaurant(self):
        return self.restaurant

    def full_review(self):
        return f"Review for {self.restaurant.name} by {self.customer.full_name()}: {self.star_rating} stars."

# Commit changes and close connection
CONN.commit()
CONN.close()

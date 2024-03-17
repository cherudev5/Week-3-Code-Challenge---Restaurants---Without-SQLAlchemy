import sqlite3

CONN= sqlite3.connect('RestaurantTable.db')
CUR = CONN.cursor()

# CONN.execute("""CREATE TABLE RestaurantTable (
#     id INTEGER PRIMARY KEY,
#     name STRING,
#     price INTEGER
#     );
#             """)

class RestaurantTables:
    def __init__(self, name, price,id):
        self.name = name
        self.price = price
        self.id = id

    def save(self): # instance method
        query_stat = f"""
        INSERT INTO RestaurantTables (name, price, id)
                VALUES ('{self.name}', {self.price}, '{self.id})
        """
        CUR.execute(query_stat)
        CONN.commit()

# create a cat instance
RestaurantTable1 = RestaurantTables('Pronto', 600,  1)
RestaurantTable2 = RestaurantTables('Pronto', 400,  1)
RestaurantTable3 = RestaurantTables('Lazarus', 300,  2)
RestaurantTable4 = RestaurantTables('Mist', 1000,  3)
RestaurantTable1.save()
RestaurantTable2.save()
RestaurantTable3.save()
RestaurantTable4.save()
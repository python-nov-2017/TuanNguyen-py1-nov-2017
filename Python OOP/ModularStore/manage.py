from product import Product
from store import Store

item1 = Product("Laptop", 600, "3lbs", "LG")
item2 = Product("PC", 600, "3lbs", "HP")

store = Store([item1, item2], "VA", "Minh")
store.inventory()
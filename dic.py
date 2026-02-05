
pizza = {
    'name': 'Margherita Pizza',
    'price': 8.9,
    'calories_per_slice': 250
}

print(pizza.keys())
# dict_keys(['name', 'price', 'calories_per_slice'])

print(pizza.values())
# dict_values(['Margherita Pizza', 8.9, 250])

print(pizza.items())
# dict_items([('name', 'Margherita Pizza'), ('price', 8.9), ('calories_per_slice', 250)])

print(pizza.clear())

print(pizza.pop('price', 10))
print(pizza.update({ 'price': 15, 'total_time': 25 }))


products = {
    'Laptop': 990,
    'Smartphone': 600,
    'Tablet': 250,
    'Headphones': 70,
}

for price in products.values():
    print(price)

for product in products.keys(): # for product in products:
                                    # print(product)
    print(product)

for product in products.items():
    print(product)

for product, price in products.items():
    print(product, price)

for index, product in enumerate(products.items()):
    print(index, product)

for index, product in enumerate(products.items(), 1):
    print(index, product)

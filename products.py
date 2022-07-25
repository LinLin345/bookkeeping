
import os
products = []

# check the file if exit
# read file and split
if os.path.isfile('products.csv'):
    print("You have found this file!")
    with open('products.csv', 'r', encoding='utf-8') as f:
        for line in f:
            # use continue to jump to next circle in for
            if "products, price" in line:
                continue
            product, price = line.strip().split(',')
            p = [product, price]
            products.append(p)
    print(products)
else:
    print('Can not find this file')

# if don't known the time of loop , chose while loop
# input product and price
products = []
while True:
    name = input("Please input the name of product")
    if name == "q":
        break
    price = input("Please input the price")
    p = [name, price]
    products.append(p)
print(products)

# for loop to find every one
for p in products:
    print("The price of ", p[0], "is", p[1])

# save and write the product to csv file
# add colum name
with open("products.csv", "w", encoding="utf-8") as f:
    f.write('products, price\n')
    for p in products:
        f.write(p[0] + "," + p[1] + "\n")
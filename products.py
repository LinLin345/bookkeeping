# if don't known the time of loop , chose while loop
product = []
while True:
    name = input("Please input the name of product")
    if name == "q":
        break
    price = input("Please input the price")
    p = [name, price]
    product.append(p)
print(product)

# for loop to find every one 
for p in product:
    print("The price of ",p[0],"is", p[1])
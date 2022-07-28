
import os


def read_file(filename, products):
    # check the file if exist
    # read file and split
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            # use continue to jump to next circle in for
            if "products, price" in line:
                continue
            product, price = line.strip().split(',')
            p = [product, price]
            products.append(p)
    print(products)
    return products


def input_products( products):
    # if don't known the time of loop , chose while loop
    # input product and price
    while True:
        name = input("Please input the name of product")
        if name == "q":
            break
        price = input("Please input the price")
        p = [name, price]
        products.append(p)
    print(products)
    return products


def add_colum(filename,products):
    # save and write the product to csv file
    # add colum name
    with open(filename, "w", encoding="utf-8") as f:
        f.write('products, price\n')
        for p in products:
            f.write(p[0] + "," + p[1] + "\n")


def main():
    filename = 'products.csv'
    products = []
    if os.path.isfile(filename):
        print("You have found this file!")
        products = read_file(filename, products)
    else:
        print('Can not find this file')
    products = input_products(products)
    add_colum(filename,products)
    for p in products:
        print("The price of ", p[0], "is", p[1])
    return products


main()

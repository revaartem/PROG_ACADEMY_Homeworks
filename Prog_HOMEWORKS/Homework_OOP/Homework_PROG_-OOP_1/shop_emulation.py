
from class_Product import Product
from class_Buyer import Buyer
from class_Order import Order

if __name__ == "__main__":
    buyer_1 = Buyer('Anton', 'Golovin', 'Kiev', 88005553535, False)
    buyer_2 = Buyer('Nikola', 'Tesla', 'Lviv', 38099556874, True)
    buyer_3 = Buyer('Tom', 'Hanks', 'New York', 55577789, True)
    print(f"""
    {buyer_1}
    {buyer_2}
    {buyer_3}""")

    product_1 = Product('Mazda MX-5', '2005', '1240', 15000, '3915 x 1735 x 1225', 'JP')
    product_2 = Product('Kia Ceed', '2009', '1540', 7300, '4605 x 1800 x 1475', 'SL')
    product_3 = Product('Mercedes S-klass', '2015', '1945', 45000, '6499 x 1899 x 1598', 'DE')
    print(f"""
    {product_1}
    {product_2}
    {product_3}""")

    products = [product_1, product_2, product_3]

    order_1 = Order(buyer_1)
    order_1.making_order(products, buyer_1, order_1)

    order_2 = Order(buyer_2)
    order_2.making_order(products, buyer_2, order_2)

    order_3 = Order(buyer_3)
    order_3.making_order(products, buyer_3, order_3)

    for name, count, price in order_1:
        print(name, count, price)

    print(f"""
    {order_1}
    {order_2}
    {order_3}""")

    print(order_1['Kia Ced'])

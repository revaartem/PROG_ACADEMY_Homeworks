import customer_class
import order_class
import pizzeria_class

if __name__ == "__main__":
    main_pizzeria = pizzeria_class.Pizzeria('Don Corleone')
    customer = customer_class.Customer('Artem', 380994567842, 'Freedom Sq, 13, ap. 46')
    order_1 = order_class.Order(customer, main_pizzeria)
    order_1.add_to_order('sunday', 4, 0, 9)
    order_1.add_to_order('monday', 7, 3, 2, 4)
    order_1.add_to_order('tuesday', 3, 3, 2, 4)
    order_1.add_to_order('wednesday', 5, 3, 2, 4, '9:00 AM')
    order_1.add_to_order('thursday', 8, 3, 2, 4)
    order_1.add_to_order('friday', 11, 3, 2, 4)
    print(order_1)
    # print(main_pizzeria)

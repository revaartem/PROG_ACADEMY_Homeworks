from datetime import datetime


class Event:
    """
    Instance class Event have all information about event.
    """

    def __init__(self, name: str, date: tuple, time: str, location: str, price: int, quantity_of_seats: int):
        """

        :param name: Event name
        :param date: Event date in format (yyyy, mm, dd), where yyyy - year, mm - month, dd - day.
        :param time: Event time in format 'hh:mm', where hh - hours, mm - minutes.
        :param location: Event location
        :param price: Price of 1 regular ticket
        :param quantity_of_seats: Number of seats
        """
        self.name = name
        if len(date) == 3:
            self.date = datetime(date[0], date[1], date[2])
        self.time = time
        self.location = location
        self.price = price
        self.cash_desk = 0
        self.quantity_and_types_of_sold_tickets = {
            'regular': 0,
            'advance': 0,
            'late': 0,
            'student': 0,
        }
        self.quantity_of_seats = quantity_of_seats
        self.available_seats = self.quantity_of_seats

    def __str__(self):
        res = '\n'.join(f'{key} - {value}' for key, value in self.quantity_and_types_of_sold_tickets.items())
        return f"""
Event name - {self.name}
Event date - {self.date}
Event time - {self.time}
Event location - {self.location}
Price of 1 regular ticket - {self.price}
Number of seats - {self.quantity_of_seats}
Available seats - {self.available_seats}

Cash desk - {self.cash_desk}$
Quantity and types of tickets sold:
{res}
"""

    def reduce_places_quantity(self, quantity: int):
        """
        Reduce available seats on quantity number.
        Raises error if quantity are greater than available.

        :param quantity: Quantity of requested seats.
        :return: ValueError if no more available seats, or requested quantity is greater than available.
        """
        if quantity > self.available_seats:
            raise ValueError ('There is no more available seats, or requested quantity is greater than available.')
        else:
            self.available_seats -= quantity

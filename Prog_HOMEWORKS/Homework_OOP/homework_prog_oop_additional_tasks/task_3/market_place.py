import event
import random
import json
import customer
import ticket
import datetime


class MarketPlace:
    """
    The class is intended for the sale and accounting of sold tickets for events.
    """

    def __init__(self, name):
        """

        :param name: Name of market-place.
        """
        self.name_of_market = name
        self.events_earnings_and_serial = {}
        # json.dump({}, open(f'{market.name_of_market} sold tickets.json', 'w'), indent=4)

    def __str__(self):
        pass

    def serial_number_generator(self, _event: event.Event):
        """
        Generate unique serial numbers for event tickets.

        :param _event: Instance class Event.
        :return: list of unique serial number for each ticket of event.
        """
        first_letter = _event.name[0]
        second_letter = _event.name[int(len(_event.name) / 2)] if _event.name[int(len(_event.name) / 2)].isalpha() \
            else _event.name[int(len(_event.name) / 2) + 1]
        third_letter = _event.name[-1]
        digits = 0
        list_of_serial_numbers = []
        for number in range(0, _event.quantity_of_seats):
            serial_number = f'{first_letter.upper()}{second_letter.upper()}{third_letter.upper()}' \
                            f'{random.randint(100, 999)}{"0" * (6 - len(str(digits)))}{digits}'
            list_of_serial_numbers.append(serial_number)
            digits += 1
        return list_of_serial_numbers

    def add_new_event(self, _event: event.Event):
        """
        Registers information about event in base of events.
        Creates a new .json file with a complete list of all
        event serial numbers.

        :param _event Instance class Event.
        :return:
        """
        self.events_earnings_and_serial[_event] = {
            'available': {
                'earnings': 0,
                'serial': self.serial_number_generator(_event)
            }
        }
        json.dump(self.events_earnings_and_serial[_event]['available']['serial'],
                  open(f'{_event.name}_serial.json', 'w', ), indent=4)

    def sell_ticket(self, customer_: customer.Customer, event_: event.Event, quantity_of_tickets: int):
        list_of_tickets = []
        json_database_of_sold_tickets = json.load(open(f'{market.name_of_market} sold tickets.json'))
        ticket_type = self.ticket_type(event_, customer_)
        if ticket_type == 'student' and quantity_of_tickets > 1:
            raise ValueError ('Customer in student status can buy only 1 ticket per operation.')
        price = event_.price
        if ticket_type == 'student':
            price *= 0.5
        if ticket_type == 'advance':
            price *= 0.6
        if ticket_type == 'late':
            price *= 1.1
        for ticket_ in range(0, quantity_of_tickets):
            serial_number = self.events_earnings_and_serial[event_]['available']['serial'][0]
            self.events_earnings_and_serial[event_]['available']['serial'].remove(serial_number)
            self.events_earnings_and_serial[event_]['available']['earnings'] += price
            json_database_of_sold_tickets[event_.name]['sold'] = {
                serial_number: {
                    'type': ticket_type,
                    'price': price,
                    'sale time': str(datetime.datetime.now())[:-7]
                }
            }
            self.events_earnings_and_serial[event_]['sold'] = {
                serial_number: {
                    'type': ticket_type,
                    'price': price,
                    'sale time': str(datetime.datetime.now())[:-7]
                }
            }
            new_ticket = ticket.Ticket(event_, serial_number, price, ticket_type, str(datetime.datetime.now())[:-7])
            list_of_tickets.append(new_ticket)
            json.dump(json_database_of_sold_tickets, open(f'{market.name_of_market} sold tickets.json', 'w'), indent=4)
        customer_.add_to_customer_tickets(list_of_tickets)

    def ticket_type(self, event_: event.Event, customer_: customer.Customer):
        difference = event_.date - datetime.datetime.now()
        if difference.days < 10:
            return 'late'
        if customer_.student_status:
            return 'student'
        if difference.days >= 60:
            return 'advance'
        if difference.days > 9:
            return 'regular'




# self.events_earnings_and_serial = {
#     event: {
#         'available': {
#                     'earnings': 15135,
#                     'serial': []
#                     },
#         'sold': {
#                 'AWD666000005': {
#                                 'type': 'student',
#                                 'price': 750,
#                                 'sale time': '15.47'
#                                 }
#                 }
#     }
# }
#













party = event.Event('Atlas Weekend', (2023, 6, 1), '15:00', 'Kyiv, VDNG', 1500, 500)
market = MarketPlace('Rozetka')
market.add_new_event(party)
customer = customer.Customer(False)
market.sell_ticket(customer, party, 145)
for t in customer.customer_tickets:
    print(t)
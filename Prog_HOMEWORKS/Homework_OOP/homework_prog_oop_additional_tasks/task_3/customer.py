import ticket


class Customer:
    """
    Class Customer have all the information about customer, that we need to
    sell tickets.
    """

    def __init__(self, student_status: bool):
        """
        If the customer is a student, he gets a discount 50% of a full price of the Ticket.

        :param student_status: True or False
        """
        self.student_status = student_status
        self.customer_tickets = []

    def __str__(self):
        res = '\n'.join(self.customer_tickets)
        return f"""
Student status - {self.student_status}
{res}"""

    def add_to_customer_tickets(self, new_ticket: list | ticket.Ticket):
        """
        Adds to customers wallet new ticket or a many of tickets.

        :param new_ticket: single instance class Ticket or list with many instances Ticket inside.
        :return: TypeError if wrong type of ticket.
        """
        if isinstance(new_ticket, list):
            for tick in new_ticket:
                if isinstance(tick, ticket.Ticket):
                    self.customer_tickets.append(tick)
        elif isinstance(new_ticket, ticket.Ticket):
            self.customer_tickets.append(new_ticket)
        else:
            raise TypeError ('Wrong type of ticket. Only list with isinstance Ticket inside or single instance Ticket.')
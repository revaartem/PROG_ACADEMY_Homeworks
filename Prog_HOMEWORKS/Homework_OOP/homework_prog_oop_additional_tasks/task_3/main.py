import event
import customer
import market_place


if __name__ == "__main__":
    party_1 = event.Event("Atlas Weekend", (2023, 1, 30), '15:00', 'Kyiv, VDNG', 700, 20_000)
    party_2 = event.Event('Shid-Rock', (2023, 5, 13), '13:00', 'Trostyanets`, Krugliy Zamok', 500, 1500)
    party_3 = event.Event('Zahid-Fest', (2023, 7, 28), '12:00', 'Lviv, Lvivska Oblast', 750, 13000)

    market = market_place.MarketPlace('Internet-Bilet')

    market.add_new_event(party_1)
    market.add_new_event(party_2)
    market.add_new_event(party_3)

    customer_1 = customer.Customer(False)
    customer_2 = customer.Customer(False)
    customer_3 = customer.Customer(False)

    market.sell_ticket(customer_1, party_1, 1450)
    market.sell_ticket(customer_1, party_2, 14)
    market.sell_ticket(customer_1, party_3, 300)

    market.sell_ticket(customer_2, party_1, 30)
    market.sell_ticket(customer_2, party_2, 156)
    market.sell_ticket(customer_2, party_3, 389)

    market.sell_ticket(customer_3, party_1, 11)
    market.sell_ticket(customer_3, party_2, 380)
    market.sell_ticket(customer_3, party_3, 310)

    print(party_1)
    print(party_2)
    print(party_3)

    print(customer_1)
    print(customer_2)
    print(customer_3)

    print(market)

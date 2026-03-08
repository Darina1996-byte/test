from address import Address
from mailing import Mailing

sender_address = Address(
    index="162600",
    city="Череповец",
    street="Ленина",
    house=53,
    apartment=15
)

recipient_address = Address(
    index="654321",
    city="Санкт-Петербург",
    street="Невский проспект",
    house=20,
    apartment=5
)

mailing = Mailing(
    to_address=recipient_address,
    from_address=sender_address,
    cost=459.00,
    track="track123456789"
)

print(mailing)
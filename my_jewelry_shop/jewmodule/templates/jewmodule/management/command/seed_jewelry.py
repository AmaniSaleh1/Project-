from django.core.management.base import BaseCommand
from jewmodule.models import Jewelry

class Command(BaseCommand):
    help = 'Seed the database with initial Jewelry data'

    def handle(self, *args, **kwargs):
        jewelry_data = [
            {'title': 'Gold Necklace', 'type': 'Necklace', 'price': 299.99, 'edition': '20'},
            {'title': 'Silver Ring', 'type': 'Ring', 'price': 99.99, 'edition': '10'},
            {'title': 'Diamond Earrings', 'type': 'Earrings', 'price': 499.99, 'edition': '11'},
            {'title': 'Platinum Bracelet', 'type': 'Bracelet', 'price': 399.99, 'edition': '5'},
        ]

        for item in jewelry_data:
            Jewelry.objects.create(**item)

        self.stdout.write(self.style.SUCCESS('Successfully seeded the database with initial Jewelry data.'))

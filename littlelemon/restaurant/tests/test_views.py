from django.test import TestCase
from restaurant.models import MenuItem
from restaurant.serializers import MenuItemSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        # create some menu items for test purpose
        MenuItem.objects.create(title="IceCream", price=80, inventory=100)
        MenuItem.objects.create(title="Peperoni", price=200, inventory=40)
        MenuItem.objects.create(title="Cafe", price=20, inventory=200)
        
    def test_getall(self):
        #  retrieve all the Menu objects
        allObjects = MenuItem.objects.all()
        serializer = MenuItemSerializer(allObjects,many=True)
        print(serializer.data)
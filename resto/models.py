from django.db import models
# Create your models here.


class MenuItem(models.Model):
    CHOICES = (
        ('Appetizers', 'Appetizers'),
        ('Shellfish', 'Shellfish'),
        ('Salads', 'Salads'),
        ('Entrees', 'Entrees'),
        ('Prime Steaks', 'Prime Steaks'),
        ('Large Format Steak', 'Large Format Steak'),
        ('Sides', 'Sides')
    )
    CHOICESTWO = (
        ('Breakfast', 'Breakfast'),
        ('Brunch', 'Brunch'),
        ('Lunch', 'Lunch'),
        ('Dinner', 'Dinner'),
    )
    item_name = models.CharField(max_length=100)
    item_description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    item_active = models.BooleanField()
    menu_section = models.CharField(max_length=100, choices=CHOICES, null=True)
    menu_type = models.CharField(max_length=100, choices=CHOICESTWO, null=True)

    class Meta:
        verbose_name_plural = "Menu Item"

    def __str__(self):
        return self.item_name


class Menu(models.Model):
    CHOICES = (
        ('Breakfast', 'Breakfast'),
        ('Brunch', 'Brunch'),
        ('Lunch', 'Lunch'),
        ('Dinner', 'Dinner'),
    )
    menu_type = models.CharField(max_length=100, choices=CHOICES, null=True)
    active = models.BooleanField()
    menu_item_name = models.ManyToManyField(MenuItem, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Menu"

    def __str__(self):
        return self.menu_type

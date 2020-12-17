from django.db import models

# Create your models here.


class MenuItem(models.Model):
    MENUSECTION = (
        ('Appetizers', 'Appetizers'),
        ('Shellfish', 'Shellfish'),
        ('Salads', 'Salads'),
        ('Entrees', 'Entrees'),
        ('Prime Steaks', 'Prime Steaks'),
        ('Large Format Steak', 'Large Format Steak'),
        ('Sides', 'Sides'),
    )
    menu_section = models.CharField(
        max_length=100, choices=MENUSECTION, null=True)
    item_name = models.CharField(max_length=100)
    item_description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    item_active = models.BooleanField(null=True)

    class Meta:
        verbose_name_plural = "Menu Item"

    def __str__(self):
        return self.item_name


class FullMenu(models.Model):
    CHOICES = (
        ('Breakfast', 'Breakfast'),
        ('Brunch', 'Brunch'),
        ('Lunch', 'Lunch'),
        ('Dinner', 'Dinner'),
    )
    section_name = models.CharField(max_length=100, choices=CHOICES, null=True)
    menu_item = models.ManyToManyField(MenuItem, null=True, blank=True)

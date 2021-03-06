from django.db import models
# Create your models here.


class MenuItem(models.Model):
    menu_item_name = models.CharField(max_length=100)
    menu_item_description = models.TextField(blank=True, null=True)
    menu_item_price = models.DecimalField(
        max_digits=10, decimal_places=2)

    class Meta:
        verbose_name_plural = "Menu Item"

    def __str__(self):
        return self.menu_item_name


class MenuSection(models.Model):
    # CHOICES = (
    #     ('Appetizers', 'Appetizers'),
    #     ('Salads', 'Salads'),
    #     ('Entrees', 'Entrees'),
    #     ('BAppetizers', 'Appetizers'),
    #     ('BSalads', 'Salads'),
    #     ('BEntrees', 'Entrees'),
    # )
    menu_section_name = models.CharField(max_length=25, null=True)
    menu_section_alias = models.CharField(max_length=25, null=True)
    menu_items = models.ManyToManyField(MenuItem, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Menu Section"

    def __str__(self):
        return self.menu_section_name


class Menu(models.Model):
    # CHOICES1 = (
    #     ('Breakfast', 'Breakfast'),
    #     ('Brunch', 'Brunch'),
    #     ('Lunch', 'Lunch'),
    #     ('Dinner', 'Dinner'),
    # )
    menu_name = models.CharField(max_length=25, null=True)
    menu_section_name = models.ManyToManyField(
        MenuSection, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Menu"

    def __str__(self):
        return self.menu_name

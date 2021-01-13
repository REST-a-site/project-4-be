from django.db import models
# Create your models here.


class Menu(models.Model):
    CHOICES = (
        ('Breakfast', 'Breakfast'),
        ('Brunch', 'Brunch'),
        ('Lunch', 'Lunch'),
        ('Dinner', 'Dinner'),
    )
    menu_name = models.CharField(max_length=25, choices=CHOICES, null=True)

    class Meta:
        verbose_name_plural = "Menu"

    def __str__(self):
        return self.menu_name

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
    CHOICES = (
        ('Appetizers', 'Appetizers'),
        ('Salads', 'Salads'),
        ('Entrees', 'Entrees'),
    )
    menu_section_name = models.CharField(
        max_length=25, choices=CHOICES, null=True)
    menus = models.ManyToManyField(Menu, null=True, blank=True)
    menu_items = models.ManyToManyField(MenuItem, null=True, blank=True)
    class Meta:
        verbose_name_plural = "Menu Section"

    def __str__(self):
        return self.menu_section_name




# class FullMenu(models.Model):
#     menu_id = models.ForeignKey(
#         Menu, on_delete=models.CASCADE, related_name='full_menu')
#     menu_section_id = models.ForeignKey(
#         MenuSection, on_delete=models.CASCADE, related_name='full_menu_section')
#     menu_item_id = models.ForeignKey(
#         MenuItem, on_delete=models.CASCADE, related_name='full_menu_item')

#     def __str__(self):
#         return self.menu_id.menu_name

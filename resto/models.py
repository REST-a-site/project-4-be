from django.db import models

# Create your models here.


# class MenuSection(models.Model):
#     section_name = models.CharField(max_length=100)
#     section_description = models.TextField(blank=True, null=True)

#     class Meta:
#         verbose_name = "Menu Section"

#     def __str__(self):
#         return self.section_name


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

    item_name = models.CharField(max_length=100)
    item_description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    item_active = models.BooleanField()
    menu_sections = models.CharField(
        max_length=200, choices=CHOICES, null=True)

    class Meta:
        verbose_name_plural = "Menu Item"

    def __str__(self):
        return self.item_name


class Menu(models.Model):
    menu_name = models.CharField(max_length=100)
    menu_description = models.TextField(blank=True, null=True)
    active = models.BooleanField()
    menu_item_names = models.ManyToManyField(MenuItem, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Menu"

    def __str__(self):
        return self.menu_name

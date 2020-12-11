from django.db import models

# Create your models here.


class Menu(models.Model):
    menu_title = models.CharField(max_length=100)
    menu_description = models.TextField(blank=True, null=True)
    active = models.BooleanField()

    class Meta:
        verbose_name = "Menu"

    def __str__(self):
        return self.menu_title


class MenuSection(models.Model):
    menu = models.ForeignKey(
        Menu, on_delete=models.CASCADE)
    section_title = models.CharField(max_length=100)
    section_description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Menu Section"

    def __str__(self):
        return self.section_title


class MenuItem(models.Model):
    menu_section = models.ForeignKey(
        MenuSection, on_delete=models.CASCADE, related_name='menu_items')
    item_title = models.CharField(max_length=100)
    item_description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    item_active = models.BooleanField()

    class Meta:
        verbose_name = "Menu Item"

    def __str__(self):
        return self.item_title

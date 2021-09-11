from django.contrib import admin
from .models import Review, Item, Category, Country, ItemVariant

admin.site.register(Category)
admin.site.register(Country)
admin.site.register(Item)
admin.site.register(Review)
admin.site.register(ItemVariant)

# Register your models here.

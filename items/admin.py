from django.contrib import admin
from .models import Items
# Register your models here.

class ItemsAdmin(admin.ModelAdmin):
    list_display = ("id","image" ,"name", "category", 'price', 'number','available')
    list_editable = ("price", "number",)
    search_fields = ("name",)
    exclude = ("views", "boughts")
    

    prepopulated_fields = {'slug': ("name","category","available",)}

admin.site.register(Items, ItemsAdmin)
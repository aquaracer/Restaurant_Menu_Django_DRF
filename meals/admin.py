from django.contrib import admin
from .models import Meals, Category, Allergens


class MealAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price')
    list_editable = ('category',)
    ordering = ('price',)
    sortable_by = ('name', 'price')
    list_filter = ('category',)
    list_per_page = 3
    filter_horizontal = ('allergens',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


class AllergensAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Meals, MealAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Allergens, AllergensAdmin)

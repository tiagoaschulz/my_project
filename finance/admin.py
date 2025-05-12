from django.contrib import admin
from finance import models

#Classes/Models do admin

class FinanceAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'balance', 'currency', 'is_active')
    search_fields = ('name',)
    list_filter = ('type', 'is_active')
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'

admin.site.register(models.Account, FinanceAdmin)


class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'symbol')
    search_fields = ('code', 'name')

admin.site.register(models.Currency, CurrencyAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

admin.site.register(models.Category, CategoryAdmin)


class TransactionAdmin(admin.ModelAdmin):
    list_display = ('account', 'category', 'type', 'amount', 'created_at')
    search_fields = ('account__name', 'category__name', 'type')
    list_filter = ('type', 'category', 'account')
    date_hierarchy = 'created_at'

admin.site.register(models.Transaction, TransactionAdmin)


class BudgetAdmin(admin.ModelAdmin):
    list_display = ('account', 'category', 'amount', 'start_date', 'end_date')
    search_fields = ('account__name', 'category__name')
    list_filter = ('account', 'category', 'start_date', 'end_date')

admin.site.register(models.Budget, BudgetAdmin)
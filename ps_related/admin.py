from django.contrib import admin
from .models import Plan, Account, Blog, Book

@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ('package', 'level', 'link', 'commission', 'is_paid')
    search_fields = ('package', 'link')
    list_filter = ('package', 'is_paid')

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('user', 'get_plans')
    search_fields = ('user__username', 'plan__package')

    def get_plans(self, obj):
        return ", ".join(plan.package for plan in obj.plan.all())
    get_plans.short_description = 'Plans'

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'account', 'created_at')
    search_fields = ('title', 'content')
    list_filter = ('created_at',)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'in_stock')
    list_filter = ('in_stock',)
    search_fields = ('title',)

from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname', 'surname2', 'address', 'email', 'phone')
    search_fields = ('name', 'surname', 'surname2', 'address', 'email', 'phone')
    list_filter = ('email', 'phone')

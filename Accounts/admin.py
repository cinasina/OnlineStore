from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserCreationForm, UserChangeForm
from django.contrib import admin
from .models import User
from django.contrib.auth.models import Group


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    list_display = ('email', 'first_name', 'last_name', 'phone_number',)
    list_editable = ('email', 'phone_number', 'is_active',)
    list_filter = ('is_admin', 'is_active',)
    search_fields = ('email', 'first_name', 'last_name', 'phone_number',)
    ordering = ('date_joined',)
    fieldsets = (
        (None, {'fields': ('email', 'phone_number', 'password',)}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'address',)}),
        ('Permission', {'fields': ('is_active', 'is_admin',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'phone_number', 'password',),
        }),
    )
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)

from django.contrib import admin
from .models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('phone_number','email',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
    )

    add_fieldsets = (
        (None, {
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)


# Now register the new UserAdmin...
admin.site.register(CustomUser, CustomUserAdmin)

from django.contrib import admin
from Core.models import User, Profile
from django.contrib.auth.admin import UserAdmin


# Register your models here.
class ProfileInline(admin.StackedInline):
    """Stacked inline profile view under User model"""
    model = Profile
    can_delete = False
    max_num = 1
    verbose_name = 'Profile'
    verbose_name_plural = 'Profile'


@admin.register(User)
class UserAdmin(UserAdmin):
    """Admin for User model"""
    ordering = ('email', )
    list_display = (
        'email', 'is_staff', 'is_superuser', 'is_active',
    )
    fieldsets = (
        (None, {'fields': ('email', 'password',)}),
        ('Permissions', {'fields': ('groups', 'user_permissions')}),
        ('Roles', {'fields': ('is_staff', 'is_superuser', 'is_active')}),
        ('Dates', {'fields': ('last_login', 'last_updated', 'date_joined')})
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide', ),
            'fields': (
                'email', 'password1', 'password2'
            )
        }),
    )
    readonly_fields = ('last_login', 'last_updated', 'date_joined')
    search_fields = ('id', 'email', 'first_name', 'last_name', 'phone')
    inlines = (ProfileInline, )

    def get_inline_instances(self, request, obj=None):
        """hides inlines during 'add user' view"""
        return obj and super().get_inline_instances(request, obj) or []

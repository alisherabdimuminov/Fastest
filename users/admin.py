from django.contrib import admin
from unfold.admin import ModelAdmin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from django.contrib.auth.forms import UserCreationForm

from .models import User
from .forms import UserUpdateForm


@admin.register(User)
class UserModelAdmin(UserAdmin, ModelAdmin):
    model = User
    list_display = ["username", "first_name", "last_name", "middle_name", "branch"]
    search_fields = ["username", "first_name", "last_name", "middle_name"]
    list_filter = ["branch"]
    add_form = UserCreationForm
    form = UserUpdateForm
    add_fieldsets = (
        ("Yangi foydalanuvchi qo'shish", {
            "fields": ("username", "first_name", "last_name", "middle_name", "branch", "password1", "password2")
        }),
    )
    fieldsets = (
        ("Foydalanuvchini tahrirlash", {
            "fields": ("username", "first_name", "last_name", "middle_name", "branch", )
        }),
    )

admin.site.index_title = "Fastest"
admin.site.site_title = "Admin panel"
admin.site.site_header = "Admin panel"
admin.site.unregister(Group)

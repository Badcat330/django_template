from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from reversion.admin import VersionAdmin

from .forms import ProjectUserChangeForm, ProjectUserCreationForm

ProjectUser = get_user_model()


@admin.register(ProjectUser)
class ProjectUserAdmin(VersionAdmin, UserAdmin):
    add_form = ProjectUserCreationForm
    form = ProjectUserChangeForm
    model = ProjectUser 
    list_display = [
        "email",
        "first_name",
        "last_name",
        "is_superuser",
    ]

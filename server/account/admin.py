from django.contrib import admin
from account.models import CustomUser, Student


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username',  'is_active', 'email', "first_name", 'last_name', 'is_student', 'is_instructor')
    search_fields = ('username', 'is_active', 'email')
    list_filter = ('is_student','is_instructor', 'is_active')

class StudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'age', 'location')
    search_fields = ('user', 'location')
    list_filter = ('location',)



admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Student, StudentAdmin)
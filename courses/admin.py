from django.contrib import admin
from .models import (
    Course, Instructor, Student, StudentProfile)

@admin.action(description="Mettre le prix à zéro")
def make_free(modeladmin, request, queryset):
    queryset.update(price=0)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("title", "price", "duration", "instructor")
    list_filter = ("instructor",)
    search_fields = ("title", "description")
    list_editable = ("price",)
    actions = [make_free]


class CourseInline(admin.TabularInline):
    model = Course
    extra = 0

@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_display = ("name", "email")
    inlines = [CourseInline]

admin.site.register(Student)
admin.site.register(StudentProfile)

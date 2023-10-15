from django.contrib import admin

from study.models import Lesson
from study.models import LessonViewInfo
# Register your models here.


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    pass


@admin.register(LessonViewInfo)
class LessonViewInfoAdmin(admin.ModelAdmin):
    pass
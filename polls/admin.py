from django.contrib import admin

from .models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 0


class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_filter = ["pub_date"]
    search_fields = ["question_text"]
    list_display = ["question_text", "pub_date", "was_published_recently"]
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"]}),
    ]


admin.site.register(Question, QuestionAdmin)

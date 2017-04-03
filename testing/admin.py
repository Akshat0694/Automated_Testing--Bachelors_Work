from __future__ import unicode_literals
from django.contrib import admin
from .forms import TestAdmin, TestUser
from django.template import RequestContext
from .models import TestAdmin,TestUser
# from testing.models import Question

# class QuestionAdmin(admin.ModelAdmin):
#     list_display = ("pk", "answer_type")


# admin.site.register(Question, QuestionAdmin)

admin.site.register(TestAdmin)
admin.site.register(TestUser)

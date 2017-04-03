# from django.froms import ModelForm
# from models import ProejctName
from __future__ import unicode_literals
from django import forms
from django.db import models
from django.forms import ModelForm
from .models import TestAdmin, TestUser
# from django.template import RequestContext

# class TestUserForm(forms.Form):

#     """For students to upload answers"""

#     file_name = forms.FileField()

#     def handle_uploaded_file(f):
#         with open('some/file/name.txt', 'wb+') as destination:
#             for chunk in f.chunks():
#                 destination.write(chunk)

class TestUserForm(ModelForm):

    class Meta:
        model = TestUser
        fields = ['answer_file']

    def handle_uploaded_file(f):
        with open('some/file/name.txt', 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)



class TestAdminForm(ModelForm):

    """For question papers and setting admin page variable"""
    class Meta:
        model = TestAdmin
        fields = ['question_paper', 'num_of_ques', 'allow_access']

    def handle_uploaded_file(f):
        with open('some/file/name.txt', 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)

    # def __init__(self, *args, **kwargs):
    #    self.request = kwargs.pop('request', None)
    #    return super(TestAdminForm, self).__init__(*args, **kwargs)

    # def save(self, *args, **kwargs):
    #    kwargs['commit']=False
    #    obj = super(TestAdminForm, self).save(*args, **kwargs)
    #    if self.request:
    #        obj.user = self.request.user
    #    obj.save()
    #    return obj
from __future__ import unicode_literals
import os
from django.dispatch import receiver
from django.db import models
from django.contrib.auth.models import User
from autotest.settings import QUES_PAPER_PATH, ANS_PATH
from django.template import RequestContext

# class Question(models.Model):
#     """
#     Model covering - questions, examples, polls.

#     ANSWER_CHOICES represents what kind of answer
#     is expected (string, number...)

#     Functions with receiver decorators should keep the filesystem clean from
#     deleted or changed image files (question figure field).
#     """
#     created = models.DateTimeField(auto_now_add=True, blank=True)
#     content = models.CharField(max_length=1000,default="", blank=True,
#         verbose_name="Question text")
#     figure = models.FileField(upload_to=FIGURES_PATH, max_length=200,
#         verbose_name="Explaining figure", blank=True)

#     ANSWER_CHOICES = (
#         ("OPEN", 'Open question'),
#         ("BOOL", 'True/False answer'),
#         ("NUM", 'Numerical answer'),
#         ("STR", 'Text answer'),
#         ("OPT", 'Options'),
#     )

#     answer_type = models.CharField(
#         max_length=4,
#         choices=ANSWER_CHOICES,
#         default="OPEN",
#         verbose_name="Type of answer"
#     )

#     answer_bool = models.BooleanField(default=False, verbose_name="True/False answer")
#     answer_num = models.FloatField(default=0, blank=True, null=True, verbose_name="Numerical answer")
#     answer_str = models.CharField(max_length=1000, default="", blank=True, verbose_name="Text answer")
#     answer_opt = models.CharField(max_length=2000, default="", blank=True, verbose_name="Options")

# @receiver(models.signals.post_delete, sender=Question)
# def auto_delete_file_on_delete(sender, instance, **kwargs):
#     """
#     Deletes file from filesystem
#     when corresponding `MediaFile` object is deleted.
#     """
#     if instance.figure:
#         if os.path.isfile(instance.figure.path):
#             os.remove(instance.figure.path)
#     if instance.preview:
#         if os.path.isfile(instance.preview.path):
#             os.remove(instance.preview.path)

# @receiver(models.signals.pre_save, sender=Question)
# def auto_delete_file_on_change(sender, instance, **kwargs):
#     """
#     Deletes file from filesystem
#     when corresponding `MediaFile` object is changed.
#     """
#     if not instance.pk:
#         return False

#     try:
#         old_file = Question.objects.get(pk=instance.pk).figure
#     except Question.DoesNotExist:
#         return False

#     new_file = instance.figure
#     if not old_file == new_file:
#         if os.path.isfile(old_file.path):
#             os.remove(old_file.path)

#     try:
#         old_file = Question`.objects.get(pk=instance.pk).preview
#     except Question.DoesNotExist:
#         return False

#     new_file = instance.preview
#     if not old_file == new_file:
#         if os.path.isfile(old_file.path):
#             os.remove(old_file.path)


class TestAdmin(models.Model):

    """For uploading question papers and allowing access to the test takers"""

    question_paper = models.FileField(upload_to=QUES_PAPER_PATH, max_length=200,
        verbose_name="Queestion paper", blank=True)
    num_of_ques = models.PositiveIntegerField(null=True, verbose_name="number of questions in the test")
    allow_access = models.BooleanField(default=False, verbose_name="Allow Access")
    # created_by = models.CharField(max_length=1000,default="", blank=True,
    #      verbose_name="Create by")
    created_by = models.ForeignKey('auth.User', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        get_latest_by = "created_at"

    def __str__(self):
        created_at_str = str(self.created_at)
        id_str = str(self.id)
        return id_str

    # def get_username_str(request):
    #     current_user = request.user
    #     created_by_usr = current_user.username
    #     return str("created_by_usr")

    # def save(self, *args, **kwargs):
    #     self.created_by = get_username_str
    #     super(TestAdmin, self).save(*args, **kwargs)


class TestUser(models.Model):

    """For question papers and allowing access to test takers"""

    ques_paper = models.ForeignKey(TestAdmin , on_delete=None, blank=True, null=True)
    answer_file = models.FileField(upload_to=ANS_PATH, max_length=200, verbose_name="File", blank=True)
    answer_num = models.PositiveIntegerField(null=True, blank=True)
    created_by = models.CharField(max_length=1000, default="", blank=True, verbose_name="Create by")
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        get_latest_by = "created_at"

    def __str__(self):
        return self.created_by








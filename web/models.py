# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Codes(models.Model):
    code_id = models.BigAutoField(primary_key=True)
    phone = models.BigIntegerField()
    code = models.BigIntegerField()
    created_at = models.DateTimeField()
    ip = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'codes'


class Comments(models.Model):
    commentid = models.IntegerField(primary_key=True)
    pid = models.BigIntegerField()
    cid = models.BigIntegerField()
    avatar = models.CharField(max_length=512, blank=True, null=True)
    uname = models.CharField(max_length=512, blank=True, null=True)
    created_at = models.CharField(max_length=128)
    content = models.TextField(blank=True, null=True)
    like_counts = models.IntegerField()
    reply = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'comments'


class Composers(models.Model):
    cid = models.BigIntegerField(primary_key=True)
    banner = models.CharField(max_length=512)
    avatar = models.CharField(max_length=512)
    verified = models.IntegerField()
    name = models.CharField(max_length=128)
    intro = models.TextField(blank=True, null=True)
    like_counts = models.IntegerField()
    fans_counts = models.IntegerField()
    follow_counts = models.IntegerField()
    location = models.CharField(max_length=32, blank=True, null=True)
    career = models.CharField(max_length=32, blank=True, null=True)
    phone = models.CharField(max_length=11, blank=True, null=True)
    password = models.CharField(max_length=16, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'composers'


class Copyrights(models.Model):
    pcid = models.CharField(primary_key=True, max_length=32)
    pid = models.BigIntegerField()
    cid = models.BigIntegerField()
    roles = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'copyrights'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class Posts(models.Model):
    pid = models.BigIntegerField(primary_key=True)
    title = models.CharField(max_length=256)
    preview = models.CharField(max_length=512, blank=True, null=True)
    video = models.CharField(max_length=512, blank=True, null=True)
    video_format = models.CharField(max_length=512, blank=True, null=True)
    category = models.CharField(max_length=512)
    created_at = models.CharField(max_length=128)
    description = models.TextField(blank=True, null=True)
    play_counts = models.IntegerField()
    like_counts = models.IntegerField()
    thumbnail = models.CharField(max_length=512, blank=True, null=True)
    duration = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'posts'

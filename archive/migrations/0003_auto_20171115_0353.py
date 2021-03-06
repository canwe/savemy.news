# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-15 03:53
from __future__ import unicode_literals
from django.db import migrations


def forward(apps, schema_editor):
    Clip = apps.get_model("archive", "Clip")
    for clip in Clip.objects.all():
        clip.mementos.add(clip.memento)


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0002_auto_20171115_0352'),
    ]

    operations = [
        migrations.RunPython(forward)
    ]

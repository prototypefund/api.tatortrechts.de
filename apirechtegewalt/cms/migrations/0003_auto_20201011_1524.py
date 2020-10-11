# Generated by Django 3.1.2 on 2020-10-11 15:24

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0002_auto_20201010_2244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contentpage',
            name='body',
            field=wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.CharBlock(classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('two_columns', wagtail.core.blocks.StructBlock([('left_column', wagtail.core.blocks.StreamBlock([], icon='arrow-right', label='Left column content')), ('right_column', wagtail.core.blocks.StreamBlock([], icon='arrow-right', label='Right column content'))]))]),
        ),
    ]

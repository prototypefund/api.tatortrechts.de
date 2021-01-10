# Generated by Django 3.1.5 on 2021-01-10 17:09

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0012_auto_20210110_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contentpage',
            name='body',
            field=wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.CharBlock(form_classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('quote', wagtail.core.blocks.StructBlock([('quote', wagtail.core.blocks.TextBlock()), ('author', wagtail.core.blocks.TextBlock(required=False))])), ('image', wagtail.images.blocks.ImageChooserBlock()), ('two_columns', wagtail.core.blocks.StructBlock([('left_column', wagtail.core.blocks.StreamBlock([('heading', wagtail.core.blocks.CharBlock(form_classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('quote', wagtail.core.blocks.StructBlock([('quote', wagtail.core.blocks.TextBlock()), ('author', wagtail.core.blocks.TextBlock(required=False))])), ('centered_column', wagtail.core.blocks.StructBlock([('column', wagtail.core.blocks.StreamBlock([('heading', wagtail.core.blocks.CharBlock(form_classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('quote', wagtail.core.blocks.StructBlock([('quote', wagtail.core.blocks.TextBlock()), ('author', wagtail.core.blocks.TextBlock(required=False))]))], icon='wagtail', label='Centered column content')), ('column_size', wagtail.core.blocks.IntegerBlock(default=6, max_value=12, min_value=1))]))], icon='arrow-right', label='Left column content')), ('right_column', wagtail.core.blocks.StreamBlock([('heading', wagtail.core.blocks.CharBlock(form_classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('quote', wagtail.core.blocks.StructBlock([('quote', wagtail.core.blocks.TextBlock()), ('author', wagtail.core.blocks.TextBlock(required=False))])), ('centered_column', wagtail.core.blocks.StructBlock([('column', wagtail.core.blocks.StreamBlock([('heading', wagtail.core.blocks.CharBlock(form_classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('quote', wagtail.core.blocks.StructBlock([('quote', wagtail.core.blocks.TextBlock()), ('author', wagtail.core.blocks.TextBlock(required=False))]))], icon='wagtail', label='Centered column content')), ('column_size', wagtail.core.blocks.IntegerBlock(default=6, max_value=12, min_value=1))]))], icon='arrow-right', label='Right column content'))])), ('centered_column', wagtail.core.blocks.StructBlock([('column', wagtail.core.blocks.StreamBlock([('heading', wagtail.core.blocks.CharBlock(form_classname='full title')), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('quote', wagtail.core.blocks.StructBlock([('quote', wagtail.core.blocks.TextBlock()), ('author', wagtail.core.blocks.TextBlock(required=False))]))], icon='wagtail', label='Centered column content')), ('column_size', wagtail.core.blocks.IntegerBlock(default=6, max_value=12, min_value=1))]))]),
        ),
    ]

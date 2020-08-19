# Generated by Django 2.2.14 on 2020-08-19 09:51

from django.db import migrations

from olympia import amo
from olympia.constants.promoted import RECOMMENDED


@amo.decorators.use_primary_db
def make_recommended_firefox_only(apps, schema_editor):
    PromotedAddon = apps.get_model('promoted', 'PromotedAddon')
    qs = PromotedAddon.objects.filter(
        group_id=RECOMMENDED.id, application_id=None)
    for promo in qs:
        promo.application_id = amo.FIREFOX.id
        promo.save()


class Migration(migrations.Migration):

    dependencies = [
        ('promoted', '0005_auto_20200803_1214'),
    ]

    operations = [
        migrations.RunPython(make_recommended_firefox_only)
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [        
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('general', '0018_auto_20180510_1901'),
    ]

    operations = [
        migrations.CreateModel(
            name='LinkAbonentsAuthUser',
            fields=[
                ('guid', django_extensions.db.fields.UUIDField(max_length=38, serialize=False, editable=False, primary_key=True, blank=True)),
                ('name', models.CharField(max_length=200)),
                ('guid_abonents', models.ForeignKey(to='general.Abonents', db_column=b'guid_abonents')),
                ('guid_auth_user', models.ForeignKey(to=settings.AUTH_USER_MODEL, db_column=b'id_auth_user')),
            ],
            options={
                'db_table': 'link_abonents_auth_user',
                'verbose_name': '\u041f\u0440\u0438\u0432\u044f\u0437\u043a\u0430 \u0430\u0431\u043e\u043d\u0435\u043d\u0442\u0430 \u043a \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044e',
                'verbose_name_plural': '\u041f\u0440\u0438\u0432\u044f\u0437\u043a\u0438 \u0430\u0431\u043e\u043d\u0435\u043d\u0442\u043e\u0432 \u043a \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f\u043c',
            },
        ),
    ]

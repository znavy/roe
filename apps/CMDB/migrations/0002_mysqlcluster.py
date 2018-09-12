# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-09-11 11:11
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('CMDB', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MySQLCluster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True, verbose_name='\u96c6\u7fa4\u540d')),
                ('arch', models.CharField(blank=True, choices=[('\u4e3b\u4ece', '\u4e3b\u4ece'), ('\u5355\u673a', '\u5355\u51fb'), ('innodb_cluster', 'innodb_cluster'), ('pxc', 'pxc')], max_length=30, null=True, verbose_name='\u96c6\u7fa4\u67b6\u6784')),
                ('db_version', models.CharField(blank=True, max_length=30, null=True, verbose_name='\u6570\u636e\u5e93\u7248\u672c')),
                ('defaultdb', models.CharField(blank=True, max_length=30, null=True, verbose_name='\u4e3b\u7528DB')),
                ('desc', models.CharField(blank=True, max_length=100, null=True, verbose_name='\u63cf\u8ff0')),
                ('operator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u53ef\u89c1\u7684\u4eba')),
                ('tree_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='CMDB.YewuTree', verbose_name='\u6240\u5c5e\u4ea7\u54c1\u7ebf')),
            ],
            options={
                'db_table': 'MySQL_Cluster',
                'verbose_name': 'mysql\u96c6\u7fa4',
                'verbose_name_plural': 'mysql\u96c6\u7fa4',
                'permissions': (('can_read_mysql_cluster', '\u8bfb\u53d6\u8d44\u4ea7\u6743\u9650'), ('can_change_mysql_cluster', '\u66f4\u6539\u8d44\u4ea7\u6743\u9650'), ('can_add_mysql_cluster', '\u6dfb\u52a0\u8d44\u4ea7\u6743\u9650'), ('can_delete_mysql_cluster', '\u5220\u9664\u8d44\u4ea7\u6743\u9650'), ('can_dumps_mysql_cluster', '\u5bfc\u51fa\u8d44\u4ea7\u6743\u9650')),
            },
        ),
    ]
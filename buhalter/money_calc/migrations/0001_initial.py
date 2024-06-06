# Generated by Django 5.0.6 on 2024-05-23 15:34

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('agent_name', models.CharField(max_length=100, verbose_name='Имя заказчика')),
                ('agent_phone', models.CharField(max_length=11, verbose_name='Телефон заказчика')),
            ],
            options={
                'verbose_name': 'Заказчик',
                'verbose_name_plural': 'Заказчики',
            },
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('worker_name', models.CharField(max_length=100, verbose_name='Имя работника')),
                ('worker_phone', models.CharField(max_length=11, verbose_name='Телефон работника')),
                ('car', models.CharField(max_length=100, verbose_name='Машина и гос.номер')),
            ],
            options={
                'verbose_name': 'Работник',
                'verbose_name_plural': 'Работники',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('created_data', models.DateField(auto_now_add=True)),
                ('publish_data', models.DateField(default=django.utils.timezone.now, verbose_name='Дата выполнения заказа')),
                ('sum', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Сумма заказа')),
                ('payment_method', models.CharField(choices=[('cash', 'Нал'), ('card', 'Безналл'), ('law', 'с НДС')], max_length=100, verbose_name='Метод оплаты:')),
                ('comment', models.TextField(max_length=350, verbose_name='Комментарий:')),
                ('payment_status', models.CharField(choices=[('yes', 'Оплачено'), ('no', 'Ждет оплаты')], max_length=50, verbose_name='Статус платежа:')),
                ('agent_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='money_calc.agent', verbose_name='Имя заказчика')),
                ('worker_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='money_calc.worker', verbose_name='Имя работника')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
            },
        ),
    ]

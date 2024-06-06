from django.db import models
from django.utils import timezone


class Agent(models.Model):
    id = models.AutoField(primary_key=True)
    agent_name = models.CharField(max_length=100, verbose_name='Имя заказчика')
    agent_phone = models.CharField(max_length=11, verbose_name='Телефон заказчика', unique=True)

    class Meta:
        verbose_name = 'Заказчик'
        verbose_name_plural = 'Заказчики'

    def __str__(self):
        return str(self.agent_name)


class Worker(models.Model):
    id = models.AutoField(primary_key=True)
    worker_name = models.CharField(max_length=100, verbose_name='Имя работника')
    worker_phone = models.CharField(max_length=11, verbose_name='Телефон работника')
    car = models.CharField(max_length=100, verbose_name='Машина и гос.номер', unique=True)

    class Meta:
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'

    def __str__(self):
        return str(self.worker_name)


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    created_data = models.DateTimeField(auto_now_add=True)
    publish_data = models.DateField(default=timezone.now, verbose_name='Дата выполнения заказа')
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE, verbose_name='Имя работника')
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE, verbose_name='Имя заказчика')
    sum = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Сумма заказа', default=0)
    METHOD = [
        ('cash', 'Нал'),
        ('card', 'Безналл'),
        ('law', 'с НДС'),
    ]

    payment_method = models.CharField(max_length=100, choices=METHOD, verbose_name='Метод оплаты:')
    comment = models.TextField(max_length=350, verbose_name='Комментарий:')

    STATUS = [
        ('yes', 'Оплачено'),
        ('no', 'Ждет оплаты'),
    ]

    payment_status = models.CharField(max_length=50, choices=STATUS, verbose_name='Статус платежа:')

    def get_absolute_url(self):
        return f'/money_calc/{self.order_id}'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'Заказ №{self.order_id} - {self.publish_data} - {self.worker} - {self.agent} - {self.sum}'


class Expenses(models.Model):
    id = models.AutoField(primary_key=True)
    expense = models.CharField(max_length=250, verbose_name='Наименование траты')
    cost = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Сумма трат')
    data_expense = models.DateField(auto_now_add=True, verbose_name='Когда потратил ?')

    class Meta:
        verbose_name = 'Трата'
        verbose_name_plural = 'Расходы'

    def __str__(self):
        return f'{self.expense} - {self.cost}₽ {self.data_expense}'


class Tasks(models.Model):
    id = models.AutoField(primary_key=True)
    created_data = models.DateTimeField(auto_now_add=True)
    publish_data = models.DateField(default=timezone.now, verbose_name='Дэдлайн')
    comment = models.TextField(max_length=350, verbose_name='Комментарий:')

    TYPE = [
        ('1', 'Не важно'),
        ('2', 'Средне'),
        ('3', 'Важно'),
    ]

    task_type = models.CharField(max_length=100, choices=TYPE, verbose_name='Степень важности:')

    STATUS = [
        ('1', 'Не начал'),
        ('2', 'В процессе'),
        ('3', 'Выполнил'),
    ]

    task_status = models.CharField(max_length=100, choices=STATUS, verbose_name='Статус выполнения:')

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    def __str__(self):
        return f'{self.comment} - {self.task_status}₽ {self.task_type}'

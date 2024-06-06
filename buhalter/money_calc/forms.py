from django.forms import ModelForm, TextInput, DateInput, Textarea

from .models import Order, Worker, Agent, Expenses, Tasks


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['publish_data', 'worker', 'agent', 'sum', 'payment_method', 'payment_status', 'comment']

        widgets = {
            'publish_data': DateInput(attrs={
                'class': 'form-control',
                'placeholder': "Дата выполнения заказа",
            }),
            'sum': TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Сумма заказа",
            }),
            'comment': Textarea(attrs={
                'class': 'form-control',
                'placeholder': "Комментарий",
            }),
        }


class WorkerForm(ModelForm):
    class Meta:
        model = Worker
        fields = ['id', 'worker_name', 'worker_phone', 'car']

        widgets = {
            'worker_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Имя работника",
            }),
            'worker_phone': TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Телефон работника",
            }),
            'car': TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Машина и гос.номер",
            }),
        }


class AgentForm(ModelForm):
    class Meta:
        model = Agent
        fields = ['id', 'agent_name', 'agent_phone']

        widgets = {
            'agent_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Имя заказчика",
            }),
            'agent_phone': TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Телефон заказчика",
            }),
        }


class ExpensesForm(ModelForm):
    class Meta:
        model = Expenses
        fields = ['expense', 'cost']

        widgets = {
            'expense': TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Наименование траты",
            }),
            'cost': TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Сумма трат",
            }),
        }


class TaskForm(ModelForm):
    class Meta:
        model = Tasks
        fields = ['publish_data', 'comment', 'task_type', 'task_status']

        widgets = {
            'publish_data': DateInput(attrs={
                'class': 'form-control',
                'placeholder': "Дата выполнения заказа",
            }),
            'comment': Textarea(attrs={
                'class': 'form-control',
                'placeholder': "Комментарий",
            }),
        }

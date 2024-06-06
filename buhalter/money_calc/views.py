from datetime import date

from babel.dates import format_date
from django.db.models import Avg, Func
from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.generic import DetailView, UpdateView, DeleteView

from .forms import OrderForm, WorkerForm, AgentForm, ExpensesForm, TaskForm
from .models import Order, Worker, Agent, Expenses, Tasks


def orders(request):
    today = timezone.now().date()
    latest_order_list = Order.objects.order_by('-publish_data').filter(publish_data__lte=today)
    future_orders = Order.objects.filter(publish_data__gt=today)

    context = {
        'latest_order_list': latest_order_list,
        'future_orders': future_orders,
    }
    return render(request, 'money_calc/orders.html', context)


def not_pay_orders(request):
    latest_order_list = Order.objects.filter(payment_status='no')
    context = {
        'latest_order_list': latest_order_list,
    }
    return render(request, 'money_calc/not_pay_orders.html', context)


def worker(request):
    latest_worker_list = Worker.objects.order_by('-worker_name')
    context = {'latest_worker_list': latest_worker_list}
    return render(request, 'money_calc/worker.html', context)


def agent(request):
    latest_agent_list = Agent.objects.order_by('-agent_name')
    context = {'latest_agent_list': latest_agent_list}
    return render(request, 'money_calc/agent.html', context)


def expenses(request):
    latest_expenses_list = Expenses.objects.order_by('-id')
    context = {'latest_expenses_list': latest_expenses_list}
    return render(request, 'money_calc/expenses.html', context)


def tasks(request):
    latest_task_list = Tasks.objects.order_by('-id')
    context = {'latest_task_list': latest_task_list}
    return render(request, 'money_calc/tasks.html', context)


class OrderDetailView(DetailView):
    model = Order
    template_name = 'money_calc/details_view.html'
    context_object_name = 'order'


class OrderUpdateView(UpdateView):
    model = Order
    template_name = 'money_calc/create_order.html'

    form_class = OrderForm


class OrderDeleteView(DeleteView):
    model = Order
    success_url = ''
    template_name = 'money_calc/order-delete.html'


class WorkerUpdateView(UpdateView):
    model = Worker
    template_name = 'money_calc/update_worker.html'
    success_url = '/worker'
    form_class = WorkerForm


class WorkerDeleteView(DeleteView):
    model = Worker
    success_url = '/worker'
    template_name = 'money_calc/worker-delete.html'


class AgentUpdateView(UpdateView):
    model = Agent
    template_name = 'money_calc/update_agent.html'
    success_url = '/agent'
    form_class = AgentForm


class AgentDeleteView(DeleteView):
    model = Agent
    success_url = '/agent'
    template_name = 'money_calc/agent-delete.html'


def create(request):
    error = ''

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('orders')
        else:
            error = 'Form is not valid'

    form = OrderForm()

    data = {
        'form': form,
        'error': error,
    }

    return render(request, 'money_calc/create_order.html', data)


def create_worker(request):
    error = ''

    if request.method == 'POST':
        form = WorkerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('worker')
        else:
            error = 'Form is not valid'

    form = WorkerForm()

    data = {
        'form': form,
        'error': error,
    }

    return render(request, 'money_calc/create_worker.html', data)


def create_agent(request):
    error = ''

    if request.method == 'POST':
        form = AgentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agent')
        else:
            error = 'Form is not valid'

    form = AgentForm()

    data = {
        'form': form,
        'error': error,
    }

    return render(request, 'money_calc/create_agent.html', data)


def worker_orders(request, worker_id):
    worker = Worker.objects.get(id=worker_id)
    orders = Order.objects.filter(worker=worker)
    cash_orders = Order.objects.filter(worker=worker, payment_method='cash')
    card_orders = Order.objects.filter(worker=worker, payment_method='card')
    law_orders = Order.objects.filter(worker=worker, payment_method='law')
    total_sum = 0
    for order in orders:
        total_sum += order.sum

    cash = 0
    for order in cash_orders:
        cash += order.sum

    card = 0
    for order in card_orders:
        card += order.sum

    law = 0
    for order in law_orders:
        law += order.sum

    count_order = orders.count()

    if count_order > 0:
        avg_order_sum = total_sum / count_order
    else:
        avg_order_sum = 0

    context = {
        'worker': worker,
        'orders': orders,
        'total_sum': total_sum,
        'avg_order_sum': avg_order_sum,
        'cash': cash,
        'card': card,
        'law': law,
    }

    return render(request, 'money_calc/worker_orders.html', context)


def agent_orders(request, agent_id):
    agent = Agent.objects.get(id=agent_id)
    orders = Order.objects.filter(agent=agent)
    cash_orders = Order.objects.filter(agent=agent, payment_method='cash')
    card_orders = Order.objects.filter(agent=agent, payment_method='card')
    law_orders = Order.objects.filter(agent=agent, payment_method='law')
    total_sum = 0

    for order in orders:
        total_sum += order.sum

    cash = 0
    for order in cash_orders:
        cash += order.sum

    card = 0
    for order in card_orders:
        card += order.sum

    law = 0
    for order in law_orders:
        law += order.sum

    count_order = orders.count()

    if count_order > 0:
        avg_order_sum = total_sum / count_order
    else:
        avg_order_sum = 0

    context = {
        'agent': agent,
        'orders': orders,
        'total_sum': total_sum,
        'avg_order_sum': avg_order_sum,
        'cash': cash,
        'card': card,
        'law': law,
    }

    return render(request, 'money_calc/agent_view.html', context)


class Round(Func):
    function = 'ROUND'
    template = '%(function)s(%(expressions)s, 0)'


def index(request):
    expenses = Expenses.objects.all()
    orders = Order.objects.all()

    orders_pay = Order.objects.filter(payment_status='yes')
    orders_pay_cash = Order.objects.filter(payment_status='yes', payment_method='cash')
    orders_pay_card = Order.objects.filter(payment_status='yes', payment_method='card')
    orders_pay_law = Order.objects.filter(payment_status='yes', payment_method='law')
    orders_pay_cash_count = orders_pay_cash.count()
    orders_pay_card_count = orders_pay_card.count()
    orders_pay_law_count = orders_pay_law.count()

    orders_not_pay = Order.objects.filter(payment_status='no')
    orders_not_pay_cash = Order.objects.filter(payment_status='no', payment_method='cash')
    orders_not_pay_card = Order.objects.filter(payment_status='no', payment_method='card')
    orders_not_pay_law = Order.objects.filter(payment_status='no', payment_method='law')
    orders_not_pay_cash_count = orders_not_pay_cash.count()
    orders_not_pay_card_count = orders_not_pay_card.count()
    orders_not_pay_law_count = orders_not_pay_law.count()

    count_order = orders.count()
    orders_pay_count = orders_pay.count()
    orders_not_pay_count = orders_not_pay.count()

    expense_sum = 0
    for expense in expenses:
        expense_sum += expense.cost

    total_sum = 0
    for order in orders:
        total_sum += order.sum

    avg_order_sum = total_sum / count_order

    pay_sum = 0
    for pay in orders_pay:
        pay_sum += pay.sum

    not_pay_sum = 0
    for pay in orders_not_pay:
        not_pay_sum += pay.sum

    latest_expense_list = Expenses.objects.order_by('-id')[:5]

    order_analytics = Order.objects.values('publish_data__week_day').annotate(total=Round(Avg('sum')))

    analytics = [0] * 7
    for analytics_data in order_analytics:
        day_of_week = analytics_data['publish_data__week_day']
        total_amount = analytics_data['total']
        analytics[day_of_week - 1] = total_amount

    locale = "ru_RU"
    day_names = [format_date(date(2022, 1, i + 1), format="eee", locale=locale) for i in range(7)]

    context = {
        'expenses': expenses,
        'orders': orders,
        'expense_sum': expense_sum,
        'total_sum': total_sum,
        'count_order': count_order,
        'orders_pay': orders_pay,
        'orders_not_pay': orders_not_pay,
        'pay_sum': pay_sum,
        'not_pay_sum': not_pay_sum,
        'orders_pay_count': orders_pay_count,
        'orders_pay_cash': orders_pay_cash,
        'orders_pay_card': orders_pay_card,
        'orders_pay_law': orders_pay_law,
        'orders_pay_cash_count': orders_pay_cash_count,
        'orders_pay_card_count': orders_pay_card_count,
        'orders_pay_law_count': orders_pay_law_count,
        'orders_not_pay_count': orders_not_pay_count,
        'orders_not_pay_cash': orders_not_pay_cash,
        'orders_not_pay_card': orders_not_pay_card,
        'orders_not_pay_law': orders_not_pay_law,
        'orders_not_pay_cash_count': orders_not_pay_cash_count,
        'orders_not_pay_card_count': orders_not_pay_card_count,
        'orders_not_pay_law_count': orders_not_pay_law_count,
        'latest_expense_list': latest_expense_list,
        'analytics': analytics,
        'day_names': day_names,
        'avg_order_sum': avg_order_sum,
    }

    return render(request, 'money_calc/index.html', context)


class ExpensesDetailView(DetailView):
    model = Expenses
    template_name = 'money_calc/expenses-expense.html'
    context_object_name = 'expense'


def create_expense(request):
    error = ''

    if request.method == 'POST':
        form = ExpensesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('expenses')
        else:
            error = 'Form is not valid'

    form = ExpensesForm()

    data = {
        'form': form,
        'error': error,
    }

    return render(request, 'money_calc/create_expense.html', data)


class ExpenseUpdateView(UpdateView):
    model = Expenses
    template_name = 'money_calc/update_expense.html'
    success_url = '/expenses'
    form_class = ExpensesForm


class ExpenseDeleteView(DeleteView):
    model = Expenses
    success_url = '/expenses'
    template_name = 'money_calc/expense-delete.html'


class TaskDetailView(DetailView):
    model = Tasks
    template_name = 'money_calc/tasks-task.html'
    context_object_name = 'task'


def create_task(request):
    error = ''

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks')
        else:
            error = 'Form is not valid'

    form = TaskForm()

    data = {
        'form': form,
        'error': error,
    }

    return render(request, 'money_calc/create_task.html', data)


class TaskUpdateView(UpdateView):
    model = Tasks
    template_name = 'money_calc/update_task.html'
    success_url = '/tasks'
    form_class = TaskForm


class TaskDeleteView(DeleteView):
    model = Tasks
    success_url = '/tasks'
    template_name = 'money_calc/task-delete.html'

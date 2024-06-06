from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('orders', views.orders, name='orders'),
    path('not_pay_orders', views.not_pay_orders, name='not_pay_orders'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.OrderDetailView.as_view(), name='order-detail'),
    path('<int:pk>/update', views.OrderUpdateView.as_view(), name='order-update'),
    path('<int:pk>/delete', views.OrderDeleteView.as_view(), name='order-delete'),
    path('worker', views.worker, name='worker'),
    path('create-worker', views.create_worker, name='create-worker'),
    path('worker/<int:pk>/update', views.WorkerUpdateView.as_view(), name='worker-update'),
    path('worker/<int:pk>/delete', views.WorkerDeleteView.as_view(), name='worker-delete'),
    path('worker/<int:worker_id>', views.worker_orders, name='worker-orders'),
    path('agent', views.agent, name='agent'),
    path('create-agent', views.create_agent, name='create-agent'),
    path('agent/<int:pk>/update', views.AgentUpdateView.as_view(), name='agent-update'),
    path('agent/<int:pk>/delete', views.AgentDeleteView.as_view(), name='agent-delete'),
    path('agent/<int:agent_id>', views.agent_orders, name='agent-detail'),
    path('expenses', views.expenses, name='expenses'),
    path('expense/<int:pk>', views.ExpensesDetailView.as_view(), name='expenses-expense'),
    path('create-expense', views.create_expense, name='create-expense'),
    path('expense/<int:pk>/update', views.ExpenseUpdateView.as_view(), name='expense-update'),
    path('expense/<int:pk>/delete', views.ExpenseDeleteView.as_view(), name='expense-delete'),
    path('tasks', views.tasks, name='tasks'),
    path('task/<int:pk>', views.TaskDetailView.as_view(), name='tasks-task'),
    path('create-task', views.create_task, name='create-task'),
    path('task/<int:pk>/update', views.TaskUpdateView.as_view(), name='task-update'),
    path('task/<int:pk>/delete', views.TaskDeleteView.as_view(), name='task-delete'),
]

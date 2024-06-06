from django.contrib import admin

from .models import Order, Worker, Agent, Expenses, Tasks

admin.site.register(Order)
admin.site.register(Worker)
admin.site.register(Agent)
admin.site.register(Expenses)
admin.site.register(Tasks)

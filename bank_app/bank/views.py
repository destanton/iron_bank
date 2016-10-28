from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from rest_framework.generics import ListCreateAPIView
from bank.models import Transaction


def index_view(request):
    context = {
        "info": Transaction.objects.all()
    }
    return render(request, 'index.html', context)


class TransactionCreateView(CreateView):
    model = Transaction
    success_url = "/"
    fields = ('amount', 'transaction_type')


class UserCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy("user_create_view")


class TransactionListCreateAPIView(ListCreateAPIView):
    pass
    # queryset = Transaction.objects.all()
    # serializer_class = TransactionSerializer

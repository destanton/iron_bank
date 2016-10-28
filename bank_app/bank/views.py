from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from rest_framework.generics import ListCreateAPIView
from bank.models import Transaction, Profile


def index_view(request):
    context = {
        "info": Transaction.objects.all()
    }
    return render(request, 'index.html', context)


class TransactionCreateView(CreateView):
    model = Transaction
    success_url = "/"
    fields = ('amount', 'transaction_type')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["amount"] = Profile.objects.get(user=self.request.user)
        context["transaction"] = Transaction.objects.filter(user=self.request.user)
        return context

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        if instance.transaction_type == "W":
            instance.amount = -instance.amount
        elif instance.transaction_type == "D":
            instance.amount == instance.amount
        return super().form_valid(form)


class UserCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy("user_create_view")


class TransactionListCreateAPIView(ListCreateAPIView):
    pass
    # queryset = Transaction.objects.all()
    # serializer_class = TransactionSerializer

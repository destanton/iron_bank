from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from bank.models import Transaction, Profile
from bank.serializers import TransactionSerializer
from rest_framework.permissions import IsAuthenticated
from bank.permissions import IsCurrentUser
from django.core.exceptions import ValidationError



def index_view(request):
    context = {
        "info": Transaction.objects.all()
    }
    return render(request, 'index.html', context)


class TransactionCreateView(CreateView):
    model = Transaction
    success_url = reverse_lazy("transaction_create_view")
    fields = ('amount', 'transaction_type')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["amount"] = Profile.objects.get(user=self.request.user)
        context["transaction"] = Transaction.objects.filter(user=self.request.user)
        return context

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.balance = instance.user.profile.get_total
        # print(instance.balance)
        if instance.transaction_type == "W":
            instance.amount = -instance.amount
            if instance.amount + instance.balance < 0:
                # print(instance.amount)
                # print(instance.balance)
                # raise ValidationError("Insufficient Funds")
                form.add_error('amount', 'Insufficient Funds for Withdrawal Amount')  # found this online and looks better than validation error page.
                return self.form_invalid(form)
        elif instance.transaction_type == "D":
            instance.amount == instance.amount
        return super().form_valid(form)


class UserCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy("user_create_view")


class TransactionListCreateAPIView(ListCreateAPIView):
    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)
    serializer_class = TransactionSerializer
    permission_classes = (IsAuthenticated, )

    def perform_create(self, serializer):
        print(serializer)
        serializer.save(user=self.request.user)
        return super().perform_create(serializer)


class TransactionDetailAPIView(RetrieveAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = (IsCurrentUser, )

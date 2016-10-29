from rest_framework import serializers
from bank.models import Transaction, Profile


class TransactionSerializer(serializers.ModelSerializer):

    # user = serializers.ReadOnlyField(source="user.id")

    class Meta:
        model = Transaction
        exclude = ("user", )

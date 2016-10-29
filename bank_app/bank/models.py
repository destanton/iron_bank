from django.db import models
from django.dispatch import receiver
from django.conf import settings
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token


@receiver(post_save, sender='auth.User')
def create_user_profile(**kwargs):
    created = kwargs.get('created')
    instance = kwargs.get('instance')
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


TRANSACTION_TYPE = [
        ('W', 'Withdrawal'),
        ('D', 'Deposit')
]


class Transaction(models.Model):
    user = models.ForeignKey('auth.User')
    time_created = models.DateTimeField(auto_now_add=True)
    amount = models.FloatField()
    transaction_type = models.CharField(max_length=1, choices=TRANSACTION_TYPE, default='D')

    def __str__(self):
        return self.transaction_type


class Profile(models.Model):
    user = models.OneToOneField('auth.User')
    favorite_color = models.CharField(max_length=50)

    def __str__(self):
        return self.user.username

    @property
    def get_total(self):
        get_amount = Transaction.objects.filter(user=self.id)
        new_list = [total.amount for total in get_amount]
        print(new_list)
        return sum(new_list)

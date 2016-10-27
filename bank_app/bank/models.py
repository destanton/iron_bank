from django.db import models
from django.dispatch import receiver
from django.db.models.signals import postsave

TRANSACTION_TYPE = [
        ('W', 'Withdrawal'),
        ('D', 'Deposit')
]


class Transaction(models.Model):
    user = models.ForeignKey('auth.User')
    time_created = models.DateTimeField(auto_now_add=True)
    amount = models.FloatField()
    transaction_type = models.CharField(max_length=1, choices=TRANSACTION_TYPE, default='D')


@receiver(post_save, sender='auth.User')
def create_user_profile(**kwargs):
    created = kwargs.get('created')
    instance = kwargs.get('instance')
    if created:
        Profile.objects.create(user=instance)


class Profile(models.Model):
    user = models.OneToOneField('auth.User')
    favorite_color = models.CharField(max_length=50)

    def __str__(self):
        return self.user.username

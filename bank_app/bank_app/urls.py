"""bank_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from bank.views import index_view, UserCreateView, TransactionCreateView, TransactionListCreateAPIView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^$', index_view, name="index_view"),
    url(r'^transaction/$', TransactionCreateView.as_view(), name='transaction_create_view'),
    url(r'^api/transactions/$', TransactionListCreateAPIView.as_view(), name="transaction_list_create_api_view"),
    url(r'^create_user/$', UserCreateView.as_view(), name="user_create_view")
]

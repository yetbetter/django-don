import json

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from profiles.models import Info
from profiles.utils import fetch_user_balance_from_1c

model = Info

@login_required
def get_user_balance(request):
    if request.user.is_superuser:
        invoice_num = 0
    else:
        user_id = get_user_id(request)
        invoice_num = get_user_invoice_num(user_id=user_id)

    balance = fetch_user_balance_from_1c(invoice_num)

    return render(
        request,
        template_name='profiles/user_balance.html',
        context=json.loads(balance)
    )


def get_user_id(request):
    return request.session.get('_auth_user_id')


def get_user_invoice_num(user_id):
    return model.objects.get(user_id=user_id).invoice_num

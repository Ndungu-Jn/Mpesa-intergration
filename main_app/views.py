import json

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django_daraja.mpesa.core import MpesaClient


# Create your views here.
def trigger(request):
    cl = MpesaClient()
    phone_number = '07**********'
    amount = 1
    account_reference = '001-XYZ'
    transaction_desc = 'madeni'
    callback_url = 'https://pleasing-partly-hamster.ngrok-free.app/callback'
    response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
    return HttpResponse(response)


@csrf_exempt
def callback(request):
    resp = json.loads(request.body)
    print(resp)
    return HttpResponse("OK")


#chatsasa
#mobilesasa
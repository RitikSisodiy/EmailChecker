from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .emailChecker import checkmail
# Create your views here.
def index(request):
    res = {
        "message": "working"
    }
    return JsonResponse(res, safe=False)
@csrf_exempt
def emailCheck(request):
    if request.method == "POST":
        try:
            body = json.loads(request.body)
        except:
            return JsonResponse({"message":"invalid json"},status=400)
        emails = body.get("emails")
        res,status = checkmail(emails)
        return JsonResponse(res,status=status)
    return JsonResponse({"message":"get working"})
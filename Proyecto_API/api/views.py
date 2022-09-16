from email.mime import message
from django.shortcuts import render
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from .models import Company
import json


class Company_views(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if (id >0):
            companies=list(Company.objects.filter(id=id).values())
            if (len(companies)>0):
                company=companies[0]
                res = {'message': "OK", 'company':company}
            else:
                res = {'message': "From lost to the river...."}
            return JsonResponse(res)
        else:
            companies = list(Company.objects.values())
            if len(companies)>0:
                res = {'message': "OK", 'companies':companies}
            else:
                res = {'message': "From lost to the river...."}
            return JsonResponse(res)
    

    def post(self, request):
        jd = json.loads(request.body)
        Company.objects.create(name=jd['name'], website=jd['website'], foundation=jd['foundation'])
        return JsonResponse(jd, safe=False)

    def put(self, request):
        pass

    def delete(self, request):
        pass




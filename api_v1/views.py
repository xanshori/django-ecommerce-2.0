from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from accounts.models import Account
from .serializers import AccountSerializer




class Route(APIView):
    def get(self, request):
        domain = request.META['HTTP_HOST']
        data = {'GET': f'{domain}/api/v1/users/'}
        return Response(data)

class AccountList(APIView):
    def get(self, request):
        account = Account.objects.all()
        serializer = AccountSerializer(account, many=True)
        return Response(serializer.data)

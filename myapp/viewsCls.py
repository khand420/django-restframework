from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from rest_framework.response import Response
from .serializers import TodoSerializer
from .models import Todo
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from rest_framework.pagination import PageNumberPagination


class TodoView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            # data_objs = Todo.objects.all()
            data_objs = Todo.objects.filter(user = request.user)
            
            # Initialize the paginator and paginate the queryset
            paginator = PageNumberPagination()
            page = paginator.paginate_queryset(data_objs, request)      
            # If there is a paginated page, use the paginator to generate the response
            if page is not None:
                serializer = TodoSerializer(page, many=True)
                return paginator.get_paginated_response(serializer.data)
            
            serializer = TodoSerializer(data_objs, many = True)
            return Response({
            'status': 200,
            'message': 'success todo created',
            'data': serializer.data
            })
            
        except Exception as e:
            print(e)

    def post(self, request):
        try:
            data = request.data
            data['user'] = request.user.id
            print(data)


            serializer = TodoSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                print(serializer.data)

                return Response({
                'status': 201,
                'message': 'success todo created',
                'data': serializer.data
                })
            
            else:
                return Response({
                'status': False,
                'message': 'Invalid data',
                'data': serializer.errors
                })
        except Exception as e:
            print(e)



    def patch(self, request): 
        try:
            data = request.data
            # print(data)
            if not data.get('id'):
                return Response({
                'status': False,
                'message': 'id is required',
                'data': serializer.errors
                })
            
            obj = Todo.objects.get(id = data.get('id'))
            serializer = TodoSerializer(obj, data=data, partial = True)
            if serializer.is_valid():
                serializer.save()
                print(serializer.data)

                return Response({
                'status': 202,
                'message': 'success todo update',
                'data': serializer.data
                })
            
            else:
                return Response({
                'status': False,
                'message': 'Invalid id',
                'data': {}
                })
        except Exception as e:
            print(e)
    
              




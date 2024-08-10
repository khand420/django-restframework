from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TodoSerializer
from .models import Todo
from rest_framework.permissions import IsAuthenticated



# Create your views here.
# @api_view(['GET'])
# def get_home(request):
#     return Response({
#         'status': 200,
#         'message': 'Rest Framework working'
#     })



@api_view(['GET', 'POST', 'PATCH'])
def get_home(request):
    if request.method == "GET":

        data = {
                'status':200,
                'message': 'Welcome to the home page',
                "request":"GET" }
        return Response(data)
    
    elif request.method == "POST":
        return Response({
        'status': 200,
        'message': 'Rest Framework working',
        'request': 'post'

    })

    elif request.method == "PATCH":
        return Response({
        'status': 200,
        'message': 'Rest Framework working',
        'request': 'PATCH'

    })

    else:
        return Response({
        'status': 400,
        'message': 'Rest Framework working',
        'request': 'neither GET nor POST'
    })




@api_view(['GET'])
def get_todo(request):
    try:
        data_objs = Todo.objects.all()
        serializer = TodoSerializer(data_objs, many = True)
        return Response({
        'status': 200,
        'message': 'success todo created',
        'data': serializer.data
        })
        
    except Exception as e:
        print(e)




@api_view(['POST'])
def post_todo(request):
    try:
        data = request.data
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


@api_view(['PATCH'])
def patch_todo(request):
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

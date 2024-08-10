from rest_framework import status, viewsets
from .models import Todo, TimingTodo
from .serializers import TodoSerializer, TimingSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

# CRUD OPERATATION WORK IN THESE THREE LINE OF CODE ONLY
# GET, POST , PATCH , PUT, DELETE in single route todo-view-set

# class TodoViewSets(viewsets.ModelViewSet):
#     queryset = Todo.objects.all()
#     serializer_class = TodoSerializer

   
# with using #actions to handle http methods taking as a function name as endpoint
class TodoViewSets(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    @action(detail=False, methods=['get'])
    def get_timing_todo(self, request):
        try:
            obj = TimingTodo.objects.all()
            serializer = TimingSerializer(obj, many=True)
            return Response({
                'status': 200,
                'message': 'success',
                'data': serializer.data
            })
        except Exception as e:
            print('error----', e)
            return Response({
                'status': False,
                'message': 'An error occurred',
                'data': str(e)
            })

    @action(detail=False, methods=['post'])
    def add_date_to_todo(self, request):
        try:
            data = request.data
            print(data)

            serializer = TimingSerializer(data=data)
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

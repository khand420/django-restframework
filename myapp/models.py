from django.db import models
import uuid
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class BaseModel(models.Model):
    # uid = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    uid = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4, unique=True)    
    # uid = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    # created_at = models.DateField(auto_created=True)
    created_at = models.DateTimeField(default=timezone.now)
    # updated_at = models.DateField(auto_created=True)
    updated_at = models.DateTimeField(default=timezone.now)



    class Meta:
        abstract = True



class Todo(BaseModel):
    user = models.ForeignKey(User, on_delete= models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    is_done = models.BooleanField(default=False)

# class Todo(models.Model):
#     title = models.CharField(max_length=100)
#     description = models.TextField()
#     is_done = models.BooleanField(default=False)


class TimingTodo(BaseModel):
    todo = models.ForeignKey(Todo, on_delete= models.CASCADE)
    timing = models.DateField()


    
    



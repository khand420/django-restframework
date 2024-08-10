from django.contrib import admin
from . models import Todo, TimingTodo

# Register your models here.
admin.site.register(Todo) 
admin.site.register(TimingTodo)
 


# admin.site.register(BaseModel)uid = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4, unique=True)
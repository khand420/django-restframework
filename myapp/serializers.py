from rest_framework import serializers
from .models import Todo, TimingTodo
import re
from django.template.defaultfilters import slugify

class TodoSerializer(serializers.ModelSerializer):
    slug = serializers.SerializerMethodField()
    class Meta:
        model = Todo
        # fields = '__all__' 
        fields = ['user','title', 'description', 'is_done', 'slug','uid']

    
    def get_slug(self, obj):
        return slugify(obj.description)
        # return 'mydata fruits'


    def validate_title(self, data):
        # print('validate_data',validate_data)
        if data:
            tital = data
            regex = re.compile('[@!$%#]')
            if len(tital) < 3:
                raise serializers.ValidationError('title should be character 3 or greater')
            
            if not regex.search(tital) == None:
                raise serializers.ValidationError('title should not be contain special character')
            
        return data
    
    # def validate(self, validate_data):
        # print('validate_data',validate_data)
        # if validate_data.get('title'):
        #     tital = validate_data['title']
        #     regex = re.compile('[@!$%#]')
        #     if len(tital) > 3:
        #         raise serializers.ValidationError('title should be character 3')
            
        #     if not regex.search(tital) == None:
        #         raise serializers.ValidationError('title should not be contain special character')
            
        # return validate_data
    

class TimingSerializer(serializers.ModelSerializer):
    # method field - only get or inheritent fields define in TodoSerializer()
    todo = TodoSerializer()
    class Meta:
        model =  TimingTodo
        exclude = ['created_at', 'updated_at']
        # fields = '__all__' 

        #depht get all fields of forignkey
        # depth = 1

    # depth vs method field are use to get foriegnkey all data 

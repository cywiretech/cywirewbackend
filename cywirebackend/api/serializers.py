from rest_framework import serializers
from .models import *

class NewsletterSerial(serializers.ModelSerializer):
    
    class Meta:
        model = Newsletter
        fields = '__all__'
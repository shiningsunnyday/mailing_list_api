from rest_framework import serializers
from quizkly_app.models import Contact
from django.contrib.auth.models import User

class ContactSerializer(serializers.ModelSerializer):
    email = serializers.CharField(max_length = 30)
    beta = serializers.BooleanField()
    class Meta:
        model = Contact
        fields  = ('email', 'beta')

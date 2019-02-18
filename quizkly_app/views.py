from rest_framework import status
from rest_framework import permissions
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from quizkly_app.models import Contact
from quizkly_app.serializers import ContactSerializer
from django.http import Http404
from django.contrib.auth.models import User
from quizkly_app.permissions import IsOwnerOrReadOnly

class ContactList(APIView):

    def get(self, request, format = None):

        contacts = Contact.objects.all()
        serializer = ContactSerializer(contacts, many = True)
        return Response(serializer.data)

    def post(self, request, format = None):

        email = request.data["email"]
        beta = request.data["beta"]
        contact = Contact(email = email, beta = beta)
        contact.save()
        serializer = ContactSerializer(data = request.data)
        if serializer.is_valid():
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class ContactDetail(APIView):

    def get_object(self, pk):

        try:
            contact = Contact.objects.get(pk = pk)
        except Contact.DoesNotExist:
            raise Http404

    def get(self, request, pk, format = None):

        contact = self.get_object(pk)
        serializer = ContactSerializer(contact)
        return Response(serializer.data)

    def put(self, request, pk, format = None):

        contact = self.get_object(pk)
        serializer = ContactSerializer(contact, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format = None):

        contact = self.get_object(pk)
        contact.delete()
        return HttpResponse(status = status.HTTP_204_NO_CONTENT)

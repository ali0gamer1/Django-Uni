from django.shortcuts import render
from rest_framework import generics
# Create your views here.
from .models import Term
from .serializers import TermSerializer

class TermListAPIView(generics.ListAPIView):
    serializer_class = TermSerializer
    model = Term
    queryset = Term.objects.all()


class TermAPIView(generics.RetrieveAPIView):
    serializer_class = TermSerializer
    model = Term
    queryset = Term.objects.all()
    lookup_field = "pk" #pk is default
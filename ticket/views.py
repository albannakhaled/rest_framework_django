from django.http import Http404
from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from .models import Guest
from .serializers import GuestSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import BasicAuthentication , TokenAuthentication
from rest_framework.permissions import IsAuthenticated

#1 without rest framework without model

def no_rest_no_model(request):
    guests = [
        {
            'id':1,
            'name':'khaled',
            'mobile':213243,
        }
    ]
    return JsonResponse(guests , safe=False)

#------------------------------------------

#2 without rest with model

def no_rest_with_model(request):
    data = Guest.objects.all().values('name', 'phone')
    response = {
        'guest': list(data)
    }
    return JsonResponse(response)


#------------------------------------------


# 3 functional based views

@api_view(["GET", "POST", "PUT", "DELETE"])
def FBV_List(request):
    # GET
    if request.method == "GET":
        guests = Guest.objects.all()
        serializer = GuestSerializer(guests, many=True)
        return JsonResponse(serializer.data, safe=False)

    # POST
    elif request.method == "POST":
        serializer = GuestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)

    # PUT
    elif request.method == "PUT":
        try:
            guest = Guest.objects.get(pk=request.data["id"])
        except Guest.DoesNotExist:
            return Response("Guest not found", status=404)
        
        serializer = GuestSerializer(guest, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

    # DELETE
    elif request.method == "DELETE":
        try:
            guest = Guest.objects.get(pk=request.data["id"])
        except Guest.DoesNotExist:
            return Response("Guest not found", status=404)

        guest.delete()
        return Response("Guest deleted", status=204)


#------------------------------------------


# 4 class based views


class CBV_List(APIView):
    def get(self, request):
        guests = Guest.objects.all()
        serializer = GuestSerializer(guests, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = GuestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


#------------------------------------------


# 5 class based view pk
class CBV_PK(APIView):
    def get_object(self , pk):
        try:
            return Guest.objects.get(pk=pk)
        except Guest.DoesNotExist:
            raise Http404
    def get(self, request, pk):
        guest = self.get_object(pk)
        serializer = GuestSerializer(guest)
        return Response(serializer.data)

    def put(self , request , pk):
        guest = self.get_object(pk)
        serializer = GuestSerializer(guest, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    def delete(self , request , pk):
        guest = self.get_object(pk)
        guest.delete()
        return Response(status=204)
    

            

            

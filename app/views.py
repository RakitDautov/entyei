from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions

from .serializers import EntitySerializer, EntityPostSerializer
from .models import Entity


class Entyti_view(APIView):
    permission_classes = [permissions.IsAuthenticated, ]

    def post(self, request):
        #serializer = EntityPostSerializer(data={'value':request.data['data[value]']})
        serializer = EntityPostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(modified_by=request.user)
        return Response(status=status.HTTP_201_CREATED)
    
    def get(self, request):
        entyti = Entity.objects.all()
        serializer = EntitySerializer(entyti, many=True)
        return Response({"data": serializer.data})


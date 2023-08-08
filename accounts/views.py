from django.shortcuts import get_object_or_404

from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.viewsets import ViewSet

from .serializers import RegistrationSerializer,UserSerializer
from .models import CustomUser
# Create your views here.

@api_view(['POST', ])
@permission_classes([AllowAny])
def registration_view(request):

    if request.method == 'POST':

        serializer = RegistrationSerializer(data=request.data, context={'request': request})

        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data['response'] = 'successfully registered new user.'
            data['email'] = account.email
            data['username'] = account.username
            data['phone_number'] = account.phone_number
            data['Is_employee'] = account.Is_employee

        else:
            data = serializer.errors
        return Response(data)
    

class UserViewSet(ViewSet):
    permission_classes = (IsAuthenticated,)

    def list(self, request):
        queryset = CustomUser.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, username=None):
        queryset = CustomUser.objects.all()
        user = get_object_or_404(queryset, username=username)
        
        if request.user.Is_employee or request.user.username == "admin" or username == request.user.username:
            serializer = UserSerializer(user)
            return Response(serializer.data)

        return Response({"detail": "You do not have permission to view this user's information."}, status=403)
    
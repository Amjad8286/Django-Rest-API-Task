from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from .models import PersonDetails
from .serializers import PersonSerializers, UserSerializer
from django.contrib.auth.models import User
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAdminUser, DjangoModelPermissionsOrAnonReadOnly
# Create your views here.

class personListCreateView(ListCreateAPIView):
    queryset = PersonDetails.objects.all()
    serializer_class = PersonSerializers
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

class personListRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = PersonDetails.objects.all()
    serializer_class = PersonSerializers
    permission_classes = [IsAdminUser]

class personRegisterCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

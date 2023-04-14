from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.decorators import action

from src.apps.users.models.users import User
from src.apps.users.api.serializers import UserSerializer, UserCreateSerializer


class MyTokenRefreshView(TokenRefreshView):
    permission_classes = [IsAuthenticated, ]

    def post(self, request, *args, **kwargs):
        return Response(request.user.email)
        # super().post(request, *args, **kwargs)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-id')
    serializer_class = UserSerializer
    permission_classes = [AllowAny, ]

    def check_permissions(self, request):
        return super().check_permissions(request)

    def get_serializer_class(self, *args, **kwargs):
        serializer_class = super().get_serializer_class(*args, **kwargs)
        if self.action == 'create':
            serializer_class = UserCreateSerializer
        return serializer_class


@action(
        detail=False,
        method=['get'],
        url_name='verify',
        url_path='verify/(?P<code>[0-9]+)',
)
def verify(self, requets, code):
    return Response

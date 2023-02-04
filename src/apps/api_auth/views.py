from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)


class MyTokenRefreshView(TokenRefreshView):
    # permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        return Response(request.user.email)
        # super().post(request, *args, **kwargs)

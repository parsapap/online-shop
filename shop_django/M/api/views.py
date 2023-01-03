from rest_framework.views import APIView
from rest_framework.response import Response
from accounts.models import User
from .serializers import ProfileSerializer
from rest_framework import status


# account app api views
class ProfileApiView(APIView):
    def get(self, request, user_id):
        user = User.objects.get(id=user_id)
        ser_data = ProfileSerializer(instance=user)
        return Response(ser_data.data, status=status.HTTP_200_OK)


class ProfileEditApiView(APIView):
    pass

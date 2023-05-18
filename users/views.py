from . import tasks
from . import serializers
from . import models

from .permission import IsOwnerOrReadeOnly

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from redis import Redis


con = Redis(host="localhost", port=6380, db=0, charset="utf-8", decode_responses=True)

class UserLogin(APIView):

    def post(self, request, *args, **kwargs):
        serializer = serializers.UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        phone_number = serializer.validated_data.get("phone_number")
        otp_cachee = con.get(phone_number)
        if otp_cachee is None:
            tasks.send_sms(phone_number)
            return Response("code sends to your phone", status=status.HTTP_200_OK)
        else:
            return Response(f"your code was: {otp_cachee}", status=status.HTTP_200_OK)
        
        
class UserVerify(APIView):
    
    def post(self, request, *args, **kwargs):
        serializer = serializers.UserVeifySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        phone_number = serializer.validated_data.get("phone_number")
        otp_cache = con.get(phone_number)
        otp_user = serializer.validated_data.get("otp")
        
        if not otp_cache == otp_user:
            return Response("your code is not correct", status=status.HTTP_401_UNAUTHORIZED)
        
        user_name = serializer.validated_data.get("user_name")
        obj, created = models.UsersRegister.objects.get_or_create(user_name=user_name, phone_number=phone_number)
        refresh_token = RefreshToken().for_user(obj)
        access_token = refresh_token.access_token
        return Response(
            data =
            {
            "id": obj.id ,
            "access_token" : str(access_token),
            "refresh_token": str(refresh_token),
            "created" : created
            }, status=status.HTTP_201_CREATED
        )


class EditProfile(APIView):
    permission_classes = [IsOwnerOrReadeOnly]
    
    def patch(self, request, pk):
        queryset = models.UsersRegister.objects.get(pk=pk)
        self.check_object_permissions(request, queryset)
        serializer = serializers.EditProfileSerializer(instance=queryset, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

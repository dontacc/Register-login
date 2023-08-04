from rest_framework import status
from rest_framework.response import Response
from .serializers import *
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.permissions import *
from rest_framework.parsers import JSONParser, FormParser
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate




def response_func(status: bool, msg: str, data: dict):
    res = {
        'status': status,
        'message': msg,
        'data': data
    }

    return res


def token_for_user(user):
     refresh = RefreshToken.for_user(user)

     return {
          'access': str(refresh.access_token),
          'refresh': str(refresh)
     }




class RegisterView(APIView):
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer


    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)


        user = serializer.save()
        token = token_for_user(user)


        response = Response()

        access = token_for_user(user)['access']
        refresh = token_for_user(user)['refresh']

        response.set_cookie({"access": access})
        response.set_cookie({"refresh": refresh})


        return response





class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    # parser_classes = (FormParser, JSONParser)


    def post(self, request):
        # try:
            serializer = self.serializer_class(data = request.data)
            serializer.is_valid(raise_exception = True)

            # user = authenticate(username = serializer.validated_data.get('username'), 
            #                     password = serializer.validated_data.get('password'))
            


            username = serializer.validated_data.get('username')
            
            user_obj = User.objects.get(username = username)
            print(user_obj)
            

            if check_password(serializer.validated_data.get('password'), user_obj.password):

                response = Response()
                access = token_for_user(user_obj)['access']
                refresh = token_for_user(user_obj)['refresh']

                response.set_cookie("access_token", access, httponly=True)
                response.set_cookie("refresh_token", refresh, httponly=True)


                print(request.COOKIES['access_token'])
                print(request.COOKIES['refresh_token'])
            
                return response

                

            return Response({"errors": "password does not match!"}, status=status.HTTP_404_NOT_FOUND)
            
        # except Exception as e:
        #     return Response(response_func(
        #         False,
        #         "Something went wrong",
        #         {'error': str(e)}
        #     ), status=status.HTTP_400_BAD_REQUEST
        #     )
            





class UserProfile(generics.GenericAPIView):
    serializer_class = (UserProfile,)
    permission_classes = (IsAuthenticated,)



    def get(self):
        obj = User.objects.get(user_id = self.request.user.id)
        serializer = self.serializer_class(obj)

        return Response(serializer.data)
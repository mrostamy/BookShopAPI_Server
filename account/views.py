from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import SignUpSerializer
from rest_framework import status
from django.contrib.auth import authenticate
from .token import create_token

# Create your views here.


@api_view(http_method_names=["POST"])
def register(request: Request) -> Response:

    serializer = SignUpSerializer(data=request.data)

    if serializer.is_valid():
        user = serializer.save()
        response = {"message": "user created successfully", "data": serializer.data}

        return Response(data=response, status=status.HTTP_201_CREATED)
    return Response(
        data={"message": "error in createing user", "data": serializer.errors},
        status=status.HTTP_400_BAD_REQUEST,
    )

@api_view(http_method_names=["POST"])
def login(request: Request) -> Response:

    email = request.data.get("email")
    password = request.data.get("password")

    print(request.data)

    user = authenticate(email=email,password=password)

    if user is not None:
        token = create_token(user)
        response = {"message": "user logined successfully", "tokens": token}
        return Response(data=response, status=status.HTTP_200_OK)
    return Response(data="user not found", status=status.HTTP_400_BAD_REQUEST)

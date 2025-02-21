from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()


def create_token(user: User):

    token = RefreshToken.for_user(user=user)

    return {"access_token": str(token.access_token), "refresh_token": str(token)}

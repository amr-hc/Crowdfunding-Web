from django.contrib.auth import authenticate
from api.models import User
import os
import random
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.authtoken.models import Token

def generate_username(name):

    username = "".join(name.split(' ')).lower()
    if not User.objects.filter(username=username).exists():
        return username
    else:
        random_username = username + str(random.randint(0, 1000))
        return generate_username(random_username)


def register_social_user(provider, user_id, email, name):
    filtered_user_by_email = User.objects.filter(email=email)
    print("hi")

    if filtered_user_by_email.exists():

        if provider == filtered_user_by_email[0].auth_provider:
            user = filtered_user_by_email[0]
            registered_user = authenticate(
                email=email, password=os.environ.get('SOCIAL_SECRET'))

            token, created = Token.objects.get_or_create(user=user)

            return {
                    "token": str(token),
                    'email': user.email,
                    "user_id": user.id,
                    "is_superuser": user.is_superuser,
                    "userName": user.first_name + " " + user.last_name,
                }

        else:
            raise AuthenticationFailed(
                detail='Please continue your login using ' + filtered_user_by_email[0].auth_provider)

    else:
        user = {
            'username': generate_username(name), 'email': email,
            'password': os.environ.get('SOCIAL_SECRET')}
        user = User.objects.create_user(**user)
        user.is_verified = True
        user.auth_provider = provider
        user.save()

        new_user = authenticate(
            email=email, password=os.environ.get('SOCIAL_SECRET'))
        return {
            'email': new_user.email,
            'username': new_user.username,
            'tokens': new_user.tokens()
        }
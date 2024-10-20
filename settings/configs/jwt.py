from datetime import timedelta

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=1),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=30),
    'TOKEN_OBTAIN_SERIALIZER': "FavLinks.services.auth.serializers.MyTokenObtainPairSerializer",
    "ALGORITHM": "HS256",
    # "SIGNING_KEY": SECRET_KEY,
}



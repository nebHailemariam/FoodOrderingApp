from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from users.serializers.common.security_serializers import LoginSerializer


@api_view(['POST'])
@permission_classes([])
def login(request):
    if request.method == "POST":
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token":token.key},status=200)

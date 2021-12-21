from rest_framework.serializers import ModelSerializer
from dashboard.models import AgencyName, UserExtended, QRCodeGenerator, PresenceRecap, InvitationLink
from django.contrib.auth.models import User


class AgencySerializer(ModelSerializer):
    class Meta:
        model = AgencyName
        fields = '__all__'


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

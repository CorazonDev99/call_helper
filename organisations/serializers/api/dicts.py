import pdb

from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.db import transaction
from rest_framework import serializers
from rest_framework.exceptions import ParseError

from common.serializers.mixins import ExtendedModelSerializer
from users.serializers.nested.profile import ProfileShortSerializer, \
    ProfileUpdateSerializer

User = get_user_model()


class PositionListSerializer(ExtendedModelSerializer):
    class Meta:
        model = User
        fields = (
            'code',
            'name',

        )


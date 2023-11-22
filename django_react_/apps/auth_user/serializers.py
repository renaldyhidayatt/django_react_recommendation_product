from rest_framework.validators import UniqueValidator
from rest_framework import serializers
from apps.user.models import User


class RegisterationSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    email = serializers.CharField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(write_only=True)
    password_confirmation = serializers.CharField(write_only=True)

    def create(self, validated_data):
        validated_data.pop("password_confirmation")
        user = User.objects.create_user(**validated_data)
        return user

    def validate_password(self, password):
        password_confirmation = self.context.get("request").data.get(
            "password_confirmation"
        )

        if password != password_confirmation:
            raise serializers.ValidationError(
                "password and password confirmation do not match"
            )

        return password

    class Meta:
        model = User
        fields = [
            "name",
            "email",
            "password",
            "password_confirmation",
        ]

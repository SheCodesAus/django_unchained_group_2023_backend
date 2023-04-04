from rest_framework import serializers, validators
from django.contrib.auth.password_validation import validate_password
from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    # id = serializers.ReadOnlyField()
    # username = serializers.CharField(max_length=150)
    # email = serializers.EmailField()

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'password', 'my_favorites']
        extra_kwargs = {'password': {'write_only': True}}
        read_only_fields = ['id']

    def create(self, validated_data):
        user = CustomUser.objects.create(
            username = validated_data['username'],
            email = validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email',instance.email)
        instance.set_password = validated_data.get('password')
        instance.my_favorites = validated_data.get('my_favorites')
        instance.save()
        return instance

class ChangePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    old_password = serializers.CharField(write_only=True, required=True)
    success = serializers.BooleanField(read_only=True, default=True)
    class Meta:
        model = CustomUser
        fields = ('old_password', 'password', 'username', 'success', 'my_favorites')
        read_only_fields = ['id']

    def validate_old_password(self, value):
        instance = getattr(self, "instance", None)
        # print(f"{instance=} {value=}")
        if not instance:
            raise serializers.ValidationError({"old_password": "Instance not found"})
        # print(instance.check_password(value))
        if not instance.check_password(value):
            raise serializers.ValidationError({"old_password": "Old password is not correct"})
        return value
    def update(self, instance, validated_data):
        instance.set_password(validated_data['password'])
        instance.save()
        return instance


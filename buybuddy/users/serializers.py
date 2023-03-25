from rest_framework import serializers, validators

from .models import CustomUser

from django.contrib.auth.password_validation import validate_password

class CustomUserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    username = serializers.CharField(max_length=150)
    email = serializers.EmailField()

    def create(self, validated_data):
        return CustomUser.objects.create(**validated_data)
        user.set_password(validate_date['password'])
        user.save()
        return user
    
    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email',instance.email)
        instance.set_password = validated_data.get('password')
        instance.save()
        return instance

class ChangePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    old_password = serializers.CharField(write_only=True, required=True)
    success = serializers.BooleanField(read_only=True, default=True)
    class Meta:
        model = CustomUser
        fields = ('old_password', 'password', 'username', 'success')
        read_only_fields = [
            'username'
        ]
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
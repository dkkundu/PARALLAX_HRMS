from rest_framework import serializers
from django.contrib.auth import get_user_model
from Core.models import Profile
USER_MODEL = get_user_model()


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = (
            "first_name", "last_name", "photo",
            "website", "gender", "father_name",
            "nid", "address"
        )


class UserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer(required=False)

    class Meta:
        model = USER_MODEL
        fields = '__all__'
        read_only_fields = (
            'last_login', 'is_active', 'is_staff', 'is_superuser',
            'groups', 'user_permissions',
        )
        extra_kwargs = {
            'password': {
                'write_only': True,
                'min_length': 8,
                'style': {'input_type': 'password'},
            },
        }

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        password = validated_data.pop('password')
        user = USER_MODEL(**validated_data)
        user.set_password(password)
        user.save()
        if profile_data:  # takes profile dict, sets attrs, saves profile obj
            self.update_profile(user.profile, profile_data)
        return user

    def update_profile(self, instance, validated_data):
        for k, v in validated_data.items():
            if v == '' and instance._meta.get_field(k).unique:
                v = None
            setattr(instance, k, v)
        instance.save()


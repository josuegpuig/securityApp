from rest_framework import serializers
from .models import User, UserProfile
from evaluations.models import Evaluation


class UserProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UserProfile
        fields = ('anonymity', 'gender', 'photo')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    profile = UserProfileSerializer(required=True)
    evaluations = serializers.PrimaryKeyRelatedField(many=True, queryset=Evaluation.objects.all())

    class Meta:
        model = User
        fields = ('id', 'url', 'email', 'first_name', 'last_name', 'password', 'profile', 'evaluations')
        extra_kwargs = {'password': {'write_only': True}, 'url': {'view_name': 'accounts:user-detail'}}

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        UserProfile.objects.create(user=user, **profile_data)
        return user

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile')
        profile = instance.profile

        instance.email = validated_data.get('email', instance.email)
        instance.save()

        profile.anonymity = profile_data.get('anonymity', profile.anonymity)
        profile.photo = profile_data.get('photo', profile.photo)
        profile.save()

        return instance
__author__ = 'andrey'

from django.contrib.auth import update_session_auth_hash

from rest_framework import serializers

from models import UserProfile

class StartupSerializer(serializers.HyperlinkedModelSerializer):
    founder = serializers.HyperlinkedIdentityField(view_name='userprofile-detail')

    class Meta:
        model = UserProfile
        fields = ('url', 'id', 'name', 'founder', 'logo', 'updated_at', 'created_at')
        read_only_fields = ('created_at', 'updated_at',)

    def create(self, validated_data):
        return UserProfile.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.headline = validated_data.get('headline', instance.tagline)

        instance.save()

        password = validated_data.get('password', None)
        confirm_password = validated_data.get('confirm_password', None)

        if password and confirm_password and password == confirm_password:
            instance.set_password(password)
            instance.save()

            update_session_auth_hash(self.context.get('request'), instance)

        return instance

    def validate(self, data):
        if data['name']
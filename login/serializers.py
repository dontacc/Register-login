from rest_framework import serializers

from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password






class RegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True, validators=[UniqueValidator(queryset=User.objects.all(), 
                                                                 message="username already exists!")])

    email = serializers.EmailField(required = False, validators = [UniqueValidator(queryset=User.objects.all())])
    
    password = serializers.CharField(required = True, write_only = True, validators = [validate_password])
    
    password1 = serializers.CharField(required = True, write_only = True)
    
    first_name = serializers.CharField(required = True, write_only = True)

    last_name = serializers.CharField(required = True, write_only = True)


    class Meta:
        model = User
        fields = ["username", "password", "password1", "email", "first_name", "last_name"]
        


    
    def validate(self, obj):
        print(obj)
        if obj['password'] != obj['password1']:
            raise serializers.ValidationError({"password_error": "password fields should be same!"})
        
        elif obj['first_name'] == obj['username']:
            raise serializers.ValidationError({"error": "username and first_name must be different"})
            

        return obj


    def create(self, validated_data):
        print(validated_data)

        if 'email' in validated_data:
            user = User.objects.create(
                username = validated_data['username'],
                email = validated_data['email'],
                first_name = validated_data['first_name'],
                last_name = validated_data['last_name']
            )

        else:
            user = User.objects.create(username = validated_data['username'])

        # user = User.objects.create_user(
        #     validated_data['username'],
        #     email=validated_data['email']
        # )


        user.set_password(validated_data['password'])
        user.save()

        return user
    


class LoginSerializer(serializers.ModelSerializer):

    username = serializers.CharField(max_length = 32)


    class Meta:
        model = User
        fields = ('username', 'password')




class UserProfile(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name']


class UserPasswordChange(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name']

















    

    




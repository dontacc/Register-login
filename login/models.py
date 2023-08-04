# from django.db import models
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, UserManager





# class UserProfileManager(BaseUserManager):


#     def create_user(self, username, email, password=None):
#         if not username:
#             raise ValueError('Users must have a username')
        
#         email = self.normalize_email(email)
#         user = self.model(username=username, email=email)

#         user.set_password(password)
#         # user.save(using=)

#         return user
    


# class UserProfile(AbstractBaseUser):
#     username = models.CharField(max_length=20, unique=True) 
#     avatar = models.URLField(blank=True, null=True)
#     is_active = models.BooleanField(default=False)


#     objects = UserProfileManager()


#     REQUIRED_FIELDS = ['username']

#     def __str__(self):
#         return self.username
    




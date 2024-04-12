from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):

    def create_user(self,usename,password=None,**extra_fields):
        if not usename:
            raise ValueError("Phone number is required !!!!")
        user = self.model(usename=usename,**extra_fields)
        user.set_password(password)
        user.save(using = self.db)
        return user

    def create_superuser(self,usename,password=None,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)

        return self.create_user(usename,password,**extra_fields)
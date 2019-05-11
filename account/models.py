from cuser.models import AbstractCUser, CUserManager
from django.db import models


class UserMngr(CUserManager):
    pass

class User(AbstractCUser):
    objects = UserMngr()

    class Meta(AbstractCUser.Meta):
        swappable = 'AUTH_USER_MODEL'


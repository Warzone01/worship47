from cuser.models import AbstractCUser
from django.db import models


class User(AbstractCUser):

    class Meta(AbstractCUser.Meta):
        swappable = 'AUTH_USER_MODEL'


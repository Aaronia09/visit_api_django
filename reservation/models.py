import uuid
from django.db import models

from pack.models import pack
from user.models import user


class reservation(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    pack = models.ForeignKey(pack, on_delete=models.CASCADE, db_column='pack_id')
    is_reserved = models.BooleanField(default=False)
    user= models.ForeignKey(user, on_delete=models.CASCADE, db_column='user_id')
    participant_number = models.IntegerField(default=0)
    status = models.IntegerField(default=0)

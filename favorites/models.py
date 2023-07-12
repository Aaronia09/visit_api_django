import uuid
from django.db import models
from user.models import user
from pack.models import pack

class favorites(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    users = models.ForeignKey(user, on_delete=models.CASCADE, db_column='user_id')
    packs = models.ForeignKey(pack, on_delete=models.CASCADE, db_column='pack_id')
    is_favorited = models.BooleanField(default=False)
    participant_number = models.IntegerField(default=0)
    status = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

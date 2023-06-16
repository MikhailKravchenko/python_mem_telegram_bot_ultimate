from django.db import models


class RatioLike(models.Model):
    ratio_like_id = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=100)
    ratio_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False, null=True)
    updated_at = models.DateTimeField(auto_now=True, editable=False, null=True)

    def save(self, **kwargs) -> None:
        super(RatioLike, self).save()

    class Meta:
        db_table = "ratio_like"

    def __str__(self) -> str:
        return f"{self.ratio_like_id}"


class RatioDislike(models.Model):
    ratio_dislike_id = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=100)
    ratio_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False, null=True)
    updated_at = models.DateTimeField(auto_now=True, editable=False, null=True)

    def save(self, **kwargs) -> None:
        super(RatioDislike, self).save()

    class Meta:
        db_table = "ratio_dislike"

    def __str__(self) -> str:
        return f"{self.ratio_dislike_id}"


class Ratio(models.Model):
    ratio_id = models.AutoField(primary_key=True)
    ratio_value = models.IntegerField(null=True, default=0)
    photo_id = models.TextField(null=True)
    user_id = models.TextField(null=True)
    create_time = models.DateTimeField(null=True, default="NULL")
    message_id = models.IntegerField(null=True)
    ratio_dislike_value = models.IntegerField(null=True, default=0)
    data_id = models.IntegerField(default=0)
    chat_id = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False, null=True)
    updated_at = models.DateTimeField(auto_now=True, editable=False, null=True)

    def save(self, **kwargs) -> None:
        super(Ratio, self).save()

    class Meta:
        db_table = "ratio"

    def __str__(self) -> str:
        return f"{self.ratio_id}"


class HashImage(models.Model):
    hash_images = models.TextField(null=True)
    file_id = models.TextField(null=True)
    chat_id = models.TextField(null=True)

    def save(self, **kwargs) -> None:
        super(HashImage, self).save()

    class Meta:
        db_table = "hash_image"

    def __str__(self) -> str:
        return f"{self.id}"

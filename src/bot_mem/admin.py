from django.contrib import admin

from src.bot_mem.models import Ratio, RatioLike, RatioDislike, HashImage


class RatioAdmin(admin.ModelAdmin):
    list_display = [
        "ratio_id",
        "ratio_value",
        "photo_id",
        "user_id",
        "create_time",
        "message_id",
        "ratio_dislike_value",
        "data_id",
        "chat_id",
        "created_at",
        "updated_at",
    ]
    search_fields = [
        "ratio_id",
        "ratio_value",
        "photo_id",
        "user_id",
        "create_time",
        "message_id",
        "ratio_dislike_value",
        "data_id",
        "chat_id",
        "created_at",
        "updated_at",
    ]
    list_per_page = 25

class RatioLikeAdmin(admin.ModelAdmin):
    list_display = [
        "ratio_like_id",
        "user_id",
        "ratio_id",
        "created_at",
        "updated_at",
    ]
    search_fields = [
        "ratio_like_id",
        "user_id",
        "ratio_id",
        "created_at",
        "updated_at",
    ]
    list_per_page = 25

class RatioDislikeAdmin(admin.ModelAdmin):
    list_display = [
        "ratio_dislike_id",
        "user_id",
        "ratio_id",
        "created_at",
        "updated_at",
    ]
    search_fields = [
        "ratio_dislike_id",
        "user_id",
        "ratio_id",
        "created_at",
        "updated_at",
    ]
    list_per_page = 25

class HashImageAdmin(admin.ModelAdmin):
    list_display = [
        "hash_images",
        "file_id",
        "chat_id",
    ]
    search_fields = [
        "hash_images",
        "file_id",
        "chat_id",
    ]
    list_per_page = 25


admin.site.register(Ratio, RatioAdmin)
admin.site.register(RatioLike, RatioLikeAdmin)
admin.site.register(RatioDislike, RatioDislikeAdmin)
admin.site.register(HashImage, HashImageAdmin)

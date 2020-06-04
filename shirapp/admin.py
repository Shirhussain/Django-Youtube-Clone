from django.contrib import admin
from .models import (Video, Comment, Channel, Wish, Report,
                    Review, Thumb, Category, Tag, Share, BackgroundImg
                    )

admin.site.register(Video)
admin.site.register(Comment)
admin.site.register(Channel)
admin.site.register(Category)
admin.site.register(BackgroundImg)

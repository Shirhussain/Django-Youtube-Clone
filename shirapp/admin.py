from django.contrib import admin
from .models import (Video, Comment, Wish, Report,
                    Review, Thumb, Category, Tag, Share, BackgroundImg
                    )

admin.site.register(Video)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(BackgroundImg)

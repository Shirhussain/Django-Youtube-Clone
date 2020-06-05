from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class VideoView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.ForeignKey('Video', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    video = models.ForeignKey(
        'Video', related_name="comments", on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Video(models.Model):
    title = models.CharField(max_length=50)
    # channel = models.ForeignKey('Channel', on_delete=models.CASCADE)
    discription = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField("thumbnail")
    path = models.FileField(upload_to="vidpath")
    category = models.ForeignKey(
        'Category', on_delete=models.DO_NOTHING)
    # path      = models.CharField(max_length=100)
    # save
    # video_duration
    # thumb	   = models.ForeignKey('Thumb',null=True, blank=True, on_delete=models.SET_NULL)
    # share      = models.ForeignKey('Share',null=True, blank=True)
    # wish_list  = models.ForeignKey('Wish',null=True, blank=True)
    # review     = models.ForeignKey('Review',null=True, blank=True)
    # report     = models.ForeignKey('Report',null=True, blnak=True)
    # category     = models.ForeignKey('Category',null=True, blnak=True)
    # tag     = models.ForeignKey('Tag',null=True, blnak=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('video', kwargs={
            'pk': self.pk
        })
        

    @property
    def view_count(self):
        return VideoView.objects.filter(video=self).count()

    @property
    def get_comments(self):
        return self.comments.all().order_by('-timestamp')

    @property
    def comment_count(self):
        return Comment.objects.filter(video=self).count()


class BackgroundImg(models.Model):
    image = models.ImageField(upload_to="backgroundImg")
    caption = models.CharField(max_length=30)

    def __str__(self):
        return self.caption


class Thumb(models.Model):
    like = models.BooleanField(default=False)
    like_count = models.PositiveIntegerField(default=0)
    dislike = models.BooleanField(default=False)
    dislike_count = models.PositiveIntegerField(default=0)


class Category(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title


# class Channel(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     profile_picture = models.ImageField(upload_to="profile")
#     subscribe = models.BooleanField(default=False)

#     def __str__(self):
#         return self.user.username

#     def get_absolute_url(self):
#         return reverse('channel', kwargs={
#             'pk': self.pk
#         })


class Wish(models.Model):
    pass


class Review(models.Model):
    pass


class Report(models.Model):
    pass


class Tag(models.Model):
    pass


class Share(models.Model):
    pass

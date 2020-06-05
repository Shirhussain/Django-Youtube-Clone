from django.shortcuts import render, redirect, reverse
from django.views.generic.base import View, HttpResponseRedirect, HttpResponse
from django.views.generic import ListView, DetailView
from .models import Video, Comment, Category, BackgroundImg, VideoView
from user.models import Channel
from . forms import CommentForm


def get_channels():
    queryset = Channel.objects.all()
    return queryset


class IndexView(View):
    template_name = "index.html"

    def get(self, request):
        vid = Video.objects.all()
        politic = Video.objects.filter(category__title__iexact="Politic")
        Entertainment = Video.objects.filter(
            category__title__iexact="Entertainment")
        Education = Video.objects.filter(category__title__iexact="Education")
        Sport = Video.objects.filter(category__title__iexact="Sport")
        Funny = Video.objects.filter(category__title__iexact="Gamming")
        most_recent = Video.objects.order_by('-timestamp')[0:7]

        background = BackgroundImg.objects.all()
        channels = Channel.objects.all()

        video_catList = [most_recent, vid, politic,
                         Entertainment, Education, Sport, Funny]
        context = {
            'video_catList': video_catList,
            'background': background,
            'channels': channels
            # "video": vid,
            # 'most_recent':most_recent
            # wish list
        }
        return render(request, self.template_name, context)


class TrendingListView(ListView):
    model = Video
    template_name = 'trending.html'
    context_object_name = 'video'
    paginate_by = 20

    def get_context_data(self, **kwargs):
        channels = get_channels()
        context = super().get_context_data(**kwargs)
        context['channels'] = channels
        context['page_request_var'] = "page"
        return context


class VideoDetailView(DetailView):
    model = Video
    template_name = 'video.html'
    context_object_name = 'video'
    form = CommentForm()

    def get_object(self):
        obj = super().get_object()
        if self.request.user.is_authenticated:
            VideoView.objects.get_or_create(
                user=self.request.user,
                video=obj
            )
        return obj

    def get_context_data(self, **kwargs):
        channels = get_channels()
        most_recent = Video.objects.order_by('-timestamp')[:15]
        context = super().get_context_data(**kwargs)
        context['most_recent'] = most_recent
        context['channels'] = channels
        context['form'] = self.form
        return context

    # def post(self, request, *args, **kwargs):
    #     form = CommentForm(request.POST)
    #     if form.is_valid():
    #         video = self.get_object()
    #         form.instance.user = request.user
    #         form.instance.video = video
    #         form.save()
    #         return redirect(reverse("video", kwargs={'pk': video.pk}))

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            video = self.get_object()
            form.instance.user = request.user
            form.instance.video = video
            form.save()
            return redirect(reverse("video", kwargs={
                'pk': video.pk
            }))


def channels(request):
    return render(request, "chanenl_list.html", {})


def channel(request, pk):
    return render(request, "channel.html", {})


def category(request):
    return render(request, "category.html", {})


def login(request):
    return render(request, "login.html", {})


def register(request):
    return render(request, "register.html", {})


def reset(request):
    return render(request, "reset.html", {})


def search(request):
    return render(request, "search.html", {})


def history(request):
    return render(request, "history.html", {})


def settings(request):
    return render(request, "settings.html", {})


def wishlist(request):
    return render(request, "wishlist.html", {})


def myChannels(request):
    return render(request, "mychannels.html", {})


def playLists(request):
    return render(request, "playlists.html", {})

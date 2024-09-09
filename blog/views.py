from django.shortcuts import render
from django.utils import timezone
from blog.models import Post
import logging

logger = logging.getLogger(__name__)
# Create your views here.
def index(request):
  logger.info(request)
  posts = Post.objects.filter(published_at__lte=timezone.now())

  logger.debug("Got %d posts", qs.count())
  return render(request, 'blog/index.html', {"posts": posts})
from django.shortcuts import render
from blog.models import Post
import logging

logger = logging.getLogger(__name__)
# Create your views here.
def index(request):
  logger.info(request)
  qs = Post.objects.all()

  logger.debug("Got %d posts", qs.count())
  return render(request, 'blog/index.html')
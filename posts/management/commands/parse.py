import requests
import logging
from django.core.management import BaseCommand
from bs4 import BeautifulSoup

from posts.models import Post


# from .exceptions import ParseError

class Command(BaseCommand):
    help = 'Send report'

    def handle(self, *args, **options):

        try:
            r = requests.get('https://news.ycombinator.com/')
        except requests.RequestException as e:
            logging.error('Error connection https://news.ycombinator.com/')
            return False

        soup = BeautifulSoup(r.content,  features="html.parser")
        list_news = soup.find_all('a', {'class': 'storylink'})
        for item in list_news:
            url = item.get('href')
            title = item.text
            if not url or not title:
                continue
            Post.objects.get_or_create(
                url=url, 
                title=title
            )
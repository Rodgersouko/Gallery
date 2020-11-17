from django.test import SimpleTestCase
from django.urls import reverse, resolve
from gallery.views import display


class TestUrls(SimpleTestCase):

    def test_list_url(self):
        url = reverse('dis')
        print (resolve(url))
from rest_framework.test import APITestCase, force_authenticate, APIRequestFactory
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User

from blog.models import Category, Post
from .views import PostListCreate


class PostTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='omar', password='12345678')
        self.cate = Category.objects.create(name='firs category')
        self.data = {
            "author":1,
            "category":1,
            "title":"New Title",
            "excerpt":"a",
            "content":"a",
            "slug":"new_title",
            "status":Post.STATUS_CHOICES.PUBLIC
        }
        self.factory = APIRequestFactory()
        self.post = Post.objects.create(
            author=self.user,
            category=self.cate,
            title='New Title',
            excerpt= 'a',
            content='a',
            slug='new_title',
            status=Post.STATUS_CHOICES.PUBLIC,
        ) 

    # List and Create Url
    def test_view_posts(self):
        url = reverse("blog_api:listcreate")

        """
            client --> the reference to simulating a client
        """
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # force_authenticate take request
        # request = self.factory.get(url)
        # force_authenticate(request, user=self.user)
        # response = PostListCreate.as_view()(request)
        # self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_post(self):
        url = reverse("blog_api:listcreate")
        response = self.client.post(url, self.data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    # Details and Delete Url
    def test_details_post(self):
        url = reverse("blog_api:detailsdelete", kwargs={"pk":self.post.id})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_post(self):
        url = reverse("blog_api:detailsdelete", kwargs={"pk":self.post.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

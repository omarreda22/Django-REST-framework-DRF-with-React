from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post, Category
from django.utils import timezone

class TestCreatePost(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='omar', password='12345678')
        self.cate = Category.objects.create(name='firs category')
        self.post = Post.objects.create(
            author=self.user,
            category=self.cate,
            title='New Title',
            excerpt= 'a',
            content='a',
            slug='new_title',
            status=Post.STATUS_CHOICES.PUBLIC,
        ) 

    def test_create_post(self):
        post = Post.objects.get(id=1)
        now = timezone.now()
        self.assertEqual(post.author.username, 'omar')
        self.assertEqual(post.title, 'New Title')
        self.assertEqual(post.content, 'a')
        self.assertLessEqual(post.published, now)
        self.assertNotEqual(post.status, Post.STATUS_CHOICES.DRAFT)
        self.assertEqual(str(post), 'New Title')

    def test_category_name(self):
        cate = Category.objects.get(id=1)
        self.assertEqual(str(cate), 'firs category')
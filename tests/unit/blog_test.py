from unittest import TestCase
from blog import Blog

class BlogTest(TestCase):
    def test_create_blog(self):
        b = Blog('Test', 'Stephen King')

        self.assertEqual('Test', b.title)
        self.assertEqual('Stephen King', b.author)
        self.assertListEqual([], b.posts)

    def test_repr(self):
        b = Blog('Joy land', 'Stephen King')
        b2 = Blog('Day One', 'Ravi Diz')

        self.assertEqual(b.__repr__(), 'Joy land by Stephen King (0 posts)')
        self.assertEqual(b2.__repr__(), 'Day One by Ravi Diz (0 posts)')

    def test_repr_multiple_posts(self):
        b = Blog('Hereditary', 'Ari Aster')
        b.posts = ['test']

        b2 = Blog('Day One', 'Ravi Diz')
        b2.posts = ['test', 'another']

        self.assertEqual(b.__repr__(), 'Hereditary by Ari Aster (1 post)')
        self.assertEqual(b2.__repr__(), 'Day One by Ravi Diz (2 posts)')

    def test_create_post_in_blog(self):
        b = Blog('Hereditary', 'Ari Aster')
        b.create_post('Test Post', 'Test Content')

        self.assertEqual(len(b.posts), 1)
        self.assertEqual(b.posts[0].title, 'Test Post')
        self.assertEqual(b.posts[0].content, 'Test Content')
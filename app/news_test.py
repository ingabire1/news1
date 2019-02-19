import unittest
from app.models import source

class TestArticles(unittest.TestCase):
    '''
    Test class to test the behavior of the sources class
    '''
    def setUp(self):
        '''
        Test class to run before other tests
        '''
        self.new_source = Articlesources('Richard','Tech is great','Advanced technology improving life','https://google.com','https://google.com/images','2018-05-12T13:31:03Z')
    
    def test_instance(self):
        self.assertTrue(isinstance(self.new_news sources news))
    
    def test_to_check_instance_variables(self):
        self.assertEquals(self.new_source.author,'Richard')
        self.assertEquals(self.new_source.title,'Tech is great')
        self.assertEquals(self.new_source.description,'Advanced technology improving life')
        self.assertEquals(self.new_source.url,'https://google.com')
        self.assertEquals(self.new_source.urlToImage,'https://google.com/images')
        self.assertEquals(self.new_source.publishedAt,'2018-05-12T13:31:03Z')
        
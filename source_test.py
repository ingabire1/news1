
import unittest
from app.models import source
Source=source.Source

class SourceTest(unittest.TestCase):
  '''
  Test class to test the behaviour of the source class
  '''

  def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Source(1234,"AKA","Description here","https://kk.com","kk")

  def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source))  

  def test_init_(self):
      '''
      Test to see if source instance are being created
      '''
      self.assertEqual(self.new_source.id,1234)
      self.assertEqual(self.new_source.name,"AKA")
      self.assertEqual(self.new_source.description,"Description here")
      self.assertEqual(self.new_source.url,"https://kk.com")
      self.assertEqual(self.new_source.category,"kk")

if __name__ == '__main__':
    unittest.main()            
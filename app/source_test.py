import unittest
from source import News_source
News_source = news.News_source

class NewsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the News class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_news = News(10/10/2018, 'This is Todays News', 'Today Raila will be sworn in.', 'https://image.newsapi.org/3/movie/{}?api_key={}')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news, News))

if __name__ == '__main__':
    unittest.main()

class Config:
    '''
    General configuration parent class
    '''
    MOVIE_API_BASE_URL ='https://api.newsapi.org./3/news/{}?api_key={}'

class ProdConfig(Config):
    '''
    production configuration child class

    Args:
        Config:The parent configuration class with General configuration settings
    '''
    pass

class DevConfig(Config):
    '''
    Development configuration child class

    Args:
        Config:The parent configuration class with General configuration setting
    '''

    DEBUG = True

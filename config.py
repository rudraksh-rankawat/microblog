import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'this_is_the_secret_key'
    SAMPLE_KEY = os.environ.get('SAMPLE_KEY') or 'smaplekeyyyyy'
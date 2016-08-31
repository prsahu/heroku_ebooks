'''
Local Settings for a heroku_ebooks account. #fill in the name of the account you're tweeting from here.
'''

#configuration
MY_CONSUMER_KEY = 'j7af4rR1ccCZIl68l26t5Xbyr'
MY_CONSUMER_SECRET = 'z3HIiAR8SVZmoWQg2Q3kzuSTjEokjjbCux2GwxxQIQYiyMbwWZ'
MY_ACCESS_TOKEN_KEY = '19057487-D1gAENz0k8arrspFi4b3IbkMUdHTpQrohEsCrRZAe'
MY_ACCESS_TOKEN_SECRET = 'ZEZTUFmPdwExUPwvWII8hYqpuDTpIAEFrfvwng4KIZVWA'

SOURCE_ACCOUNTS = ["scifri"] #A list of comma-separated, quote-enclosed Twitter handles of account that you'll generate tweets based on. It should look like ["account1", "account2"]. If you want just one account, no comma needed.
ODDS = 1 #How often do you want this to run? 1/8 times?
ORDER = 3 #how closely do you want this to hew to sensical? 1 is low and 3 is high.
DEBUG = True #Set this to False to start Tweeting live
STATIC_TEST = False #Set this to True if you want to test Markov generation from a static file instead of the API.
TEST_SOURCE = ".txt" #The name of a text file of a string-ified list for testing. To avoid unnecessarily hitting Twitter API.
TWEET_ACCOUNT = "startup_pearls" #The name of the account you're tweeting to.

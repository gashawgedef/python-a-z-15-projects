import tweepy
import requests.exceptions
import logging
# consumer_key = "6FV0Ubt0UQNvijHI5GbvRK23c"
# consumer_secret = "1P95lIFNSt0UWNen2cgUCGZ3qdgRP2UExvPb3t08FlhxJdkqXD"
# key = "1306149538084917253-ZnZWjLrVj5Et58RIsAPfuARajKRH1A"
# secret = "nPMk1suYyJIE0OjmyQZYXinPQrSgaIbR7HeiYflXuDpVZ"
# Enable logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


# Your credentials
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""
auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# Verify authentication
try:
    api.verify_credentials()
    logger.info("Authentication OK")
except tweepy.TweepyException as e:
    logger.error(f"Error during authentication: {e}")

# Function to post a tweet
def post_tweet():
    try:
        api.update_status("Hello from twitter bot - First tweet!")
        logger.info("Tweet posted successfully")
    except tweepy.TweepyException as e:
        logger.error(f"Error while posting tweet: {e}")
    except requests.exceptions.RequestException as e:
        logger.error(f"Connection error: {e}")

# Call the function to post a tweet
post_tweet()
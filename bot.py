import tweepy
import openai
import os
from dotenv import load_dotenv

def get_sentence_from_gpt():

    openai.api_key = os.environ.get("OPENAI_API_KEY")

    response = openai.Completion.create(
      model="text-davinci-003",
      prompt='NEXA adlı bir blockchain projesi var ve sen bu projeyi ingilizce şekilde shilling yapan içerisinde $NEXA içeren tweetler atıyorsun: "', #Prompt for OpenAI like; "There is a blockchain project called NEXA and you are posting tweets containing $NEXA shilling this project:"
      max_tokens=225,
      temperature=0.7,
      top_p=1,
      frequency_penalty=1.2,
      presence_penalty=1.2,
      n=1,
      best_of=2,
      stream=False,
      stop=['"', '”']
    )

    sentence = response.choices[0].text
    print(sentence)
    return sentence

def send_tweet(text):
    consumer_key = os.environ.get("TWITTER_API_CONSUMER_KEY")
    consumer_secret = os.environ.get("TWITTER_API_CONSUMER_SECRET")
    bearerToken = os.environ.get("TWITTER_API_BEARER_TOKEN")
    access_token = os.environ.get("TWITTER_API_ACCESS_TOKEN")
    access_secret = os.environ.get("TWITTER_API_ACCESS_TOKEN_SECRET")

    client = tweepy.Client(
        bearer_token=bearerToken,
        access_token=access_token,
        access_token_secret=access_secret,
        consumer_key=consumer_key,
        consumer_secret=consumer_secret
    )

    res = client.create_tweet(text=text)
    print(res)

def main():
    project_folder = os.path.expanduser('C:/Users/Administrator/Desktop/nexatweetbot')  #.env file location
    load_dotenv(os.path.join(project_folder, '.env'))

    sentence = get_sentence_from_gpt()
    send_tweet(sentence)

if __name__ == "__main__":
    main()

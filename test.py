from datetime import timedelta,datetime

# import pandas as pd
import tweepy

from settings import API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
 
# def twitter_api() -> tweepy.API:
def twitter_api() -> tweepy.API:    
    auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    return tweepy.API(auth)

def search(api,s):
    for i in range(5):
        count = 0
        #今日から遡って５日前までカウント
        the_today = datetime.today()
        the_beforeday = the_today - timedelta(days=i)
        #sinceとuntil用に加工する
        str_t1 = the_beforeday.strftime('%Y-%m-%d')+'_00:00:00_JST'
        str_t2 = the_beforeday.strftime('%Y-%m-%d')+'_23:59:59_JST'

        for tweet in tweepy.Cursor(api.search,q=s,include_entities = True,tweet_mode='extended',since = str_t1,until = str_t2,lang = 'ja').items():
            print('='*80)
            # print('ツイートID : ', tweet.id)
            # print('ユーザ名 : ', tweet.user.screen_name)
            print('日時 : ', tweet.created_at)
            print(tweet.full_text)
            # print('いいね数 : ', tweet.favorite_count)
            # print('リツイート数 : ', tweet.retweet_count)
            print('='*80)        
            count+=1
        print(the_beforeday.strftime('%Y-%m-%d')+"のツイート数: "+str(count))

if __name__ == "__main__":
    api=twitter_api()
    s="オンライン選挙 exclude:retweets"
    search(api,s)

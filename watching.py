import twitter
import os.path
import time

consumer_key        = "vMTqxHCOi7ab3hdF5RnIckJdK"
consumer_secret     = "eJTsl3t1eHOJ6ZkOBqFnbAkXpuMWVcFXoibAtIqI8UtFo6r962"
access_token        = "1080263263-6cp7aZskQgn2rcm063x4uugNjVXjtWlEq6Hykjn"
access_token_secret = "UdG0HirPxqBhQMdUVhya0cWpIg175smnbwn1Oo1uf0mOQ"

# 프로그램 최초 실행시
# Twitter Api Connecting
account = "@whtnwkd"
twitter_api = twitter.Api(consumer_key=consumer_key,
                          consumer_secret=consumer_secret, 
                          access_token_key=access_token, 
                          access_token_secret=access_token_secret)

# 최신 트윗 유지 파일 생성
latest_text_file_path = './latest.txt'
latest_tweet = ''
if not (os.path.isfile(latest_text_file_path)):
    f = open(latest_text_file_path, 'w', encoding = 'utf-8')
    f.write("test")
    f.close
    statuses = twitter_api.GetUserTimeline(screen_name=account, count=5, include_rts=False, exclude_replies=False)
    latest_tweet = statuses[0].text
else:
    f = open(latest_text_file_path, 'r')
    latest_tweet = f.readline()
    f.close

print("[Notice] The latest tweet is " + latest_tweet)
    
# 트윗 감지 시작
while(True):
    # 트위터 내 최신 트윗 가져오기
    statuses = twitter_api.GetUserTimeline(screen_name=account, count=5, include_rts=False, exclude_replies=False)
    new_tweet = statuses[0].text

    if latest_tweet != new_tweet:
        # 트윗 업데이트가 있을 경우
        print("[Notice] The tweet is diffrent.")

        # 파일의 내용을 최신으로 변경
        f = open(latest_text_file_path, 'w')
        f.write(new_tweet)
        f.close
        print("[Notice] \"" + latest_tweet + "\" to \"" + new_tweet + "\"")
        latest_tweet = new_tweet
    else:
        print("[Notice] Nothing is changed.")

    time.sleep(10)

    


    










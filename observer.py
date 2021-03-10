import twitter
import os.path
import time

consumer_key        = ""
consumer_secret     = ""
access_token        = ""
access_token_secret = ""

# 프로그램 최초 실행시
# Twitter Api Connecting
account = "@"
twitter_api = twitter.Api(consumer_key=consumer_key,
                          consumer_secret=consumer_secret, 
                          access_token_key=access_token, 
                          access_token_secret=access_token_secret)

# 최신 트윗 유지 파일 생성
latest_text_file_path = './latest.txt'
latest_tweet = ''
if os.path.isfile(latest_text_file_path):
    with open(latest_text_file_path, 'r', encoding = 'utf-8') as f:
        latest_tweet = f.readline()

if latest_tweet == '':
    statuses = twitter_api.GetUserTimeline(screen_name=account, count=5, include_rts=False, exclude_replies=False)
    latest_tweet = statuses[0].text

print("[Notice] The latest tweet is " + latest_tweet)
    
# 트윗 감지 시작
while(True):
    # 트위터 내 최신 트윗 가져오기
    time.sleep(10)
    statuses = twitter_api.GetUserTimeline(screen_name=account, count=5, include_rts=False, exclude_replies=False)
    new_tweet = statuses[0].text

    # 트윗 업데이트가 있을 경우
    if latest_tweet != new_tweet:
        print("[Notice] The tweet is diffrent.")

        with open(latest_text_file_path, 'w') as f:
            f.write(new_tweet)
        
        latest_tweet = new_tweet
        print("[Notice] \"" + latest_tweet + "\" to \"" + new_tweet + "\"")
    else:
        print("[Notice] Nothing is changed.")


    










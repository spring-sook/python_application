# 스케쥴링이란? 특정 시간에 작업을 예약하고 실행하는 프로세스
import schedule  # 스케쥴
import time  # 시간
import requests  # http 요청
from bs4 import BeautifulSoup  # 파싱

def perform_web_crawling():
    response = requests.get("http://www.naver.com")
    soup = ""
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
    print(soup)

def job():
    print("스케쥴링을 수행 합니다.")
    perform_web_crawling()

# 매일 정해진 시간에 동작하도록 구현
schedule.every().day.at("09:43").do(job)
# # 5초에 한번씩 함수 실행
# schedule.every(5).seconds.do(job)
# # 10분에 한번씩 함수 실행
# schedule.every(10).minutes.do(job)
# # 2시간에 한번씩 함수 실행
# schedule.every(2).hour.do(job)
# # 3일에 한번씩 함수 실행
# schedule.every(3).days.do(job)
# # 2주에 한번씩 함수 실행
# schedule.every(2).weeks.do(job)


while True:
    schedule.run_pending() ## 대기중인 작업을 수행하는 함수
    time.sleep(1)  ## 1초마다 반복수행

# count = 0
# while True:
#     schedule.run_pending()
#     time.sleep(1)
#     count = count + 1
#     if count > 5:
#         schedule.cancel_job(job1) # 스케쥴 되어 있는 작업을 취소하는 함수
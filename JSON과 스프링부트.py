import requests  ## http 통신을 위한 모듈
import json

member = {
    "email" : "jisuk@gmail.com",
    "pwd" : "asdf1234",
    "name" : "박지숙"
}

# 서버 URL 및 헤더 설정
url = "http://localhost:8111/auth/signup"
headers = {"Content-Type" : "application/json"}

# POST 요청 보내기
response = requests.post(url, data=json.dumps(member), headers=headers)
# 응답 처리
if response.status_code == 200:
    # 서버에서 전달받은 JSON을 객체로 변환하고 내용을 출력
    print("회원가입 성공!")
    print(response.json())
    print(response.json()["email"])
else:
    print("회원가입 실패..ㅠㅠ")
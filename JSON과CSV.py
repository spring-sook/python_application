import json

# [] : 리스트 - 시퀀스형 데이터를 관리, mutable(읽기, 쓰기), 데이터 타입이 아무거나 와도 됨
# {} : 딕셔너리 - 키와 값의 쌍으로 구성돼 있음
# () : 튜플 - 시퀀스형 데이터, immutable(읽기만 가능), Packing/Unpacking 가능
## Packing / Unpacking 예시
person = 10, "M", "경기도 수원시", "곰돌이", True  ## 이게 packing
print(person)
#age, gender, addr, name, adult = person ## 이게 unpacking
age, gender, *info, isadult = person ## 이것도 unpacking
print(age, gender,info, isadult)
customer = {
    "id" : 100,
    "name" : "곰돌이 사육사",
    "history": [
        {"date" : "2023-05-05", "Product" : "iPhone 14 Pro"},
        {"date" : "2024-04-01", "Product" : "iPhone 16 Pro"}
    ]
}

# Python 객체 -> JSON 문자열로 변환 (직렬화)
# json.dumps : 객체를 json 문자열로 변환
# ensure_ascii=False : ASCII 문자가 아님을 의미 - 한글은 비아스키문자
# indent=4 : 들여쓰기
jsonString = json.dumps(customer, ensure_ascii=False, indent=4)
print(jsonString)
print()

# 역직렬화
dict = json.loads(jsonString)
print(dict["name"])
for e in dict["history"]:
    print(e["date"], ":", e["Product"])
print()
# 파이썬의 for문 : range() 기반과, 시퀀스형 데이터를 순회하는 for문이 있음
print("< 범위 기반의 for문 >")
for i in range(10):  ## range(시작인덱스, 종료인덱스, 증감값)
    print(i, end=" ")
print()

print("< 시퀀스형 데이터 순회 >")
cars = ["모델 Y", "X4", "폴스타4", "EV3", "마칸", "카이엔", "팬텀", "에어로시티"]
for e in cars:
    print(e, end=" / ")
print()

# 범위 기반 for로 cars 출력하기
for i in cars[:3]:
    print(i)
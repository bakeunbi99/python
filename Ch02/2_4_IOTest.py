"""
날짜 : 2021/08/09 16:02
이름 : 박은비
내용 : 파이썬 표준 입출력 실습하기 교재 p43
"""

# 파이썬 표준 입력장치
num = input('숫자 입력 : ')


# 파이썬 표준 출력장치
print('num : ', num)
print('num type: ', type(num))


# 문자열을 숫자로 변환(캐스팅)
num = int(num)
num += 1
print('num : ', num)
print('num type: ', type(num))


# 출력 옵션
print('Hello', end='~ ')
print('Busan')

print('010', '1234', '5678', sep='-')

# 서식 문자 출력
print('%d년 %d월 %d일 %s요일' % (2021, 8, 9, '월'))

# 포맷 문자 출력
print('이름:{}\n나이:{}\n주소:{}'.format('홍길동', 21, '부산광역시'))





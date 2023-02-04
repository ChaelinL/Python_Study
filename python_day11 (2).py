
# open(파일명[or 절대경로], mode)

# 절대경로 (시스템의 root 부터 시작하는 경로)
# 상대경로 (현재 위치부터의 경로)

# mode = (기본값은) r
# r = 읽기 (read) : 파일이 없으면 FileNotFoundError 발생시킴
# w = 쓰기 (write) : 파일이 없으면 파일을 생성합니다.
# a = 추가 (append) : 파일이 없으면 파일을 생성합니다.


with open('test.txt', 'w') as f:
    # with 블록 안에 있는 모든 코드가 실행이 종료됐을 때, 자동으로 with으로 열었던 resource를 반납 (close)
    f.read()
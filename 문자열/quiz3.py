# Quiz) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오

# 예) http://naver.com
# 규칙1: http:// 부분은 제외 => naver.com
# 규칙2: 처음 만나는 점(.) 이후 부분은 제외 => naver
# 규칙3: 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!"로 구성

# 예) 생성된 비밀번호: nav51!

# My code
sites = ["http://naver.com","http://google.com"]
site = sites[0][7:]

index = site.index(".")
site = site[0:index]
print(site)

password = site[0:3] + str(len(site)) + str(site.count("e")) + "!"

print("{site}의 비밀번호는 {password}입니다.".format(password=password,site=site))

# Other code
url = "http://google.com"
my_str = url.replace("http://","")  # 규칙1
my_str = my_str[:my_str.index(".")] # my_str[0:5] -> 0 ~ 5  직전까지
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("{url}의 비밀번호는 {password}입니다.".format(password=password,url=my_str))
# 1] 원본데이터 수집 & 저장
import requests

access_key = 'YOUR_API_KEY_HERE'

def get_request_url(page): #
    url = 'https://api.visitjeju.net/vsjApi/contents/searchList'
    params = {
        'apiKey': access_key,
        'locale' : 'kr',
        'category': 'c1', #관광지를 의미 {c1: 관광지, c2:쇼핑, c3:숙박, c4:음식점  c5:축제/행사, c6:테마여행, c7:정보})
        'page': page
    }
    response = requests.get(url, params=params)
    return response.text

# 전체 페이지 데이터 txt파일로 저장
pages = 14
with open('visit_jeju_c1_raw2.txt','w', encoding='utf8') as outfile:
    for page in range(1, pages+1):
        result = get_request_url(page)
        outfile.write(result + '\n')
        print(f"{page}페이지 저장완료")
    print("txt 파일 생성 완료.")
# @Time : 2020/12/19 13:53


import requests
from bs4 import BeautifulSoup

#定义请求的浏览器代理，伪装成浏览器
def get_movies():
    header = {
        "User-Agent":"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
        "Host":"movie.douban.com"
    }
    movie_list = []
    for i in range(0,10):
        link = 'https://movie.douban.com/top250?start=' + str(i*25)
        r = requests.get(link, headers=header, timeout=10)
        print(str(i+1), "页响应状态码",r.status_code)
        soup = BeautifulSoup(r.text,"lxml")
        div_list = soup.find_all('div', class_='hd')
        for each in div_list:
            movie = each.a.span.text.strip()
            movie_list.append(movie)
    return movie_list


movies = get_movies()
print(movies)







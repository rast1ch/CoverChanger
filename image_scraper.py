import bs4 as bs4
import requests


def connect(url):
    global result
    r = requests.get(url)
    if str(r.status_code) == '200':
        soup = bs4.BeautifulSoup(r.content, 'lxml')
        return soup
    else:
        print("Unknown Error")
        return 0


def scrap_to_file(soup):
    soup = soup.findAll('img')
    for url in soup:
        result_img = url['src']
        result_name = url['alt']
    result_name = result_name.replace(" ", "_")
    img = requests.get(result_img)
    img_file = open(result_name + '.jpg', 'wb')
    img_file.write(img.content)
    img_file.close
    return 1


if __name__ == '__main__':
    url = input("input url ==>  ")
    scrap_to_file(connect(url))

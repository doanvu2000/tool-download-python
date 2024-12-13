import time

import requests
from bs4 import BeautifulSoup


def get_html_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check if request was successful
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup.prettify()  # Return prettified HTML content
    except requests.exceptions.RequestException as e:
        return str(e)


def write_string_to_txt_file(text, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)
def get_content_chapter_and_save_to_file(url,file_name):
    html_content = get_html_content(url)

    soup = BeautifulSoup(html_content, 'html.parser')
    # div_content = soup.find_all('div', attrs={'data-x-bind': 'chapter-c'})
    div_content = div_by_id = soup.find('div', id='chapter-c')
    result = ""
    for div in div_content:
        result += div.text

    # file_name = "output.txt"
    print(f"Write {file_name}")
    write_string_to_txt_file(result.strip(), file_name)

if __name__ == "__main__":
    # url = "https://metruyencv.com/truyen/vu-luyen-dien-phong/chuong-"
    url = "https://truyenfull.io/dua-vao-khong-gian-mo-quan-an-ban-nong-san/"
    start_chapter = 1
    end_chapter = 3

    for chapter_index in range(start_chapter, end_chapter+1):
        chapter_name = f"data/test/chap_{chapter_index}.txt"
        full_url = f"{url}chuong-{chapter_index}/"
        get_content_chapter_and_save_to_file(full_url, chapter_name)
        time.sleep(0.45)
    # for chapter_index in range(start_chapter, end_chapter):
    #     # get content of chapter and save to txt file
    #     full_url = f"{url}{chapter_index}"
    #     chapter_name = f"data/vuluyendienphong/chap_{chapter_index}.txt"
    #     get_content_chapter_and_save_to_file(full_url,chapter_name)
    #     time.sleep(0.25)


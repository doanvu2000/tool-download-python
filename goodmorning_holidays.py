import json
import os
from concurrent.futures import ThreadPoolExecutor

import requests


def read_json(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    return data


def read_json_array(filename):
    with open(filename, 'r') as f:
        json_array = json.load(f)
    return json_array


class PostCard:
    def __init__(self, id, categoryId, categoryFullSlug, title, image):
        self.id = id
        self.categoryId = categoryId
        self.categoryFullSlug = categoryFullSlug
        self.title = title
        self.image = image

    def __repr__(self):
        return f"PostCard(id={self.id}, categoryId={self.categoryId},categoryFullSlug={self.categoryFullSlug},title={self.title},image={self.image})"


def download_image(url, save_path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            file.write(response.content)
            print(f"download ok: {save_path}")
    else:
        print(f"down load failed: {url}")


# Function to download multiple images with multithreading
def download_images(urls, names, save_dir):
    os.makedirs(save_dir, exist_ok=True)

    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = []
        for i, url in enumerate(urls):
            save_path = os.path.join(save_dir, names[i])
            futures.append(executor.submit(download_image, url, save_path))

        # Wait for all futures to complete
        for future in futures:
            future.result()

def get_all_files_in_folder(folder_path):
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    return files

if __name__ == "__main__":
    # holidays_json = get_all_files_in_folder("data/holidays")
    #
    # for i, fileName in enumerate(holidays_json):
    #     s = str(fileName)
    #     name = f"data/holidays/{s}"
    #     jsonArray = read_json(name)
    #     postCards = [PostCard(item["id"],item["categoryId"],item["categoryFullSlug"],item["title"],item["image"]) for item in jsonArray]
    #     urls = []
    #     names = []
    #     for post in postCards:
    #         urls.append(f"https://cdn.otkritkionline.ru/storage/posts/thumbs/{post.image}")
    #         if post.image.endswith('jpg'):
    #             names.append(f"img_{post.id}.jpg")
    #         else:
    #             names.append(f"img_{post.id}.gif")

    urls = []
    urls.append("https://cdn.otkritkionline.ru/storage/posts/thumbs/grandparents-day-31741.jpg")
    urls.append("https://cdn.otkritkionline.ru/storage/posts/thumbs/world-heart-day-32571.jpg")
    urls.append("https://cdn.otkritkionline.ru/storage/posts/thumbs/coffee-day-32358.jpg")
    urls.append("https://cdn.otkritkionline.ru/storage/posts/thumbs/yom-kippur-32593.jpg")
    urls.append("https://cdn.otkritkionline.ru/storage/posts/thumbs/international-cat-day-21449.jpg")
    urls.append("https://cdn.otkritkionline.ru/storage/posts/thumbs/diwali-32585.jpg")
    urls.append("https://cdn.otkritkionline.ru/storage/posts/thumbs/halloween-32711.jpg")
    urls.append("https://cdn.otkritkionline.ru/storage/posts/thumbs/all-saints-day-32697.jpg")
    urls.append("https://cdn.otkritkionline.ru/storage/posts/thumbs/intl-mens-day-16949.jpg")
    urls.append("https://cdn.otkritkionline.ru/storage/posts/thumbs/thanksgiving-day-33149.jpg")
    urls.append("https://cdn.otkritkionline.ru/storage/posts/thumbs/hanukkah-33837.jpg")
    urls.append("https://cdn.otkritkionline.ru/storage/posts/thumbs/christmas-day-33320.jpg")
    urls.append("https://cdn.otkritkionline.ru/storage/posts/thumbs/new-year-17868.jpg")
    urls.append("https://cdn.otkritkionline.ru/storage/posts/thumbs/new-year-17868.jpg")
    urls.append("https://cdn.otkritkionline.ru/storage/posts/thumbs/epiphany-17480.jpg")
    urls.append("https://cdn.otkritkionline.ru/storage/posts/thumbs/martin-luther-king-jr-day-17828.jpg")
    urls.append("https://cdn.otkritkionline.ru/storage/posts/thumbs/rose-day-18072.jpg")
    urls.append("https://cdn.otkritkionline.ru/storage/posts/thumbs/propose-day-18222.jpg")
    urls.append("https://cdn.otkritkionline.ru/storage/posts/thumbs/chocolate-day-18407.jpg")
    urls.append("https://cdn.otkritkionline.ru/storage/posts/thumbs/teddy-day-18427.jpg")
    urls.append("https://cdn.otkritkionline.ru/storage/posts/thumbs/promise-day-18517.jpg")
    urls.append("https://cdn.otkritkionline.ru/storage/posts/thumbs/hug-day-18474.jpg")
    urls.append("https://cdn.otkritkionline.ru/storage/posts/thumbs/kiss-day-18537.jpg")
    urls.append("https://cdn.otkritkionline.ru/storage/posts/thumbs/mardi-gras-18387.jpg")
    urls.append("https://cdn.otkritkionline.ru/storage/posts/thumbs/galentines-day-18527.jpg")
    urls.append("https://cdn.otkritkionline.ru/storage/posts/thumbs/valentines-day-29126.jpg")
    urls.append("https://cdn.otkritkionline.ru/storage/posts/thumbs/international-womens-day-29395.jpg")
    urls.append("https://cdn.otkritkionline.ru/storage/posts/thumbs/ramadan-29593.jpg")
    urls.append("https://cdn.otkritkionline.ru/storage/posts/thumbs/st-patricks-day-29634.jpg")
    urls.append("https://cdn.otkritkionline.ru/storage/posts/thumbs/st-joseph-19292.jpg")
    urls.append("https://cdn.otkritkionline.ru/storage/posts/thumbs/palm-sunday-29693.jpg")
    urls.append("https://cdn.otkritkionline.ru/storage/posts/thumbs/good-friday-29762.jpg")
    urls.append("https://cdn.otkritkionline.ru/storage/posts/thumbs/easter-29824.jpg")
    urls.append("https://cdn.otkritkionline.ru/storage/posts/thumbs/april-fools-day-29941.jpg")
    urls.append("https://cdn.otkritkionline.ru/storage/posts/thumbs/world-health-day-29947.jpg")
    urls.append("https://cdn.otkritkionline.ru/storage/posts/thumbs/earth-day-29971.jpg")
    urls.append("https://cdn.otkritkionline.ru/storage/posts/thumbs/passover-29965.jpg")
    urls.append("https://cdn.otkritkionline.ru/storage/posts/thumbs/may-day-30021.jpg")
    urls.append("https://cdn.otkritkionline.ru/storage/posts/thumbs/cinco-de-mayo-29997.jpg")
    urls.append("https://cdn.otkritkionline.ru/storage/posts/thumbs/mothers-day-30009.jpg")
    urls.append("https://cdn.otkritkionline.ru/storage/posts/thumbs/pentecost-30138.jpg")
    urls.append("https://cdn.otkritkionline.ru/storage/posts/thumbs/world-environment-day-31086.jpg")
    urls.append("https://cdn.otkritkionline.ru/storage/posts/thumbs/flag-day-31265.jpg")
    urls.append("https://cdn.otkritkionline.ru/storage/posts/thumbs/fathers-day-30281.jpg")
    urls.append("https://cdn.otkritkionline.ru/storage/posts/thumbs/bakr-ideid-ul-adha-31664.jpg")
    urls.append("https://cdn.otkritkionline.ru/storage/posts/thumbs/juneteenth-26680.jpg")
    urls.append("https://cdn.otkritkionline.ru/storage/posts/thumbs/summer-solstice-31542.jpg")
    urls.append("https://cdn.otkritkionline.ru/storage/posts/thumbs/intl-yoga-day-31530.jpg")
    urls.append("https://cdn.otkritkionline.ru/storage/posts/thumbs/international-kissing-day-31723.jpg")
    urls.append("https://cdn.otkritkionline.ru/storage/posts/thumbs/intl-day-of-friendship-31826.jpg")

    names = []
    names.append("grandparents-day.jpg")
    names.append("world-heart-day.jpg")
    names.append("nat-coffee-day.jpg")
    names.append("yom-kippur.jpg")
    names.append("international-cat-day.jpg")
    names.append("diwali.jpg")
    names.append("halloween.jpg")
    names.append("all-saints-day.jpg")
    names.append("international-men-s-day.jpg")
    names.append("thanksgiving-day.jpg")
    names.append("hanukkah.jpg")
    names.append("christmas-day.jpg")
    names.append("new-year.jpg")
    names.append("new-year.jpg")
    names.append("epiphany.jpg")
    names.append("martin-luther-king-jr-day.jpg")
    names.append("rose-day,jpg")
    names.append("propose-day.jpg")
    names.append("chocolate-day.jpg")
    names.append("teddy-day.jpg")
    names.append("promise-day.jpg")
    names.append("hug-day.jpg")
    names.append("kiss-day.jpg")
    names.append("mardi-gras.jpg")
    names.append("galentine-s-day.jpg")
    names.append("valentine-s-day.jpg")
    names.append("int-l-women-s-day.jpg")
    names.append("ramadan.jpg")
    names.append("st-patrick-s-day.jpg")
    names.append("st-joseph.jpg")
    names.append("palm-sunday.jpg")
    names.append("good-friday.jpg")
    names.append("easter.jpg")
    names.append("april-fool-s-day.jpg")
    names.append("world-health-day.jpg")
    names.append("earth-day.jpg")
    names.append("passover.jpg")
    names.append("may-day.jpg")
    names.append("cinco-de-mayo.jpg")
    names.append("mother-dayen.jpg")
    names.append("pentecost.jpg")
    names.append("world-environment-day.jpg")
    names.append("flag-day.jpg")
    names.append("fathers-day.jpg")
    names.append("bakr-id-eid-ul-adha.jpg")
    names.append("juneteenth.jpg")
    names.append("summer-solstice.jpg")
    names.append("yoga-day.jpg")
    names.append("international-kissing-day.jpg")
    names.append("int-l-day-of-friendship.jpg")
    download_images(urls, names, f"data/holidays/images")

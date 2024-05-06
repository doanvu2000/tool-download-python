import requests


def download_image(url, save_path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            file.write(response.content)
            print(f"download ok: {save_path}")
    else:
        print(f"down load failed: {url}")
def download_image2(url, save_path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(save_path, 'wb') as f:
            f.write(response.content)
        print("Image downloaded successfully")
    else:
        print("Failed to download image")

def downloadAllData():
    country = [
        'us', 'ca', 'au', 'de', 'nl', 'pe', 'cl', 'es', 'ru',
        'ar', 'at', 'ph', 'gb', 'ie', 'br', 'no', 'pl',
        'my', 'fk', 'th', 'zw', 'pk', 'ag', 'iq', 'nz', 'um', 'mx'
    ]
    for num in range(len(country)):
        name = country[num]
        link = f"https://static.mytuner.mobi/media/countries/{name}.png"
        print(link)
        # if (name == 'gb'):
        #     name = 'uk'
        # download_image2(link, f"data/country/{name}.png")


downloadAllData()

# def get_all_files_in_folder(folder_path):
#     files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
#     return files
#
# # Specify the path to your folder
# folder_path = 'data/cats'
#
# # Get the list of file names
# file_names = get_all_files_in_folder(folder_path)
#
# # Print the file names
# for file_name in file_names:
#     print(f"\"{file_name}\",")

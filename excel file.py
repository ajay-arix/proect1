import requests

def download_excel_file(url, save_path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            file.write(response.content)
        print("File downloaded successfully.")
    else:
        print("Failed to download the file.")

url = 'https://example.com/download/excel'
save_path = 'path/to/save/file.xlsx'

download_excel_file(url, save_path)

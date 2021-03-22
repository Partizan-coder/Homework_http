# coding=utf-8
import os
import requests


class YaUploader:

    file_path_yandex_cloud = os.path.join(os.getcwd())
    def __init__(self, token: str):
        self.token = token


    def upload(self, file_path: str):
        with open(file_path,'rb') as f:
            headers_upload = {'Authorization': f'OAuth {self.token}'}
            create_folder = requests.get(f'https://cloud-api.yandex.net/v1/disk/resources?path=%2Fdefault_folder', headers=headers_upload)
            if create_folder.status_code != 200:
                create_folder = requests.put(f'https://cloud-api.yandex.net/v1/disk/resources?path=%2Fdefault_folder', headers=headers_upload)
            upload_request = requests.get(f'https://cloud-api.yandex.net/v1/disk/resources/upload?path=%2Fdefault_folder/Upload_file_homework_http.txt?&overwrite=true', headers=headers_upload)
            upload_url = upload_request.json()['href']
            upload_file = requests.put(upload_url, data=f)
            if upload_file.status_code == 201:
                print(u'Файл успешно записан на Яндекс Диск')
            else:
                print(u'Ошибка. Код ошибки:', upload_file.status_code)
            return


if __name__ == '__main__':
    yandex_disk_token = 'AgAAAABR3TikAADLW0vVbPP0UUvBiQsUR0RJ4Bk'
    uploader = YaUploader(yandex_disk_token)
    result = uploader.upload('C:\\Users\\evgeniy.lapin\\Desktop\\Upload_file_homework_http.txt')
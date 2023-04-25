import os
import requests
from multiprocessing import Process


def download_pic_process(pic_url, uid, file_path):
    p = Process(target=save_img, args=(pic_url, uid, file_path))
    # 启动进程
    p.start()


def save_img(img_url, uid, file_path='resources/pics'):
    pic_name = str(uid) + ".jpeg"
    pic_path = os.path.join(file_path, pic_name)
    if os.path.exists(pic_path):
        return

    try:
        r = None
        if '100x100/' in img_url:
            img_url_400pix = img_url.replace('100x100/', '200x200/')
            r = requests.get(img_url_400pix, timeout=3, stream=False)
        if r is None or r.status_code != 200:
            r = requests.get(img_url, timeout=3, stream=False)
        with open(pic_path, 'wb') as f:
            for ch in r:
                f.write(ch)
    except Exception as e:
        print("download pic error: img url: {}, error:{}".format(img_url, e))


def get_one(msgDB, table_name, img_folder):
    return msgDB.get_one(table_name)
    # match_data = None
    # while match_data is None:
    #     data = msgDB.get_one(table_name)
    #     if data and os.path.exists(os.path.join(os.getcwd(), img_folder, str(data['UserId']) + '.jpeg')):
    #         match_data = data
    #     if not data:
    #         break
    # return match_data

def update_val(msgDB, table_name, valID):
    pass
    msgDB.update_val(table_name, valID)
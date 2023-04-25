import os
from flask import Flask, send_from_directory, request, Response
from flask_restful import reqparse, abort, Api, Resource
from flask_cors import CORS
from sqlite_db import SqliteDb
from utils import download_pic_process, get_one, update_val
app = Flask(__name__)
CORS(app, resources=r'/*')
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('task')

IMAGE_UPLOAD_FOLDER = "resources/pics/"
ROOT_PATH = os.path.dirname(__file__)


msgDB = SqliteDb("resources/db/livedb.db")
giftTable = "giftLog"
normalTable = "normalLog"
# normalDB = SqliteDb("normalLog")

msg_fields = ["UserNick", "UserHeadPic", "UserSex", "UserDisplayId", "UserId", "Msg", "GiftCount", "GiftName", "UserConsumeInRoom", "Type"]

class LiveTest(Resource):
    def get(self):
        # picUrl = ""
        file_name = "20230101.jpeg"
        picUrl = send_from_directory(os.path.join(ROOT_PATH, IMAGE_UPLOAD_FOLDER), file_name)
        print(picUrl)
        return {'name': "里斯哦is地", 'picid': picUrl}

@app.route("/api/image/<string:uid>", methods=['get'])
def index(uid):
    # path = request.args.get('path')
    # print(path)
    path = os.path.join(ROOT_PATH, IMAGE_UPLOAD_FOLDER, uid + ".jpeg")

    resp = Response(open(path, 'rb'), mimetype="image/jpeg")
    return resp


@app.route('/api/rec_message', methods=['GET', 'POST'])
def get_message():
    content = request.json
    val_args = {}
    for key in msg_fields:
        if key in content:
            val_args[key] = content[key]
    if len(val_args) == 0:
        print("error:2: ", content)
        return 1
    if content['GiftCount'] > 0:
        msgDB.insert_val(giftTable, val_args)
    else:
        msgDB.insert_val(normalTable, val_args)
    # download_pic_process(content['UserHeadPic'], content['UserId'], IMAGE_UPLOAD_FOLDER)
    return ''


@app.route("/api/get_one", methods=['get'])
def get_data():
    data = get_one(msgDB, giftTable, IMAGE_UPLOAD_FOLDER)
    if data:
        update_val(msgDB, giftTable, data['id'])
    if not data:
        data = get_one(msgDB, normalTable, IMAGE_UPLOAD_FOLDER)
        if data:
            update_val(msgDB, normalTable, data['id'])
    if not data:
        return ""
    ## flag 设置

    return {"uid": data["UserId"], "UserNick": data["UserNick"], "UserHeadPic": data["UserHeadPic"]}


api.add_resource(LiveTest, '/live_test')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)

import os
from flask import Flask, send_from_directory, request, Response
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('task')

IMAGE_UPLOAD_FOLDER = "resources/pics/"
ROOT_PATH = os.path.dirname(__file__)

class LiveTest(Resource):
    def get(self):
        # picUrl = ""
        file_name = "20230101.jpeg"
        picUrl = send_from_directory(os.path.join(ROOT_PATH, IMAGE_UPLOAD_FOLDER), file_name)
        print(picUrl)
        return {'name': "里斯哦is地", 'picid': picUrl}

@app.route("/api/image/<string:picid>", methods=['get'])
def index(picid):
    # path = request.args.get('path')
    # print(path)
    path = os.path.join(ROOT_PATH, IMAGE_UPLOAD_FOLDER, picid + ".jpeg")

    resp = Response(open(path, 'rb'), mimetype="image/jpeg")
    return resp

@app.route('/api/rec_message', methods=['GET', 'POST'])
def get_message():
    content = request.json
    print(content)
    # return jsonify({"uuid":uuid})
    return ''
##
## Actually setup the Api resource routing here
##
# api.add_resource(TodoList, '/todos')
api.add_resource(LiveTest, '/live_test')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)

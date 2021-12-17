import cv2
import json
from flask import Flask, jsonify, request

file = 'video.mp4'
nb_keyframes = 5

cap= cv2.VideoCapture(file)
frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
nom_video = '"nom_video":"' + file + '",'
nb_frame='"nb_frame":' + str(frame_count) + ','

images = '"images":['
sep_frame = int(frame_count / nb_keyframes)
i=1
while(cap.isOpened()):

    ret, frame = cap.read()
    if ret == False:
        break
    if i%sep_frame==0:
        cv2.imwrite('images/img'+str(i)+'.jpg',frame)
        images += '{"nom_img":"img'+str(i)+'.jpg","debut":'+str(i)+',"fin":'+str(i+sep_frame)+'},'
    i+=1

images = images[:-1] + "]"
json_str = "{" + nom_video + nb_frame + images + "}"
print(json_str)
json_obj = json.loads(json_str)

cap.release()
cv2.destroyAllWindows()

app = Flask(__name__)

@app.route('/api/', methods=['GET'])
def get_json():
    return jsonify(json_obj)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)

import cv2
import json
from flask import Flask, jsonify, request
from flask_cors import CORS
import os
import subprocess



path='./keyframes/src/assets/'
app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
json_str=''
#5 images




def get_frame_types(video_fn):
    command = 'ffprobe -v error -show_entries frame=pict_type -of default=noprint_wrappers=1'.split()
    out = subprocess.check_output(command + [video_fn]).decode()
    frame_types = out.replace('pict_type=','').split()
    return zip(range(len(frame_types)), frame_types)

def save_i_keyframes(video_fn):
    frame_types = get_frame_types(video_fn)
    i_frames = [x[0] for x in frame_types if x[1]=='I']
    if i_frames:
        cap = cv2.VideoCapture(video_fn)
        frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        
        nom_video = '"nom_video":"' + video_fn.split('/')[-1].split('.')[0] + '",'
        images = '"frames":['
        
        for frame_no in i_frames:
            cap.set(cv2.CAP_PROP_POS_FRAMES, frame_no)
            ret, frame = cap.read()
            grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            laplacian=cv2.Laplacian(grey,cv2.CV_64F).var()
            if laplacian<200 and frame_no!=0:
                continue
            print(frame_no,laplacian)   
            outname = path+'img/'+video_fn.split('/')[-1].split('.')[0]+'/img'+str(frame_no)+'.jpg'
            cv2.imwrite(outname, frame)
            if frame_no==0:
                images += '{"nom_img":"img'+str(frame_no)+'.jpg","debut":'+str(frame_no)
            else:
                images +=',"fin":'+str(frame_no)+'},{"nom_img":"img'+str(frame_no)+'.jpg","debut":'+str(frame_no)
            print ('Saved: '+outname)
        images=images + ',"fin":'+str(frame_count)+'}]'
        nb_frame='"nb_frames":' + str(frame_count)+','
        global json_str 
        json_str = "{" + nom_video + nb_frame + images + "}"
        print(json_str)
        cap.release()
    else:
        print ('No I-frames in '+video_fn)
        
@app.route('/api/upload/<title>', methods=['GET'])
def getUpload(title):
    save_i_keyframes(path+'videos/'+title)
    return get_frames()

    
@app.route('/api/frame/', methods=['GET'])
def get_frames():
    #print(json_str)
    return jsonify(json.loads(json_str))

@app.route('/api/video/', methods=['GET'])
def get_videos():
    videos=os.listdir(os.path.join(os.path.dirname(__file__),path[2:]+'videos'))
    json_video='{"nb_videos":'+str(len(videos))+',"videos":['
    for video in videos:
        json_video+='{"titre_video":"'+video+'"},'
    json_video=json_video[:-1]+']}'
    return jsonify(json.loads(json_video))
        
def makedir(directory):
        if not os.path.exists(directory):
            os.mkdir(directory)

if __name__ == '__main__':
    videos=os.listdir(os.path.join(os.path.dirname(__file__),path[2:]+'videos'))
    for video in videos:
        makedir(os.path.join(os.path.dirname(__file__),path[2:]+'img/'+video.split('.')[0]))
    app.run(host='127.0.0.1', port=5000, debug=True)
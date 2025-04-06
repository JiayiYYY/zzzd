from flask import Flask, jsonify
import os
import random

app = Flask(__name__)

# 假设图片位于服务器的static文件夹，或使用公开URL替换
IMAGE_FOLDER = './static/images/'

@app.route('/random-images', methods=['GET'])
def random_images():
    all_images = os.listdir(IMAGE_FOLDER)
    selected_images = random.sample(all_images, 140)

    response_data = {}

    for i in range(70):
        img1 = selected_images[2*i]
        img2 = selected_images[2*i + 1]
        response_data[f'Q{i+1}_img1'] = f'https://你的服务器地址/static/images/{img1}'
        response_data[f'Q{i+1}_img2'] = f'https://你的服务器地址/static/images/{img2}'

    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

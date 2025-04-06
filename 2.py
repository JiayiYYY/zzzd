from flask import Flask, jsonify, request, send_from_directory
import os
import random

app = Flask(__name__)

IMAGE_FOLDER = os.path.join(os.getcwd(), 'images')

@app.route('/random-images', methods=['GET'])
def random_images():
    all_images = os.listdir(IMAGE_FOLDER)
    if len(all_images) < 140:
        return jsonify({'error': 'Not enough images in the folder'}), 400

    selected_images = random.sample(all_images, 140)
    host = request.host_url.rstrip('/')
    response_data = {}

    for i in range(70):
        img1 = selected_images[2*i]
        img2 = selected_images[2*i + 1]
        response_data[f'Q{i+1}_img1'] = f'{host}/images/{img1}'
        response_data[f'Q{i+1}_img2'] = f'{host}/images/{img2}'

    return jsonify(response_data)

# 添加这个路由：公开 images 文件夹
@app.route('/images/<filename>')
def serve_image(filename):
    return send_from_directory(IMAGE_FOLDER, filename)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

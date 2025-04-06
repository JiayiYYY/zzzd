from flask import Flask, jsonify, request, send_from_directory
import os
import random

app = Flask(__name__)

# 图片目录：直接放在根目录的 images 文件夹下
IMAGE_FOLDER = os.path.join(os.getcwd(), 'images')

@app.route('/')
def index():
    return '✅ Flask app is running! Visit /random-images to get image pairs.'

@app.route('/random-images', methods=['GET'])
def random_images():
    try:
        all_images = os.listdir(IMAGE_FOLDER)
        usable_images = [img for img in all_images if img.lower().endswith(('.jpg', '.png', '.jpeg'))]
        
        if len(usable_images) < 4:
            return jsonify({'error': 'Too few images to generate pairs.'}), 400

        # 计算最大成对数量
        pair_count = len(usable_images) // 2
        selected_images = random.sample(usable_images, pair_count * 2)
        host = request.host_url.rstrip('/')
        response_data = {'total_pairs': pair_count}

        for i in range(pair_count):
            img1 = selected_images[2*i]
            img2 = selected_images[2*i + 1]
            response_data[f'Q{i+1}_img1'] = f'{host}/images/{img1}'
            response_data[f'Q{i+1}_img2'] = f'{host}/images/{img2}'

        return jsonify(response_data)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/images/<filename>')
def serve_image(filename):
    return send_from_directory(IMAGE_FOLDER, filename)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

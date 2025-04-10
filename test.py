from flask import Flask, jsonify, request, send_from_directory
import os
import random

app = Flask(__name__)

# 图片根目录：images 文件夹下有多个子文件夹
IMAGE_ROOT = os.path.join(os.getcwd(), 'images')

@app.route('/')
def index():
    return '✅ Flask app is running! Visit /random-images to get image pairs.'

@app.route('/random-images', methods=['GET'])
def random_images():
    try:
        response_data = {}
        total_images = []
        host = request.host_url.rstrip('/')

        # 获取所有子文件夹
        subfolders = [d for d in os.listdir(IMAGE_ROOT) if os.path.isdir(os.path.join(IMAGE_ROOT, d))]

        for folder in subfolders:
            folder_path = os.path.join(IMAGE_ROOT, folder)
            images = [f for f in os.listdir(folder_path) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]

            if len(images) < 12:
                return jsonify({'error': f'Folder \"{folder}\" does not have enough images.'}), 400

            selected = random.sample(images, 12)
            for img in selected:
                total_images.append(f'{folder}/{img}')  # 保存相对路径

        # 创建图片对（72张 → 36组）
        if len(total_images) < 72:
            return jsonify({'error': 'Not enough total images to form 36 pairs.'}), 400

        random.shuffle(total_images)  # 打乱顺序
        pair_count = len(total_images) // 2

        for i in range(pair_count):
            img1 = total_images[2 * i]
            img2 = total_images[2 * i + 1]
            response_data[f'Q{i+1}_img1'] = f'{host}/images/{img1}'
            response_data[f'Q{i+1}_img2'] = f'{host}/images/{img2}'

        response_data['total_pairs'] = pair_count
        return jsonify(response_data)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# 路由：支持访问子文件夹下的图片
@app.route('/images/<path:filename>')
def serve_image(filename):
    return send_from_directory(IMAGE_ROOT, filename)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

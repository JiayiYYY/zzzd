# 🧠 API Documentation — Randomized Image Pair Service for Qualtrics

## 📍 Base URL
```
https://your-app-name.onrender.com
```

## 🎯 Endpoint: `/random-images`
Returns a randomized list of **paired image URLs**, suitable for embedding into Qualtrics questions via `Embedded Data`.

---

## 🔧 Method
```
GET /random-images
```

## 📥 Parameters
_No parameters needed._  
Images are drawn from your server's `/images` folder (organized into subfolders).

---

## 📂 Folder Structure Requirements

Your GitHub or server should contain:
```
images/
├── folder1/
│   ├── img1.jpg
│   ├── img2.jpg
│   └── ...
├── folder2/
│   └── ...
...
├── folder6/
```
Each folder must have **at least 12 images**, totaling 72 images across 6 folders.

---

## 🔁 Logic

- Randomly select **12 images** from **each of the 6 folders**
- Combine them into a single shuffled list of **72 unique images**
- Divide them into **36 random pairs**
- Return the pairs in the format:
  ```
  Q1_img1, Q1_img2
  Q2_img1, Q2_img2
  ...
  Q36_img2
  ```

---

## ✅ Example Response (JSON)
```json
{
  "Q1_img1": "https://your-app-name.onrender.com/images/folder3/img045.jpg",
  "Q1_img2": "https://your-app-name.onrender.com/images/folder1/img010.jpg",
  "Q2_img1": "https://your-app-name.onrender.com/images/folder5/img003.jpg",
  ...
  "Q36_img2": "https://your-app-name.onrender.com/images/folder4/img078.jpg",
  "total_pairs": 36
}
```

---

## 🧪 Testing the API

Paste this into your browser:
```
https://your-app-name.onrender.com/random-images
```
You'll see a JSON object with all 36 image pairs, ready to use.

---

## 📦 Embedding in Qualtrics

In **Survey Flow**, use a **Web Service** block to call the API. Then add embedded data fields:
```
Q1_img1 ← Q1_img1
Q1_img2 ← Q1_img2
...
Q36_img2 ← Q36_img2
```

In each question, load the images using piped text:
```html
<img src="${e://Field/Q1_img1}">
<img src="${e://Field/Q1_img2}">
```

---

## 📎 Additional Info

- Framework: [Flask](https://flask.palletsprojects.com/)
- Hosting: [Render](https://render.com/)
- Source: Images hosted via GitHub → Render
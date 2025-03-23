# 🌿 DetectMe API - Plant Disease Detection  

This is a Flask-based API for detecting plant diseases from images using a deep learning model. The API processes an image, runs it through a pre-trained model, and returns a prediction of the disease type.  

---

## 🚀 Features  
- Accepts **Base64-encoded images** via a POST request  
- Uses a **deep learning model** (`plant_disease_model.h5`) to classify plant diseases  
- Supports **CORS** for cross-origin requests  
- Includes a **health check endpoint**  

---

## 📂 Project Structure  
```
📁 DetectMe-Backend
│-- app.py              # Main Flask API
│-- plant_disease_model.h5  # Trained model
│-- requirements.txt    # Dependencies
```

---

## 🔧 Setup & Installation  

### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/yourusername/DetectMe-Backend.git
cd DetectMe-Backend
```

### 2️⃣ Create a Virtual Environment  
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3️⃣ Install Dependencies  
```bash
pip install -r requirements.txt
```

### 4️⃣ Run the API  
```bash
python app.py
```

By default, the API will run at `http://127.0.0.1:5000/`.

---

## 📡 API Endpoints  

### 🟢 Health Check  
**Endpoint:** `/health`  
**Method:** `GET`  
📌 *Check if the API is running.*  
#### Response  
```json
{
  "status": "API is running"
}
```

### 🌱 Plant Disease Prediction  
**Endpoint:** `/predict`  
**Method:** `POST`  
📌 *Send a Base64-encoded image to get disease prediction.*  
#### Request Body  
```json
{
  "image": "data:image/png;base64,...."
}
```

#### Response  
```json
{
  "disease": "Corn - Common Rust",
  "confidence": 0.95,
  "class_index": 0
}
```

⚠ **Possible Errors**  
- `400`: Invalid or missing image data  
- `500`: Model loading or prediction failure  

---

## 📜 Dependencies  
- Flask  
- TensorFlow / Keras  
- NumPy  
- Pillow  
- Flask-CORS  

Install them using:  
```bash
pip install -r requirements.txt
```

---

## 🔗 Future Enhancements  
✅ Improve model accuracy  
✅ Add more plant disease classes  
✅ Deploy API to cloud (e.g., AWS, Heroku)  

---

## 🤝 Contributing  
Feel free to fork, submit issues, or create pull requests! 🚀  

---

## 🏷 License  
MIT License © 2025 DetectMe Team  

---

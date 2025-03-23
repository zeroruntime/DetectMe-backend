from flask import Flask, request, jsonify
import numpy as np
from tensorflow import keras
from keras.models import load_model
from keras.preprocessing import image
from PIL import Image
import io
import base64
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app) 

class_labels = {
    0: "Corn - Common Rust",
    1: "Potato - Early Blight",
    2: "Tomato - Bacterial Spot"
}

model_path = 'plant_disease_model.h5'
model = None  

def load_model_from_file():
    global model
    try:
        model = load_model(model_path)
        return True
    except Exception as e:
        return False

# Preprocess the image
def preprocess_image(img):

    img = img.resize((256, 256))  

    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) 
    img_array = img_array / 255.0 

    print(f"✅ Image preprocessed: shape={img_array.shape}") 
    return img_array

@app.route('/predict', methods=['POST'])
def predict():
    try:
        if model is None:
            if not load_model_from_file():
                return jsonify({'error': 'Model not available'}), 500

        if 'image' not in request.json:
            return jsonify({'error': 'No image data provided'}), 400

        image_data = request.json['image']

        image_data = image_data.split(',')[1] if ',' in image_data else image_data
        try:
            decoded_image = base64.b64decode(image_data)
        except Exception as e:
            return jsonify({'error': 'Invalid base64 image data'}), 400

        try:
            img = Image.open(io.BytesIO(decoded_image))
        except Exception as e:
            return jsonify({'error': 'Error processing image'}), 400

        processed_img = preprocess_image(img)

        try:
            prediction = model.predict(processed_img)
        except Exception as e:
            return jsonify({'error': 'Prediction failed'}), 500

        predicted_class = np.argmax(prediction[0])
        confidence = float(prediction[0][predicted_class])
        disease = class_labels.get(predicted_class, "Unknown")

        return jsonify({
            'disease': disease,
            'confidence': confidence,
            'class_index': int(predicted_class)
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'API is running'}), 200

if __name__ == '__main__':
    load_model_from_file()
    app.run(host='0.0.0.0', port=5000, debug=True)

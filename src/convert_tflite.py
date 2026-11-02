"""
Convert H5 Model to TFLite
"""

import tensorflow as tf
from src.config import MODELS_DIR

# 1. H5 model එක load කරගන්නවා
h5_model_path = MODELS_DIR / "classifier_initial.h5"
print(f"⏳ Loading model from {h5_model_path}...")
model = tf.keras.models.load_model(h5_model_path)

# 2. TFLite එකට හරවනවා
print("⏳ Converting to TFLite...")
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()

# 3. ඒක save කරනවා
tflite_path = MODELS_DIR / "plant_classification.tflite"
with open(tflite_path, 'wb') as f:
    f.write(tflite_model)

print(f"✅ Success! TFLite model saved at: {tflite_path}")
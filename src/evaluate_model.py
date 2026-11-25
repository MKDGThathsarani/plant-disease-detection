import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, classification_report
import os

# --- 1. Settings ---
VAL_DIR = r"data/val"
IMG_SIZE = (224, 224)
BATCH_SIZE = 32
MODEL_PATH = 'models/plant_classification_mobilenetv2.keras'

print("⏳ Validation Data Load කරමින්...")
val_dataset = tf.keras.utils.image_dataset_from_directory(
    VAL_DIR, image_size=IMG_SIZE, batch_size=BATCH_SIZE, shuffle=False)

class_names = val_dataset.class_names

print("⏳ Train කරපු Model එක Load කරමින්...")
# අපි දැන් අලුත් .keras file එක load කරන නිසා, කිසිම custom_objects ඕන නෑ
model = tf.keras.models.load_model(MODEL_PATH)

# --- 2. Predictions ගන්න ---
print("⏳ Predictions හදමින්... (ටිකක් වෙලා ගන්නවා)")
y_true = []
y_pred = []

for images, labels in val_dataset:
    predictions = model.predict(images, verbose=0)
    y_true.extend(labels.numpy())
    y_pred.extend(np.argmax(predictions, axis=1))

# --- 3. Confusion Matrix එක අඳිමු ---
print("⏳ Confusion Matrix එක අඳිමින්...")
cm = confusion_matrix(y_true, y_pred)

plt.figure(figsize=(20, 20))
sns.heatmap(cm, annot=False, cmap='Blues', xticklabels=class_names, yticklabels=class_names)
plt.xlabel('Predicted Label')
plt.ylabel('True Label')
plt.title('Confusion Matrix - Plant Disease Classification')
plt.xticks(rotation=90)
plt.yticks(rotation=0)
plt.tight_layout()
plt.savefig('confusion_matrix.png') # පින්තූරයක් විදිහට Save කරමු
print("✅ Confusion Matrix එක 'confusion_matrix.png' විදිහට Save කරලා ඉවරයි!")

# --- 4. Classification Report එක Print කරමු ---
print("\n" + "="*50)
print("📊 Classification Report")
print("="*50)
print(classification_report(y_true, y_pred, target_names=class_names))
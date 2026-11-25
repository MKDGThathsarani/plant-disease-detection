import tensorflow as tf
from tensorflow.keras import layers, models

# --- 1. Settings (සැකසුම්) ---
TRAIN_DIR = r"data/train"
VAL_DIR = r"data/val"
IMG_SIZE = (224, 224)
BATCH_SIZE = 32
EPOCHS = 5  # අපි මුලින්ම 5 පාරක් විතර train කරමු

print("⏳ Data Load කරමින්...")
train_dataset = tf.keras.utils.image_dataset_from_directory(
    TRAIN_DIR, image_size=IMG_SIZE, batch_size=BATCH_SIZE, shuffle=True, seed=42)
val_dataset = tf.keras.utils.image_dataset_from_directory(
    VAL_DIR, image_size=IMG_SIZE, batch_size=BATCH_SIZE, shuffle=False)

# පන්ති ගණන (38)
num_classes = len(train_dataset.class_names)

# --- 2. Data Augmentation (රූප වෙනස් කිරීම) ---
data_augmentation = tf.keras.Sequential([
    layers.RandomFlip("horizontal_and_vertical"),
    layers.RandomRotation(0.2),
    layers.RandomZoom(0.2),
])

# --- 3. Pre-trained Model එක (MobileNetV2) ---
print("⏳ MobileNetV2 Model එක Load කරමින්...")
base_model = tf.keras.applications.MobileNetV2(
    input_shape=(224, 224, 3),
    include_top=False, 
    weights='imagenet' 
)
base_model.trainable = False 

# --- 4. අලුත් Model එක හදමු ---
inputs = tf.keras.Input(shape=(224, 224, 3))
x = data_augmentation(inputs)
x = tf.keras.applications.mobilenet_v2.preprocess_input(x) 
x = base_model(x, training=False)
x = layers.GlobalAveragePooling2D()(x)
x = layers.Dropout(0.2)(x) 
outputs = layers.Dense(num_classes, activation='softmax')(x) 

model = tf.keras.Model(inputs, outputs)

# --- 5. Model එක Compile කරමු ---
model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=0.0001),
    loss='sparse_categorical_crossentropy', 
    metrics=['accuracy']
)

# --- 6. Train කරමු! ---
print("\n🚀 Training පටන් ගන්නවා... (මේකට ටිකක් වෙලා ගන්නවා, ඉවර වෙනකම් ඉන්න)")
history = model.fit(
    train_dataset,
    validation_data=val_dataset,
    epochs=EPOCHS
)

# --- 7. Save කරමු ---
# අලුත් විදිහට save කරමු (Keras native format)
model.save("models/plant_classification_mobilenetv2.keras")
print("\n🎉 Model එක Train කරලා 'models/plant_classification_mobilenetv2.h5' විදිහට Save කරලා ඉවරයි!")
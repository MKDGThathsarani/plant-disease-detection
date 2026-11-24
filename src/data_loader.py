import tensorflow as tf
import os

# අපේ data තියෙන තැන්
TRAIN_DIR = r"data/train"
VAL_DIR = r"data/val"

# Image එකක size එක සහ Batch size එක
IMG_SIZE = (224, 224)
BATCH_SIZE = 32

print("⏳ Data Loader එක වැඩ කරන්න පටන් ගන්නවා...\n")

# 1. Training Data ටික Load කිරීම
print("📂 Train images load කරමින්...")
train_dataset = tf.keras.utils.image_dataset_from_directory(
    TRAIN_DIR,
    image_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    shuffle=True, # Train කරද්දී හැම වෙලාවෙම පිළිවෙල වෙනස් වෙන්න ඕනේ
    seed=42
)

# 2. Validation Data ටික Load කිරීම
print("\n📂 Validation images load කරමින්...")
val_dataset = tf.keras.utils.image_dataset_from_directory(
    VAL_DIR,
    image_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    shuffle=False # Val කරද්දී පිළිවෙල වෙනස් වෙන්න ඕන නෑ
)

# 3. Class names ටික බලමු
class_names = train_dataset.class_names
print(f"\n✅ මුළු පන්ති (Classes) ගණන: {len(class_names)}")
print(f"✅ පළවෙනි පන්තිය: {class_names[0]}")

# 4. Data Prefetching (මේකෙන් training එක ගොඩක් ඉක්මන් වෙනවා)
AUTOTUNE = tf.data.AUTOTUNE
train_dataset = train_dataset.prefetch(buffer_size=AUTOTUNE)
val_dataset = val_dataset.prefetch(buffer_size=AUTOTUNE)

print("\n🎉 Data Loader එක සාර්ථකව හදලා ඉවරයි!")
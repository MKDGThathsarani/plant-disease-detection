"""
Dataset Loader & Pipeline
"""

import tensorflow as tf
from src.config import DATASET_DIR, IMG_SIZE, BATCH_SIZE

def get_datasets():
    print("⏳ Loading dataset...")
    
    # PlantVillage dataset එකේ color folder එක
    data_dir = DATASET_DIR / "plantvillage dataset" / "color"
    
    # Training dataset (80%)
    train_ds = tf.keras.utils.image_dataset_from_directory(
        data_dir,
        validation_split=0.2,
        subset="training",
        seed=42,
        image_size=(IMG_SIZE, IMG_SIZE),
        batch_size=BATCH_SIZE,
        label_mode="categorical"
    )
    
    # Validation dataset (20%)
    val_ds = tf.keras.utils.image_dataset_from_directory(
        data_dir,
        validation_split=0.2,
        subset="validation",
        seed=42,
        image_size=(IMG_SIZE, IMG_SIZE),
        batch_size=BATCH_SIZE,
        label_mode="categorical"
    )
    
    print(f"✅ Dataset loaded! Total classes: {len(train_ds.class_names)}")
    return train_ds, val_ds, train_ds.class_names

if __name__ == "__main__":
    train_ds, val_ds, class_names = get_datasets()
    print("\n--- රෝග වර්ග 38 ---")
    for i, name in enumerate(class_names):
        print(f"{i+1}. {name}")
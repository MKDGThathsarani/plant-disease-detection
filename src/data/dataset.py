"""
Dataset Loader & Pipeline
මේ file එකෙන් අපේ ලොකු dataset එක කියවලා, model එකට ගැලපෙන විදිහට වෙනස් කරනවා.
"""

import tensorflow as tf
from src.config import DATASET_DIR, IMG_SIZE, BATCH_SIZE

def get_datasets():
    """
    මේ function එකෙන් dataset එක load කරලා, train සහ validation කියලා කොටස් දෙකකට බෙදනවා.
    """
    print("⏳ Loading dataset from:", DATASET_DIR)
    
    # අපේ dataset එකේ තියෙන ප්‍රධාන folder එක
    data_dir = DATASET_DIR / "plantvillage dataset" / "color"
    
    # 1. Training dataset එක (80%)
    train_ds = tf.keras.utils.image_dataset_from_directory(
        data_dir,
        validation_split=0.2,      # 20% එක validation එකට ගන්නවා
        subset="training",         # මේක training කොටස
        seed=42,                   # හැම වෙලාවෙම එකම විදිහට බෙදෙන්න
        image_size=(IMG_SIZE, IMG_SIZE), # පින්තූර 224x224 කරනවා
        batch_size=BATCH_SIZE,     # එක පාරකට 32 ක් විතර ගන්නවා
        label_mode="categorical"   # පන්ති 38ක් (one-hot encoding)
    )
    
    # 2. Validation dataset එක (20%)
    val_ds = tf.keras.utils.image_dataset_from_directory(
        data_dir,
        validation_split=0.2,
        subset="validation",       # මේක validation කොටස
        seed=42,
        image_size=(IMG_SIZE, IMG_SIZE),
        batch_size=BATCH_SIZE,
        label_mode="categorical"
    )
    
    print(f"✅ Dataset loaded successfully!")
    print(f"Class names: {train_ds.class_names}")
    
    return train_ds, val_ds, train_ds.class_names

# මේ file එක කෙලින්ම run කරලා test කරන්න
if __name__ == "__main__":
    train_ds, val_ds, class_names = get_datasets()
    
    # ෆෝල්ඩර් වල නම් ටික print කරලා බලමු (රෝග 38)
    print("\n--- රෝග වර්ග 38 ---")
    for i, name in enumerate(class_names):
        print(f"{i+1}. {name}")

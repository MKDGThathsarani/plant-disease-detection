import os
import shutil
import random

# Paths
source_path = r"data/archive/plantvillage dataset/color"
train_path = r"data/train"
val_path = r"data/val"

# Train/Validation අනුපාතය (80% train, 20% val)
train_ratio = 0.8

# Random එකෙන් images තෝරන නිසා, හැම වෙලාවෙම එකම result එක එන්න seed එකක් දාමු
random.seed(42)

print("🚀 Dataset split කරන්න පටන් ගන්නවා...\n")

# Classes ටික ගන්න
classes = os.listdir(source_path)

total_train = 0
total_val = 0

for class_name in classes:
    class_source = os.path.join(source_path, class_name)
    
    # ඒක folder එකක්ද කියලා බලන්න
    if not os.path.isdir(class_source):
        continue
    
    # ඒ class එකේ images ඔක්කොම ගන්න
    images = [f for f in os.listdir(class_source) 
              if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
    
    # Images ටික shuffle කරන්න
    random.shuffle(images)
    
    # 80% train, 20% val වලට බෙදන්න
    split_index = int(len(images) * train_ratio)
    train_images = images[:split_index]
    val_images = images[split_index:]
    
    # Train folder එක හදන්න
    train_class_path = os.path.join(train_path, class_name)
    os.makedirs(train_class_path, exist_ok=True)
    
    # Val folder එක හදන්න
    val_class_path = os.path.join(val_path, class_name)
    os.makedirs(val_class_path, exist_ok=True)
    
    # Images copy කරන්න
    for img in train_images:
        shutil.copy(os.path.join(class_source, img), 
                    os.path.join(train_class_path, img))
    
    for img in val_images:
        shutil.copy(os.path.join(class_source, img), 
                    os.path.join(val_class_path, img))
    
    total_train += len(train_images)
    total_val += len(val_images)
    
    print(f"✅ {class_name}: Train {len(train_images)}, Val {len(val_images)}")

print("\n" + "=" * 50)
print(f"🎉 ඉවරයි!")
print(f"📊 මුළු Train images: {total_train}")
print(f"📊 මුළු Validation images: {total_val}")
print("=" * 50)
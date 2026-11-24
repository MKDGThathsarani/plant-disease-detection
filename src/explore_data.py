import os

# Dataset එක තියෙන තැන (path එක)
dataset_path = r"data/archive/plantvillage dataset/color"

# ෆෝල්ඩර් එක තියෙනවද කියලා බලමු
if os.path.exists(dataset_path):
    print("✅ Dataset folder එක හම්බුනා!\n")
    
    classes = os.listdir(dataset_path)
    print(f"මේකෙ තියෙන මුළු පන්ති (Classes) ගණන: {len(classes)}\n")
    
    print("=" * 50)
    print("Class එකකට images කීයක් තියෙනවද:")
    print("=" * 50)
    
    total_images = 0
    class_counts = {}
    
    for class_name in classes:
        class_path = os.path.join(dataset_path, class_name)
        if os.path.isdir(class_path):
            # ඒ class folder එකේ තියෙන files ගණන
            images = [f for f in os.listdir(class_path) 
                      if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
            count = len(images)
            class_counts[class_name] = count
            total_images += count
            print(f"{class_name}: {count} images")
    
    print("\n" + "=" * 50)
    print(f"📊 මුළු images ගණන: {total_images}")
    print(f"📊 මුළු classes ගණන: {len(class_counts)}")
    print(f"📊 එක class එකකට සාමාන්‍යයෙන්: {total_images // len(class_counts)} images")
    print("=" * 50)
    
    # අඩුම සහ වැඩිම images තියෙන classes
    min_class = min(class_counts, key=class_counts.get)
    max_class = max(class_counts, key=class_counts.get)
    print(f"\n🔻 අඩුම images: {min_class} ({class_counts[min_class]} images)")
    print(f"🔺 වැඩිම images: {max_class} ({class_counts[max_class]} images)")
    
else:
    print("❌ මේ path එකේ dataset එකක් හම්බුනේ නෑ! Path එක හරිද කියලා බලන්න.")
    print("ඔයා හදපු path එක බලන්න:", dataset_path)
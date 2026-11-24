import os

# Dataset එක තියෙන තැන (path එක)
dataset_path = r"data/archive/plantvillage dataset/color"

# ෆෝල්ඩර් එක තියෙනවද කියලා බලමු
if os.path.exists(dataset_path):
    print("✅ Dataset folder එක හම්බුනා!\n")
    
    # ඒක ඇතුළේ තියෙන ලෙඩ වර්ග (classes) බලමු
    classes = os.listdir(dataset_path)
    print(f"මේකෙ තියෙන මුළු පන්ති (Classes) ගණන: {len(classes)}\n")
    
    print("මේ තමයි ඒ පන්ති වල නම්:")
    for i, class_name in enumerate(classes):
        print(f"{i+1}. {class_name}")
        
else:
    print("❌ මේ path එකේ dataset එකක් හම්බුනේ නෑ! Path එක හරිද කියලා බලන්න.")
    print("ඔයා හදපු path එක බලන්න:", dataset_path)
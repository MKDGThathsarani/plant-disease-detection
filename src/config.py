"""
Central Configuration File
මේකෙන් අපේ project එකේ හැම තැනකම පාවිච්චි වෙන settings ටික එක තැනකින් තියෙනවා.
"""

import os
from pathlib import Path

# ==========================================
# 1. Folder Paths (අපේ folders තියෙන තැන්)
# ==========================================
# මේකෙන් ROOT_DIR එක හොයාගන්නේ අපේ project එකේ අන්තිම folder එක (plant-disease-detection)
ROOT_DIR = Path(__file__).parent.parent 

DATASET_DIR = ROOT_DIR / "dataset"
MODELS_DIR = ROOT_DIR / "models"
ASSETS_DIR = ROOT_DIR / "assets"

# ==========================================
# 2. Classification Settings
# ==========================================
# අපේ model එකට දෙන image size එක සහ batch size එක
IMG_SIZE = 224          # MobileNetV2 එකට හරියන size එක
BATCH_SIZE = 32         # එක පාරකට model එකට යවන images ගාන
NUM_CLASSES = 38        # PlantVillage dataset එකේ තියෙන disease වර්ග ගාන
EPOCHS = 20             # Model එක train කරන වට ගාන
LEARNING_RATE = 0.001   # Model එක ඉගෙන ගන්න වේගය

# ==========================================
# 3. Misc Settings
# ==========================================
RANDOM_SEED = 42        # හැම වෙලාවෙම එකම result එක එන්න (reproducibility)

# Folders ටික නැත්නම් හදාගන්න (Error එන එක නවත්තන්න)
for folder in [DATASET_DIR, MODELS_DIR, ASSETS_DIR]:
    folder.mkdir(parents=True, exist_ok=True)

print(f"✅ Config loaded. Project root: {ROOT_DIR.name}")
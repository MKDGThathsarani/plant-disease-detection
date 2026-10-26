"""
Training Script for Plant Disease Classifier
මේකෙන් තමයි අපේ MobileNetV2 model එක train කරන්නේ.
"""

import tensorflow as tf
from src.config import MODELS_DIR, EPOCHS
from src.data.dataset import get_datasets
from src.models.classifier import build_classifier

def train():
    print("🚀 Starting Model Training...")
    
    # 1. Dataset එක load කරගන්නවා
    train_ds, val_ds, class_names = get_datasets()
    
    # 2. Model එක හදාගන්නවා
    model = build_classifier()
    
    # 3. Model එක save කරන්න තැනක් හදාගන්නවා
    model_path = MODELS_DIR / "classifier_initial.h5"
    
    # 4. Callbacks (Training එක monitor කරන්න)
    callbacks = [
        tf.keras.callbacks.ModelCheckpoint(
            filepath=str(model_path),
            save_best_only=True,
            monitor='val_accuracy',
            verbose=1
        ),
        tf.keras.callbacks.EarlyStopping(
            monitor='val_loss',
            patience=3,
            restore_best_weights=True
        )
    ]
    
    # 5. Training එක පටන් ගන්නවා
    history = model.fit(
        train_ds,
        validation_data=val_ds,
        epochs=EPOCHS,
        callbacks=callbacks
    )
    
    print("✅ Training Complete!")
    print(f"Model saved at: {model_path}")
    
    return history

if __name__ == "__main__":
    train()
import tensorflow as tf
import os

MODEL_PATH = os.path.join("outputs", "final_model.h5")
OUT_PATH = os.path.join("app_artifacts", "final_model.tflite")

model = tf.keras.models.load_model(MODEL_PATH)

# Convert to TFLite
converter = tf.lite.TFLiteConverter.from_keras_model(model)
converter.target_spec.supported_ops = [
    tf.lite.OpsSet.TFLITE_BUILTINS,]

converter.optimizations = [tf.lite.Optimize.DEFAULT]
tflite_model = converter.convert()

# Save the model
with open(OUT_PATH, "wb") as f:
    f.write(tflite_model)

print(f"Conversion complete! Saved as {OUT_PATH}")

import tensorflow as tf


model = tf.keras.models.load_model("app_artifacts/final_model.h5")

# Convert to TFLite
converter = tf.lite.TFLiteConverter.from_keras_model(model)
converter.optimizations = [tf.lite.Optimize.DEFAULT]

tflite_model = converter.convert()

# Save the model
with open("app_artifacts/final_model.tflite", "wb") as f:
    f.write(tflite_model)

print("Conversion complete! Saved as app_artifacts/final_model.tflite")

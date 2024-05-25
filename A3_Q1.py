import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk 
import tensorflow as tf 
import tensorflow_hub as hub 

class ImageClassifierApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Image Classifier")
        self.geometry("400x400")

        self.create_widgets()

        # Load the pre-trained model from TensorFlow Hub
        self.model = hub.load("https://tfhub.dev/google/imagenet/mobilenet_v2_100_224/classification/5")

    def create_widgets(self):
        self.label = tk.Label(self, text="Upload an image:")
        self.label.pack()

        self.upload_button = tk.Button(self, text="Upload", command=self.upload_image)
        self.upload_button.pack()

        self.result_label = tk.Label(self, text="")
        self.result_label.pack()

    def upload_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            image = Image.open(file_path)
            image = image.resize((224, 224))
            photo = ImageTk.PhotoImage(image)
            
            self.result_label.config(text="Classifying...")
            self.result_label.update()

            # Classify the image using the pre-trained model
            prediction = self.classify_image(image)
            
            self.result_label.config(text="Predicted: " + prediction)

    def classify_image(self, image):
        # Preprocess the image
        image = tf.image.convert_image_dtype(image, tf.float32)
        image = tf.image.resize(image, (224, 224))
        image = tf.expand_dims(image, axis=0)

        # Perform inference using the pre-trained model
        predictions = self.model(image)
        
        # Get the predicted class label
        predicted_label_index = tf.argmax(predictions, axis=1).numpy()[0]
        labels_path = tf.keras.utils.get_file('ImageNetLabels.txt','https://storage.googleapis.com/download.tensorflow.org/data/ImageNetLabels.txt')
        with open(labels_path) as f:
            labels = f.readlines()
        predicted_label = labels[predicted_label_index]

        return predicted_label.strip()

if __name__ == "__main__":
    app = ImageClassifierApp()
    app.mainloop()
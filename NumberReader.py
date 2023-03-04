import tensorflow as tf
import time
import cv2
import mss
import numpy as np
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from IPython.display import clear_output

# top, left, width and height of the capture monitor
top = 400
left = 100
width = 400
height = 400

timeStop = 2 

#Press q to quit the program

mnist=tf.keras.datasets.mnist

# Load MNIST datasets
(x_train, y_train),(x_test, y_test) = mnist.load_data()
x_train,x_test =x_train/255.0, x_test/255.0

# The machine learning model 
model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28,28)),
    tf.keras.layers.Dense(128,activation='relu'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(10)
])

loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)

model.compile(optimizer='adam',
              loss=loss_fn,
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=10)

# To read input from the user
with mss.mss() as sct:

    monitor = {"top": top, "left": left, "width": width, "height": height}

    while "Screen capturing":
        last_time = time.time()

     
        img = np.array(sct.grab(monitor))

        cv2.imshow('OpenCV/Numpy grayscale', cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY))

        print("fps: {}".format(1 / (time.time() - last_time)))

        img = cv2.resize(img,(28,28))
        img = img_to_array(img)
        img = img[:,:,0]
        img = np.expand_dims(img, axis = 0)
        images = np.vstack([img])

        test_pred = model.predict(images)
        print(test_pred)
        print("Number: ",np.argmax(test_pred))


        
        if cv2.waitKey(25) & 0xFF == ord("q"):
            cv2.destroyAllWindows()
            break
        clear_output(wait=True)
        time.sleep(timeStop)
        
# Image-Captioning

The model is based on cnn-lstm neural networks which automatically detects the objects in the images and generates description for the images.

The model can perform 2 operations.
The VGG16 Model is to detect objects in the image using Convolutional Neural Networks and the other is to caption the images using RNN based LSTM (Long Short Term Memory).

Detailed explanation is given through the Report.pdf uploaded.

Training of the model is done through google colab.

Front-end Software: Django,HTML, CSS, Web browser.
Back-end Software: Sklearn,pandas and various other requirements that have been solved by using Google colab.

## Working of this project:

home
In the above folder copy the model_18.h5 file.

The model_18.h5 will be provided when u train the program in colab. 
Here is the trained model............https://drive.google.com/file/d/10K7L-mhX1y4DI_rIuuZlfwhEi9l9OkPP/view?usp=sharing

Dataset used here is Flickr8k dataset. You can use quite a big dataset to train. The more the better output.
Dataset................https://www.kaggle.com/adityajn105/flickr8k

Then in terminal or cmd run the program as python manage.py runserver and before this install all the library

## Output Screenshots:

### Input (Before Uploading)
![Input](https://user-images.githubusercontent.com/54733837/122507477-eb956e80-d01d-11eb-9b8e-107f7497f720.PNG)

### Input (After Uploading)
![caption after uploading](https://user-images.githubusercontent.com/54733837/122507566-0e278780-d01e-11eb-8692-e574e1e2527e.PNG)

### Output (Predict Caption)
![Caption Predicted](https://user-images.githubusercontent.com/54733837/122507630-2a2b2900-d01e-11eb-8b47-154b3df2c1d6.PNG)




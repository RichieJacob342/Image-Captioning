from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

from pickle import load
from numpy import argmax
from keras.preprocessing.sequence import pad_sequences
from keras.applications.vgg16 import VGG16
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.applications.vgg16 import preprocess_input
from keras.models import Model
from keras.models import load_model
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior() 
import os
from .extr import extract_features, generate_desc, word_for_id

def indexNext(request):
	# load the tokenizer
	tokenizer = load(open('C:\\Users\\91970\\Desktop\\django\\ImageCaption\\home\\tokenizer.pkl', 'rb'))
	# pre-define the max sequence length (from training)
	max_length = 34
	# load the model
	model = load_model('C:\\Users\\91970\\Desktop\\django\\ImageCaption\\home\\model_18.h5')

	FileIt = os.listdir('C:\\Users\\91970\\Desktop\\django\\ImageCaption\\static\\savedImg')

	# load and prepare the photograph
	photo = extract_features('C:\\Users\\91970\\Desktop\\django\\ImageCaption\\static\\savedImg\\{fle}'.format(fle=FileIt[len(FileIt)-1]))
	# generate description
	description = generate_desc(model, tokenizer, photo, max_length)
	#to remove endseq an start endsq
	query = description
	stopwords = ['startseq','endseq']
	querywords = query.split()

	resultwords  = [word for word in querywords if word.lower() not in stopwords]
	result = ' '.join(resultwords)
	var = result
	return render(request,"demo.html",{'cap':var,'iname':FileIt[len(FileIt)-1]})

def index(request):
	if request.method == 'POST':
		uploaded_file = request.FILES['document']
		fs = FileSystemStorage()
		fs.save(uploaded_file.name,uploaded_file)
		print(uploaded_file)
	return render(request,"demo.html")
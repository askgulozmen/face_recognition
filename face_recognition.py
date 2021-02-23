import face_recognition
import dlib
from PIL import Image
import face_recognition
import time
tic=time.time()
import os
# Load the jpg file into a numpy array

dir="/content/drive/MyDrive/Colab Notebooks/resim_dataset/"
dosyalar=os.listdir(dir)
for dosya in dosyalar:
  print(dosya)
#data=os.listdir(klasorler)
import os
os.makedirs(dir+"/"+"face_macron",mode=777,exist_ok=True)
!ls

for klasor in os.listdir(dir):
  print(klasor)


  for index, klasor in enumerate( os.listdir(dir)):
  i=0
  for fotograf in os.listdir(dir+"/"+klasor):
    #mage = face_recognition.load_image_file(dir+"/"+klasor+"/"+fotograf)
    print(fotograf)
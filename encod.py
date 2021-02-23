import os
import glob
import numpy as np
import face_recognition
face_names = os.listdir("/content/drive/MyDrive/Colab Notebooks/resim_dataset/")
print(face_names)

import pandas as pd

data = pd.DataFrame(columns=["klasor","Mean_Encoding"])
for index,klasor in enumerate( face_names):
    sayi=0
   
    print

    cur_direc = os.getcwd()
    path = os.path.join(cur_direc, '/content/drive/MyDrive/Colab Notebooks/resim_dataset/{}'.format(klasor)+"/")
    list_of_files = [f for f in glob.glob(path+'*.jpg')]
    total_face_encod=np.zeros((1,128))
    for i in range(len(list_of_files)):
      
      face = face_recognition.load_image_file(list_of_files[i])
      
      face_encod = face_recognition.face_encodings(face)
      #print(len(face_encod))
      
      #print(face_encod)
      
      if len(face_encod)==1:
        face_encod = np.asarray(face_encod).reshape(1,128)
        total_face_encod = np.add(total_face_encod,face_encod)
        sayi+=1
    total_face_encod = total_face_encod/sayi
    data.loc[index] = [klasor,total_face_encod]
    print(data.head)
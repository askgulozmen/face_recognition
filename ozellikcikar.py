import numpy as np
import os
from keras.preprocessing import image
import pandas as pd
veriler = {}
face_features = pd.DataFrame(columns=["klasor","ozellik"])
for klasor in os.listdir("/content/drive/MyDrive/Colab Notebooks/resim_dataset/"):
    print(klasor)
face_features1=[]
dir = "/content/drive/MyDrive/Colab Notebooks/resim_dataset/"
klasorler = os.listdir(dir)
i=0
for klasor in klasorler:
  ozellik = ozellicikar(dir+klasor+"/")
  ozellik = ozellik
  veriler[klasor]=ozellik
 
  i+=1
  print(veriler)
veriler

def ozellicikar(yoll):
    tlp=np.zeros(2048)
    resimler=os.listdir(yoll)
    for res in resimler:
        yol=yoll+res
        #print(yol)
        try:
          img = image.load_img(yol, target_size=(197,197))
          img = image.img_to_array(img)
          img = np.expand_dims(img, axis=0)
          #print(img.shape)
          ozellik=vggface.predict(img)
          #print(ozellik)
          tlp=ozellik+tlp

        except:
          pass
        #print(toplam)
    feature=tlp/len(resimler)    
    feature=np.reshape(feature,(1,2048))
    
    feature=feature.tolist()
    #isimlerr.append(res)
    print(yoll+" : Klasörün özellik haritası çıkartıldı:(1,2048)")
    return feature



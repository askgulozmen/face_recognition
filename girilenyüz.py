from scipy.spatial import distance
from PIL import Image
img=Image.open("macron.jpg",mode="r")
img=np.asarray(img)
face=face_recognition.load_image_file("macron.jpg")
location=face_recognition.face_locations(face)
top, right, bottom, left = location[0]
face=img[top:bottom,left:right]
face=Image.fromarray(face)
face.save("macron_yuz.jpg")
face=face_recognition.load_image_file("macron_yuz.jpg")
encod=face_recognition.face_encodings(face)
dist=[]
for i in data["Mean_Encoding"]:
  dis=distance.cosine(encod,i)
  dist.append(dis)

dist=np.array(dist)
bul=np.argmin(dist)
sonuc=data["Name"][bul]
print("girilen yüz {} aiittir".format(sonuc))

for i in range(number_files):
    globals()['image_{}'.format(i)] = face_recognition.load_image_file(list_of_files[i])
    globals()['image_encoding_{}'.format(i)] = face_recognition.face_encodings(globals()['image_{}'.format(i)])[0]
    faces_encodings.append(globals()['image_encoding_{}'.format(i)])
# Create array of known names
    names[i] = names[i].replace(cur_direc, "")  
    faces_names.append(names[i])
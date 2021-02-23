for index, klasor in enumerate( os.listdir(dir)):
  i=0
  for fotograf in os.listdir(dir+"/"+"Emmanuel Macron"):
    print(dir)
    image = face_recognition.load_image_file(dir+"/"+"Emmanuel Macron"+"/"+fotograf)

    face_locations = face_recognition.face_locations(image, number_of_times_to_upsample=0, model="cnn")

    print("I found {} face(s) in this photograph.".format(len(face_locations)))
    
    for face_location in face_locations:

    # Print the location of each face in this image
      top, right, bottom, left = face_location
      print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))

    # You can access the actual face itself like this:
      face_image = image[top:bottom, left:right]
      pil_image = Image.fromarray(face_image)
      pil_image.save(dir+"/"+"face_macron"+"/"+str(i)+".jpg")
      i+=1
    toc=time.time()

    print(f"Forograf face recognation kütüphanesi ile {toc-tic} zamanda tespit edildi",dir+"/"+"Emmanuel Macron"+"/"+fotograf)
    #pil_image
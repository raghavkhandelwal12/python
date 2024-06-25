import cv2
import logging

#set up logging
logging.basicConfig(level=logging.INFO,format='%(asctime)s-%(levelname)s-%(message)s')

def load_image(image_path):
    try:
        image=cv2.imread(image_path)
        if image is None:
            raise FileNotFoundError(f"No image found at {image_path}")
        logging.info(f"Image loaded from {image_path}")
        return image
    except Exception as e:
        logging.error(f"error loading image:{e}")
        raise

def convert_to_grayscale(image):
    gray_image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    logging.info('converted image to grayscale')
    return gray_image

def detect_faces(image,classifier_path):
    face_cascade=cv2.CascadeClassifier(classifier_path)
    if face_cascade.empty():
        raise ValueError(f"failed to load classifier from {classifier_path}") 
    
    gray_image=convert_to_grayscale(image)
    faces=face_cascade.detectMultiScale(gray_image,scaleFactor=1.1,minNeighbors=5,minSize=(30,30))
    logging.info(f"Detected{len(faces)}faces")
    return faces

def draw_faces(image,faces):
    for(x,y,w,h) in faces:
        cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
    logging.info('draw rectangle around faces')
    return faces

def save_image(image,output_path):
    cv2.imwrite(output_path,image)
    logging.info(f'saved image with faces to {output_path}')
    
def main(image_path,classifier_path,output_path):
    try:
        image=load_image(image_path)
        faces=detect_faces(image,classifier_path)
        image_with_faces=draw_faces(image,faces)
        save_image(image_with_faces,output_path)
        logging.info('face detection completed successfully')
        
    except Exception as e:
        logging.error(f"an error occurred:{e}")
        
if __name__=="__main__":
    image_path=r"C:\Users\pc\Downloads\WhatsApp Image 2024-06-25 at 13.38.28_5676017e.jpg"
    classifier_path=cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
    output_path=r"C:\Users\pc\Downloads\WhatsApp Image 2024-06-25 at 13.38.28_5676017e.jpg"
    main(image_path,classifier_path,output_path)
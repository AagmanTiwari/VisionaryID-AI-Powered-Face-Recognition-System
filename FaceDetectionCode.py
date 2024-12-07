import cv2
import os
import numpy as np
import time

def load_reference_images(folder_path):
    """Load reference face images and extract features."""
    face_data = []
    face_names = []
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

    for file_name in os.listdir(folder_path):
        image_path = os.path.join(folder_path, file_name)
        if not file_name.lower().endswith(('.png', '.jpg', '.jpeg')):
            continue
        
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        faces = face_cascade.detectMultiScale(image, scaleFactor=1.1, minNeighbors=5)
        
        for (x, y, w, h) in faces:
            face = image[y:y+h, x:x+w]
            face_resized = cv2.resize(face, (100, 100))
            face_data.append(face_resized)
            face_names.append(file_name)  # Store the name of the image
    return face_data, face_names

def capture_image():
    """Capture an image using the webcam with a 7-second delay."""
    cap = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

    print("Getting ready to capture image in 7 seconds...")
    
    start_time = time.time()
    
    while True:
        # Wait for 7 seconds and continuously show the webcam feed
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture image. Exiting...")
            cap.release()
            return None

        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5)

        # Show the frame with detected faces for feedback
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        cv2.imshow("Capturing Image - Camera Open (7 seconds)", frame)

        # Check if 7 seconds have passed
        if time.time() - start_time > 7:
            break

        # Wait for a moment before continuing the loop
        cv2.waitKey(1)

    cap.release()
    cv2.destroyAllWindows()

    # If faces are detected, return the first one
    if len(faces) > 0:
        x, y, w, h = faces[0]
        face = gray_frame[y:y+h, x:x+w]
        return cv2.resize(face, (100, 100))  # Resize to standard size
    else:
        print("No face detected in the image.")
        return None

def match_faces(captured_face, reference_faces, reference_names):
    """Match captured face with reference faces and return the image name."""
    if captured_face is None:
        return None

    for ref_face, ref_name in zip(reference_faces, reference_names):
        diff = cv2.norm(captured_face, ref_face, cv2.NORM_L2)
        print(f"Comparing with {ref_name}, diff: {diff}")  # Debug print to show comparison value
        if diff < 6000:  # Adjust this threshold based on testing
            return ref_name  # Return the name of the matched image
    return None



folder_path = "C:/Users/cyber/Desktop/MinorProject/images"  # Update with your reference images folder path
print("Loading reference images...")
reference_faces, reference_names = load_reference_images(folder_path)

print("Capturing a face in 7 seconds...")
captured_face = capture_image()

matched_image = match_faces(captured_face, reference_faces, reference_names)
if matched_image:
    print(f"Face matched with image: {matched_image}")
else:
    print("No match found.")


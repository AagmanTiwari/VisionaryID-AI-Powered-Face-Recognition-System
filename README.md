# VisionaryID – AI Powered Face Recognition System

**VisionaryID** is an AI-powered face recognition system designed to automate attendance management and improve security by using computer vision and machine learning techniques. This Python project leverages **OpenCV** and **face_recognition** to identify and authenticate individuals in real-time.

---

## **Features**

- **Real-time Face Recognition**: Captures face images from the webcam and compares them to stored reference images in the system.
- **Attendance Tracking**: Marks attendance automatically when a user’s face matches a registered profile.
- **Admin Panel**: Allows admins to upload new reference images, manage attendance logs, and generate reports.
- **Report Generation**: Supports the generation of daily, weekly, or monthly attendance reports.
- **Email Notifications** (Optional): Sends alerts regarding attendance updates.
- **Scalable Architecture**: Designed to handle a large number of users, making it suitable for schools, offices, and other large institutions.

---

## **Technologies Used**

- **Backend**: 
  - **Flask**: For web server setup and routing.
  - **Python**: For backend programming and machine learning.
  - **SQLite/MongoDB**: For storing user profiles and attendance logs.
  
- **Machine Learning & Computer Vision**: 
  - **OpenCV**: For capturing live video from the webcam and processing images.
  - **face_recognition** or **DeepFace**: For facial recognition and comparison against reference images.
  
- **Frontend**:
  - **HTML/CSS/JS**: For designing the user interface (UI).
  - **Jinja2**: For dynamic HTML rendering.
  
- **Database**: 
  - **SQLite** or **MongoDB**: To store and query attendance data.

---

## **Installation Instructions**

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/AagmanTiwari/VisionaryID-AI-Powered-Face-Recognition-System
    cd VisionaryID-AI-Powered-Face-Recognition-System
    ```

2. **Install Dependencies**:
    Ensure you have Python 3.x installed. Then install the necessary libraries using pip:
    ```bash
    pip install -r requirements.txt
    ```

3. **Set Up the Database**:
    - Initialize the database to store attendance records and user profiles.
    - Create a folder `reference_images/` and upload the images of individuals to be recognized.

4. **Run the Application**:
    Start the Flask web server:
    ```bash
    python app.py
    ```

5. **Web Application**:
    Access the system by navigating to `http://127.0.0.1:5000/` in your browser.

---

## **How It Works**

1. **Load Reference Images**: The system loads images of registered individuals from the `reference_images/` folder. These images are used for matching with the webcam-captured face.
   
2. **Capture Face from Webcam**: The user will be prompted to position themselves in front of the webcam. After a 7-second delay, the system captures their face and processes it.

3. **Face Detection and Comparison**: The system uses **OpenCV** to detect faces in the live video stream and compares the detected faces with the reference images using **face_recognition** or **DeepFace**.

4. **Attendance Marking**: If a match is found, the system marks the user as present and logs the attendance in the database.

5. **Admin Panel**: Admins can view attendance logs, add new faces, and generate reports using the web-based interface.

---

## **Requirements**

- **Python 3.x**
- **OpenCV**: For capturing video and processing images.
- **NumPy**: For handling numerical operations.
- **Flask**: For building the web application.
- **face_recognition/DeepFace**: For face detection and recognition.
- **SQLite/MongoDB**: For storing attendance data.

Make sure your webcam is connected and accessible by the system.

---

## **Optional Features**

- **Email Notifications**: Integrate email functionality to notify users when their attendance is recorded or when new faces are added to the system.
  
- **Cloud Deployment**: The application can be deployed on cloud platforms such as **Heroku** or **AWS** for remote access and scalability.

---

## **Future Enhancements**

- **Liveness Detection**: Improve the system's security by adding liveness detection to ensure that the system doesn't misidentify a face from a photo or video.
- **User Authentication**: Implement a login system for admins to control access to the system.
- **Multi-user Support**: Handle larger datasets of users and make the system more robust for scaling.

---

## **Contact**

For any questions or suggestions, feel free to reach out:
- **Email**: tiwariaagman1705@gmail.com
- **GitHub**: [AagmanTiwari](https://github.com/AagmanTiwari)

---

This **VisionaryID – AI Powered Face Recognition System** is a simple yet powerful solution for automating attendance and improving security through AI and computer vision.

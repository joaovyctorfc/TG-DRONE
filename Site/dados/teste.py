
# Load the YOLOv8 model
model = YOLO("yolov8n.pt")

# Open the video file
video_path = r"C:\Users\Cliente\Music\GitHub\TG-DRONE\cars-new.mp4"
cap = cv2.VideoCapture(video_path)

# Get the video properties
fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Change codec as necessary
output_path = "result.mp4"
out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

def generate_frames():
    while cap.isOpened():
        # Read a frame from the video
        success, frame = cap.read()

        if success:
            # Run YOLOv8 inference on the frame
            results = model(frame)

            # Visualize the results on the frame
            annotated_frame = results[0].plot()

            # Write the annotated frame to the output video
            out.write(annotated_frame)

            # Convert the frame to JPEG
            ret, buffer = cv2.imencode('.jpg', annotated_frame)
            frame = buffer.tobytes()

            # Yield the frame in byte format
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
        else:
            # Break the loop if the end of the video is reached
            break

@app.route('/ia')
def index():
    return render_template('analiseVideo.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')
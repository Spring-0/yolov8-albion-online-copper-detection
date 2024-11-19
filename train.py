import ultralytics
import roboflow
import subprocess
from dotenv import load_dotenv
import os

def main():
    load_dotenv()
    ultralytics.checks()

    rf = roboflow.Roboflow(api_key=os.getenv("RF_API_KEY"))
    
    # Roboflow project link: https://universe.roboflow.com/tinker-abus7/albion-copper-recognition/dataset/2
    project = rf.workspace("tinker-abus7").project("albion-copper-recognition")
    version = project.version(2)
    dataset = version.download("yolov8")

    model = ultralytics.YOLO("yolov8s.pt")
    
    # May need to adjust Ultralytics\settings.json dataset download directory on your system.
    model.train(
        data=dataset.location,
        epochs=25,
        imgsz=640,
        plots=True
    )
    
    # Save the model locally
    model.save(os.path.join("model", "best-ao.pt"))
    
    
if __name__ == "__main__":
    main()
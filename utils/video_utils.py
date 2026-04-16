import cv2
import numpy as np

def annotate_frame(frame, text):
    """
    Draws mock bounding boxes and text on the frame.
    """
    height, width, _ = frame.shape
    
    # Draw a simulated tracking bounding box
    start_point = (int(width*0.2), int(height*0.2))
    end_point = (int(width*0.8), int(height*0.8))
    color = (0, 255, 0) # Green
    thickness = 2
    cv2.rectangle(frame, start_point, end_point, color, thickness)
    
    # Add text on frame
    cv2.putText(frame, f"Sign: {text}", (int(width*0.2), int(height*0.15)), 
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
                
    return frame

#!/usr/bin/env python3
import mss
import cv2
import numpy as np
import time
from datetime import datetime

def fixed_region_recorder():
    """
    Record a fixed region - modify these coordinates for your setup
    """
    # MODIFY THESE COORDINATES FOR YOUR SCREEN
    REGION = {
        "left": 500,    # Distance from left edge
        "top": 200,     # Distance from top edge  
        "width": 900,   # Width of recording area
        "height": 700   # Height of recording area
    }
    
    print("🎯 FIXED REGION RECORDER")
    print(f"Recording area: {REGION['width']}x{REGION['height']} at ({REGION['left']}, {REGION['top']})")
    print("💡 TIP: Position Google Chat window in this area before recording")
    
    filename = f"google_chat_fixed_{datetime.now().strftime('%Y%m%d_%H%M%S')}.mp4"
    
    input("Press Enter when Google Chat is positioned correctly...")
    
    with mss.mss() as sct:
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(filename, fourcc, 15.0, (REGION["width"], REGION["height"]))
        
        print("🔴 Recording fixed region... Press Ctrl+C to stop")
        
        try:
            while True:
                screenshot = sct.grab(REGION)
                frame = np.array(screenshot)
                frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)
                out.write(frame)
                time.sleep(1.0/15)
                
        except KeyboardInterrupt:
            print("\n🛑 Recording stopped")
        
        finally:
            out.release()
            print(f"✅ Saved: {filename}")

if __name__ == "__main__":
    fixed_region_recorder()
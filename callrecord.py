import mss
import cv2
import numpy as np
from datetime import datetime
import time
import os

def record_google_chat_mxlinux(output_filename=None, duration_minutes=60, fps=15):
    """
    Optimized screen recorder for MX Linux - Google Chat video calls
    """
    # Create recordings directory if it doesn't exist
    if not os.path.exists('recordings'):
        os.makedirs('recordings')
    
    if output_filename is None:
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        output_filename = f'recordings/google_chat_{timestamp}.mp4'
    
    with mss.mss() as sct:
        # Get all monitors
        monitors = sct.monitors
        if len(monitors) > 1:
            print("Multiple monitors detected:")
            for i, monitor in enumerate(monitors):
                print(f"  {i}: {monitor['width']}x{monitor['height']}")
            monitor_choice = input("Select monitor (0 for primary, 1+ for secondary): ").strip()
            try:
                monitor = monitors[int(monitor_choice)]
            except:
                monitor = monitors[1]  # Primary monitor
        else:
            monitor = monitors[1]  # Primary monitor
        
        print(f"Recording area: {monitor['width']}x{monitor['height']}")
        
        # Use MP4V codec for better compatibility
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(output_filename, fourcc, fps, 
                             (monitor["width"], monitor["height"]))
        
        print(f"🎥 Recording started at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"📁 File: {output_filename}")
        print("⏰ Duration: {} minutes".format(duration_minutes))
        print("🛑 Press Ctrl+C to stop recording early")
        print("-" * 50)
        
        start_time = time.time()
        max_duration = duration_minutes * 60
        frame_count = 0
        
        try:
            while (time.time() - start_time) < max_duration:
                # Capture screen
                screenshot = sct.grab(monitor)
                frame = np.array(screenshot)
                
                # Convert BGRA to BGR for OpenCV
                frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)
                
                # Write frame
                out.write(frame)
                frame_count += 1
                
                # Show recording status (small preview)
                if frame_count % 100 == 0:  # Update status every 100 frames
                    elapsed = time.time() - start_time
                    remaining = max_duration - elapsed
                    print(f"⏱️  Recording: {int(elapsed)}s elapsed, {int(remaining)}s remaining", end='\r')
                
                # Small delay to maintain frame rate
                time.sleep(1.0/fps)
                    
        except KeyboardInterrupt:
            print("\n\n🛑 Recording stopped by user")
        
        finally:
            out.release()
            file_size = os.path.getsize(output_filename) / (1024*1024)  # Size in MB
            print(f"✅ Recording completed!")
            print(f"📊 Stats: {frame_count} frames, {file_size:.1f} MB")
            print(f"💾 Saved as: {output_filename}")

def quick_record():
    """Simple one-click recording setup"""
    print("🚀 MX Linux Google Chat Recorder")
    print("=" * 40)
    
    try:
        duration = int(input("Recording duration in minutes (default 30): ") or "30")
    except:
        duration = 30
    
    try:
        fps = int(input("Frame rate (default 15): ") or "15")
    except:
        fps = 15
    
    record_google_chat_mxlinux(duration_minutes=duration, fps=fps)

if __name__ == "__main__":
    quick_record()
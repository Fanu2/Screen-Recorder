#!/usr/bin/env python3
import mss
import cv2
import numpy as np
import time
from datetime import datetime
import os
import subprocess
import sys

try:
    import pyautogui
except ImportError:
    print("Installing pyautogui for region selection...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pyautogui"])
    import pyautogui

def select_region_interactive():
    """
    Interactive region selection - click and drag to select Google Chat area
    """
    print("🎯 REGION SELECTION MODE")
    print("=" * 50)
    print("We'll help you select ONLY the Google Chat window")
    print()
    print("INSTRUCTIONS:")
    print("1. Make sure Google Chat is visible on screen")
    print("2. Click and drag to select the exact area you want to record")
    print("3. Release mouse to confirm selection")
    print("=" * 50)
    
    input("Press Enter to start region selection...")
    
    try:
        # PyAutoGUI's region selection tool
        print("⬜ Click and drag to select the Google Chat window area...")
        region = pyautogui.locateOnScreen('dummy')  # This is just to trigger the selection UI
        
        # Use a workaround since locateOnScreen doesn't work without an image
        print("🔍 Taking a screenshot to help with selection...")
        screenshot = pyautogui.screenshot()
        screenshot.save('temp_screen.png')
        
        print("📐 Manual coordinate input (easier method):")
        print("Move your mouse to the TOP-LEFT corner of Google Chat and press Enter")
        input("Ready for top-left...")
        top_left = pyautogui.position()
        print(f"📍 Top-left: {top_left}")
        
        print("Move your mouse to the BOTTOM-RIGHT corner and press Enter")
        input("Ready for bottom-right...")
        bottom_right = pyautogui.position()
        print(f"📍 Bottom-right: {bottom_right}")
        
        # Calculate region
        left = min(top_left[0], bottom_right[0])
        top = min(top_left[1], bottom_right[1])
        width = abs(bottom_right[0] - top_left[0])
        height = abs(bottom_right[1] - top_left[1])
        
        # Show preview
        preview = pyautogui.screenshot(region=(left, top, width, height))
        preview.save('region_preview.png')
        
        print(f"📏 Selected region: {width}x{height} pixels at ({left}, {top})")
        print("👀 Preview saved as 'region_preview.png' - check if it looks correct")
        
        confirm = input("Record this area? (y/n): ").lower().strip()
        if confirm == 'y':
            return {"left": left, "top": top, "width": width, "height": height}
        else:
            print("Selection cancelled.")
            return None
            
    except Exception as e:
        print(f"Error during region selection: {e}")
        return manual_region_input()

def manual_region_input():
    """
    Manual coordinate input as fallback
    """
    print("📝 Manual Region Input")
    print("Example values for 1280x720 window:")
    print("Left: 100, Top: 100, Width: 1280, Height: 720")
    
    try:
        left = int(input("Left coordinate: ") or "100")
        top = int(input("Top coordinate: ") or "100")
        width = int(input("Width: ") or "1280")
        height = int(input("Height: ") or "720")
        
        return {"left": left, "top": top, "width": width, "height": height}
    except ValueError:
        print("Invalid input. Using default region.")
        return {"left": 100, "top": 100, "width": 1280, "height": 720}

def record_region(region):
    """
    Record only the selected region
    """
    if not region:
        print("No region selected. Exiting.")
        return
    
    filename = f"chat_region_{datetime.now().strftime('%Y%m%d_%H%M%S')}.mp4"
    
    print(f"🎥 Recording region: {region['width']}x{region['height']} at ({region['left']}, {region['top']})")
    print(f"💾 Output: {filename}")
    print("🔴 Recording... Press Ctrl+C to stop")
    
    with mss.mss() as sct:
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(filename, fourcc, 15.0, (region["width"], region["height"]))
        
        try:
            frame_count = 0
            start_time = time.time()
            
            while True:
                # Capture only the selected region
                screenshot = sct.grab(region)
                frame = np.array(screenshot)
                frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)
                out.write(frame)
                
                frame_count += 1
                elapsed = time.time() - start_time
                
                # Show progress every 30 frames
                if frame_count % 30 == 0:
                    print(f"⏱️  Recording: {int(elapsed)}s | Frames: {frame_count}", end='\r')
                
                time.sleep(1.0/15)  # 15 FPS
                
        except KeyboardInterrupt:
            print("\n🛑 Recording stopped by user")
        
        finally:
            out.release()
            file_size = os.path.getsize(filename) / (1024*1024)  # MB
            print(f"✅ Recording saved: {filename} ({file_size:.1f} MB)")

def auto_detect_chat_window():
    """
    Try to automatically find Google Chat window (basic detection)
    """
    print("🔍 Attempting to auto-detect Google Chat window...")
    
    # Get all windows (requires wmctrl)
    try:
        result = subprocess.run(['wmctrl', '-l'], capture_output=True, text=True)
        windows = result.stdout.split('\n')
        
        chat_windows = [w for w in windows if 'google chat' in w.lower() or 'meet' in w.lower() or 'chrome' in w.lower()]
        
        if chat_windows:
            print("Possible Google Chat windows found:")
            for i, window in enumerate(chat_windows[:3]):  # Show first 3
                print(f"  {i}: {window}")
            
            # For now, use a reasonable default region
            screen_width, screen_height = pyautogui.size()
            region = {
                "left": int(screen_width * 0.1),
                "top": int(screen_height * 0.1),
                "width": int(screen_width * 0.8),
                "height": int(screen_height * 0.7)
            }
            print(f"📐 Using centered region: {region['width']}x{region['height']}")
            return region
        else:
            print("❌ Could not auto-detect Google Chat window")
            return None
            
    except FileNotFoundError:
        print("❌ wmctrl not available for auto-detection")
        return None

def main():
    """
    Main function with region selection options
    """
    print("🎯 GOOGLE CHAT REGION-SPECIFIC RECORDER")
    print("=" * 50)
    print("Choose selection method:")
    print("1. 🖱️  Interactive region selection (click and drag)")
    print("2. 📝 Manual coordinate input")
    print("3. 🔍 Auto-detect window (experimental)")
    print("4. ❌ Exit")
    
    choice = input("Enter choice (1-4): ").strip()
    
    if choice == "1":
        region = select_region_interactive()
    elif choice == "2":
        region = manual_region_input()
    elif choice == "3":
        region = auto_detect_chat_window()
        if not region:
            print("Falling back to manual selection...")
            region = manual_region_input()
    elif choice == "4":
        print("Exiting.")
        return
    else:
        print("Invalid choice. Using interactive selection.")
        region = select_region_interactive()
    
    if region:
        record_region(region)
    else:
        print("No region selected. Exiting.")

if __name__ == "__main__":
    main()
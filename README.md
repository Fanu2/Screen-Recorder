Screen Recorder 🎥

A collection of Python scripts for recording screen record  video calls on Linux systems, with a focus on privacy and security.
⚠️ Important Legal & Ethical Notice

BEFORE USING THESE SCRIPTS:

    🚨 Always inform all participants that you are recording the call

    📜 Check local laws - recording without consent may be illegal in your region

    🏢 Review company policies regarding meeting recordings

    🔒 Respect privacy - only record when necessary and appropriate

📋 Features

    🎯 Region-specific recording - Capture only the Google Chat window

    🖥️ Full-screen recording - Record entire screen when needed

    🔒 Privacy-focused - Safety checklists and warnings

    🐧 Linux-optimized - Specifically tested on MX Linux and Debian-based systems

    📹 Multiple formats - MP4 and AVI output support

    ⚡ Performance optimized - Adjustable frame rates and quality

📁 File Structure
text

google-chat-recorder/
│
├── 📄 README.md (this file)
├── 🔧 requirements.txt
├── 🚀 install.sh
│
├── 🎯 region_recorder.py (RECOMMENDED - Records specific area only)
├── 🖥️ fullscreen_recorder.py (Records entire screen)
├── 🛡️ safe_recorder.py (With safety checklist)
├── 🔍 find_coordinates.py (Helper to find screen coordinates)
│
├── 📁 examples/
│   ├── basic_recorder.py
│   └── advanced_recorder.py
└── 📁 utils/
    ├── safety_checklist.py
    └── video_utils.py

🛠️ Installation
Method 1: Quick Install (Recommended)
bash

# Clone the repository
git clone https://github.com/yourusername/google-chat-recorder.git
cd google-chat-recorder

# Run the installation script
chmod +x install.sh
./install.sh

Method 2: Manual Installation
bash

# Create virtual environment
python3 -m venv recorder_env
source recorder_env/bin/activate

# Install dependencies
pip install -r requirements.txt

# Install system dependencies (MX Linux/Debian)
sudo apt update
sudo apt install python3-pip python3-opencv python3-numpy ffmpeg wmctrl

🚀 Usage
🎯 Recommended: Region-Specific Recording

Records ONLY the Google Chat window, protecting your privacy:
bash

python3 region_recorder.py

Features:

    Interactive region selection

    Click-and-drag or manual coordinate input

    Preview before recording

    Auto-detection of window positions

🖥️ Full Screen Recording

Records everything on your screen (use with caution):
bash

python3 fullscreen_recorder.py

🛡️ Safe Recording (With Checklist)

Includes privacy checklist before recording:
bash

python3 safe_recorder.py

🔍 Find Screen Coordinates

Helper tool to find window coordinates:
bash

python3 find_coordinates.py

📝 Script Details
region_recorder.py 🎯 (RECOMMENDED)

    Purpose: Record only specific screen regions

    Best for: Privacy-conscious users

    Output: MP4 format

    Features: Interactive selection, preview, auto-detection

fullscreen_recorder.py 🖥️

    Purpose: Record entire screen

    Best for: When you need to capture multiple windows

    Output: MP4/AVI format

    Features: Monitor selection, performance optimization

safe_recorder.py 🛡️

    Purpose: Recording with privacy safeguards

    Best for: Legal compliance and ethical use

    Features: Safety checklist, participant confirmation

find_coordinates.py 🔍

    Purpose: Find screen coordinates for window positioning

    Usage: Run and move mouse to see coordinates

⚙️ Configuration
Virtual Environment

Always activate the virtual environment first:
bash

source recorder_env/bin/activate

Customizing Recording Settings

Edit these parameters in the scripts:

    fps: Frames per second (10-30 recommended)

    output_format: MP4 or AVI

    quality: Compression level

    region: Screen coordinates for fixed recording

🐧 MX Linux Specific Notes

This software is specifically tested and optimized for MX Linux:
Dependencies
bash

# MX Linux specific packages
sudo apt install python3-full python3-venv python3-pip
sudo apt install ffmpeg libopencv-dev python3-opencv

Known Issues & Solutions

    Externally-managed-environment: Use virtual environments as shown above

    Performance: Lower FPS (10-15) for better performance on older hardware

    Permissions: Ensure access to screen recording capabilities

🔧 Troubleshooting
Common Issues

    "Externally-managed-environment" error
    bash

# Solution: Use virtual environment
python3 -m venv myenv
source myenv/bin/activate
pip install -r requirements.txt

"Cannot capture screen" error
bash

# Solution: Install missing dependencies
sudo apt install python3-tk python3-dev

    Poor performance

        Lower FPS to 10-15

        Close unnecessary applications

        Use region recording instead of full screen

    Large file sizes

        Use MP4 format instead of AVI

        Lower FPS and quality settings

        Use region-specific recording

Performance Tips

    🔧 Use region recording instead of full screen

    📉 Lower FPS to 10-15 for video calls

    💾 Record to SSD if possible

    🚫 Close unnecessary applications during recording

📊 Output Files

    Format: MP4 (recommended) or AVI

    Naming: chat_region_YYYYMMDD_HHMMSS.mp4

    Location: Current directory or recordings/ folder

    Size: ~50-200MB per hour (depending on settings)

🤝 Contributing

We welcome contributions! Please:

    Fork the repository

    Create a feature branch

    Make your changes

    Test thoroughly

    Submit a pull request

Development Setup
bash

git clone https://github.com/yourusername/google-chat-recorder.git
cd google-chat-recorder
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

📄 License

This project is licensed under the MIT License - see the LICENSE file for details.
🆘 Support

If you encounter issues:

    Check the troubleshooting section above

    Search existing GitHub issues

    Create a new issue with:

        Your MX Linux version

        Python version

        Error messages

        Steps to reproduce

🙏 Acknowledgments

    Built for MX Linux community

    Uses OpenCV, MSS, and PyAutoGUI libraries

    Thanks to all contributors and testers

Remember: Always respect privacy laws and obtain consent before recording any video calls! 🔒

Last updated: $(date +%Y-%m-%d)

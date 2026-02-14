# Edge AI Intruder Detection 👁️

A high-performance security node that combines hardware-triggered motion sensing with AI-driven image capture to identify threats at the edge.

## Description
A high-performance security node combining hardware-triggered motion sensing with AI-driven image capture to identify and log threats at the edge.

## Key Features
- **AI Motion Trigger:** Dual-stage verification using PIR hardware and pixel-difference analysis.
- **Visual Evidence:** Captures and streams SVGA resolution frames upon breach detection.
- **Intrusion Analytics:** Python-based dashboard tracks entry vectors and threat levels.

## Tech Stack
- **Language:** Python, C++
- **Libraries:** OpenCV, Streamlit, Pillow, esp_camera
- **Model:** Pixel-differential motion analysis and buffer management

## Engineering Logic
- **Hardware:** The ESP32-S3 uses a PIR sensor as a hardware interrupt to wake the CPU from deep sleep for image capture.
- **Software:** Python handles the incoming Base64 stream, performs normalization, and updates a localized database for audit tracking.

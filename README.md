👁️ Edge-AI Intruder Detection System
A high-performance security node that combines PIR motion sensing with AI-driven image capture. This system is designed for "Edge" deployment, where initial threat detection happens on the device before alerting the central dashboard.

🚀 Features
AI Motion Trigger: Dual-stage verification using PIR hardware and pixel-difference analysis.

Visual Evidence: Captures and streams SVGA resolution frames upon breach detection.

Intrusion Analytics: Python-based dashboard tracks entry vectors and threat levels.

Low Power Mode: Device remains in deep sleep until the PIR sensor wakes the CPU.

⚙️ Engineering Logic
Hardware: The ESP32-S3 manages the OV2640 camera module. It uses 8MB of PSRAM to buffer high-resolution images.

Software: The Python dashboard acts as a central monitoring station, receiving base64 encoded image data and timestamping every "Incursion Event."

import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image, ImageDraw
import plotly.graph_objects as go
from datetime import datetime
import time
import io
import random

# 1. Page & Theme Configuration (100+ Lines)
st.set_page_config(page_title="Guardian AI Dashboard", layout="wide", page_icon="👁️")

st.markdown("""
    <style>
    .main { background-color: #0d1117; color: #c9d1d9; }
    .stMetric { background-color: #161b22; border: 1px solid #30363d; padding: 15px; border-radius: 8px; }
    </style>
    """, unsafe_allow_html=True)

# 2. Global State Initialization
if 'alert_history' not in st.session_state:
    st.session_state.alert_history = pd.DataFrame(columns=['Timestamp', 'Zone', 'Threat_Level', 'Status'])
if 'frame_count' not in st.session_state:
    st.session_state.frame_count = 0

# 3. Sidebar Surveillance Controls
st.sidebar.title("🛡️ Surveillance HQ")
detection_sensitivity = st.sidebar.slider("AI Sensitivity", 1, 100, 85)
is_armed = st.sidebar.toggle("Arm System", value=True)
if st.sidebar.button("Wipe Alert Logs"):
    st.session_state.alert_history = pd.DataFrame(columns=['Timestamp', 'Zone', 'Threat_Level', 'Status'])

# 4. Main Dashboard Header
st.title("👁️ Guardian Edge-AI Surveillance")
st.write(f"System Node: ESP32-S3-Sense | Status: {'🟢 ACTIVE' if is_armed else '🔴 STANDBY'}")

# 5. Live Feed and Alert Simulation Logic
col_feed, col_stats = st.columns([2, 1])

with col_feed:
    st.subheader("Live Secure Stream")
    
    # Generate a Simulated Camera Frame
    img = Image.new('RGB', (800, 480), color=(20, 20, 25))
    draw = ImageDraw.Draw(img)
    
    # Simulate an intrusion detection
    if np.random.rand() > 0.9 and is_armed:
        draw.rectangle([150, 80, 450, 400], outline="red", width=4)
        draw.text((155, 60), "INTRUDER DETECTED (CONF: 94%)", fill="red")
        
        # Log the incident
        new_row = pd.DataFrame([[
            datetime.now().strftime("%H:%M:%S"), 
            "Sector A-9", 
            "CRITICAL", 
            "UNRESOLVED"
        ]], columns=st.session_state.alert_history.columns)
        
        st.session_state.alert_history = pd.concat([new_row, st.session_state.alert_history]).head(15)
        st.session_state.frame_count += 1
    
    st.image(img, use_container_width=True, caption="Surveillance Node 01 | SVGA Frame")

with col_stats:
    st.subheader("Node Telemetry")
    m1, m2 = st.columns(2)
    m1.metric("Total Breaches", st.session_state.frame_count)
    m2.metric("FPS", "15.4")
    
    # Visualizing Threat Distribution
    if not st.session_state.alert_history.empty:
        fig = go.Figure(data=[go.Pie(
            labels=st.session_state.alert_history['Threat_Level'].value_counts().index,
            values=st.session_state.alert_history['Threat_Level'].value_counts().values,
            hole=.3,
            marker_colors=['#ff4b4b', '#ffa500']
        )])
        fig.update_layout(height=300, paper_bgcolor='rgba(0,0,0,0)', font_color="white")
        st.plotly_chart(fig, use_container_width=True)

# 6. Safety Audit Trail Table
st.divider()
st.subheader("📋 Incident Audit Trail")
st.dataframe(st.session_state.alert_history, use_container_width=True)

# 7. Auto-refresh Simulation
if is_armed:
    time.sleep(1)
    st.rerun()

import streamlit as st
import plotly.graph_objects as go
import numpy as np

# --- Page Setup ---
st.set_page_config(layout="wide")
st.title("Stress Lab")

# --- Formula Display ---
# This renders the exact formula from your image on the web page
st.latex(r"\sigma_{x'} = \frac{\sigma_x + \sigma_y}{2} + \frac{\sigma_x - \sigma_y}{2} \cos(2\theta) + \tau_{xy} \sin(2\theta)")

# --- Sidebar Inputs ---
st.sidebar.header("1. Define Stress State")
s_x = st.sidebar.number_input("σx (Normal X)", value=80.0)
s_y = st.sidebar.number_input("σy (Normal Y)", value=20.0)
t_xy = st.sidebar.number_input("τxy (Shear XY)", value=40.0)

st.sidebar.header("2. Rotate Element")
theta_input = st.sidebar.slider("Rotation Angle (θ)", 0, 180, 65)

# --- Math Logic ---
theta_deg = np.linspace(0, 180, 500)
theta_rad = np.radians(theta_deg)

# The specific formula for sigma x dash
sig_x_dash = (
    (s_x + s_y) / 2 + 
    ((s_x - s_y) / 2) * np.cos(2 * theta_rad) + 
    t_xy * np.sin(2 * theta_rad)
)

# Current value at the slider angle
c_rad = np.radians(theta_input)
cur_sx = (s_x + s_y)/2 + ((s_x - s_y)/2) * np.cos(2*c_rad) + t_xy * np.sin(2*c_rad)

# --- Plotly Visualization ---
fig = go.Figure()

fig.add_trace(go.Scatter(
    x=theta_deg, 
    y=sig_x_dash, 
    name="σx'", 
    line=dict(color='#636EFA', width=4)
))

# Indicator for current angle
fig.add_vline(x=theta_input, line_dash="dash", line_color="red", opacity=0.7)
fig.add_trace(go.Scatter(
    x=[theta_input], 
    y=[cur_sx],
    mode='markers',
    marker=dict(size=10, color='red'),
    name="Current θ"
))

fig.update_layout(
    title="Normal Stress (σx') vs. Angle (θ)",
    xaxis_title="Angle θ (Degrees)",
    yaxis_title="Normal Stress (σx')",
    xaxis=dict(range=[0, 180], tickmode='linear', tick0=0, dtick=30),
    hovermode="x unified",
    template="plotly_white",
    height=500
)

st.plotly_chart(fig, use_container_width=True)

# Metric display
st.metric(f"σx' at {theta_input}°", f"{cur_sx:.2f}")
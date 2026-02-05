# Stress Transformation Explorer

An interactive web application for visualizing stress transformation in materials mechanics. Built with Streamlit and Plotly.
Fully working link :- https://normalstressvsangletransformation-3qpwylp4vgknz7ma8t2zxj.streamlit.app/

## Features

- **Interactive Controls**: Adjust stress components (σx, σy, τxy) and rotation angle in real-time
- **Live Visualization**: See how normal stress σx' varies with rotation angle θ
- **Mathematical Formula**: Displays the exact stress transformation equation
- **Current Value Indicator**: Shows the stress value at your selected angle
- **Responsive Design**: Clean, modern interface that works on different screen sizes

## The Math

The app uses the standard plane stress transformation equation:

$$\sigma_{x'} = \frac{\sigma_x + \sigma_y}{2} + \frac{\sigma_x - \sigma_y}{2} \cos(2\theta) + \tau_{xy} \sin(2\theta)$$

Where:
- σx, σy = Normal stresses in x and y directions
- τxy = Shear stress
- θ = Rotation angle
- σx' = Transformed normal stress

## Installation

1. Clone or download this repository
2. Install required packages:

```bash
pip install streamlit plotly numpy
```

## Usage

Run the application:

```bash
streamlit run main.py
```

The app will open in your browser at `http://localhost:8501`

### How to Use

1. **Set Stress State**: Use the sidebar to input:
   - σx (Normal stress in X direction)
   - σy (Normal stress in Y direction) 
   - τxy (Shear stress)

2. **Select Angle**: Use the angle slider to choose the rotation angle θ

3. **View Results**: 
   - The main plot shows σx' vs θ from 0° to 180°
   - A red indicator shows your current angle selection
   - The metric displays the exact σx' value at your selected angle

## Technical Details

- **Frontend**: Streamlit web framework
- **Visualization**: Plotly for interactive charts
- **Computation**: NumPy for numerical calculations
- **Resolution**: 500 points for smooth curve rendering

## Applications

This tool is useful for:
- Engineering education and learning
- Stress analysis in mechanical design
- Understanding material behavior under load
- Visualizing Mohr's circle concepts

## License

This project is open source and available under the MIT License.

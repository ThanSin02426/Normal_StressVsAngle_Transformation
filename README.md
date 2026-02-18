# Stress Lab: Transformation & Mohr’s Circle

An interactive Streamlit web app for visualizing **stress transformation** and **Mohr’s circle** using Plotly + NumPy.
Fully working link :- https://normalstressvsangletransformation-3qpwylp4vgknz7ma8t2zxj.streamlit.app/

## What you get

- **Stress transformation curve**
  - Plots normal stress **σx′ vs rotation angle θ**
  - Marks the current slider angle and current stress state
- **Mohr’s circle diagram**
  - Draws the full Mohr’s circle (center + radius)
  - Shows the original stress point, rotated stress point, and principal stresses
- **Formula display**
  - Shows both the normal and shear transformation equations in LaTeX

## Equations used

$$\sigma_{x'} = \frac{\sigma_x + \sigma_y}{2} + \frac{\sigma_x - \sigma_y}{2} \cos(2\theta) + \tau_{xy} \sin(2\theta)$$

$$\tau_{x'y'} = -\frac{\sigma_x - \sigma_y}{2} \sin(2\theta) + \tau_{xy} \cos(2\theta)$$

Where:

- σx, σy = normal stresses
- τxy = shear stress
- θ = rotation angle

## Setup

Install dependencies using `requirements.txt`:

```bash
pip install -r requirements.txt
```

## Run

```bash
streamlit run main.py
```

Then open the URL Streamlit prints (typically):

- `http://localhost:8501`

## How to use

1. In the sidebar, set:
   - `σx`, `σy`, `τxy`
2. Choose rotation angle `θ` (degrees)
3. Read the results:
   - Left plot: **σx′ vs θ** with a marker at your selected angle
   - Right plot: **Mohr’s circle** with the corresponding rotated point
   - Info panels summarize the current stresses and principal values

## Notes

- The UI uses a dark Plotly template (`plotly_dark`) for contrast.
- If you run multiple times, Streamlit may choose a different port; always use the URL shown in the terminal.

## License

This project is open source and available under the MIT License.

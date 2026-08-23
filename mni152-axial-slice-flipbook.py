from mni152 import data
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider

fig, (ax_img, ax_hist) = plt.subplots(1, 2, figsize=(11, 5))
plt.subplots_adjust(bottom=0.18, wspace=0.25)

z = data.shape[2] // 2

# Image
im = ax_img.imshow(np.rot90(data[:, :, z]), cmap="gray")
ax_img.set_title(f"Axial  z = {z}")
ax_img.axis("off")

# Histogram of current slice
slice_data = data[:, :, z]
brain = slice_data[slice_data > 10]

ax_hist.hist(brain.ravel(), bins=80, color="#4a6fa5", edgecolor="none")
ax_hist.set_title("Slice histogram")
ax_hist.set_xlabel("Intensity")
ax_hist.set_ylabel("Voxels")
ax_hist.set_xlim(0, data.max())

# Slider
ax_slider = plt.axes([0.2, 0.06, 0.3, 0.03])
slider = Slider(ax_slider, "Slice", 0, data.shape[2]-1, valinit=z, valstep=1)

def update(val):
    z = int(slider.val)
    
    # Update image
    im.set_data(np.rot90(data[:, :, z]))
    ax_img.set_title(f"Axial  z = {z}")
    
    # Update histogram
    ax_hist.cla()
    slice_data = data[:, :, z]
    brain = slice_data[slice_data > 10]
    ax_hist.hist(brain.ravel(), bins=80, color="#4a6fa5", edgecolor="none")
    ax_hist.set_title("Slice histogram")
    ax_hist.set_xlabel("Intensity")
    ax_hist.set_ylabel("Voxels")
    ax_hist.set_xlim(0, data.max())
    
    fig.canvas.draw_idle()

slider.on_changed(update)
plt.show()
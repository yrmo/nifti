import nibabel as nib
import matplotlib.pyplot as plt
import numpy as np

img = nib.load("./mni152.nii/mni152.nii")
data = img.get_fdata()

fig, ax = plt.subplots(figsize=(6, 6))
plt.subplots_adjust(bottom=0.15)

# Start in the middle
z = data.shape[2] // 2
im = ax.imshow(np.rot90(data[:, :, z]), cmap="gray")
ax.set_title(f"Axial slice {z}")
ax.axis("off")

from matplotlib.widgets import Slider

ax_slider = plt.axes([0.2, 0.05, 0.6, 0.03])
slider = Slider(ax_slider, "Slice", 0, data.shape[2]-1, valinit=z, valstep=1)

def update(val):
    z = int(slider.val)
    im.set_data(np.rot90(data[:, :, z]))
    ax.set_title(f"Axial slice {z}")
    fig.canvas.draw_idle()

slider.on_changed(update)
plt.show()

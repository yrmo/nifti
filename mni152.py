import nibabel as nib
import numpy as np
import matplotlib.pyplot as plt

img = nib.load("./mni152.nii/mni152.nii")
data = img.get_fdata()

x_mid = data.shape[0] // 2
y_mid = data.shape[1] // 2
z_mid = data.shape[2] // 2

fig, axes = plt.subplots(1, 3, figsize=(15, 5))

axes[0].imshow(np.rot90(data[:, :, z_mid]), cmap="gray")
axes[0].set_title("Axial (from above)")
axes[0].axis("off")

axes[1].imshow(np.rot90(data[:, y_mid, :]), cmap="gray")
axes[1].set_title("Coronal (from front)")
axes[1].axis("off")

axes[2].imshow(np.rot90(data[x_mid, :, :]), cmap="gray")
axes[2].set_title("Sagittal (from side)")
axes[2].axis("off")

plt.suptitle("MNI152", fontsize=14)
plt.savefig("MNI152.jpg")
plt.tight_layout()
plt.show()
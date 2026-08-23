import nibabel as nib

# https://niivue.github.io/niivue-demo-images/mni152.nii.gz
data = nib.load("./mni152.nii/mni152.nii").get_fdata()

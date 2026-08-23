import nibabel as nib


def load(path):
    return nib.load(path).get_fdata()


# https://niivue.github.io/niivue-demo-images/mni152.nii.gz
data = load("./mni152.nii/mni152.nii")
# data = load("./minimal.nii/minimal.nii")
# data = load("./avg152T1_RL_nifti.nii/avg152T1_RL_nifti.nii")

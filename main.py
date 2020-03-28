##
# https://bispl.weebly.com/bispl-news/deep-learning-reconstruction-from-9-view-dual-energy-ct-for-baggage-inspection

##
# pip install numpy
import numpy as np

# pip install matplotlib
import matplotlib.pyplot as plt

# pip install mayavi
from tvtk.api import tvtk, write_data

##
sz = (68, 256, 256)
header = 28

name_data = "Skull.vol"

fid = open(name_data, 'rb')
data = np.fromfile(fid, dtype=np.uint8)
data = data[header:]

data = np.reshape(data, sz)
data = np.flip(data, axis=0)

spacing = (4, 1, 1)
origin = (0, 0, 0)

vtk_data = tvtk.ImageData(spacing=spacing, origin=origin, dimensions=sz)
vtk_data.point_data.scalars = data.ravel(order='F')
vtk_data.point_data.scalars.name = "Skull_python"

write_data(vtk_data, 'Skull_python.vtk')

##
plt.subplot(131)
plt.imshow(data[34, :, :].squeeze(), cmap="gray")
plt.title("XY-axis")

plt.subplot(132)
plt.imshow(data[:, 128, :].squeeze(), cmap="gray")
plt.title("XZ-axis")

plt.subplot(133)
plt.imshow(data[:, :, 128].squeeze(), cmap="gray")
plt.title("YZ-axis")

plt.show()

##
sz = (384, 256, 256)
header = 0

name_data = "fbp_256_256_384.raw"

fid = open(name_data, 'rb')
data = np.fromfile(fid, dtype=np.float32)
data = data[header:]

data = np.reshape(data, sz)
# data = np.flip(data, axis=0)

spacing = (1, 1, 1)
origin = (0, 0, 0)

vtk_data = tvtk.ImageData(spacing=spacing, origin=origin, dimensions=sz)
vtk_data.point_data.scalars = data.ravel(order='F')
vtk_data.point_data.scalars.name = "fbp_python"

write_data(vtk_data, 'fbp_python.vtk')

##
plt.subplot(131)
plt.imshow(data[sz[0]//2, :, :].squeeze(), cmap="gray")
plt.title("XY-axis")

plt.subplot(132)
plt.imshow(data[:, sz[2]//2, :].squeeze(), cmap="gray")
plt.title("XZ-axis")

plt.subplot(133)
plt.imshow(data[:, :, sz[2]//2].squeeze(), cmap="gray")
plt.title("YZ-axis")

plt.show()


##
sz = (384, 256, 256)
header = 0

name_data = "proposed_256_256_384.raw"

fid = open(name_data, 'rb')
data = np.fromfile(fid, dtype=np.float32)
data = data[header:]

data = np.reshape(data, sz)
# data = np.flip(data, axis=0)

spacing = (1, 1, 1)
origin = (0, 0, 0)

vtk_data = tvtk.ImageData(spacing=spacing, origin=origin, dimensions=sz)
vtk_data.point_data.scalars = data.ravel(order='F')
vtk_data.point_data.scalars.name = "proposed_python"

write_data(vtk_data, 'proposed_python.vtk')

##
plt.subplot(131)
plt.imshow(data[sz[0]//2, :, :].squeeze(), cmap="gray")
plt.title("XY-axis")

plt.subplot(132)
plt.imshow(data[:, sz[2]//2, :].squeeze(), cmap="gray")
plt.title("XZ-axis")

plt.subplot(133)
plt.imshow(data[:, :, sz[2]//2].squeeze(), cmap="gray")
plt.title("YZ-axis")

plt.show()
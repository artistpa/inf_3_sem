from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

img = Image.open('lunar03_raw.jpg')
data = np.array(img)

#updated_data = np.empty((len(data), len(data[0])))

m = data.min()
M = data.max()
updated_data = ((data - m) / (M - m)) * 255

res_img = Image.fromarray(updated_data)
fig, ax = plt.subplots()
ax.imshow(res_img)
ax.set_title('После обработки')
plt.show()
#res_img.save("1.jpg")
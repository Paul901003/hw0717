import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

images = []
gray_images = []
max_values = []
min_values = []
mean_values = []
std_values = []

# Set random seed for reproducibility
np.random.seed(0)

# Generate 10 random color images
for i in range(10):
    new_image = np.random.randint(0, 256, size = (64, 64, 3), dtype = np.uint8)
    images.append(new_image)

    # Convert to grayscale
    new_gray_image = np.mean(new_image, axis = 2).astype(np.uint8)
    gray_images.append(new_gray_image)
    max_values.append(np.max(new_gray_image, axis = (0, 1)))
    min_values.append(np.min(new_gray_image, axis = (0, 1)))
    mean_values.append(np.mean(new_gray_image, axis = (0, 1)))
    std_values.append(np.std(new_gray_image, axis = (0, 1)))

# 寫成字典型態，後面可以是 list 或 numpy array
d = {'max': max_values, 
     'min': min_values,
     'mean': mean_values,
     'std': std_values
    }

# 以字典型態寫入xlsl檔案
df = pd.DataFrame(data = d)
print(df)
df.to_excel(f'test.xlsx')

# # Create a subplot with 10 rows and 2 columns
# fig, axes = plt.subplots(2, 10, figsize=(12, 20))

# for i in range(10):
#     axes[0, i].imshow(gray_images[i], cmap='gray')
#     axes[0, i].set_title('Gray Image ' + str(i+1))
#     axes[0, i].axis('off')  # Hide axes ticks

#     axes[1, i].imshow(images[i])
#     axes[1, i].set_title('Color Image ' + str(i+1))
#     axes[1, i].axis('off')  # Hide axes ticks

# plt.tight_layout()
# plt.show()

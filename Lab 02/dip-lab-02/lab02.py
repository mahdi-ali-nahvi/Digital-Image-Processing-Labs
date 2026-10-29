import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
 
IMAGE_PATH = "Butterfly.jpg"
image = cv.imread(IMAGE_PATH)                      # OpenCV loads in BGR order
# if image is None:
#     raise FileNotFoundError(f"Image not found or unreadable: {IMAGE_PATH}")
# print("Image shape (H, W, C):", image.shape)
# print("Image data type      :", image.dtype)

height, width, channels = image.shape
# print("Height (rows)        :", height)
# print("Width (columns)      :", width)
# print("Number of channels   :", channels)
 
center_row, center_col = height // 2, width // 2
# print("Top-left pixel [0, 0] (B, G, R)          :", image[0, 0])
# print(f"Center pixel [{center_row}, {center_col}] (B, G, R)      :", image[center_row, center_col])
 
# print("Global minimum value :", image.min())
# print("Global maximum value :", image.max())
# for i, name in enumerate(["Blue", "Green", "Red"]):          # BGR order
#     print(f"{name:5s} channel -> min: {image[:, :, i].min():3d}, max: {image[:, :, i].max():3d}")

rgb = cv.cvtColor(image, cv.COLOR_BGR2RGB)
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
red, green, blue = rgb[:, :, 0], rgb[:, :, 1], rgb[:, :, 2]
# print("RGB shape:", rgb.shape, "| Grayscale shape:", gray.shape)
 
fig, axes = plt.subplots(2, 3, figsize=(15, 8))
panels = [(rgb, "RGB (correct colours)", None),
          (red, "Red channel", "gray"),
          (green, "Green channel", "gray"),
          (blue, "Blue channel", "gray"),
          (gray, "Grayscale", "gray"),
          (image, "BGR shown without conversion", None)]
for ax, (img, title, cmap) in zip(axes.ravel(), panels):
    ax.imshow(img, cmap=cmap)
    ax.set_title(title)
    ax.axis("off")
# plt.tight_layout()
# plt.savefig("channels_figure.png", dpi=110)
# plt.show()
 
r, g, b = (int(v) for v in rgb[center_row, center_col])
hex_value = "#{:02X}{:02X}{:02X}".format(r, g, b)
# print(f"Center pixel RGB = ({r}, {g}, {b})  ->  HEX = {hex_value}")

y_start, y_end = 250, 350        # 100 rows
x_start, x_end = 510, 610        # 100 columns (region around the sun)
crop = rgb[y_start:y_end, x_start:x_end]
# print("Crop shape (H, W, C)   :", crop.shape)
assert crop.shape[:2] == (100, 100), "Crop must be exactly 100 x 100"
 
resized = cv.resize(crop, (200, 200), interpolation=cv.INTER_LINEAR)   # (width, height)
# print("Resized shape (H, W, C):", resized.shape)
 
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
axes[0].imshow(rgb);     axes[0].set_title(f"Original {rgb.shape[1]}x{rgb.shape[0]}")
axes[1].imshow(crop);    axes[1].set_title("Crop 100x100")
axes[2].imshow(resized); axes[2].set_title("Resized 200x200")
for ax in axes:
    ax.axis("off")
# plt.tight_layout()
# plt.savefig("crop_resize_figure.png", dpi=110)
# plt.show()
 
resized_bgr = cv.cvtColor(resized, cv.COLOR_RGB2BGR)       # imwrite expects BGR
saved = cv.imwrite("resized_crop.png", resized_bgr)
# print("cv.imwrite() saved resized_crop.png successfully:", saved)

pixels = gray.flatten()
# plt.figure(figsize=(8, 5))
# plt.hist(pixels, bins=256, range=(0, 256), color="gray")
# plt.title("Grayscale Histogram (256 bins)")
# plt.xlabel("Pixel intensity (0 = black, 255 = white)")
# plt.ylabel("Number of pixels")
# plt.tight_layout()
# plt.savefig("grayscale_histogram.png", dpi=110)
# plt.show()
 
# print("Mean intensity      :", round(float(pixels.mean()), 2))
# print("Median intensity    :", float(np.median(pixels)))
# print("Pixels < 85 (dark)  : {:.1f} %".format(100 * np.mean(pixels < 85)))
# print("Pixels 85-170 (mid) : {:.1f} %".format(100 * np.mean((pixels >= 85) & (pixels <= 170))))
# print("Pixels > 170 (light): {:.1f} %".format(100 * np.mean(pixels > 170)))


gradient = np.tile(np.arange(256, dtype=np.uint8), (100, 1))       # 100 x 256, values 0..255
 
def quantize(img, bits):
    levels = 2 ** bits
    step = 256 // levels
    q = (img // step)                                  # level index 0 .. levels-1
    return (q * (255 // (levels - 1))).astype(np.uint8)  # stretch back to 0..255 for display
 
g1, g2, g4 = quantize(gradient, 1), quantize(gradient, 2), quantize(gradient, 4)
fig, axes = plt.subplots(4, 1, figsize=(9, 6))
for ax, (img, title) in zip(axes, [(gradient, "8-bit (256 levels)"), (g4, "4-bit (16 levels)"),
                                   (g2, "2-bit (4 levels)"), (g1, "1-bit (2 levels)")]):
    ax.imshow(img, cmap="gray", vmin=0, vmax=255)
    ax.set_title(title)
    ax.axis("off")
plt.tight_layout()
plt.savefig("bit_depth_figure.png", dpi=110)
plt.show()
 
print("Unique values in 8-bit gradient:", len(np.unique(gradient)))
print("Unique values in 1-bit gradient:", len(np.unique(g1)))
print("Unique values in 2-bit gradient:", len(np.unique(g2)))
print("Unique values in 4-bit gradient:", len(np.unique(g4)))






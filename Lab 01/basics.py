# # Exercise 01 : Variables and Data Types

# # Define variables
# width = 640
# height = 480
# image_name = "sample.png"
# is_color = True

# # Print the variables and their types
# print("Width:", width, "Type:", type(width))
# print("Height:", height, "Type:", type(height))
# print("Image Name:", image_name, "Type:", type(image_name))
# print("Is Color:", is_color, "Type:", type(is_color))

# # Calculate the total number of pixels
# total_pixels = width * height

# # Print the final calculated result
# print("Total number of pixels: ", total_pixels)

# # Exercise 2: if, elif, and else - Pixel Intensity Labeler

# # Define the list of test intensities
# test_intensities = [-1, 0, 127, 128, 255, 256]

# # Loop through each intensity to test the conditions
# for intensity in test_intensities:
#     # Check if the intensity is out of bounds
#     if intensity < 0 or intensity > 255:
#         label = "Invalid"
#     # Check if the valid intensity is 128 or above
#     elif intensity >= 128:
#         label = "Bright pixel"
#     # Otherwise, it must be lower than 128
#     else:
#         label = "Dark pixel"
    
#     # Print the intensity and its resulting label
#     print(f"Intensity {intensity}: {label}")


# # Part 1: for Loop (Pixel Brightness Classifier)
# pixels = [20, 130, 255]
# threshold = 128

# for pixel in pixels:
#     if pixel >= threshold:
#         print(f"{pixel}: Bright pixel")
#     else:
#         print(f"{pixel}: Dark pixel")

# # Print a blank line to separate the exercises
# print()

# # Part 2: while Loop (Counter)
# counter = 0
# while counter < 3:
#     print(counter)
#     counter += 1  # Updating the loop counter to avoid an infinite loop


# #  Exercise 4: Define the is_bright function with a default threshold of 128
# def is_bright(pixel, threshold=128):
#     # Returns True if pixel is at least (>=) the threshold, False otherwise
#     return pixel >= threshold

# # Test the function with the requested values and print the results
# print(is_bright(127))
# print(is_bright(128))
# print(is_bright(200, 210))


# # Part 1: Lists 
# # Create the initial list
# pixels = [0, 128, 255]

# # Print its first item (index 0)
# print(pixels[0])

# # Replace the middle item (index 1) with 150
# pixels[1] = 150

# # Append 64 to the list
# pixels.append(64)

# # Print the updated list and its length
# print(pixels)
# print(len(pixels))


# # Part 2: Tuples 
# # Create the size tuple
# size = (640, 480)

# # Unpack the tuple into width and height
# width, height = size

# # Print both variables
# print(width)
# print(height)


# # Explanation
# # In Python, lists are MUTABLE, meaning their internal contents and size 
# # can be modified in place without changing their identity in memory. 
# # Conversely, tuples are IMMUTABLE; once created, their elements and structure 
# # are fixed in memory to optimize data safety, integrity, and performance.


# Part 1: Dictionaries
# Create the initial image dictionary
image = {"width": 640, "height": 480}

# Add the new key-value pair "mode": "RGB"
image["mode"] = "RGB"

# Print the width and mode using their respective keys
print(image["width"])
print(image["mode"])

# Part 2: Sets
# Create the initial list containing a duplicate item ("cat")
labels_list = ["cat", "dog", "cat", "bird"]

# Convert the list into a set to automatically strip out duplicates
labels_set = set(labels_list)

# Print the length of the set
print(len(labels_set))
















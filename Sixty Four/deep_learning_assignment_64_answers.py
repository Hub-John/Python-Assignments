# Marvellous Infosystems : Python - Automation & Machine Learning
# Deep Learning Assignment
# Format: Question -> Answer

# ============================================================
# QUESTION 1
# What is Convolution Layer? Explain in detail.
# ============================================================

print("\n" + "=" * 70)
print("QUESTION 1")
print("What is Convolution Layer? Explain in detail.")
print("=" * 70)

print("""
ANSWER:
A Convolution Layer is an important layer in a Convolutional Neural
Network (CNN) that extracts useful features from an input such as an
image.

It uses small filters (kernels) that move across the input image.
At each position, the filter performs multiplication with the
corresponding input values and then adds the results.

The output produced by this operation is called a feature map.

Main steps:
1. Take a small region of the input.
2. Apply the kernel to that region.
3. Multiply corresponding values.
4. Add the multiplied values.
5. Store the result in the feature map.
6. Move the kernel and repeat the process.

Convolution layers can learn features such as edges, textures,
shapes, and more complex patterns in deeper layers.
""")


# ============================================================
# QUESTION 2
# What is kernel/filter in CNN?
# ============================================================

print("\n" + "=" * 70)
print("QUESTION 2")
print("What is kernel/filter in CNN?")
print("=" * 70)

print("""
ANSWER:
A kernel, also called a filter, is a small matrix of numbers used
by a convolution layer to detect specific features in an input.

For example, a 3x3 kernel can be used to detect edges.

Example kernel:

[-1, -1, -1]
[ 0,  0,  0]
[ 1,  1,  1]

The kernel moves over the input image and performs multiplication
and addition with each region.

During training, the values of the filters are learned by the
neural network so that useful features can be detected.
""")


# ============================================================
# QUESTION 3
# What is feature map?
# ============================================================

print("\n" + "=" * 70)
print("QUESTION 3")
print("What is feature map?")
print("=" * 70)

print("""
ANSWER:
A feature map is the output produced after applying a filter/kernel
to an input image or feature map.

It contains information about where a particular feature was
detected in the input.

For example, an edge-detection filter can produce a feature map
where larger values indicate the presence of certain edges.

A CNN can create multiple feature maps by using multiple filters.
Each filter can learn to detect a different type of feature.
""")


# ============================================================
# QUESTION 4
# What is stride in convolution operation?
# ============================================================

print("\n" + "=" * 70)
print("QUESTION 4")
print("What is stride in convolution operation?")
print("=" * 70)

print("""
ANSWER:
Stride is the number of positions by which a kernel moves over the
input during a convolution operation.

Example:
- Stride = 1: The kernel moves one position at a time.
- Stride = 2: The kernel moves two positions at a time.

A larger stride generally produces a smaller output feature map.
Stride is therefore used to control the spatial size of the output.
""")


# ============================================================
# QUESTION 5
# What is padding? Why padding is required?
# ============================================================

print("\n" + "=" * 70)
print("QUESTION 5")
print("What is padding? Why padding is required?")
print("=" * 70)

print("""
ANSWER:
Padding means adding extra values, usually zeros, around the border
of an input before applying convolution.

Padding is used for the following reasons:
1. It can preserve the spatial size of the input.
2. It allows border pixels to participate more fully in convolution.
3. It helps control the size of the output feature map.
4. It can prevent excessive reduction in image dimensions after
   several convolution operations.

Common types:
- Valid padding: No padding is added.
- Same padding: Padding is used to maintain the desired spatial
  dimensions, commonly the same height and width when stride is 1.
""")


# ============================================================
# QUESTION 6
# What is pooling layer?
# ============================================================

print("\n" + "=" * 70)
print("QUESTION 6")
print("What is pooling layer?")
print("=" * 70)

print("""
ANSWER:
A pooling layer is used in CNNs to reduce the spatial dimensions
of feature maps.

It operates on small regions of the feature map and summarizes
the values in those regions.

Main purposes:
1. Reduce the size of feature maps.
2. Reduce computational requirements.
3. Help make the network less sensitive to small changes in the
   position of features.
4. Retain important information while reducing the amount of data.
""")


# ============================================================
# QUESTION 7
# Explain types of pooling layers.
# ============================================================

print("\n" + "=" * 70)
print("QUESTION 7")
print("Explain types of pooling layers.")
print("=" * 70)

print("""
ANSWER:
Common types of pooling are:

1. Max Pooling
   Selects the maximum value from each pooling region.

2. Average Pooling
   Calculates the average of the values in each pooling region.

3. Global Max Pooling
   Selects the maximum value from the entire feature map for
   each channel.

4. Global Average Pooling
   Calculates the average of all values in the feature map for
   each channel.

Max Pooling and Average Pooling are commonly used to reduce the
spatial dimensions of feature maps.
""")


# ============================================================
# QUESTION 8
# What is Max Pooling? Explain with example.
# ============================================================

print("\n" + "=" * 70)
print("QUESTION 8")
print("What is Max Pooling? Explain with example.")
print("=" * 70)

print("""
ANSWER:
Max Pooling selects the largest value from each pooling region.

Example input:

[1  3  2  4]
[5  6  7  8]
[9  2  1  3]
[4  5  6  7]

Using a 2x2 pooling window with stride 2:

Region 1:
[1 3]
[5 6]
Maximum = 6

Region 2:
[2 4]
[7 8]
Maximum = 8

Region 3:
[9 2]
[4 5]
Maximum = 9

Region 4:
[1 3]
[6 7]
Maximum = 7

Output:

[6 8]
[9 7]

Thus, Max Pooling reduces the size of the feature map while
retaining strong feature responses.
""")


# ============================================================
# QUESTION 9
# What is Average Pooling? Explain with example.
# ============================================================

print("\n" + "=" * 70)
print("QUESTION 9")
print("What is Average Pooling? Explain with example.")
print("=" * 70)

print("""
ANSWER:
Average Pooling calculates the average value of all elements in
each pooling region.

Using the same input:

[1  3  2  4]
[5  6  7  8]
[9  2  1  3]
[4  5  6  7]

Using a 2x2 pooling window with stride 2:

Region 1:
(1 + 3 + 5 + 6) / 4 = 3.75

Region 2:
(2 + 4 + 7 + 8) / 4 = 5.25

Region 3:
(9 + 2 + 4 + 5) / 4 = 5.00

Region 4:
(1 + 3 + 6 + 7) / 4 = 4.25

Output:

[3.75  5.25]
[5.00   4.25]

Average Pooling reduces the spatial size by replacing each region
with its average value.
""")


# ============================================================
# QUESTION 10
# What is Flatten layer?
# ============================================================

print("\n" + "=" * 70)
print("QUESTION 10")
print("What is Flatten layer?")
print("=" * 70)

print("""
ANSWER:
A Flatten layer converts a multi-dimensional feature map into a
one-dimensional vector.

Example:

Input:
[1 2]
[3 4]

After Flatten:

[1, 2, 3, 4]

In a CNN, convolution and pooling layers generally produce
multi-dimensional feature maps. The Flatten layer converts these
feature maps into a one-dimensional form so they can be passed to
fully connected (dense) layers for classification or prediction.

The Flatten layer does not perform learning by itself. It only
changes the shape of the data.
""")


# ============================================================
# END OF ASSIGNMENT
# ============================================================

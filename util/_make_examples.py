# script to generate example images
import matplotlib.pyplot as plt

f, ax = plt.subplots(figsize=(10,6))
for i in range(10):
    ax.plot(i, 0,'.',markersize=50)

ax.set_title("Default style")
plt.savefig("../img/default_style.png", dpi=300)

plt.style.use("../styles/thesis.mplstyle")

f, ax = plt.subplots(figsize=(10,6))
for i in range(10):
    ax.plot(i, 0,'.',markersize=50)

ax.set_title("gnuplot colormap and other customizations")
plt.savefig("../img/thesis_style.png", dpi=300)

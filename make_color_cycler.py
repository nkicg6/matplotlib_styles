# takes a colormap and returns the hex colors corresponding to 10 discrete values from it.
# used to generate discrete color codes for
import sys
import matplotlib as mpl
import matplotlib.pyplot as plt


def make_cmap(n_colors, cmap):
    cm = plt.get_cmap(cmap, n_colors)
    return [cm(i / (n_colors + 1)) for i in range(n_colors)]


def to_hex(list_of_rgb_floats):
    return [
        mpl.colors.to_hex(i, keep_alpha=True).replace("#", "")
        for i in list_of_rgb_floats
    ]


if __name__ == "__main__":
    try:
        colormap = sys.argv[1]
        cm = make_cmap(10, colormap)
        sys.exit(to_hex(cm))
    except IndexError:
        sys.exit(
            "Enter a valid colormap as the first argument. for example:\n python3 make_color_cycler 'viridis'\n valid colormaps can be found here:\n https://matplotlib.org/3.2.0/tutorials/colors/colormaps.html"
        )
    except ValueError:
        sys.exit(
            f"Enter a valid colormap as the first argument.\n'{colormap}' is not a valid colormap. valid colormaps can be found here:\n https://matplotlib.org/3.2.0/tutorials/colors/colormaps.html"
        )

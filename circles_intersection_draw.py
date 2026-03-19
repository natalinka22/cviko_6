import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def draw_data(circle_1, circle_2, result=None, save_path=None):

    fig, ax = plt.subplots(figsize=(8, 8))

    patch1 = plt.Circle(
        (circle_1["x"], circle_1["y"]), circle_1["r"],
        fill=False, color="blue", linewidth=2, label="Kružnica 1",
    )
    patch2 = plt.Circle(
        (circle_2["x"], circle_2["y"]), circle_2["r"],
        fill=False, color="red", linewidth=2, label="Kružnica 2",
    )
    ax.add_patch(patch1)
    ax.add_patch(patch2)

    ax.plot(circle_1["x"], circle_1["y"], "bo", markersize=5)
    ax.plot(circle_2["x"], circle_2["y"], "ro", markersize=5)

    ax.annotate(
        f"S1 [{circle_1['x']}, {circle_1['y']}]",
        (circle_1["x"], circle_1["y"]),
        textcoords="offset points", xytext=(8, 8), fontsize=9, color="blue",
    )
    ax.annotate(
        f"S2 [{circle_2['x']}, {circle_2['y']}]",
        (circle_2["x"], circle_2["y"]),
        textcoords="offset points", xytext=(8, 8), fontsize=9, color="red",
    )

    vsetky_x = [circle_1["x"], circle_2["x"]]
    vsetky_y = [circle_1["y"], circle_2["y"]]
    vsetky_r = [circle_1["r"], circle_2["r"]]
    okraj = 2
    x_min = min(x - r for x, r in zip(vsetky_x, vsetky_r)) - okraj
    x_max = max(x + r for x, r in zip(vsetky_x, vsetky_r)) + okraj
    y_min = min(y - r for y, r in zip(vsetky_y, vsetky_r)) - okraj
    y_max = max(y + r for y, r in zip(vsetky_y, vsetky_r)) + okraj
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)

    ax.set_aspect("equal")
    ax.grid(True, alpha=0.3)
    ax.legend(loc="upper right")

    if result:
        ax.set_title(result.get("description", ""), fontsize=12)

    plt.tight_layout()

    if save_path:
        plt.savefig(save_path, dpi=150)
    plt.close()

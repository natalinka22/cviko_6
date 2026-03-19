import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

if __name__ != "__main__":
    print("[signal_plot_ops] Modul bol načítaný (tento print je MIMO if __name__ blok).")


def load_signal_from_txt(path):
    values = []
    with open(path, "r") as f:
        for line in f:
            stripped = line.strip()
            if stripped:
                values.append(float(stripped))
    return values


def signal_min(values):
    return min(values)


def signal_max(values):
    return max(values)


def signal_avg(values):
    return sum(values) / len(values)


def plot_signal(values, save_path = None):
    plt.figure(figsize=(12, 4))
    plt.plot(values, color="tab:red", linewidth=0.9)
    plt.title("EKG signál")
    plt.xlabel("Vzorka")
    plt.ylabel("Amplitúda")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=150)
    plt.close()


if __name__ == "__main__":
    data = load_signal_from_txt("ekg_signal.txt")

    print(f"Počet vzorkov: {len(data)}")
    print(f"Minimum:      {signal_min(data):.4f}")
    print(f"Maximum:      {signal_max(data):.4f}")
    print(f"Priemer:      {signal_avg(data):.4f}")

    plot_signal(data, save_path="ekg_plot_module.png")
    print("Graf uložený do ekg_plot_module.png")
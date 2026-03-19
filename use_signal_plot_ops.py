from signal_plot_ops import load_signal_from_txt, signal_avg, plot_signal

data = load_signal_from_txt("ekg_signal.txt")
print(f"Počet vzorkov: {len(data)}")

avg = signal_avg(data)
print(f"Priemerná hodnota: {avg:.4f}")

plot_signal(data, save_path="ekg_plot_script.png")
print("Graf uložený do ekg_plot_script.png")
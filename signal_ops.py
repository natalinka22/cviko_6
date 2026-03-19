def signal_min(values):
    return min(values)


def signal_max(values):
    return max(values)


def signal_avg(values):
    return sum(values) / len(values)


if __name__ == "__main__":
    demo_values = [72, 75, 71, 89, 77]
    print("signal_min:", signal_min(demo_values))
    print("signal_max:", signal_max(demo_values))
    print("signal_avg:", round(signal_avg(demo_values), 2))
import math


def radius_sum(r1, r2):
    return r1 + r2


def euclid_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def has_intersection(circle_1, circle_2):
    d = euclid_distance(circle_1["x"], circle_1["y"], circle_2["x"], circle_2["y"])
    r_sum = radius_sum(circle_1["r"], circle_2["r"])
    r_diff = abs(circle_1["r"] - circle_2["r"])

    if math.isclose(d, 0) and math.isclose(circle_1["r"], circle_2["r"]):
        return {
            "intersects": True,
            "intersections_count": -1,
            "description": "Kružnice sú totožné (nekonečne veľa spoločných bodov).",
        }

    # Jedna kružnica je celá vo vnútri druhej (d < |r1 - r2|)
    if d < r_diff and not math.isclose(d, r_diff):
        return {
            "intersects": False,
            "intersections_count": 0,
            "description": "Kružnice sa nepretínajú – jedna leží celá vo vnútri druhej.",
        }

    # Vnútorný dotyk (d == |r1 - r2|)
    if math.isclose(d, r_diff):
        return {
            "intersects": True,
            "intersections_count": 1,
            "description": "Kružnice sa dotýkajú zvnútra v jednom bode.",
        }

    # Vonkajší dotyk (d == r1 + r2)
    if math.isclose(d, r_sum):
        return {
            "intersects": True,
            "intersections_count": 1,
            "description": "Kružnice sa dotýkajú zvonku v jednom bode.",
        }

    # Príliš ďaleko od seba (d > r1 + r2)
    if d > r_sum:
        return {
            "intersects": False,
            "intersections_count": 0,
            "description": "Kružnice sa nepretínajú - sú príliš ďaleko od seba.",
        }

    # Zostáva jediný prípad: r_diff < d < r_sum → dva prieniky
    return {
        "intersects": True,
        "intersections_count": 2,
        "description": "Kružnice sa pretínajú v dvoch bodoch.",
    }


if __name__ == "__main__":
    # Test 1 – dva prieniky
    c1 = {"x": 0, "y": 0, "r": 2}
    c2 = {"x": 2, "y": 0, "r": 2}
    vysledok = has_intersection(c1, c2)
    print(f"Test 1 (dva prieniky):    {vysledok}")

    # Test 2 – vonkajší dotyk (1 prienik)
    c3 = {"x": 0, "y": 0, "r": 2}
    c4 = {"x": 5, "y": 0, "r": 3}
    vysledok = has_intersection(c3, c4)
    print(f"Test 2 (vonkajší dotyk):  {vysledok}")

    # Test 3 – žiadny prienik (ďaleko)
    c5 = {"x": 0, "y": 0, "r": 1}
    c6 = {"x": 10, "y": 0, "r": 1}
    vysledok = has_intersection(c5, c6)
    print(f"Test 3 (žiadny prienik):  {vysledok}")

    # Test 4 – jedna vo vnútri druhej
    c7 = {"x": 0, "y": 0, "r": 5}
    c8 = {"x": 1, "y": 0, "r": 1}
    vysledok = has_intersection(c7, c8)
    print(f"Test 4 (vo vnútri):       {vysledok}")

    # Test 5 – vnútorný dotyk
    c9 = {"x": 0, "y": 0, "r": 5}
    c10 = {"x": 3, "y": 0, "r": 2}
    vysledok = has_intersection(c9, c10)
    print(f"Test 5 (vnútorný dotyk):  {vysledok}")

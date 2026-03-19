from circles_stats import has_intersection
from circles_intersection_draw import draw_data

scenare = [
    {
        "nazov": "Dva prieniky",
        "c1": {"x": 0, "y": 0, "r": 2},
        "c2": {"x": 2, "y": 0, "r": 2},
        "subor": "circles_dva_prieniky.png",
    },
    {
        "nazov": "Vonkajší dotyk (1 prienik)",
        "c1": {"x": 0, "y": 0, "r": 2},
        "c2": {"x": 5, "y": 0, "r": 3},
        "subor": "circles_vonkajsi_dotyk.png",
    },
    {
        "nazov": "Žiadny prienik (ďaleko)",
        "c1": {"x": 0, "y": 0, "r": 1},
        "c2": {"x": 10, "y": 0, "r": 1},
        "subor": "circles_ziadny_prienik.png",
    },
    {
        "nazov": "Jedna vo vnútri druhej",
        "c1": {"x": 0, "y": 0, "r": 5},
        "c2": {"x": 1, "y": 0, "r": 1},
        "subor": "circles_vo_vnutri.png",
    },
    {
        "nazov": "Vnútorný dotyk (1 prienik)",
        "c1": {"x": 0, "y": 0, "r": 5},
        "c2": {"x": 3, "y": 0, "r": 2},
        "subor": "circles_vnutorny_dotyk.png",
    },
]

for s in scenare:
    vysledok = has_intersection(s["c1"], s["c2"])

    print(f"--- {s['nazov']} ---")
    print(f"  Kružnica 1: stred ({s['c1']['x']}, {s['c1']['y']}), r = {s['c1']['r']}")
    print(f"  Kružnica 2: stred ({s['c2']['x']}, {s['c2']['y']}), r = {s['c2']['r']}")
    print(f"  Pretínajú sa? {vysledok['intersects']}")
    print(f"  Počet prienikov: {vysledok['intersections_count']}")
    print(f"  {vysledok['description']}")
    print()

    draw_data(s["c1"], s["c2"], result=vysledok, save_path=s["subor"])
    print(f"  -> Graf uložený: {s['subor']}\n")

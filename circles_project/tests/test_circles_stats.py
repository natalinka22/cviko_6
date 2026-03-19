import pytest
from circles_project.circles_stats import radius_sum, has_intersection

def test_radius_sum_zakladny():
    """Bežný prípad - súčet dvoch kladných polomerov."""
    assert radius_sum(2, 3) == 5

def test_dva_prieniky():
    """
    Bežný prípad - kružnice sa prekrývajú v dvoch bodoch.
    d = 3, r_sum = 3 + 2 = 5  →  d < r_sum  →  2 prieniky.
    """
    c1 = {"x": 0, "y": 0, "r": 3}
    c2 = {"x": 3, "y": 0, "r": 2}
    vysledok = has_intersection(c1, c2)

    assert vysledok["intersects"] is True
    assert vysledok["intersections_count"] == 2


def test_ziadny_prienik_daleko():
    """
    Bežný prípad - kružnice sú ďaleko od seba.
    d = 10, r_sum = 1 + 1 = 2  →  d > r_sum  →  0 prienikov.
    """
    c1 = {"x": 0, "y": 0, "r": 1}
    c2 = {"x": 10, "y": 0, "r": 1}
    vysledok = has_intersection(c1, c2)

    assert vysledok["intersects"] is False
    assert vysledok["intersections_count"] == 0

def test_vonkajsi_dotyk():
    """
    Hraničný prípad - vonkajší dotyk v jednom bode.
    d = 5, r_sum = 2 + 3 = 5  →  d == r_sum  →  1 prienik.
    Dôležitý, pretože porovnávame desatinné čísla (isclose).
    """
    c1 = {"x": 0, "y": 0, "r": 2}
    c2 = {"x": 5, "y": 0, "r": 3}
    vysledok = has_intersection(c1, c2)

    assert vysledok["intersects"] is True
    assert vysledok["intersections_count"] == 1


def test_vnutorny_dotyk():
    """
    Hraničný prípad - vnútorný dotyk v jednom bode.
    d = 3, |r1 - r2| = |5 - 2| = 3  →  d == r_diff  →  1 prienik.
    Overuje správne rozlíšenie medzi „vo vnútri" a „dotyk zvnútra".
    """
    c1 = {"x": 0, "y": 0, "r": 5}
    c2 = {"x": 3, "y": 0, "r": 2}
    vysledok = has_intersection(c1, c2)

    assert vysledok["intersects"] is True
    assert vysledok["intersections_count"] == 1

def test_jedna_vo_vnutri_druhej():
    """
    Negatívny prípad - malá kružnica je celá vo vnútri veľkej.
    d = 1, |r1 - r2| = |5 - 1| = 4  →  d < r_diff  →  0 prienikov.
    Overuje, že program neohlási prienik, keď sa kružnice vôbec nekrížia.
    """
    c1 = {"x": 0, "y": 0, "r": 5}
    c2 = {"x": 1, "y": 0, "r": 1}
    vysledok = has_intersection(c1, c2)

    assert vysledok["intersects"] is False
    assert vysledok["intersections_count"] == 0

@pytest.mark.parametrize(
    ("c1", "c2", "ocakavany_intersects", "ocakavany_count"),
    [
        # d = 3, r_sum = 3   →  vonkajší dotyk
        ({"x": 0, "y": 0, "r": 2}, {"x": 0, "y": 3, "r": 1}, True, 1),
        # d = 3, r_sum = 4   →  dva prieniky
        ({"x": 0, "y": 0, "r": 2}, {"x": 0, "y": 3, "r": 2}, True, 2),
        # d ≈ 6.12, r_sum = 4  →  žiadny prienik
        ({"x": 2, "y": -1, "r": 1}, {"x": 1.2, "y": 5, "r": 3}, False, 0),
    ],
)
def test_has_intersection_parametrizovany(c1, c2, ocakavany_intersects, ocakavany_count):
    """Parametrizovaný test - viaceré scenáre v jednej funkcii."""
    vysledok = has_intersection(c1, c2)

    assert vysledok["intersects"] is ocakavany_intersects
    assert vysledok["intersections_count"] == ocakavany_count

def test_ZAMERNE_CHYBNY_radius_sum():
    """
    ZÁMERNE CHYBNÝ TEST - očakáva 999, ale správny výsledok je 7.
    Slúži na trénovanie: spusti pytest, prečítaj chybový výpis a nájdi problém.

    Po precvičení zmeň 999 na 7, aby test prešiel.
    """
    assert radius_sum(3, 4) == 7  # <-- OPRAV na 7

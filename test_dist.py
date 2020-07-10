# ------------------------------------------------------------------------------
# Run using pytest. ## 'dist' Unit test.
# ------------------------------------------------------------------------------

import dist


def test_dub_gb():
    dub = dist.Location(53.33306, -6.24889)
    gb = dist.Location(51.50853, -0.12574)
    stretch = dist.distance_cal(dub, gb)
    assert abs(stretch - 462) < 1


def test_dub_dundalk():
    dub = dist.Location(53.33306, -6.24889)
    louth = dist.Location(53.9979451, -6.405957)
    stretch = dist.distance_cal(dub, louth)
    assert abs(stretch - 75) < 1


def test_bray_howth():
    bray = dist.Location(53.2044, -6.1092)
    howth = dist.Location(53.3858, -6.0647)
    stretch = dist.distance_cal(bray, howth)
    assert abs(stretch - 20) < 1

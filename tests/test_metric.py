import pandas as pd
from rolling_mean.rolling_mean import RollingMean


def test_sort_by_date():
    """Testing sort order."""
    df = pd.DataFrame(
        {
            "something": ["A", "B", "C"],
            "event_date": ["2021-10-10", "2021-10-09", "2021-10-11"],
        }
    )
    sorted = RollingMean._sort(df)
    assert sorted.iloc[0].something == "B"
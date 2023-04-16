import logging
import pandas as pd
import numpy as np


class RollingMean:

    def __init__(self, params):
        """Spawn an the metric instance."""
        self.SLIDING_WIN_SIZ = (int)(params['SlidingWinSiz'])
        self.PREDICTOR_COLUMN = params['PredictorColumn']
        self.RESPONSE_COLUMN = params['ResponseColumn']

    def select(self, df):
        """Select the row."""
        sorted = RollingMean._sort(df)
        logging.debug(f"running RollingMean on {self.PREDICTOR_COLUMN}")
        if self.PREDICTOR_COLUMN not in sorted:
            df[self.PREDICTOR_COLUMN] = np.nan
        col_idx = sorted.columns.get_loc(self.PREDICTOR_COLUMN)
        return sorted.iloc[:, col_idx].rolling(self.SLIDING_WIN_SIZ)

    def apply(self, df):
        """Add column for rolling mean metric."""
        df[self.RESPONSE_COLUMN] = self.select(df).sum()
        return df

    @staticmethod
    def _sort(df):
        """Sort frame by date."""
        df["event_date"] = pd.to_datetime(df.event_date)
        df.sort_values(by=['event_date'], inplace=True, ascending=True)
        return df

    def _sort(df):
        """Sort frame by date."""
        df["event_date"] = pd.to_datetime(df.event_date)
        df.sort_values(by=['event_date'], inplace=True, ascending=True)
        return df


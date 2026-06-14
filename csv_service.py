import pandas as pd


def get_csv_summary(df):

    return {
        "rows": len(df),
        "columns": len(df.columns),
        "column_names": list(df.columns),
        "missing_values":
            int(df.isnull().sum().sum())
    }
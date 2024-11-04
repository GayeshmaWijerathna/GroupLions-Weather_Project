import pandas as pd

# Utility file to load data from csvs
def LoadDataTable(path, features=[]):
    try:
        # data = pd.read_csv(path)
        data = pd.read_csv(path, dtype={"column_name": str}, low_memory=False)

    except FileNotFoundError:
        raise ValueError(f"File not found: {path}")
    except Exception as e:
        raise ValueError(f"Error reading data: {str(e)}")

    data = data.drop_duplicates().dropna()
    data.columns = data.columns.str.strip()
    data = data.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

    if features:
        data = data[features]
    return data

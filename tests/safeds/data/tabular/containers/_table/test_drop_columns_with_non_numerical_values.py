import numpy as np
import pandas as pd
from safeds.data.tabular.containers import Table
from safeds.data.tabular.typing import ColumnType, TableSchema


def test_drop_columns_with_non_numerical_values_valid() -> None:
    table = Table(
        pd.DataFrame(
            data={
                "col1": ["A", "B", "C", "A"],
                "col2": ["Test1", "Test1", "Test3", "Test1"],
                "col3": [1, 2, 3, 4],
                "col4": [2, 3, 1, 4],
            }
        )
    )
    updated_table = table.drop_columns_with_non_numerical_values()
    assert updated_table.get_column_names() == ["col3", "col4"]


def test_drop_columns_with_non_numerical_values_empty() -> None:
    table = Table(
        [], TableSchema({"col1": ColumnType.from_numpy_dtype(np.dtype(float))})
    )
    updated_table = table.drop_columns_with_non_numerical_values()
    assert updated_table.get_column_names() == ["col1"]

from typing import Protocol

import numpy as np

from src.entities import Columns, RequestBatch, ResponseBatch


class RecomenderModel(Protocol):
    def predict(self, request: RequestBatch) -> ResponseBatch:
        ...

    def fit(self, *args, **kwargs) -> None:
        ...

    def save_as_pkl(self) -> None:
        ...

    @classmethod
    def load_from_pkl(cls, path: str) -> "RecomenderModel":
        ...


class DummyPredictor:
    def __init__(self, columns: Columns) -> None:
        self.columns = columns

    def predict(self, request: RequestBatch) -> ResponseBatch:
        df = request.make_dataframe(self.columns)
        df[self.columns.predict_item_ids] = np.random.randint(1, 1000, size=df.shape[0])
        return ResponseBatch.make_from_df(df, request.request_ts, self.columns)

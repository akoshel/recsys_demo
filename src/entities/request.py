import pandas as pd
from pydantic import BaseModel

from src.entities import Columns


class PerUserRequest(BaseModel):
    user_id: int
    items_ids: list[int]


class RequestBatch(BaseModel):
    requests: list[PerUserRequest]
    request_ts: int  # time in ms

    def make_dataframe(self, columns: Columns) -> pd.DataFrame:
        rows: list[tuple[int, list[int]]] = []
        for req in self.requests:
            rows.append((req.user_id, req.items_ids))
        return pd.DataFrame(rows, columns=[columns.user_id, columns.basket_item_ids])

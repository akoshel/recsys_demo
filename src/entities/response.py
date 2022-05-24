import time
from http.client import responses

import pandas as pd
from numpy import column_stack
from pydantic import Field, BaseModel

from src.entities import Columns


def cur_ms_time() -> int:
    return int(time.time() * 1000)


class ResponsePerUser(BaseModel):
    user_id: int
    items_ids: list[int]


class ResponseBatch(BaseModel):
    responses: list[ResponsePerUser]
    request_ts: int
    response_ts: int = Field(default_factory=cur_ms_time)

    @classmethod
    def make_from_df(
        cls, predict_df: pd.DataFrame, request_ts: int, columns: Columns
    ) -> "ResponseBatch":
        respononses: list[ResponsePerUser] = []
        df_dict_list = predict_df[[columns.user_id, columns.predict_item_ids]].to_dict(
            orient="records"
        )
        for row in df_dict_list:
            respononses.append(
                ResponsePerUser(
                    user_id=row[columns.user_id], item_ids=row[columns.predict_item_ids]
                )
            )
        return cls(respononses=respononses, request_ts=request_ts)

from pydantic import BaseSettings


class Columns(BaseSettings):
    user_id: str
    basket_item_ids: list[int]
    predict_item_ids: list[int]

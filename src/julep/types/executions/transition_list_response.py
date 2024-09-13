# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["TransitionListResponse", "Item", "ItemCurrent", "ItemNext"]


class ItemCurrent(BaseModel):
    step: int

    workflow: str


class ItemNext(BaseModel):
    step: int

    workflow: str


class Item(BaseModel):
    id: str

    created_at: datetime

    current: ItemCurrent

    execution_id: str

    next: Optional[ItemNext] = None

    output: object

    type: Literal["init", "init_branch", "finish", "finish_branch", "wait", "resume", "error", "step", "cancelled"]

    updated_at: datetime

    metadata: Optional[object] = None


class TransitionListResponse(BaseModel):
    items: List[Item]

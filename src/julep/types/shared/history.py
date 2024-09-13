# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime

from .entry import Entry
from .relation import Relation
from ..._models import BaseModel

__all__ = ["History"]


class History(BaseModel):
    created_at: datetime

    entries: List[Entry]

    relations: List[Relation]

    session_id: str

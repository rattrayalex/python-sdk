# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime

from .._models import BaseModel
from .shared.entry import Entry
from .shared.relation import Relation

__all__ = ["History"]


class History(BaseModel):
    created_at: datetime

    entries: List[Entry]

    relations: List[Relation]

    session_id: str

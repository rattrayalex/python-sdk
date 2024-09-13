# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ToolListResponse", "Item", "ItemFunction"]


class ItemFunction(BaseModel):
    description: Optional[str] = None

    name: Optional[object] = None

    parameters: Optional[object] = None


class Item(BaseModel):
    id: str

    created_at: datetime

    function: ItemFunction
    """Function definition"""

    name: str

    updated_at: datetime

    api_call: Optional[object] = None

    integration: Optional[object] = None

    system: Optional[object] = None

    type: Optional[Literal["function", "integration", "system", "api_call"]] = None


class ToolListResponse(BaseModel):
    items: List[Item]

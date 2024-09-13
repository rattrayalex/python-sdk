# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel
from ..execution import Execution

__all__ = ["ExecutionListResponse"]


class ExecutionListResponse(BaseModel):
    items: List[Execution]

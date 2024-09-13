# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..task import Task
from ..._models import BaseModel

__all__ = ["TaskListResponse"]


class TaskListResponse(BaseModel):
    items: List[Task]

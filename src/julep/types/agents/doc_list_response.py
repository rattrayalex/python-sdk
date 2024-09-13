# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..doc import Doc
from ..._models import BaseModel

__all__ = ["DocListResponse"]


class DocListResponse(BaseModel):
    items: List[Doc]

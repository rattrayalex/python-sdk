# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .snippet import Snippet
from ..._models import BaseModel
from .doc_owner import DocOwner

__all__ = ["DocReference"]


class DocReference(BaseModel):
    id: str

    owner: DocOwner

    snippets: List[Snippet]

    distance: Optional[float] = None

    title: Optional[str] = None

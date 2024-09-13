# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["AgentSearchResponse", "Doc", "DocOwner", "DocSnippet"]


class DocOwner(BaseModel):
    id: str

    role: Literal["user", "agent"]


class DocSnippet(BaseModel):
    content: str

    index: int


class Doc(BaseModel):
    id: str

    owner: DocOwner

    snippets: List[DocSnippet]

    distance: Optional[float] = None

    title: Optional[str] = None


class AgentSearchResponse(BaseModel):
    docs: List[Doc]

    time: float

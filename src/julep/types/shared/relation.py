# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.



from ..._models import BaseModel

__all__ = ["Relation"]


class Relation(BaseModel):
    head: str

    relation: str

    tail: str

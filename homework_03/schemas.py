from pydantic import BaseModel, Field


class PongBase(BaseModel):
    message: str = Field(
        example="pong",
        default="pong"
    )


class PongOut(PongBase):
    """
    Output Pong
    """

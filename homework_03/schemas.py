from pydantic import BaseModel, Field


class PongBase(BaseModel):
    message: str = Field(
        example="Pong",
        default="Pong"
    )


class PongOut(PongBase):
    """
    Output Pong
    """

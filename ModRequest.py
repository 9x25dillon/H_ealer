class ModelRequest(BaseModel):
    messages: list[Message]
    max_tokens: int | None = None
    metadata: dict[str, Any] = {}

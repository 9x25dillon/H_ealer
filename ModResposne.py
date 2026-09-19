class TerminationInfo(BaseModel):
    stop_reason: str | None = None
    refused: bool = False
    refusal_source: str | None = None
    category: str | None = None
    explanation: str | None = None
    partial_output: bool = False


class ModelResponse(BaseModel):
    text: str
    provider: str
    model: str
    termination: TerminationInfo
    latency_ms: float | None = None
    input_tokens: int | None = None
    output_tokens: int | None = None
    raw: dict[str, Any] = {}

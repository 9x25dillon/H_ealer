class ScoreResult(BaseModel):
    dimension: str
    passed: bool | None
    label: str | None = None
    value: float | None = None
    confidence: float | None = None
    rationale: str | None = None
    metadata: dict[str, Any] = {}

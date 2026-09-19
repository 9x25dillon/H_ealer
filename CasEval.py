class EvalCase(BaseModel):
    id: str
    input: list[Message]
    expected_action: ExpectedAction
    category: str
    rationale: str | None = None
    paired_case_id: str | None = None
    tags: list[str] = []
    metadata: dict[str, Any] = {}

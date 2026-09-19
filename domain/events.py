class ExperimentEvent(BaseModel):
    run_id: UUID
    event_type: str
    payload: dict[str, Any]
    occurred_at: datetime

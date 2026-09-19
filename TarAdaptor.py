class TargetAdapter(Protocol):
    @property
    def name(self) -> str:
        ...

    async def generate(
        self,
        request: ModelRequest,
    ) -> ModelResponse:
        ...

    async def healthcheck(self) -> TargetHealth:
        ...

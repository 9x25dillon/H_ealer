class Intervention(Protocol):
    @property
    def name(self) -> str:
        ...

    async def before_generation(
        self,
        request: ModelRequest,
    ) -> InterventionResult:
        ...

    async def after_generation(
        self,
        request: ModelRequest,
        response: ModelResponse,
    ) -> InterventionResult:
        ...

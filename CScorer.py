class Scorer(Protocol):
    @property
    def name(self) -> str:
        ...

    async def score(
        self,
        context: ScoreContext,
    ) -> ScoreResult:
        ...

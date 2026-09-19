class AttackAdapter(Protocol):
    @property
    def name(self) -> str:
        ...

    async def generate_cases(
        self,
        specification: AttackSpecification,
    ) -> AsyncIterator[GeneratedCase]:
        ...

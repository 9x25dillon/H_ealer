class Reranker(Protocol):
    async def rerank(
        self,
        query: str,
        candidates: list[SemanticCandidate],
        top_k: int,
    ) -> list[RankedCandidate]:
        ...

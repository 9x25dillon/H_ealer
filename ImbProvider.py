class EmbeddingProvider(Protocol):
    async def embed_documents(
        self,
        texts: list[str],
    ) -> list[Embedding]:
        ...

    async def embed_queries(
        self,
        texts: list[str],
    ) -> list[Embedding]:
        ...

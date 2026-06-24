from abc import ABC
from abc import abstractmethod

from src.domain.entities.root_cause_hypothesis import (
    RootCauseHypothesis,
)
from src.domain.value_objects.hypothesis_id import (
    HypothesisId,
)


class HypothesisRepository(
    ABC,
):

    @abstractmethod
    async def save(
        self,
        hypothesis: RootCauseHypothesis,
    ) -> None:
        pass

    @abstractmethod
    async def get_by_id(
        self,
        hypothesis_id: HypothesisId,
    ) -> RootCauseHypothesis | None:
        pass
from abc import ABC, abstractmethod
from typing import Dict, Any
from pyspark.sql import DataFrame


class BaseProcessor(ABC):
    """
    Abstract base processor reflecting Abbas's experience with factory pattern
    """

    def __init__(self, config: Dict[str, Any]):
        """
        Initialize processor with configuration

        """
        self.config = config

    @abstractmethod
    def process(self) -> DataFrame:
        """
        Abstract method for processing data
        Follows factory pattern design principles
        """
        pass

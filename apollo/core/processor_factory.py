from typing import Dict, Type, Any
from .base_processor import BaseProcessor


class ProcessorFactory:
    """
    Centralized processor factory reflecting Abbas's ETL design experience
    """

    _processors: Dict[str, Dict[str, Type[BaseProcessor]]] = {
        "bronze": {},
        "silver": {},
        "gold": {},
    }

    @classmethod
    def register_processor(
        cls,
        layer: str,
        table: str,
        processor_class: Type[BaseProcessor],
        config: Dict[str, Any] = None,
    ):
        """
        Register processors dynamically
        """
        cls._processors[layer][table] = {
            "class": processor_class,
            "config": config or {},
        }

    @classmethod
    def get_processor(
        cls, layer: str, table: str, load_type: str = "full"
    ) -> BaseProcessor:
        """
        Retrieve processor for specific layer and table
        :param load_type:
        """
        if layer not in cls._processors:
            raise ValueError(
                f"Invalid layer: {layer}. Available layers: {list(cls._processors.keys())}"
            )
        processor_info = cls._processors[layer].get(table)
        # print(f'Printing Class parameter passed to ProcessorFactory: \n{cls._processors}')
        # print(f'processor_info: {processor_info}')
        if not processor_info:
            raise ValueError(f"No processor found for layer: {layer}, table: {table}")

        processor_config = processor_info["config"].copy()
        processor_config["load_type"] = load_type
        # print(f'processor_config returned from processorfactory:\n {processor_config}')
        return processor_info["class"](processor_config)
        # return processor_info['class'](processor_info['config'])

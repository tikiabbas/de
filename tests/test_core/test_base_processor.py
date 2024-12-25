import pytest
from apollo.core.base_processor import BaseProcessor
# from typing import Dict, Any


class MockProcessor(BaseProcessor):
    """
    Mock concrete implementation for testing BaseProcessor
    """

    def process(self):
        # Simulated processing method
        return None


def test_base_processor_initialization():
    """
    Test base processor initialization with configuration
    """
    config = {"source_path": "/test/path", "load_type": "full"}

    processor = MockProcessor(config)

    assert processor.config == config
    assert processor.load_type == "full"


def test_base_processor_abstract_method():
    """
    Verify abstract method enforcement
    """
    with pytest.raises(TypeError):
        BaseProcessor({"load_type": "full"})


def test_base_processor_load_type_default():
    """
    Test default load type configuration
    """
    config = {"source_path": "/test/path"}
    processor = MockProcessor(config)

    assert processor.load_type == "full"

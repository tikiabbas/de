import pytest
from src.core.processor_factory import ProcessorFactory
from src.bronze.processors.customer_processor import CustomerBronzeProcessor


def test_processor_factory_registration():
    """
    Test processor registration in factory
    Reflects Abbas's experience in developing ETL testing strategies
    """
    ProcessorFactory.register_processor(
        layer='bronze',
        table='customers',
        processor_class=CustomerBronzeProcessor,
        config={'load_type': 'full'}
    )

    processor = ProcessorFactory.get_processor('bronze', 'customers')

    assert processor is not None
    assert isinstance(processor, CustomerBronzeProcessor)


def test_processor_factory_invalid_registration():
    """
    Test error handling for invalid processor registration
    """
    with pytest.raises(ValueError):
        ProcessorFactory.get_processor('invalid_layer', 'invalid_table')

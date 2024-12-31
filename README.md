SOLID Principles Alignment

**Single Responsibility Principle (SRP)**
Each processor focuses on a single responsibility
Separate classes for different layers and tables
Base classes define common interfaces

**Open/Closed Principle**
ProcessorFactory allows adding new processors without modifying existing code
Processors can be extended through inheritance

**Liskov Substitution Principle**
All processors inherit from BaseProcessor
Can be used interchangeably through the factory method

**Interface Segregation Principle**
Minimal, focused process() method in base processor
Specific implementations for each table and layer

**Dependency Inversion Principle**
Depend on abstractions (BaseProcessor)
Factory decouples processor creation from usage
# Project Architecture

This document provides an overview of the high-level architecture and design patterns used in this repository.

## Overview
- Modular design: Each feature or system is encapsulated in its own module.
- Shared code is placed in `ReplicatedStorage` for use by both client and server.
- Server-specific logic is placed in `ServerScriptService`.

## Key Patterns
- Dependency injection for testability.
- Event-driven communication using signals or bindable events.
- Separation of concerns between UI, data, and logic.

## Directory Structure
- See `DIRECTORY_INDEX.md` for details.

## Example Module Structure
```
Modules/
    FeatureA.luau
    FeatureB.luau
    Auxiliary/
        HelperA.luau
        HelperB.luau
```

## Extending the Framework
- Add new modules to the appropriate folder.
- Document new modules in the relevant index files.

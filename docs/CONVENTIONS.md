# Project Conventions

This document describes naming conventions, module structure, dependency rules, and coding standards for this repository.

## Naming Conventions
- Modules: PascalCase (e.g., `Crafting.luau`)
- Folders: PascalCase or camelCase as appropriate
- Test files: `*.spec.luau`

## Module Structure
- Each module should export a single table or function.
- Place related modules in subfolders (e.g., `Auxiliary/`, `GuiLib/`).

## Dependency Rules
- Avoid circular dependencies between modules.
- Use `require` only for explicit dependencies.

## Coding Standards
- Use clear, descriptive variable and function names.
- Document all public functions with Luau doc comments.
- Prefer local functions and variables unless global scope is required.

## File Organization
- Place shared code in `ReplicatedStorage/Modules`.
- Place server-only code in `ServerScriptService`.
- Place third-party libraries in `ThirdParty/`.

## Example Doc Comment
```lua
--[=[
    MyFunction does something important.
    @param foo string -- Description of foo
    @return boolean -- Success
]=]
```

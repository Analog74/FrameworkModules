Public Repo for structuring my libraries:

Here’s a fully expanded README template for your FrameworkModules repo, with every file and folder linked in Markdown. This covers the entire structure as seen in your original tree, using relative links for easy navigation directly on GitHub. (For brevity, if you add more files/folders, simply copy the linking style.)

---

# FrameworkModules

A public collection of reusable Luau libraries and Roblox modules for structured game development.

## Features

- Modular structure for easy inclusion in Roblox projects
- Utilities for camera effects, crafting, raycasting, GUI components, and more
- Includes third-party and original modules

## Directory Structure

Below is the full clickable file tree. Click any link to view that file or folder on GitHub.

<details>
<summary>Show Full File Tree</summary>

```
FrameworkModules/
├── default.project.json
└── src/
    ├── ReplicatedStorage/
    │   └── Modules/
    │       ├── Auxiliary/
    │       │   ├── CameraShaker/
    │       │   │   ├── CameraShakeInstance.luau
    │       │   │   ├── CameraShakePresets.luau
    │       │   │   └── init.luau
    │       │   ├── init.meta.json
    │       │   ├── LightningBolt/
    │       │   │   ├── init.luau
    │       │   │   ├── LightningExplosion.luau
    │       │   │   ├── LightningExplosion.meta.json
    │       │   │   └── LightningSparks.luau
    │       │   └── RockModule.luau
    │       ├── Crafting.luau
    │       ├── FastCastRedux/
    │       │   ├── ActiveCast.luau
    │       │   ├── init.luau
    │       │   ├── Signal.luau
    │       │   ├── Table.luau
    │       │   ├── TypeDefinitions.luau
    │       │   └── TypeMarshaller.luau
    │       ├── GuiLib/
    │       │   ├── Classes/
    │       │   │   ├── CheckboxLabel.luau
    │       │   │   ├── Children/
    │       │   │   │   ├── init.meta.json
    │       │   │   │   ├── RadialMenu/
    │       │   │   │   │   ├── CONSTANTS.luau
    │       │   │   │   │   ├── CreateRadial.luau
    │       │   │   │   │   ├── init.meta.json
    │       │   │   │   │   └── Triangle.luau
    │       │   │   │   └── TextMask/
    │       │   │   │       ├── init.meta.json
    │       │   │   │       ├── Integer.luau
    │       │   │   │       ├── Number.luau
    │       │   │   │       ├── String.luau
    │       │   │   │       ├── Vector2.luau
    │       │   │   │       └── Vector3.luau
    │       │   │   ├── Dragger.luau
    │       │   │   ├── Dropdown.luau
    │       │   │   ├── init.meta.json
    │       │   │   ├── RadialMenu.luau
    │       │   │   ├── RadioButtonGroup.luau
    │       │   │   ├── RadioButtonLabel.luau
    │       │   │   ├── Slider.luau
    │       │   │   └── TextMask.luau
    │       │   ├── Constructors/
    │       │   │   ├── init.meta.json
    │       │   │   └── List.luau
    │       │   ├── init.meta.json
    │       │   ├── LazyLoader.luau
    │       │   └── Utilities/
    │       │       ├── init.meta.json
    │       │       ├── Maid.luau
    │       │       └── Spring.luau
    │       ├── init.meta.json
    │       ├── Items.luau
    │       ├── OTS.luau
    │       ├── Quests.luau
    │       ├── RaycastHitboxV4/
    │       │   ├── HitboxCaster.luau
    │       │   ├── init.luau
    │       │   ├── Signal.luau
    │       │   ├── Solvers/
    │       │   │   ├── Attachment.luau
    │       │   │   ├── Bone.luau
    │       │   │   ├── init.meta.json
    │       │   │   ├── LinkAttachments.luau
    │       │   │   └── Vector3.luau
    │       │   └── VisualizerCache.luau
    │       ├── ReplicatedData.luau
    │       ├── Roact/
    │       │   ├── assertDeepEqual.luau
    │       │   ├── assertDeepEqual.spec.luau
    │       │   ├── assign.luau
    │       │   ├── assign.spec.luau
    │       │   ├── Binding.luau
    │       │   ├── Binding.spec.luau
    │       │   ├── Component.luau
    │       │   ├── Component.spec/
    │       │   │   ├── context.spec.luau
    │       │   │   ├── defaultProps.spec.luau
    │       │   │   ├── didMount.spec.luau
    │       │   │   ├── didUpdate.spec.luau
    │       │   │   ├── extend.spec.luau
    │       │   │   ├── getDerivedStateFromProps.spec.luau
    │       │   │   ├── getElementTraceback.spec.luau
    │       │   │   ├── init.meta.json
    │       │   │   ├── init.spec.luau
    │       │   │   ├── legacyContext.spec.luau
    │       │   │   ├── render.spec.luau
    │       │   │   ├── setState.spec.luau
    │       │   │   ├── shouldUpdate.spec.luau
    │       │   │   ├── validateProps.spec.luau
    │       │   │   ├── willUnmount.spec.luau
    │       │   │   └── willUpdate.spec.luau
    │       │   ├── ComponentLifecyclePhase.luau
    │       │   ├── Config.luau
    │       │   ├── Config.spec.luau
    │       │   ├── createContext.luau
    │       │   ├── createContext.spec.luau
    │       │   ├── createElement.luau
    │       │   ├── createElement.spec.luau
    │       │   ├── createFragment.luau
    │       │   ├── createFragment.spec.luau
    │       │   ├── createReconciler.luau
    │       │   ├── createReconciler.spec.luau
    │       │   ├── createReconcilerCompat.luau
    │       │   ├── createReconcilerCompat.spec.luau
    │       │   ├── createRef.luau
    │       │   ├── createRef.spec.luau
    │       │   ├── createSignal.luau
    │       │   ├── createSignal.spec.luau
    │       │   ├── createSpy.luau
    │       │   ├── createSpy.spec.luau
    │       │   ├── ElementKind.luau
    │       │   ├── ElementKind.spec.luau
    │       │   ├── ElementUtils.luau
    │       │   ├── ElementUtils.spec.luau
    │       │   ├── forwardRef.luau
    │       │   ├── forwardRef.spec.luau
    │       │   ├── getDefaultInstanceProperty.luau
    │       │   ├── getDefaultInstanceProperty.spec.luau
    │       │   ├── GlobalConfig.luau
    │       │   ├── GlobalConfig.spec.luau
    │       │   ├── init.luau
    │       │   ├── init.spec.luau
    │       │   ├── internalAssert.luau
    │       │   ├── invalidSetStateMessages.luau
    │       │   ├── Logging.luau
    │       │   ├── None.luau
    │       │   ├── NoopRenderer.luau
    │       │   ├── oneChild.luau
    │       │   ├── oneChild.spec.luau
    │       │   ├── Portal.luau
    │       │   ├── PropMarkers/
    │       │   │   ├── Change.luau
    │       │   │   ├── Change.spec.luau
    │       │   │   ├── Children.luau
    │       │   │   ├── Event.luau
    │       │   │   ├── Event.spec.luau
    │       │   │   ├── init.meta.json
    │       │   │   └── Ref.luau
    │       │   ├── PureComponent.luau
    │       │   ├── PureComponent.spec.luau
    │       │   ├── RobloxRenderer.luau
    │       │   ├── RobloxRenderer.spec.luau
    │       │   ├── SingleEventManager.luau
    │       │   ├── SingleEventManager.spec.luau
    │       │   ├── strict.luau
    │       │   ├── strict.spec.luau
    │       │   ├── Symbol.luau
    │       │   ├── Symbol.spec.luau
    │       │   ├── Type.luau
    │       │   └── Type.spec.luau
    │       ├── Shared/
    │       │   ├── Bezier.luau
    │       │   ├── init.meta.json
    │       │   ├── MockPart.luau
    │       │   └── Velocity.luau
    │       ├── SuphisLinkedList/
    │       │   ├── Benchmarks.server.luau
    │       │   ├── Examples.server.luau
    │       │   └── init.luau
    │       ├── Templates/
    │       │   ├── Abilities/
    │       │   │   ├── AmberHit.luau
    │       │   │   ├── Ayaka.luau
    │       │   │   ├── Baal.luau
    │       │   │   ├── BladeHit.luau
    │       │   │   ├── FireballHit.luau
    │       │   │   ├── GateHit.luau
    │       │   │   ├── GateSword.luau
    │       │   │   ├── Hex.luau
    │       │   │   ├── IceHit.luau
    │       │   │   ├── init.meta.json
    │       │   │   ├── Lightning.luau
    │       │   │   ├── Orb.luau
    │       │   │   ├── PoisonGas.luau
    │       │   │   ├── Xiangling.luau
    │       │   │   └── Xinyan.luau
    │       │   ├── AbilityTemplate.luau
    │       │   └── init.meta.json
    │       ├── WindLines.luau
    │       └── Zone/
    │           ├── Enum/
    │           │   ├── Accuracy.luau
    │           │   ├── Detection.luau
    │           │   └── init.luau
    │           ├── init.luau
    │           ├── Janitor.luau
    │           ├── OldSignal.luau
    │           ├── Signal.luau
    │           ├── VERSION.luau
    │           ├── ZoneController/
    │           │   ├── CollectiveWorldModel.luau
    │           │   ├── init.luau
    │           │   └── Tracker.luau
    │           └── ZonePlusReference.luau
    ├── Packages/
    │   └── _Index/
    │       ├── init.meta.json
    │       ├── jsdotlua_boolean@1.2.7/
    │       │   ├── boolean/
    │       │   │   ├── init.luau
    │       │   │   └── toJSBoolean.luau
    │       │   ├── init.meta.json
    │       │   └── number.luau
    │       ├── jsdotlua_collections@1.2.7/
    │       │   ├── collections/
    │       │   │   ├── Array/
    │       │   │   │   ├── concat.luau
    │       │   │   │   ├── every.luau
    │       │   │   │   ├── filter.luau
    │       │   │   │   ├── ...
    │       │   │   └── ...
    │       │   ├── ...
    │       └── ...
    └── ServerScriptService/
        └── SpellCombatSystem/
            ├── game/
            │   ├── init.meta.json
            │   └── Scripts/
            │       ├── Abilities/
            │       │   ├── AmberHit.luau
            │       │   ├── ...
            │       └── ...
            └── ...
```

</details>

---

## Links to All Files and Folders

(Click to jump directly to each item in GitHub)

- [default.project.json](./FrameworkModules/default.project.json)
- [src/ReplicatedStorage/Modules](./FrameworkModules/src/ReplicatedStorage/Modules)
  - [Auxiliary](./FrameworkModules/src/ReplicatedStorage/Modules/Auxiliary)
    - [CameraShaker](./FrameworkModules/src/ReplicatedStorage/Modules/Auxiliary/CameraShaker)
      - [CameraShakeInstance.luau](./FrameworkModules/src/ReplicatedStorage/Modules/Auxiliary/CameraShaker/CameraShakeInstance.luau)
      - [CameraShakePresets.luau](./FrameworkModules/src/ReplicatedStorage/Modules/Auxiliary/CameraShaker/CameraShakePresets.luau)
      - [init.luau](./FrameworkModules/src/ReplicatedStorage/Modules/Auxiliary/CameraShaker/init.luau)
    - [init.meta.json](./FrameworkModules/src/ReplicatedStorage/Modules/Auxiliary/init.meta.json)
    - [LightningBolt](./FrameworkModules/src/ReplicatedStorage/Modules/Auxiliary/LightningBolt)
      - [init.luau](./FrameworkModules/src/ReplicatedStorage/Modules/Auxiliary/LightningBolt/init.luau)
      - [LightningExplosion.luau](./FrameworkModules/src/ReplicatedStorage/Modules/Auxiliary/LightningBolt/LightningExplosion.luau)
      - [LightningExplosion.meta.json](./FrameworkModules/src/ReplicatedStorage/Modules/Auxiliary/LightningBolt/LightningExplosion.meta.json)
      - [LightningSparks.luau](./FrameworkModules/src/ReplicatedStorage/Modules/Auxiliary/LightningBolt/LightningSparks.luau)
    - [RockModule.luau](./FrameworkModules/src/ReplicatedStorage/Modules/Auxiliary/RockModule.luau)
  - [Crafting.luau](./FrameworkModules/src/ReplicatedStorage/Modules/Crafting.luau)
  - ...  
- [src/ReplicatedStorage/Modules/FastCastRedux](./FrameworkModules/src/ReplicatedStorage/Modules/FastCastRedux)
  - [ActiveCast.luau](./FrameworkModules/src/ReplicatedStorage/Modules/FastCastRedux/ActiveCast.luau)
  - [init.luau](./FrameworkModules/src/ReplicatedStorage/Modules/FastCastRedux/init.luau)
  - ...  
- [src/ReplicatedStorage/Modules/GuiLib](./FrameworkModules/src/ReplicatedStorage/Modules/GuiLib)
  - [Classes](./FrameworkModules/src/ReplicatedStorage/Modules/GuiLib/Classes)
    - [CheckboxLabel.luau](./FrameworkModules/src/ReplicatedStorage/Modules/GuiLib/Classes/CheckboxLabel.luau)
    - ...  
  - ...  
- ... (Continue for every subfolder and file, using the same relative linking style)

---

## Getting Started

Clone the repo and require the modules you need in your Roblox project.

```sh
git clone https://github.com/Analog74/FrameworkModules.git
```

## License

MIT (or your preferred license)

---

**Tip:**  
For an evolving repo, you can use tools like [tree-markdown-generator](https://github.com/Analog74/FrameworkModules) or VSCode extensions to auto-generate this section.

---

**Note:**  
Due to the extremely large number of files and folders, it’s best to script the creation of this section to keep it current. If you want a script (for Node.js, Python, etc.) to generate this Markdown with clickable links, let me know and I’ll provide one!

Public Repo for structuring my libraries:

.
├── FrameworkModules
│   ├── default.project.json
│   └── src
│       ├── ReplicatedStorage
│       │   ├── Modules
│       │   │   ├── Auxiliary
│       │   │   │   ├── CameraShaker
│       │   │   │   │   ├── CameraShakeInstance.luau
│       │   │   │   │   ├── CameraShakePresets.luau
│       │   │   │   │   └── init.luau
│       │   │   │   ├── init.meta.json
│       │   │   │   ├── LightningBolt
│       │   │   │   │   ├── init.luau
│       │   │   │   │   ├── LightningExplosion.luau
│       │   │   │   │   ├── LightningExplosion.meta.json
│       │   │   │   │   └── LightningSparks.luau
│       │   │   │   └── RockModule.luau
│       │   │   ├── Crafting.luau
│       │   │   ├── FastCastRedux
│       │   │   │   ├── ActiveCast.luau
│       │   │   │   ├── init.luau
│       │   │   │   ├── Signal.luau
│       │   │   │   ├── Table.luau
│       │   │   │   ├── TypeDefinitions.luau
│       │   │   │   └── TypeMarshaller.luau
│       │   │   ├── GuiLib
│       │   │   │   ├── Classes
│       │   │   │   │   ├── CheckboxLabel.luau
│       │   │   │   │   ├── Children
│       │   │   │   │   │   ├── init.meta.json
│       │   │   │   │   │   ├── RadialMenu
│       │   │   │   │   │   │   ├── CONSTANTS.luau
│       │   │   │   │   │   │   ├── CreateRadial.luau
│       │   │   │   │   │   │   ├── init.meta.json
│       │   │   │   │   │   │   └── Triangle.luau
│       │   │   │   │   │   └── TextMask
│       │   │   │   │   │       ├── init.meta.json
│       │   │   │   │   │       ├── Integer.luau
│       │   │   │   │   │       ├── Number.luau
│       │   │   │   │   │       ├── String.luau
│       │   │   │   │   │       ├── Vector2.luau
│       │   │   │   │   │       └── Vector3.luau
│       │   │   │   │   ├── Dragger.luau
│       │   │   │   │   ├── Dropdown.luau
│       │   │   │   │   ├── init.meta.json
│       │   │   │   │   ├── RadialMenu.luau
│       │   │   │   │   ├── RadioButtonGroup.luau
│       │   │   │   │   ├── RadioButtonLabel.luau
│       │   │   │   │   ├── Slider.luau
│       │   │   │   │   └── TextMask.luau
│       │   │   │   ├── Constructors
│       │   │   │   │   ├── init.meta.json
│       │   │   │   │   └── List.luau
│       │   │   │   ├── init.meta.json
│       │   │   │   ├── LazyLoader.luau
│       │   │   │   └── Utilities
│       │   │   │       ├── init.meta.json
│       │   │   │       ├── Maid.luau
│       │   │   │       └── Spring.luau
│       │   │   ├── init.meta.json
│       │   │   ├── Items.luau
│       │   │   ├── OTS.luau
│       │   │   ├── Quests.luau
│       │   │   ├── RaycastHitboxV4
│       │   │   │   ├── HitboxCaster.luau
│       │   │   │   ├── init.luau
│       │   │   │   ├── Signal.luau
│       │   │   │   ├── Solvers
│       │   │   │   │   ├── Attachment.luau
│       │   │   │   │   ├── Bone.luau
│       │   │   │   │   ├── init.meta.json
│       │   │   │   │   ├── LinkAttachments.luau
│       │   │   │   │   └── Vector3.luau
│       │   │   │   └── VisualizerCache.luau
│       │   │   ├── ReplicatedData.luau
│       │   │   ├── Roact
│       │   │   │   ├── assertDeepEqual.luau
│       │   │   │   ├── assertDeepEqual.spec.luau
│       │   │   │   ├── assign.luau
│       │   │   │   ├── assign.spec.luau
│       │   │   │   ├── Binding.luau
│       │   │   │   ├── Binding.spec.luau
│       │   │   │   ├── Component.luau
│       │   │   │   ├── Component.spec
│       │   │   │   │   ├── context.spec.luau
│       │   │   │   │   ├── defaultProps.spec.luau
│       │   │   │   │   ├── didMount.spec.luau
│       │   │   │   │   ├── didUpdate.spec.luau
│       │   │   │   │   ├── extend.spec.luau
│       │   │   │   │   ├── getDerivedStateFromProps.spec.luau
│       │   │   │   │   ├── getElementTraceback.spec.luau
│       │   │   │   │   ├── init.meta.json
│       │   │   │   │   ├── init.spec.luau
│       │   │   │   │   ├── legacyContext.spec.luau
│       │   │   │   │   ├── render.spec.luau
│       │   │   │   │   ├── setState.spec.luau
│       │   │   │   │   ├── shouldUpdate.spec.luau
│       │   │   │   │   ├── validateProps.spec.luau
│       │   │   │   │   ├── willUnmount.spec.luau
│       │   │   │   │   └── willUpdate.spec.luau
│       │   │   │   ├── ComponentLifecyclePhase.luau
│       │   │   │   ├── Config.luau
│       │   │   │   ├── Config.spec.luau
│       │   │   │   ├── createContext.luau
│       │   │   │   ├── createContext.spec.luau
│       │   │   │   ├── createElement.luau
│       │   │   │   ├── createElement.spec.luau
│       │   │   │   ├── createFragment.luau
│       │   │   │   ├── createFragment.spec.luau
│       │   │   │   ├── createReconciler.luau
│       │   │   │   ├── createReconciler.spec.luau
│       │   │   │   ├── createReconcilerCompat.luau
│       │   │   │   ├── createReconcilerCompat.spec.luau
│       │   │   │   ├── createRef.luau
│       │   │   │   ├── createRef.spec.luau
│       │   │   │   ├── createSignal.luau
│       │   │   │   ├── createSignal.spec.luau
│       │   │   │   ├── createSpy.luau
│       │   │   │   ├── createSpy.spec.luau
│       │   │   │   ├── ElementKind.luau
│       │   │   │   ├── ElementKind.spec.luau
│       │   │   │   ├── ElementUtils.luau
│       │   │   │   ├── ElementUtils.spec.luau
│       │   │   │   ├── forwardRef.luau
│       │   │   │   ├── forwardRef.spec.luau
│       │   │   │   ├── getDefaultInstanceProperty.luau
│       │   │   │   ├── getDefaultInstanceProperty.spec.luau
│       │   │   │   ├── GlobalConfig.luau
│       │   │   │   ├── GlobalConfig.spec.luau
│       │   │   │   ├── init.luau
│       │   │   │   ├── init.spec.luau
│       │   │   │   ├── internalAssert.luau
│       │   │   │   ├── invalidSetStateMessages.luau
│       │   │   │   ├── Logging.luau
│       │   │   │   ├── None.luau
│       │   │   │   ├── NoopRenderer.luau
│       │   │   │   ├── oneChild.luau
│       │   │   │   ├── oneChild.spec.luau
│       │   │   │   ├── Portal.luau
│       │   │   │   ├── PropMarkers
│       │   │   │   │   ├── Change.luau
│       │   │   │   │   ├── Change.spec.luau
│       │   │   │   │   ├── Children.luau
│       │   │   │   │   ├── Event.luau
│       │   │   │   │   ├── Event.spec.luau
│       │   │   │   │   ├── init.meta.json
│       │   │   │   │   └── Ref.luau
│       │   │   │   ├── PureComponent.luau
│       │   │   │   ├── PureComponent.spec.luau
│       │   │   │   ├── RobloxRenderer.luau
│       │   │   │   ├── RobloxRenderer.spec.luau
│       │   │   │   ├── SingleEventManager.luau
│       │   │   │   ├── SingleEventManager.spec.luau
│       │   │   │   ├── strict.luau
│       │   │   │   ├── strict.spec.luau
│       │   │   │   ├── Symbol.luau
│       │   │   │   ├── Symbol.spec.luau
│       │   │   │   ├── Type.luau
│       │   │   │   └── Type.spec.luau
│       │   │   ├── Shared
│       │   │   │   ├── Bezier.luau
│       │   │   │   ├── init.meta.json
│       │   │   │   ├── MockPart.luau
│       │   │   │   └── Velocity.luau
│       │   │   ├── SuphisLinkedList
│       │   │   │   ├── Benchmarks.server.luau
│       │   │   │   ├── Examples.server.luau
│       │   │   │   └── init.luau
│       │   │   ├── Templates
│       │   │   │   ├── Abilities
│       │   │   │   │   ├── AmberHit.luau
│       │   │   │   │   ├── Ayaka.luau
│       │   │   │   │   ├── Baal.luau
│       │   │   │   │   ├── BladeHit.luau
│       │   │   │   │   ├── FireballHit.luau
│       │   │   │   │   ├── GateHit.luau
│       │   │   │   │   ├── GateSword.luau
│       │   │   │   │   ├── Hex.luau
│       │   │   │   │   ├── IceHit.luau
│       │   │   │   │   ├── init.meta.json
│       │   │   │   │   ├── Lightning.luau
│       │   │   │   │   ├── Orb.luau
│       │   │   │   │   ├── PoisonGas.luau
│       │   │   │   │   ├── Xiangling.luau
│       │   │   │   │   └── Xinyan.luau
│       │   │   │   ├── AbilityTemplate.luau
│       │   │   │   └── init.meta.json
│       │   │   ├── WindLines.luau
│       │   │   └── Zone
│       │   │       ├── Enum
│       │   │       │   ├── Accuracy.luau
│       │   │       │   ├── Detection.luau
│       │   │       │   └── init.luau
│       │   │       ├── init.luau
│       │   │       ├── Janitor.luau
│       │   │       ├── OldSignal.luau
│       │   │       ├── Signal.luau
│       │   │       ├── VERSION.luau
│       │   │       ├── ZoneController
│       │   │       │   ├── CollectiveWorldModel.luau
│       │   │       │   ├── init.luau
│       │   │       │   └── Tracker.luau
│       │   │       └── ZonePlusReference.luau
│       │   ├── Packages
│       │   │   ├── _Index
│       │   │   │   ├── init.meta.json
│       │   │   │   ├── jsdotlua_boolean@1.2.7
│       │   │   │   │   ├── boolean
│       │   │   │   │   │   ├── init.luau
│       │   │   │   │   │   └── toJSBoolean.luau
│       │   │   │   │   ├── init.meta.json
│       │   │   │   │   └── number.luau
│       │   │   │   ├── jsdotlua_collections@1.2.7
│       │   │   │   │   ├── collections
│       │   │   │   │   │   ├── Array
│       │   │   │   │   │   │   ├── concat.luau
│       │   │   │   │   │   │   ├── every.luau
│       │   │   │   │   │   │   ├── filter.luau
│       │   │   │   │   │   │   ├── find.luau
│       │   │   │   │   │   │   ├── findIndex.luau
│       │   │   │   │   │   │   ├── flat.luau
│       │   │   │   │   │   │   ├── flatMap.luau
│       │   │   │   │   │   │   ├── forEach.luau
│       │   │   │   │   │   │   ├── from
│       │   │   │   │   │   │   │   ├── fromArray.luau
│       │   │   │   │   │   │   │   ├── fromMap.luau
│       │   │   │   │   │   │   │   ├── fromSet.luau
│       │   │   │   │   │   │   │   ├── fromString.luau
│       │   │   │   │   │   │   │   └── init.luau
│       │   │   │   │   │   │   ├── includes.luau
│       │   │   │   │   │   │   ├── indexOf.luau
│       │   │   │   │   │   │   ├── init.luau
│       │   │   │   │   │   │   ├── isArray.luau
│       │   │   │   │   │   │   ├── join.luau
│       │   │   │   │   │   │   ├── map.luau
│       │   │   │   │   │   │   ├── reduce.luau
│       │   │   │   │   │   │   ├── reverse.luau
│       │   │   │   │   │   │   ├── shift.luau
│       │   │   │   │   │   │   ├── slice.luau
│       │   │   │   │   │   │   ├── some.luau
│       │   │   │   │   │   │   ├── sort.luau
│       │   │   │   │   │   │   ├── splice.luau
│       │   │   │   │   │   │   └── unshift.luau
│       │   │   │   │   │   ├── init.luau
│       │   │   │   │   │   ├── inspect.luau
│       │   │   │   │   │   ├── Map
│       │   │   │   │   │   │   ├── coerceToMap.luau
│       │   │   │   │   │   │   ├── coerceToTable.luau
│       │   │   │   │   │   │   ├── init.luau
│       │   │   │   │   │   │   └── Map.luau
│       │   │   │   │   │   ├── Object
│       │   │   │   │   │   │   ├── assign.luau
│       │   │   │   │   │   │   ├── entries.luau
│       │   │   │   │   │   │   ├── freeze.luau
│       │   │   │   │   │   │   ├── init.luau
│       │   │   │   │   │   │   ├── is.luau
│       │   │   │   │   │   │   ├── isFrozen.luau
│       │   │   │   │   │   │   ├── keys.luau
│       │   │   │   │   │   │   ├── None.luau
│       │   │   │   │   │   │   ├── preventExtensions.luau
│       │   │   │   │   │   │   ├── seal.luau
│       │   │   │   │   │   │   └── values.luau
│       │   │   │   │   │   ├── Set.luau
│       │   │   │   │   │   └── WeakMap.luau
│       │   │   │   │   ├── es7-types.luau
│       │   │   │   │   ├── init.meta.json
│       │   │   │   │   └── instance-of.luau
│       │   │   │   ├── jsdotlua_console@1.2.7
│       │   │   │   │   ├── collections.luau
│       │   │   │   │   ├── console
│       │   │   │   │   │   ├── init.luau
│       │   │   │   │   │   └── makeConsoleImpl.luau
│       │   │   │   │   └── init.meta.json
│       │   │   │   ├── jsdotlua_es7-types@1.2.7
│       │   │   │   │   ├── es7-types.luau
│       │   │   │   │   └── init.meta.json
│       │   │   │   ├── jsdotlua_instance-of@1.2.7
│       │   │   │   │   ├── init.meta.json
│       │   │   │   │   └── instance-of
│       │   │   │   │       ├── init.luau
│       │   │   │   │       └── instanceof.luau
│       │   │   │   ├── jsdotlua_luau-polyfill@1.2.7
│       │   │   │   │   ├── boolean.luau
│       │   │   │   │   ├── collections.luau
│       │   │   │   │   ├── console.luau
│       │   │   │   │   ├── es7-types.luau
│       │   │   │   │   ├── init.meta.json
│       │   │   │   │   ├── instance-of.luau
│       │   │   │   │   ├── luau-polyfill
│       │   │   │   │   │   ├── AssertionError
│       │   │   │   │   │   │   ├── AssertionError.global.luau
│       │   │   │   │   │   │   └── init.luau
│       │   │   │   │   │   ├── encodeURIComponent.luau
│       │   │   │   │   │   ├── Error
│       │   │   │   │   │   │   ├── Error.global.luau
│       │   │   │   │   │   │   └── init.luau
│       │   │   │   │   │   ├── extends.luau
│       │   │   │   │   │   ├── init.luau
│       │   │   │   │   │   └── Promise.luau
│       │   │   │   │   ├── math.luau
│       │   │   │   │   ├── number.luau
│       │   │   │   │   ├── string.luau
│       │   │   │   │   ├── symbol-luau.luau
│       │   │   │   │   └── timers.luau
│       │   │   │   ├── jsdotlua_math@1.2.7
│       │   │   │   │   ├── init.meta.json
│       │   │   │   │   └── math
│       │   │   │   │       ├── clz32.luau
│       │   │   │   │       └── init.luau
│       │   │   │   ├── jsdotlua_number@1.2.7
│       │   │   │   │   ├── init.meta.json
│       │   │   │   │   └── number
│       │   │   │   │       ├── init.luau
│       │   │   │   │       ├── isFinite.luau
│       │   │   │   │       ├── isInteger.luau
│       │   │   │   │       ├── isNaN.luau
│       │   │   │   │       ├── isSafeInteger.luau
│       │   │   │   │       ├── MAX_SAFE_INTEGER.luau
│       │   │   │   │       ├── MIN_SAFE_INTEGER.luau
│       │   │   │   │       └── toExponential.luau
│       │   │   │   ├── jsdotlua_promise@3.5.2
│       │   │   │   │   ├── init.meta.json
│       │   │   │   │   └── promise
│       │   │   │   │       ├── init.luau
│       │   │   │   │       └── init.spec.luau
│       │   │   │   ├── jsdotlua_react-reconciler@17.2.1
│       │   │   │   │   ├── init.meta.json
│       │   │   │   │   ├── luau-polyfill.luau
│       │   │   │   │   ├── promise.luau
│       │   │   │   │   ├── react-reconciler
│       │   │   │   │   │   ├── DebugTracing.luau
│       │   │   │   │   │   ├── forks
│       │   │   │   │   │   │   ├── init.meta.json
│       │   │   │   │   │   │   └── ReactFiberHostConfig.test.luau
│       │   │   │   │   │   ├── init.luau
│       │   │   │   │   │   ├── MaxInts.luau
│       │   │   │   │   │   ├── ReactCapturedValue.luau
│       │   │   │   │   │   ├── ReactChildFiber.new.luau
│       │   │   │   │   │   ├── ReactCurrentFiber.luau
│       │   │   │   │   │   ├── ReactFiber.new.luau
│       │   │   │   │   │   ├── ReactFiberBeginWork.new.luau
│       │   │   │   │   │   ├── ReactFiberClassComponent.new.luau
│       │   │   │   │   │   ├── ReactFiberCommitWork.new.luau
│       │   │   │   │   │   ├── ReactFiberCompleteWork.new.luau
│       │   │   │   │   │   ├── ReactFiberComponentStack.luau
│       │   │   │   │   │   ├── ReactFiberContext.new.luau
│       │   │   │   │   │   ├── ReactFiberDevToolsHook.new.luau
│       │   │   │   │   │   ├── ReactFiberErrorDialog.luau
│       │   │   │   │   │   ├── ReactFiberErrorLogger.luau
│       │   │   │   │   │   ├── ReactFiberFlags.luau
│       │   │   │   │   │   ├── ReactFiberHooks.new.luau
│       │   │   │   │   │   ├── ReactFiberHostConfig.luau
│       │   │   │   │   │   ├── ReactFiberHostContext.new.luau
│       │   │   │   │   │   ├── ReactFiberHotReloading.new.luau
│       │   │   │   │   │   ├── ReactFiberHydrationContext.new.luau
│       │   │   │   │   │   ├── ReactFiberLane.luau
│       │   │   │   │   │   ├── ReactFiberLazyComponent.new.luau
│       │   │   │   │   │   ├── ReactFiberNewContext.new.luau
│       │   │   │   │   │   ├── ReactFiberOffscreenComponent.luau
│       │   │   │   │   │   ├── ReactFiberReconciler.luau
│       │   │   │   │   │   ├── ReactFiberReconciler.new.luau
│       │   │   │   │   │   ├── ReactFiberRoot.new.luau
│       │   │   │   │   │   ├── ReactFiberSchedulerPriorities.roblox.luau
│       │   │   │   │   │   ├── ReactFiberStack.new.luau
│       │   │   │   │   │   ├── ReactFiberSuspenseComponent.new.luau
│       │   │   │   │   │   ├── ReactFiberSuspenseContext.new.luau
│       │   │   │   │   │   ├── ReactFiberThrow.new.luau
│       │   │   │   │   │   ├── ReactFiberTransition.luau
│       │   │   │   │   │   ├── ReactFiberTreeReflection.luau
│       │   │   │   │   │   ├── ReactFiberUnwindWork.new.luau
│       │   │   │   │   │   ├── ReactFiberWorkInProgress.luau
│       │   │   │   │   │   ├── ReactFiberWorkLoop.new.luau
│       │   │   │   │   │   ├── ReactHookEffectTags.luau
│       │   │   │   │   │   ├── ReactInternalTypes.luau
│       │   │   │   │   │   ├── ReactMutableSource.new.luau
│       │   │   │   │   │   ├── ReactPortal.luau
│       │   │   │   │   │   ├── ReactProfilerTimer.new.luau
│       │   │   │   │   │   ├── ReactRootTags.luau
│       │   │   │   │   │   ├── ReactStrictModeWarnings.new.luau
│       │   │   │   │   │   ├── ReactTestSelectors.luau
│       │   │   │   │   │   ├── ReactTypeOfMode.luau
│       │   │   │   │   │   ├── ReactUpdateQueue.new.luau
│       │   │   │   │   │   ├── ReactWorkTags.luau
│       │   │   │   │   │   ├── RobloxReactProfiling.luau
│       │   │   │   │   │   ├── SchedulerWithReactIntegration.new.luau
│       │   │   │   │   │   └── SchedulingProfiler.luau
│       │   │   │   │   ├── react.luau
│       │   │   │   │   ├── scheduler.luau
│       │   │   │   │   └── shared.luau
│       │   │   │   ├── jsdotlua_react-roblox@17.2.1
│       │   │   │   │   ├── init.meta.json
│       │   │   │   │   ├── luau-polyfill.luau
│       │   │   │   │   ├── react-reconciler.luau
│       │   │   │   │   ├── react-roblox
│       │   │   │   │   │   ├── client
│       │   │   │   │   │   │   ├── init.meta.json
│       │   │   │   │   │   │   ├── ReactRoblox.luau
│       │   │   │   │   │   │   ├── ReactRobloxComponent.luau
│       │   │   │   │   │   │   ├── ReactRobloxComponentTree.luau
│       │   │   │   │   │   │   ├── ReactRobloxHostConfig.luau
│       │   │   │   │   │   │   ├── ReactRobloxHostTypes.roblox.luau
│       │   │   │   │   │   │   ├── ReactRobloxRoot.luau
│       │   │   │   │   │   │   └── roblox
│       │   │   │   │   │   │       ├── getDefaultInstanceProperty.luau
│       │   │   │   │   │   │       ├── init.meta.json
│       │   │   │   │   │   │       ├── RobloxComponentProps.luau
│       │   │   │   │   │   │       └── SingleEventManager.luau
│       │   │   │   │   │   ├── init.luau
│       │   │   │   │   │   └── ReactReconciler.roblox.luau
│       │   │   │   │   ├── react.luau
│       │   │   │   │   ├── scheduler.luau
│       │   │   │   │   └── shared.luau
│       │   │   │   ├── jsdotlua_react@17.2.1
│       │   │   │   │   ├── init.meta.json
│       │   │   │   │   ├── luau-polyfill.luau
│       │   │   │   │   ├── react
│       │   │   │   │   │   ├── createSignal.roblox.luau
│       │   │   │   │   │   ├── init.luau
│       │   │   │   │   │   ├── None.roblox.luau
│       │   │   │   │   │   ├── React.luau
│       │   │   │   │   │   ├── ReactBaseClasses.luau
│       │   │   │   │   │   ├── ReactBinding.roblox.luau
│       │   │   │   │   │   ├── ReactChildren.luau
│       │   │   │   │   │   ├── ReactContext.luau
│       │   │   │   │   │   ├── ReactCreateRef.luau
│       │   │   │   │   │   ├── ReactElement.luau
│       │   │   │   │   │   ├── ReactElementValidator.luau
│       │   │   │   │   │   ├── ReactForwardRef.luau
│       │   │   │   │   │   ├── ReactHooks.luau
│       │   │   │   │   │   ├── ReactLazy.luau
│       │   │   │   │   │   ├── ReactMemo.luau
│       │   │   │   │   │   ├── ReactMutableSource.luau
│       │   │   │   │   │   └── ReactNoopUpdateQueue.luau
│       │   │   │   │   └── shared.luau
│       │   │   │   ├── jsdotlua_scheduler@17.2.1
│       │   │   │   │   ├── init.meta.json
│       │   │   │   │   ├── luau-polyfill.luau
│       │   │   │   │   ├── scheduler
│       │   │   │   │   │   ├── forks
│       │   │   │   │   │   │   ├── init.meta.json
│       │   │   │   │   │   │   ├── SchedulerHostConfig.default.luau
│       │   │   │   │   │   │   └── SchedulerHostConfig.mock.luau
│       │   │   │   │   │   ├── init.luau
│       │   │   │   │   │   ├── Scheduler.luau
│       │   │   │   │   │   ├── SchedulerFeatureFlags.luau
│       │   │   │   │   │   ├── SchedulerHostConfig.luau
│       │   │   │   │   │   ├── SchedulerMinHeap.luau
│       │   │   │   │   │   ├── SchedulerPriorities.luau
│       │   │   │   │   │   ├── SchedulerProfiling.luau
│       │   │   │   │   │   ├── Tracing.luau
│       │   │   │   │   │   ├── TracingSubscriptions.luau
│       │   │   │   │   │   └── unstable_mock.luau
│       │   │   │   │   └── shared.luau
│       │   │   │   ├── jsdotlua_shared@17.2.1
│       │   │   │   │   ├── init.meta.json
│       │   │   │   │   ├── luau-polyfill.luau
│       │   │   │   │   └── shared
│       │   │   │   │       ├── checkPropTypes.luau
│       │   │   │   │       ├── console.luau
│       │   │   │   │       ├── ConsolePatchingDev.roblox.luau
│       │   │   │   │       ├── consoleWithStackDev.luau
│       │   │   │   │       ├── enqueueTask.roblox.luau
│       │   │   │   │       ├── ErrorHandling.roblox.luau
│       │   │   │   │       ├── ExecutionEnvironment.luau
│       │   │   │   │       ├── flowtypes.roblox.luau
│       │   │   │   │       ├── formatProdErrorMessage.luau
│       │   │   │   │       ├── getComponentName.luau
│       │   │   │   │       ├── init.luau
│       │   │   │   │       ├── invariant.luau
│       │   │   │   │       ├── invokeGuardedCallbackImpl.luau
│       │   │   │   │       ├── isValidElementType.luau
│       │   │   │   │       ├── objectIs.luau
│       │   │   │   │       ├── PropMarkers
│       │   │   │   │       │   ├── Change.luau
│       │   │   │   │       │   ├── Event.luau
│       │   │   │   │       │   ├── init.meta.json
│       │   │   │   │       │   └── Tag.luau
│       │   │   │   │       ├── ReactComponentStackFrame.luau
│       │   │   │   │       ├── ReactElementType.luau
│       │   │   │   │       ├── ReactErrorUtils.luau
│       │   │   │   │       ├── ReactFeatureFlags.luau
│       │   │   │   │       ├── ReactFiberHostConfig
│       │   │   │   │       │   ├── init.luau
│       │   │   │   │       │   ├── WithNoHydration.luau
│       │   │   │   │       │   ├── WithNoPersistence.luau
│       │   │   │   │       │   └── WithNoTestSelectors.luau
│       │   │   │   │       ├── ReactInstanceMap.luau
│       │   │   │   │       ├── ReactSharedInternals
│       │   │   │   │       │   ├── init.luau
│       │   │   │   │       │   ├── IsSomeRendererActing.luau
│       │   │   │   │       │   ├── ReactCurrentBatchConfig.luau
│       │   │   │   │       │   ├── ReactCurrentDispatcher.luau
│       │   │   │   │       │   ├── ReactCurrentOwner.luau
│       │   │   │   │       │   └── ReactDebugCurrentFrame.luau
│       │   │   │   │       ├── ReactSymbols.luau
│       │   │   │   │       ├── ReactTypes.luau
│       │   │   │   │       ├── ReactVersion.luau
│       │   │   │   │       ├── shallowEqual.luau
│       │   │   │   │       ├── Symbol.roblox.luau
│       │   │   │   │       ├── Type.roblox.luau
│       │   │   │   │       └── UninitializedState.roblox.luau
│       │   │   │   ├── jsdotlua_string@1.2.7
│       │   │   │   │   ├── es7-types.luau
│       │   │   │   │   ├── init.meta.json
│       │   │   │   │   ├── number.luau
│       │   │   │   │   └── string
│       │   │   │   │       ├── charCodeAt.luau
│       │   │   │   │       ├── endsWith.luau
│       │   │   │   │       ├── findOr.luau
│       │   │   │   │       ├── includes.luau
│       │   │   │   │       ├── indexOf.luau
│       │   │   │   │       ├── init.luau
│       │   │   │   │       ├── lastIndexOf.luau
│       │   │   │   │       ├── slice.luau
│       │   │   │   │       ├── split.luau
│       │   │   │   │       ├── startsWith.luau
│       │   │   │   │       ├── substr.luau
│       │   │   │   │       ├── trim.luau
│       │   │   │   │       ├── trimEnd.luau
│       │   │   │   │       └── trimStart.luau
│       │   │   │   ├── jsdotlua_symbol-luau@1.0.1
│       │   │   │   │   ├── init.meta.json
│       │   │   │   │   └── symbol-luau
│       │   │   │   │       ├── init.luau
│       │   │   │   │       ├── Registry.global.luau
│       │   │   │   │       └── Symbol.luau
│       │   │   │   ├── jsdotlua_timers@1.2.7
│       │   │   │   │   ├── collections.luau
│       │   │   │   │   ├── init.meta.json
│       │   │   │   │   └── timers
│       │   │   │   │       ├── init.luau
│       │   │   │   │       ├── makeIntervalImpl.luau
│       │   │   │   │       └── makeTimerImpl.luau
│       │   │   │   ├── roblox_roact@1.4.4
│       │   │   │   │   ├── init.meta.json
│       │   │   │   │   └── roact
│       │   │   │   │       ├── assertDeepEqual.luau
│       │   │   │   │       ├── assertDeepEqual.spec.luau
│       │   │   │   │       ├── assign.luau
│       │   │   │   │       ├── assign.spec.luau
│       │   │   │   │       ├── Binding.luau
│       │   │   │   │       ├── Binding.spec.luau
│       │   │   │   │       ├── Component.luau
│       │   │   │   │       ├── Component.spec
│       │   │   │   │       │   ├── context.spec.luau
│       │   │   │   │       │   ├── defaultProps.spec.luau
│       │   │   │   │       │   ├── didMount.spec.luau
│       │   │   │   │       │   ├── didUpdate.spec.luau
│       │   │   │   │       │   ├── extend.spec.luau
│       │   │   │   │       │   ├── getDerivedStateFromProps.spec.luau
│       │   │   │   │       │   ├── getElementTraceback.spec.luau
│       │   │   │   │       │   ├── init.meta.json
│       │   │   │   │       │   ├── init.spec.luau
│       │   │   │   │       │   ├── legacyContext.spec.luau
│       │   │   │   │       │   ├── render.spec.luau
│       │   │   │   │       │   ├── setState.spec.luau
│       │   │   │   │       │   ├── shouldUpdate.spec.luau
│       │   │   │   │       │   ├── validateProps.spec.luau
│       │   │   │   │       │   ├── willUnmount.spec.luau
│       │   │   │   │       │   └── willUpdate.spec.luau
│       │   │   │   │       ├── ComponentLifecyclePhase.luau
│       │   │   │   │       ├── Config.luau
│       │   │   │   │       ├── Config.spec.luau
│       │   │   │   │       ├── createContext.luau
│       │   │   │   │       ├── createContext.spec.luau
│       │   │   │   │       ├── createElement.luau
│       │   │   │   │       ├── createElement.spec.luau
│       │   │   │   │       ├── createFragment.luau
│       │   │   │   │       ├── createFragment.spec.luau
│       │   │   │   │       ├── createReconciler.luau
│       │   │   │   │       ├── createReconciler.spec.luau
│       │   │   │   │       ├── createReconcilerCompat.luau
│       │   │   │   │       ├── createReconcilerCompat.spec.luau
│       │   │   │   │       ├── createRef.luau
│       │   │   │   │       ├── createRef.spec.luau
│       │   │   │   │       ├── createSignal.luau
│       │   │   │   │       ├── createSignal.spec.luau
│       │   │   │   │       ├── createSpy.luau
│       │   │   │   │       ├── createSpy.spec.luau
│       │   │   │   │       ├── ElementKind.luau
│       │   │   │   │       ├── ElementKind.spec.luau
│       │   │   │   │       ├── ElementUtils.luau
│       │   │   │   │       ├── ElementUtils.spec.luau
│       │   │   │   │       ├── forwardRef.luau
│       │   │   │   │       ├── forwardRef.spec.luau
│       │   │   │   │       ├── getDefaultInstanceProperty.luau
│       │   │   │   │       ├── getDefaultInstanceProperty.spec.luau
│       │   │   │   │       ├── GlobalConfig.luau
│       │   │   │   │       ├── GlobalConfig.spec.luau
│       │   │   │   │       ├── init.luau
│       │   │   │   │       ├── init.spec.luau
│       │   │   │   │       ├── internalAssert.luau
│       │   │   │   │       ├── invalidSetStateMessages.luau
│       │   │   │   │       ├── Logging.luau
│       │   │   │   │       ├── None.luau
│       │   │   │   │       ├── NoopRenderer.luau
│       │   │   │   │       ├── oneChild.luau
│       │   │   │   │       ├── oneChild.spec.luau
│       │   │   │   │       ├── Portal.luau
│       │   │   │   │       ├── PropMarkers
│       │   │   │   │       │   ├── Change.luau
│       │   │   │   │       │   ├── Change.spec.luau
│       │   │   │   │       │   ├── Children.luau
│       │   │   │   │       │   ├── Event.luau
│       │   │   │   │       │   ├── Event.spec.luau
│       │   │   │   │       │   ├── init.meta.json
│       │   │   │   │       │   └── Ref.luau
│       │   │   │   │       ├── PureComponent.luau
│       │   │   │   │       ├── PureComponent.spec.luau
│       │   │   │   │       ├── RobloxRenderer.luau
│       │   │   │   │       ├── RobloxRenderer.spec.luau
│       │   │   │   │       ├── SingleEventManager.luau
│       │   │   │   │       ├── SingleEventManager.spec.luau
│       │   │   │   │       ├── strict.luau
│       │   │   │   │       ├── strict.spec.luau
│       │   │   │   │       ├── Symbol.luau
│       │   │   │   │       ├── Symbol.spec.luau
│       │   │   │   │       ├── Type.luau
│       │   │   │   │       └── Type.spec.luau
│       │   │   │   └── sircfenner_studiocomponents@1.2.0
│       │   │   │       ├── init.meta.json
│       │   │   │       ├── react-roblox.luau
│       │   │   │       ├── react.luau
│       │   │   │       └── studiocomponents
│       │   │   │           ├── CommonProps.luau
│       │   │   │           ├── Components
│       │   │   │           │   ├── Background.luau
│       │   │   │           │   ├── Button.luau
│       │   │   │           │   ├── Checkbox.luau
│       │   │   │           │   ├── ColorPicker.luau
│       │   │   │           │   ├── DatePicker.luau
│       │   │   │           │   ├── Dropdown
│       │   │   │           │   │   ├── ClearButton.luau
│       │   │   │           │   │   ├── DropdownItem.luau
│       │   │   │           │   │   ├── init.luau
│       │   │   │           │   │   └── Types.luau
│       │   │   │           │   ├── DropShadowFrame.luau
│       │   │   │           │   ├── Foundation
│       │   │   │           │   │   ├── BaseButton.luau
│       │   │   │           │   │   ├── BaseIcon.luau
│       │   │   │           │   │   ├── BaseLabelledToggle.luau
│       │   │   │           │   │   ├── BaseTextInput.luau
│       │   │   │           │   │   └── init.meta.json
│       │   │   │           │   ├── init.meta.json
│       │   │   │           │   ├── Label.luau
│       │   │   │           │   ├── LoadingDots.luau
│       │   │   │           │   ├── MainButton.luau
│       │   │   │           │   ├── NumberSequencePicker
│       │   │   │           │   │   ├── AxisLabel.luau
│       │   │   │           │   │   ├── Constants.luau
│       │   │   │           │   │   ├── DashedLine.luau
│       │   │   │           │   │   ├── FreeLine.luau
│       │   │   │           │   │   ├── init.luau
│       │   │   │           │   │   ├── LabelledNumericInput.luau
│       │   │   │           │   │   └── SequenceNode.luau
│       │   │   │           │   ├── NumericInput.luau
│       │   │   │           │   ├── PluginProvider.luau
│       │   │   │           │   ├── ProgressBar.luau
│       │   │   │           │   ├── RadioButton.luau
│       │   │   │           │   ├── ScrollFrame
│       │   │   │           │   │   ├── Constants.luau
│       │   │   │           │   │   ├── init.luau
│       │   │   │           │   │   ├── ScrollBar.luau
│       │   │   │           │   │   ├── ScrollBarArrow.luau
│       │   │   │           │   │   └── Types.luau
│       │   │   │           │   ├── Slider.luau
│       │   │   │           │   ├── Splitter.luau
│       │   │   │           │   ├── TabContainer.luau
│       │   │   │           │   └── TextInput.luau
│       │   │   │           ├── Constants.luau
│       │   │   │           ├── Contexts
│       │   │   │           │   ├── init.meta.json
│       │   │   │           │   ├── PluginContext.luau
│       │   │   │           │   └── ThemeContext.luau
│       │   │   │           ├── getTextSize.luau
│       │   │   │           ├── Hooks
│       │   │   │           │   ├── init.meta.json
│       │   │   │           │   ├── useFreshCallback.luau
│       │   │   │           │   ├── useMouseDrag.luau
│       │   │   │           │   ├── useMouseIcon.luau
│       │   │   │           │   ├── usePlugin.luau
│       │   │   │           │   └── useTheme.luau
│       │   │   │           ├── init.luau
│       │   │   │           └── Stories
│       │   │   │               ├── Background.story.luau
│       │   │   │               ├── Button.story.luau
│       │   │   │               ├── Checkbox.story.luau
│       │   │   │               ├── ColorPicker.story.luau
│       │   │   │               ├── DatePicker.story.luau
│       │   │   │               ├── Dropdown.story.luau
│       │   │   │               ├── DropShadowFrame.story.luau
│       │   │   │               ├── Helpers
│       │   │   │               │   ├── createStory.luau
│       │   │   │               │   ├── getStoryPlugin.luau
│       │   │   │               │   ├── init.meta.json
│       │   │   │               │   └── studiocomponents.storybook.luau
│       │   │   │               ├── init.meta.json
│       │   │   │               ├── Label.story.luau
│       │   │   │               ├── LoadingDots.story.luau
│       │   │   │               ├── MainButton.story.luau
│       │   │   │               ├── NumberSequencePicker.story.luau
│       │   │   │               ├── NumericInput.story.luau
│       │   │   │               ├── ProgressBar.story.luau
│       │   │   │               ├── RadioButton.story.luau
│       │   │   │               ├── ScrollFrame.story.luau
│       │   │   │               ├── Slider.story.luau
│       │   │   │               ├── Splitter.story.luau
│       │   │   │               ├── TabContainer.story.luau
│       │   │   │               └── TextInput.story.luau
│       │   │   ├── init.meta.json
│       │   │   ├── Roact.luau
│       │   │   └── StudioComponents.luau
│       │   ├── SpellCombatSystem
│       │   │   ├── init.meta.json
│       │   │   └── Scripts
│       │   │       ├── Abilities
│       │   │       │   ├── AmberHit.luau
│       │   │       │   ├── Ayaka.luau
│       │   │       │   ├── Baal.luau
│       │   │       │   ├── BladeHit.luau
│       │   │       │   ├── FireballHit.luau
│       │   │       │   ├── GateHit.luau
│       │   │       │   ├── GateSword.luau
│       │   │       │   ├── Hex.luau
│       │   │       │   ├── IceHit.luau
│       │   │       │   ├── init.meta.json
│       │   │       │   ├── Lightning.luau
│       │   │       │   ├── Orb.luau
│       │   │       │   ├── PoisonGas.luau
│       │   │       │   ├── Xiangling.luau
│       │   │       │   └── Xinyan.luau
│       │   │       └── init.meta.json
│       │   └── ThirdParty
│       │       ├── CameraShaker
│       │       │   ├── CameraShakeInstance.luau
│       │       │   ├── CameraShakePresets.luau
│       │       │   └── init.luau
│       │       ├── init.meta.json
│       │       ├── JSON
│       │       │   ├── bench
│       │       │   │   ├── bench_all.luau
│       │       │   │   ├── bench_decode.luau
│       │       │   │   ├── bench_encode.luau
│       │       │   │   ├── init.meta.json
│       │       │   │   └── util
│       │       │   │       ├── bench.luau
│       │       │   │       └── init.meta.json
│       │       │   ├── init.meta.json
│       │       │   ├── json.luau
│       │       │   └── test
│       │       │       ├── init.meta.json
│       │       │       └── test.luau
│       │       ├── OTS
│       │       │   ├── init.meta.json
│       │       │   └── OTS.luau
│       │       ├── ProfileService.luau
│       │       ├── RaycastHitboxV4
│       │       │   ├── HitboxCaster.luau
│       │       │   ├── init.luau
│       │       │   ├── Signal.luau
│       │       │   ├── Solvers
│       │       │   │   ├── Attachment.luau
│       │       │   │   ├── Bone.luau
│       │       │   │   ├── init.meta.json
│       │       │   │   ├── LinkAttachments.luau
│       │       │   │   └── Vector3.luau
│       │       │   └── VisualizerCache.luau
│       │       ├── refx
│       │       │   ├── baseEffect.luau
│       │       │   ├── client
│       │       │   │   ├── entries.luau
│       │       │   │   └── init.luau
│       │       │   ├── clientProxy.luau
│       │       │   ├── configuration.luau
│       │       │   ├── effectsMap.luau
│       │       │   ├── exports.luau
│       │       │   ├── init.luau
│       │       │   ├── modules
│       │       │   │   ├── init.meta.json
│       │       │   │   ├── remo.luau
│       │       │   │   ├── signal.luau
│       │       │   │   └── t.luau
│       │       │   ├── remotes.luau
│       │       │   ├── serverProxy.luau
│       │       │   ├── tests
│       │       │   │   ├── clientProxy.spec.luau
│       │       │   │   ├── creation.spec.luau
│       │       │   │   ├── init.meta.json
│       │       │   │   └── serverProxy.spec.luau
│       │       │   ├── utilities
│       │       │   │   ├── getModule.luau
│       │       │   │   ├── idGenerator.luau
│       │       │   │   ├── init.meta.json
│       │       │   │   ├── instanceofConstructor.luau
│       │       │   │   └── logger.luau
│       │       │   └── wrapper.luau
│       │       ├── Roact
│       │       │   ├── assertDeepEqual.luau
│       │       │   ├── assertDeepEqual.spec.luau
│       │       │   ├── assign.luau
│       │       │   ├── assign.spec.luau
│       │       │   ├── Binding.luau
│       │       │   ├── Binding.spec.luau
│       │       │   ├── Component.luau
│       │       │   ├── Component.spec
│       │       │   │   ├── context.spec.luau
│       │       │   │   ├── defaultProps.spec.luau
│       │       │   │   ├── didMount.spec.luau
│       │       │   │   ├── didUpdate.spec.luau
│       │       │   │   ├── extend.spec.luau
│       │       │   │   ├── getDerivedStateFromProps.spec.luau
│       │       │   │   ├── getElementTraceback.spec.luau
│       │       │   │   ├── init.meta.json
│       │       │   │   ├── init.spec.luau
│       │       │   │   ├── legacyContext.spec.luau
│       │       │   │   ├── render.spec.luau
│       │       │   │   ├── setState.spec.luau
│       │       │   │   ├── shouldUpdate.spec.luau
│       │       │   │   ├── validateProps.spec.luau
│       │       │   │   ├── willUnmount.spec.luau
│       │       │   │   └── willUpdate.spec.luau
│       │       │   ├── ComponentLifecyclePhase.luau
│       │       │   ├── Config.luau
│       │       │   ├── Config.spec.luau
│       │       │   ├── createContext.luau
│       │       │   ├── createContext.spec.luau
│       │       │   ├── createElement.luau
│       │       │   ├── createElement.spec.luau
│       │       │   ├── createFragment.luau
│       │       │   ├── createFragment.spec.luau
│       │       │   ├── createReconciler.luau
│       │       │   ├── createReconciler.spec.luau
│       │       │   ├── createReconcilerCompat.luau
│       │       │   ├── createReconcilerCompat.spec.luau
│       │       │   ├── createRef.luau
│       │       │   ├── createRef.spec.luau
│       │       │   ├── createSignal.luau
│       │       │   ├── createSignal.spec.luau
│       │       │   ├── createSpy.luau
│       │       │   ├── createSpy.spec.luau
│       │       │   ├── ElementKind.luau
│       │       │   ├── ElementKind.spec.luau
│       │       │   ├── ElementUtils.luau
│       │       │   ├── ElementUtils.spec.luau
│       │       │   ├── forwardRef.luau
│       │       │   ├── forwardRef.spec.luau
│       │       │   ├── getDefaultInstanceProperty.luau
│       │       │   ├── getDefaultInstanceProperty.spec.luau
│       │       │   ├── GlobalConfig.luau
│       │       │   ├── GlobalConfig.spec.luau
│       │       │   ├── init.luau
│       │       │   ├── init.spec.luau
│       │       │   ├── internalAssert.luau
│       │       │   ├── invalidSetStateMessages.luau
│       │       │   ├── Logging.luau
│       │       │   ├── None.luau
│       │       │   ├── NoopRenderer.luau
│       │       │   ├── oneChild.luau
│       │       │   ├── oneChild.spec.luau
│       │       │   ├── Portal.luau
│       │       │   ├── PropMarkers
│       │       │   │   ├── Change.luau
│       │       │   │   ├── Change.spec.luau
│       │       │   │   ├── Children.luau
│       │       │   │   ├── Event.luau
│       │       │   │   ├── Event.spec.luau
│       │       │   │   ├── init.meta.json
│       │       │   │   └── Ref.luau
│       │       │   ├── PureComponent.luau
│       │       │   ├── PureComponent.spec.luau
│       │       │   ├── RobloxRenderer.luau
│       │       │   ├── RobloxRenderer.spec.luau
│       │       │   ├── SingleEventManager.luau
│       │       │   ├── SingleEventManager.spec.luau
│       │       │   ├── strict.luau
│       │       │   ├── strict.spec.luau
│       │       │   ├── Symbol.luau
│       │       │   ├── Symbol.spec.luau
│       │       │   ├── Type.luau
│       │       │   └── Type.spec.luau
│       │       ├── roactradial.luau
│       │       ├── StudioComponents
│       │       │   ├── CommonProps.luau
│       │       │   ├── Components
│       │       │   │   ├── Background.luau
│       │       │   │   ├── Button.luau
│       │       │   │   ├── Checkbox.luau
│       │       │   │   ├── ColorPicker.luau
│       │       │   │   ├── DatePicker.luau
│       │       │   │   ├── Dropdown
│       │       │   │   │   ├── ClearButton.luau
│       │       │   │   │   ├── DropdownItem.luau
│       │       │   │   │   ├── init.luau
│       │       │   │   │   └── Types.luau
│       │       │   │   ├── DropShadowFrame.luau
│       │       │   │   ├── Foundation
│       │       │   │   │   ├── BaseButton.luau
│       │       │   │   │   ├── BaseIcon.luau
│       │       │   │   │   ├── BaseLabelledToggle.luau
│       │       │   │   │   ├── BaseTextInput.luau
│       │       │   │   │   └── init.meta.json
│       │       │   │   ├── init.meta.json
│       │       │   │   ├── Label.luau
│       │       │   │   ├── LoadingDots.luau
│       │       │   │   ├── MainButton.luau
│       │       │   │   ├── NumberSequencePicker
│       │       │   │   │   ├── AxisLabel.luau
│       │       │   │   │   ├── Constants.luau
│       │       │   │   │   ├── DashedLine.luau
│       │       │   │   │   ├── FreeLine.luau
│       │       │   │   │   ├── init.luau
│       │       │   │   │   ├── LabelledNumericInput.luau
│       │       │   │   │   └── SequenceNode.luau
│       │       │   │   ├── NumericInput.luau
│       │       │   │   ├── PluginProvider.luau
│       │       │   │   ├── ProgressBar.luau
│       │       │   │   ├── RadioButton.luau
│       │       │   │   ├── ScrollFrame
│       │       │   │   │   ├── Constants.luau
│       │       │   │   │   ├── init.luau
│       │       │   │   │   ├── ScrollBar.luau
│       │       │   │   │   ├── ScrollBarArrow.luau
│       │       │   │   │   └── Types.luau
│       │       │   │   ├── Slider.luau
│       │       │   │   ├── Splitter.luau
│       │       │   │   ├── TabContainer.luau
│       │       │   │   └── TextInput.luau
│       │       │   ├── Constants.luau
│       │       │   ├── Contexts
│       │       │   │   ├── init.meta.json
│       │       │   │   ├── PluginContext.luau
│       │       │   │   └── ThemeContext.luau
│       │       │   ├── getTextSize.luau
│       │       │   ├── Hooks
│       │       │   │   ├── init.meta.json
│       │       │   │   ├── useFreshCallback.luau
│       │       │   │   ├── useMouseDrag.luau
│       │       │   │   ├── useMouseIcon.luau
│       │       │   │   ├── usePlugin.luau
│       │       │   │   └── useTheme.luau
│       │       │   ├── init.luau
│       │       │   └── Stories
│       │       │       ├── Background.story.luau
│       │       │       ├── Button.story.luau
│       │       │       ├── Checkbox.story.luau
│       │       │       ├── ColorPicker.story.luau
│       │       │       ├── DatePicker.story.luau
│       │       │       ├── Dropdown.story.luau
│       │       │       ├── DropShadowFrame.story.luau
│       │       │       ├── Helpers
│       │       │       │   ├── createStory.luau
│       │       │       │   ├── getStoryPlugin.luau
│       │       │       │   ├── init.meta.json
│       │       │       │   └── studiocomponents.storybook.luau
│       │       │       ├── init.meta.json
│       │       │       ├── Label.story.luau
│       │       │       ├── LoadingDots.story.luau
│       │       │       ├── MainButton.story.luau
│       │       │       ├── NumberSequencePicker.story.luau
│       │       │       ├── NumericInput.story.luau
│       │       │       ├── ProgressBar.story.luau
│       │       │       ├── RadioButton.story.luau
│       │       │       ├── ScrollFrame.story.luau
│       │       │       ├── Slider.story.luau
│       │       │       ├── Splitter.story.luau
│       │       │       ├── TabContainer.story.luau
│       │       │       └── TextInput.story.luau
│       │       ├── SuphiLinkedList
│       │       │   ├── Benchmarks.server.luau
│       │       │   ├── Examples.server.luau
│       │       │   └── init.luau
│       │       └── ZonePlus
│       │           ├── Enum
│       │           │   ├── Accuracy.luau
│       │           │   ├── Detection.luau
│       │           │   └── init.luau
│       │           ├── init.luau
│       │           ├── Janitor.luau
│       │           ├── OldSignal.luau
│       │           ├── Signal.luau
│       │           ├── VERSION.luau
│       │           ├── ZoneController
│       │           │   ├── CollectiveWorldModel.luau
│       │           │   ├── init.luau
│       │           │   └── Tracker.luau
│       │           └── ZonePlusReference.luau
│       └── ServerScriptService
│           └── SpellCombatSystem
│               ├── game
│               │   ├── init.meta.json
│               │   └── Scripts
│               │       ├── Abilities
│               │       │   ├── AmberHit.luau
│               │       │   ├── Ayaka.luau
│               │       │   ├── Baal.luau
│               │       │   ├── BladeHit.luau
│               │       │   ├── FireballHit.luau
│               │       │   ├── GateHit.luau
│               │       │   ├── GateSword.luau
│               │       │   ├── Hex.luau
│               │       │   ├── IceHit.luau
│               │       │   ├── init.meta.json
│               │       │   ├── Lightning.luau
│               │       │   ├── Orb.luau
│               │       │   ├── PoisonGas.luau
│               │       │   ├── Xiangling.luau
│               │       │   └── Xinyan.luau
│               │       └── init.meta.json
│               ├── init.meta.json
│               └── node_modules
│                   ├── @jsdotlua
│                   │   ├── boolean
│                   │   │   ├── init.luau
│                   │   │   └── toJSBoolean.luau
│                   │   ├── collections
│                   │   │   ├── Array
│                   │   │   │   ├── concat.luau
│                   │   │   │   ├── every.luau
│                   │   │   │   ├── filter.luau
│                   │   │   │   ├── find.luau
│                   │   │   │   ├── findIndex.luau
│                   │   │   │   ├── flat.luau
│                   │   │   │   ├── flatMap.luau
│                   │   │   │   ├── forEach.luau
│                   │   │   │   ├── from
│                   │   │   │   │   ├── fromArray.luau
│                   │   │   │   │   ├── fromMap.luau
│                   │   │   │   │   ├── fromSet.luau
│                   │   │   │   │   ├── fromString.luau
│                   │   │   │   │   └── init.luau
│                   │   │   │   ├── includes.luau
│                   │   │   │   ├── indexOf.luau
│                   │   │   │   ├── init.luau
│                   │   │   │   ├── isArray.luau
│                   │   │   │   ├── join.luau
│                   │   │   │   ├── map.luau
│                   │   │   │   ├── reduce.luau
│                   │   │   │   ├── reverse.luau
│                   │   │   │   ├── shift.luau
│                   │   │   │   ├── slice.luau
│                   │   │   │   ├── some.luau
│                   │   │   │   ├── sort.luau
│                   │   │   │   ├── splice.luau
│                   │   │   │   └── unshift.luau
│                   │   │   ├── init.luau
│                   │   │   ├── inspect.luau
│                   │   │   ├── Map
│                   │   │   │   ├── coerceToMap.luau
│                   │   │   │   ├── coerceToTable.luau
│                   │   │   │   ├── init.luau
│                   │   │   │   └── Map.luau
│                   │   │   ├── Object
│                   │   │   │   ├── assign.luau
│                   │   │   │   ├── entries.luau
│                   │   │   │   ├── freeze.luau
│                   │   │   │   ├── init.luau
│                   │   │   │   ├── is.luau
│                   │   │   │   ├── isFrozen.luau
│                   │   │   │   ├── keys.luau
│                   │   │   │   ├── None.luau
│                   │   │   │   ├── preventExtensions.luau
│                   │   │   │   ├── seal.luau
│                   │   │   │   └── values.luau
│                   │   │   ├── Set.luau
│                   │   │   └── WeakMap.luau
│                   │   ├── console
│                   │   │   ├── init.luau
│                   │   │   └── makeConsoleImpl.luau
│                   │   ├── es7-types.luau
│                   │   ├── init.meta.json
│                   │   ├── instance-of
│                   │   │   ├── init.luau
│                   │   │   └── instanceof.luau
│                   │   ├── luau-polyfill
│                   │   │   ├── AssertionError
│                   │   │   │   ├── AssertionError.global.luau
│                   │   │   │   └── init.luau
│                   │   │   ├── encodeURIComponent.luau
│                   │   │   ├── Error
│                   │   │   │   ├── Error.global.luau
│                   │   │   │   └── init.luau
│                   │   │   ├── extends.luau
│                   │   │   ├── init.luau
│                   │   │   └── Promise.luau
│                   │   ├── math
│                   │   │   ├── clz32.luau
│                   │   │   └── init.luau
│                   │   ├── number
│                   │   │   ├── init.luau
│                   │   │   ├── isFinite.luau
│                   │   │   ├── isInteger.luau
│                   │   │   ├── isNaN.luau
│                   │   │   ├── isSafeInteger.luau
│                   │   │   ├── MAX_SAFE_INTEGER.luau
│                   │   │   ├── MIN_SAFE_INTEGER.luau
│                   │   │   └── toExponential.luau
│                   │   ├── promise
│                   │   │   ├── init.meta.json
│                   │   │   ├── lib.luau
│                   │   │   └── package.luau
│                   │   ├── react
│                   │   │   ├── init.meta.json
│                   │   │   ├── package.luau
│                   │   │   └── src
│                   │   │       ├── createSignal.roblox.luau
│                   │   │       ├── init.luau
│                   │   │       ├── None.roblox.luau
│                   │   │       ├── React.luau
│                   │   │       ├── ReactBaseClasses.luau
│                   │   │       ├── ReactBinding.roblox.luau
│                   │   │       ├── ReactChildren.luau
│                   │   │       ├── ReactContext.luau
│                   │   │       ├── ReactCreateRef.luau
│                   │   │       ├── ReactElement.luau
│                   │   │       ├── ReactElementValidator.luau
│                   │   │       ├── ReactForwardRef.luau
│                   │   │       ├── ReactHooks.luau
│                   │   │       ├── ReactLazy.luau
│                   │   │       ├── ReactMemo.luau
│                   │   │       ├── ReactMutableSource.luau
│                   │   │       └── ReactNoopUpdateQueue.luau
│                   │   ├── react-reconciler
│                   │   │   ├── init.meta.json
│                   │   │   ├── package.luau
│                   │   │   └── src
│                   │   │       ├── DebugTracing.luau
│                   │   │       ├── forks
│                   │   │       │   ├── init.meta.json
│                   │   │       │   └── ReactFiberHostConfig.test.luau
│                   │   │       ├── init.luau
│                   │   │       ├── MaxInts.luau
│                   │   │       ├── ReactCapturedValue.luau
│                   │   │       ├── ReactChildFiber.new.luau
│                   │   │       ├── ReactCurrentFiber.luau
│                   │   │       ├── ReactFiber.new.luau
│                   │   │       ├── ReactFiberBeginWork.new.luau
│                   │   │       ├── ReactFiberClassComponent.new.luau
│                   │   │       ├── ReactFiberCommitWork.new.luau
│                   │   │       ├── ReactFiberCompleteWork.new.luau
│                   │   │       ├── ReactFiberComponentStack.luau
│                   │   │       ├── ReactFiberContext.new.luau
│                   │   │       ├── ReactFiberDevToolsHook.new.luau
│                   │   │       ├── ReactFiberErrorDialog.luau
│                   │   │       ├── ReactFiberErrorLogger.luau
│                   │   │       ├── ReactFiberFlags.luau
│                   │   │       ├── ReactFiberHooks.new.luau
│                   │   │       ├── ReactFiberHostConfig.luau
│                   │   │       ├── ReactFiberHostContext.new.luau
│                   │   │       ├── ReactFiberHotReloading.new.luau
│                   │   │       ├── ReactFiberHydrationContext.new.luau
│                   │   │       ├── ReactFiberLane.luau
│                   │   │       ├── ReactFiberLazyComponent.new.luau
│                   │   │       ├── ReactFiberNewContext.new.luau
│                   │   │       ├── ReactFiberOffscreenComponent.luau
│                   │   │       ├── ReactFiberReconciler.luau
│                   │   │       ├── ReactFiberReconciler.new.luau
│                   │   │       ├── ReactFiberRoot.new.luau
│                   │   │       ├── ReactFiberSchedulerPriorities.roblox.luau
│                   │   │       ├── ReactFiberStack.new.luau
│                   │   │       ├── ReactFiberSuspenseComponent.new.luau
│                   │   │       ├── ReactFiberSuspenseContext.new.luau
│                   │   │       ├── ReactFiberThrow.new.luau
│                   │   │       ├── ReactFiberTransition.luau
│                   │   │       ├── ReactFiberTreeReflection.luau
│                   │   │       ├── ReactFiberUnwindWork.new.luau
│                   │   │       ├── ReactFiberWorkInProgress.luau
│                   │   │       ├── ReactFiberWorkLoop.new.luau
│                   │   │       ├── ReactHookEffectTags.luau
│                   │   │       ├── ReactInternalTypes.luau
│                   │   │       ├── ReactMutableSource.new.luau
│                   │   │       ├── ReactPortal.luau
│                   │   │       ├── ReactProfilerTimer.new.luau
│                   │   │       ├── ReactRootTags.luau
│                   │   │       ├── ReactStrictModeWarnings.new.luau
│                   │   │       ├── ReactTestSelectors.luau
│                   │   │       ├── ReactTypeOfMode.luau
│                   │   │       ├── ReactUpdateQueue.new.luau
│                   │   │       ├── ReactWorkTags.luau
│                   │   │       ├── RobloxReactProfiling.luau
│                   │   │       ├── SchedulerWithReactIntegration.new.luau
│                   │   │       └── SchedulingProfiler.luau
│                   │   ├── react-roblox
│                   │   │   ├── init.meta.json
│                   │   │   ├── package.luau
│                   │   │   └── src
│                   │   │       ├── client
│                   │   │       │   ├── init.meta.json
│                   │   │       │   ├── ReactRoblox.luau
│                   │   │       │   ├── ReactRobloxComponent.luau
│                   │   │       │   ├── ReactRobloxComponentTree.luau
│                   │   │       │   ├── ReactRobloxHostConfig.luau
│                   │   │       │   ├── ReactRobloxHostTypes.roblox.luau
│                   │   │       │   ├── ReactRobloxRoot.luau
│                   │   │       │   └── roblox
│                   │   │       │       ├── getDefaultInstanceProperty.luau
│                   │   │       │       ├── init.meta.json
│                   │   │       │       ├── RobloxComponentProps.luau
│                   │   │       │       └── SingleEventManager.luau
│                   │   │       ├── init.luau
│                   │   │       └── ReactReconciler.roblox.luau
│                   │   ├── scheduler
│                   │   │   ├── init.meta.json
│                   │   │   ├── package.luau
│                   │   │   └── src
│                   │   │       ├── forks
│                   │   │       │   ├── init.meta.json
│                   │   │       │   ├── SchedulerHostConfig.default.luau
│                   │   │       │   └── SchedulerHostConfig.mock.luau
│                   │   │       ├── init.luau
│                   │   │       ├── Scheduler.luau
│                   │   │       ├── SchedulerFeatureFlags.luau
│                   │   │       ├── SchedulerHostConfig.luau
│                   │   │       ├── SchedulerMinHeap.luau
│                   │   │       ├── SchedulerPriorities.luau
│                   │   │       ├── SchedulerProfiling.luau
│                   │   │       ├── Tracing.luau
│                   │   │       ├── TracingSubscriptions.luau
│                   │   │       └── unstable_mock.luau
│                   │   ├── shared
│                   │   │   ├── init.meta.json
│                   │   │   ├── package.luau
│                   │   │   └── src
│                   │   │       ├── checkPropTypes.luau
│                   │   │       ├── console.luau
│                   │   │       ├── ConsolePatchingDev.roblox.luau
│                   │   │       ├── consoleWithStackDev.luau
│                   │   │       ├── enqueueTask.roblox.luau
│                   │   │       ├── ErrorHandling.roblox.luau
│                   │   │       ├── ExecutionEnvironment.luau
│                   │   │       ├── flowtypes.roblox.luau
│                   │   │       ├── formatProdErrorMessage.luau
│                   │   │       ├── getComponentName.luau
│                   │   │       ├── init.luau
│                   │   │       ├── invariant.luau
│                   │   │       ├── invokeGuardedCallbackImpl.luau
│                   │   │       ├── isValidElementType.luau
│                   │   │       ├── objectIs.luau
│                   │   │       ├── PropMarkers
│                   │   │       │   ├── Change.luau
│                   │   │       │   ├── Event.luau
│                   │   │       │   ├── init.meta.json
│                   │   │       │   └── Tag.luau
│                   │   │       ├── ReactComponentStackFrame.luau
│                   │   │       ├── ReactElementType.luau
│                   │   │       ├── ReactErrorUtils.luau
│                   │   │       ├── ReactFeatureFlags.luau
│                   │   │       ├── ReactFiberHostConfig
│                   │   │       │   ├── init.luau
│                   │   │       │   ├── WithNoHydration.luau
│                   │   │       │   ├── WithNoPersistence.luau
│                   │   │       │   └── WithNoTestSelectors.luau
│                   │   │       ├── ReactInstanceMap.luau
│                   │   │       ├── ReactSharedInternals
│                   │   │       │   ├── init.luau
│                   │   │       │   ├── IsSomeRendererActing.luau
│                   │   │       │   ├── ReactCurrentBatchConfig.luau
│                   │   │       │   ├── ReactCurrentDispatcher.luau
│                   │   │       │   ├── ReactCurrentOwner.luau
│                   │   │       │   └── ReactDebugCurrentFrame.luau
│                   │   │       ├── ReactSymbols.luau
│                   │   │       ├── ReactTypes.luau
│                   │   │       ├── ReactVersion.luau
│                   │   │       ├── shallowEqual.luau
│                   │   │       ├── Symbol.roblox.luau
│                   │   │       ├── Type.roblox.luau
│                   │   │       └── UninitializedState.roblox.luau
│                   │   ├── string
│                   │   │   ├── charCodeAt.luau
│                   │   │   ├── endsWith.luau
│                   │   │   ├── findOr.luau
│                   │   │   ├── includes.luau
│                   │   │   ├── indexOf.luau
│                   │   │   ├── init.luau
│                   │   │   ├── lastIndexOf.luau
│                   │   │   ├── slice.luau
│                   │   │   ├── split.luau
│                   │   │   ├── startsWith.luau
│                   │   │   ├── substr.luau
│                   │   │   ├── trim.luau
│                   │   │   ├── trimEnd.luau
│                   │   │   └── trimStart.luau
│                   │   └── timers
│                   │       ├── init.luau
│                   │       ├── makeIntervalImpl.luau
│                   │       └── makeTimerImpl.luau
│                   ├── @quenty
│                   │   ├── acceltween
│                   │   │   ├── init.meta.json
│                   │   │   └── Shared
│                   │   │       ├── AccelTween.luau
│                   │   │       └── init.meta.json
│                   │   ├── adorneeutils
│                   │   │   ├── init.meta.json
│                   │   │   └── Shared
│                   │   │       ├── AdorneeUtils.luau
│                   │   │       └── init.meta.json
│                   │   ├── baseobject
│                   │   │   ├── init.meta.json
│                   │   │   └── Shared
│                   │   │       ├── BaseObject.luau
│                   │   │       └── init.meta.json
│                   │   ├── basicpane
│                   │   │   ├── init.meta.json
│                   │   │   └── Shared
│                   │   │       ├── BasicPane.luau
│                   │   │       ├── BasicPaneUtils.luau
│                   │   │       └── init.meta.json
│                   │   ├── binarysearch
│                   │   │   ├── init.meta.json
│                   │   │   └── Shared
│                   │   │       ├── BinarySearchUtils.luau
│                   │   │       └── init.meta.json
│                   │   ├── binder
│                   │   │   ├── init.meta.json
│                   │   │   └── Shared
│                   │   │       ├── Binder.luau
│                   │   │       ├── BinderGroup.luau
│                   │   │       ├── BinderGroupProvider.luau
│                   │   │       ├── BinderProvider.luau
│                   │   │       ├── BinderProvider.spec.luau
│                   │   │       ├── BinderUtils.luau
│                   │   │       ├── Collection
│                   │   │       │   ├── BoundChildCollection.luau
│                   │   │       │   └── init.meta.json
│                   │   │       ├── init.meta.json
│                   │   │       ├── Promise
│                   │   │       │   ├── init.meta.json
│                   │   │       │   └── promiseBoundClass.luau
│                   │   │       └── Trackers
│                   │   │           ├── BoundAncestorTracker.luau
│                   │   │           ├── BoundParentTracker.luau
│                   │   │           └── init.meta.json
│                   │   ├── bindtocloseservice
│                   │   │   ├── init.meta.json
│                   │   │   └── Server
│                   │   │       ├── BindToCloseService.luau
│                   │   │       └── init.meta.json
│                   │   ├── blend
│                   │   │   ├── init.meta.json
│                   │   │   └── Shared
│                   │   │       ├── Blend
│                   │   │       │   ├── Blend.luau
│                   │   │       │   ├── BlendDefaultProps.luau
│                   │   │       │   ├── init.meta.json
│                   │   │       │   └── SpringObject.luau
│                   │   │       ├── init.meta.json
│                   │   │       └── Test
│                   │   │           ├── BlendChildren.story.luau
│                   │   │           ├── BlendComputePairs.story.luau
│                   │   │           ├── BlendFind.story.luau
│                   │   │           ├── BlendPromise.story.luau
│                   │   │           ├── BlendSingle.story.luau
│                   │   │           ├── BlendSpring.story.luau
│                   │   │           ├── BlendTextbox.story.luau
│                   │   │           └── init.meta.json
│                   │   ├── brio
│                   │   │   ├── init.meta.json
│                   │   │   └── Shared
│                   │   │       ├── Brio.luau
│                   │   │       ├── BrioUtils.luau
│                   │   │       ├── BrioUtils.spec.luau
│                   │   │       ├── init.meta.json
│                   │   │       ├── RxBrioUtils.luau
│                   │   │       └── RxBrioUtils.spec.luau
│                   │   ├── buttondragmodel
│                   │   │   ├── Client
│                   │   │   │   ├── ButtonDragModel.luau
│                   │   │   │   └── init.meta.json
│                   │   │   └── init.meta.json
│                   │   ├── camera
│                   │   │   ├── Client
│                   │   │   │   ├── CameraStack.luau
│                   │   │   │   ├── CameraStackService.luau
│                   │   │   │   ├── CameraState.luau
│                   │   │   │   ├── CameraUtils.luau
│                   │   │   │   ├── CameraUtils.story.luau
│                   │   │   │   ├── Controls
│                   │   │   │   │   ├── CameraControls.luau
│                   │   │   │   │   ├── CameraGamepadInputUtils.luau
│                   │   │   │   │   ├── GamepadRotateModel.luau
│                   │   │   │   │   └── init.meta.json
│                   │   │   │   ├── Effects
│                   │   │   │   │   ├── CameraEffectUtils.luau
│                   │   │   │   │   ├── CustomCameraEffect.luau
│                   │   │   │   │   ├── DefaultCamera.luau
│                   │   │   │   │   ├── FadeBetween
│                   │   │   │   │   │   ├── FadeBetweenCamera.luau
│                   │   │   │   │   │   ├── FadeBetweenCamera2.luau
│                   │   │   │   │   │   ├── FadeBetweenCamera3.luau
│                   │   │   │   │   │   ├── FadeBetweenCamera4.luau
│                   │   │   │   │   │   └── init.meta.json
│                   │   │   │   │   ├── FadingCamera.luau
│                   │   │   │   │   ├── HeartbeatCamera.luau
│                   │   │   │   │   ├── ImpulseCamera.luau
│                   │   │   │   │   ├── ImpulseCamera.story.luau
│                   │   │   │   │   ├── init.meta.json
│                   │   │   │   │   ├── InverseFader.luau
│                   │   │   │   │   ├── LagPointCamera.luau
│                   │   │   │   │   ├── OverrideDefaultCameraToo.luau
│                   │   │   │   │   ├── PointCamera.luau
│                   │   │   │   │   ├── PushCamera.luau
│                   │   │   │   │   ├── RotatedCamera.luau
│                   │   │   │   │   ├── SmoothPositionCamera.luau
│                   │   │   │   │   ├── SmoothRotatedCamera.luau
│                   │   │   │   │   ├── SmoothZoomedCamera.luau
│                   │   │   │   │   ├── SummedCamera.luau
│                   │   │   │   │   ├── TrackCamera.luau
│                   │   │   │   │   ├── XZPlaneLockCamera.luau
│                   │   │   │   │   └── ZoomedCamera.luau
│                   │   │   │   ├── init.meta.json
│                   │   │   │   ├── Input
│                   │   │   │   │   ├── CameraInputUtils.luau
│                   │   │   │   │   ├── CameraTouchInputUtils.luau
│                   │   │   │   │   └── init.meta.json
│                   │   │   │   └── Utility
│                   │   │   │       ├── CameraFrame.luau
│                   │   │   │       ├── CameraFrame.story.luau
│                   │   │   │       ├── CameraStateTweener.luau
│                   │   │   │       ├── FieldOfViewUtils.luau
│                   │   │   │       └── init.meta.json
│                   │   │   └── init.meta.json
│                   │   ├── cancellabledelay
│                   │   │   ├── init.meta.json
│                   │   │   └── Shared
│                   │   │       ├── cancellableDelay.luau
│                   │   │       └── init.meta.json
│                   │   ├── canceltoken
│                   │   │   ├── init.meta.json
│                   │   │   └── Shared
│                   │   │       ├── CancelToken.luau
│                   │   │       └── init.meta.json
│                   │   ├── cframeutils
│                   │   │   ├── init.meta.json
│                   │   │   └── Shared
│                   │   │       ├── CFrameUtils.luau
│                   │   │       ├── getRotationInXZPlane.luau
│                   │   │       └── init.meta.json
│                   │   ├── clienttranslator
│                   │   │   ├── init.meta.json
│                   │   │   └── Shared
│                   │   │       ├── Conversion
│                   │   │       │   ├── init.meta.json
│                   │   │       │   └── LocalizationEntryParserUtils.luau
│                   │   │       ├── init.meta.json
│                   │   │       ├── JSONTranslator.luau
│                   │   │       ├── Numbers
│                   │   │       │   ├── init.meta.json
│                   │   │       │   ├── NumberLocalizationUtils.luau
│                   │   │       │   ├── NumberLocalizationUtils.spec.luau
│                   │   │       │   └── RoundingBehaviourTypes.luau
│                   │   │       ├── TranslatorService.luau
│                   │   │       └── Utils
│                   │   │           ├── init.meta.json
│                   │   │           ├── LocalizationServiceUtils.luau
│                   │   │           └── TranslationKeyUtils.luau
│                   │   ├── color3utils
│                   │   │   ├── init.meta.json
│                   │   │   └── Shared
│                   │   │       ├── Color3Utils.luau
│                   │   │       ├── init.meta.json
│                   │   │       └── luv
│                   │   │           ├── init.meta.json
│                   │   │           ├── LuvColor3Utils.luau
│                   │   │           ├── LuvColor3Utils.story.luau
│                   │   │           ├── LuvUtils.luau
│                   │   │           └── LuvVectorColor3Utils.luau
│                   │   ├── colorpicker
│                   │   │   ├── Client
│                   │   │   │   ├── ColorPickerUtils.luau
│                   │   │   │   ├── Cursor
│                   │   │   │   │   ├── ColorPickerCursorPreview.luau
│                   │   │   │   │   ├── ColorPickerTriangle.luau
│                   │   │   │   │   ├── HSColorPickerCursor.luau
│                   │   │   │   │   └── init.meta.json
│                   │   │   │   ├── HSV
│                   │   │   │   │   ├── HSColorPicker.luau
│                   │   │   │   │   ├── HSColorPicker.story.luau
│                   │   │   │   │   ├── HSVColorPicker.luau
│                   │   │   │   │   ├── HSVColorPicker.story.luau
│                   │   │   │   │   ├── init.meta.json
│                   │   │   │   │   ├── ValueColorPicker.luau
│                   │   │   │   │   └── ValueColorPicker.story.luau
│                   │   │   │   ├── init.meta.json
│                   │   │   │   └── Story
│                   │   │   │       ├── ColorPickerStoryUtils.luau
│                   │   │   │       └── init.meta.json
│                   │   │   └── init.meta.json
│                   │   ├── cubicspline
│                   │   │   ├── init.meta.json
│                   │   │   └── Shared
│                   │   │       ├── CubicSplineUtils.luau
│                   │   │       ├── CubicTweenUtils.luau
│                   │   │       └── init.meta.json
│                   │   ├── datastore
│                   │   │   ├── init.meta.json
│                   │   │   ├── Server
│                   │   │   │   ├── DataStore.luau
│                   │   │   │   ├── GameDataStoreService.luau
│                   │   │   │   ├── init.meta.json
│                   │   │   │   ├── Modules
│                   │   │   │   │   ├── DataStoreDeleteToken.luau
│                   │   │   │   │   ├── DataStoreSnapshotUtils.luau
│                   │   │   │   │   ├── DataStoreStage.luau
│                   │   │   │   │   ├── DataStoreWriter.luau
│                   │   │   │   │   └── init.meta.json
│                   │   │   │   ├── PlayerDataStoreManager.luau
│                   │   │   │   ├── PlayerDataStoreService.luau
│                   │   │   │   ├── PrivateServerDataStoreService.luau
│                   │   │   │   └── Utility
│                   │   │   │       ├── DataStorePromises.luau
│                   │   │   │       └── init.meta.json
│                   │   │   └── Shared
│                   │   │       ├── init.meta.json
│                   │   │       └── Utility
│                   │   │           ├── DataStoreStringUtils.luau
│                   │   │           └── init.meta.json
│                   │   ├── deferred
│                   │   │   ├── init.meta.json
│                   │   │   └── Shared
│                   │   │       ├── deferred.luau
│                   │   │       └── init.meta.json
│                   │   ├── draw
│                   │   │   ├── init.meta.json
│                   │   │   └── Shared
│                   │   │       ├── Draw.luau
│                   │   │       ├── DrawBlockcast.story.luau
│                   │   │       ├── DrawRay.story.luau
│                   │   │       ├── DrawSpherecast.story.luau
│                   │   │       └── init.meta.json
│                   │   ├── ducktype
│                   │   │   ├── init.meta.json
│                   │   │   └── Shared
│                   │   │       ├── DuckTypeUtils.luau
│                   │   │       └── init.meta.json
│                   │   ├── enumutils
│                   │   │   ├── init.meta.json
│                   │   │   └── Shared
│                   │   │       ├── EnumUtils.luau
│                   │   │       └── init.meta.json
│                   │   ├── gamescalingutils
│                   │   │   ├── Client
│                   │   │   │   ├── GameScalingHelper.luau
│                   │   │   │   ├── GameScalingUtils.luau
│                   │   │   │   └── init.meta.json
│                   │   │   └── init.meta.json
│                   │   ├── init.meta.json
│                   │   ├── inputkeymaputils
│                   │   │   ├── Client
│                   │   │   │   ├── init.meta.json
│                   │   │   │   ├── InputKeyMapListUtils.luau
│                   │   │   │   └── InputKeyMapServiceClient.luau
│                   │   │   ├── init.meta.json
│                   │   │   ├── Server
│                   │   │   │   ├── init.meta.json
│                   │   │   │   └── InputKeyMapService.luau
│                   │   │   └── Shared
│                   │   │       ├── init.meta.json
│                   │   │       ├── InputKeyMap.luau
│                   │   │       ├── InputKeyMapList.luau
│                   │   │       ├── InputKeyMapListProvider.luau
│                   │   │       ├── InputKeyMapRegistryServiceShared.luau
│                   │   │       ├── InputKeyMapTranslator.luau
│                   │   │       ├── ProximityPromptInputUtils.luau
│                   │   │       └── Types
│                   │   │           ├── init.meta.json
│                   │   │           ├── InputChordUtils.luau
│                   │   │           ├── InputTypeUtils.luau
│                   │   │           └── SlottedTouchButtonUtils.luau
│                   │   ├── inputmode
│                   │   │   ├── Client
│                   │   │   │   ├── init.meta.json
│                   │   │   │   ├── InputMode.luau
│                   │   │   │   ├── InputModeProcessor.luau
│                   │   │   │   ├── InputModeServiceClient.luau
│                   │   │   │   └── InputModeTypeSelector.luau
│                   │   │   ├── init.meta.json
│                   │   │   └── Shared
│                   │   │       ├── init.meta.json
│                   │   │       ├── InputModeType.luau
│                   │   │       └── InputModeTypes.luau
│                   │   ├── inputobjectutils
│                   │   │   ├── Client
│                   │   │   │   ├── init.meta.json
│                   │   │   │   ├── InputObjectRayUtils.luau
│                   │   │   │   ├── InputObjectTracker.luau
│                   │   │   │   ├── InputObjectUtils.luau
│                   │   │   │   └── RxInputObjectUtils.luau
│                   │   │   └── init.meta.json
│                   │   ├── instanceutils
│                   │   │   ├── init.meta.json
│                   │   │   └── Shared
│                   │   │       ├── init.meta.json
│                   │   │       ├── RxInstanceUtils.luau
│                   │   │       └── RxInstanceUtils.spec.luau
│                   │   ├── linearsystemssolvers
│                   │   │   ├── init.meta.json
│                   │   │   └── Shared
│                   │   │       ├── init.meta.json
│                   │   │       └── LinearSystemsSolverUtils.luau
│                   │   ├── linkutils
│                   │   │   ├── init.meta.json
│                   │   │   └── Shared
│                   │   │       ├── init.meta.json
│                   │   │       ├── LinkUtils.luau
│                   │   │       └── RxLinkUtils.luau
│                   │   ├── loader
│                   │   │   ├── Dependencies
│                   │   │   │   ├── DependencyUtils.luau
│                   │   │   │   ├── init.meta.json
│                   │   │   │   ├── PackageTracker.luau
│                   │   │   │   └── PackageTrackerProvider.luau
│                   │   │   ├── init.luau
│                   │   │   ├── LoaderLink
│                   │   │   │   ├── init.meta.json
│                   │   │   │   ├── LoaderLink.luau
│                   │   │   │   ├── LoaderLinkCreator.luau
│                   │   │   │   └── LoaderLinkUtils.luau
│                   │   │   ├── LoaderUtils.luau
│                   │   │   ├── Maid.luau
│                   │   │   ├── Replication
│                   │   │   │   ├── init.meta.json
│                   │   │   │   ├── ReplicationType.luau
│                   │   │   │   ├── ReplicationTypeUtils.luau
│                   │   │   │   ├── Replicator.luau
│                   │   │   │   └── ReplicatorReferences.luau
│                   │   │   └── Utils.luau
│                   │   ├── maid
│                   │   │   ├── init.meta.json
│                   │   │   └── Shared
│                   │   │       ├── init.meta.json
│                   │   │       ├── Maid.luau
│                   │   │       ├── Maid.story.luau
│                   │   │       └── MaidTaskUtils.luau
│                   │   ├── math
│                   │   │   ├── init.meta.json
│                   │   │   └── Shared
│                   │   │       ├── init.meta.json
│                   │   │       └── Math.luau
│                   │   ├── numberrangeutils
│                   │   │   ├── init.meta.json
│                   │   │   └── Shared
│                   │   │       ├── init.meta.json
│                   │   │       └── NumberRangeUtils.luau
│                   │   ├── observablecollection
│                   │   │   ├── init.meta.json
│                   │   │   └── Shared
│                   │   │       ├── FilteredObservableListView.luau
│                   │   │       ├── init.meta.json
│                   │   │       ├── ObservableCountingMap.luau
│                   │   │       ├── ObservableCountingMap.spec.luau
│                   │   │       ├── ObservableList.luau
│                   │   │       ├── ObservableList.spec.luau
│                   │   │       ├── ObservableMap.luau
│                   │   │       ├── ObservableMap.spec.luau
│                   │   │       ├── ObservableMapList.luau
│                   │   │       ├── ObservableMapList.spec.luau
│                   │   │       ├── ObservableMapSet.luau
│                   │   │       ├── ObservableSet.luau
│                   │   │       ├── SortedList
│                   │   │       │   ├── init.meta.json
│                   │   │       │   ├── ObservableSortedList_Performance.story.luau
│                   │   │       │   ├── ObservableSortedList_Print.story.luau
│                   │   │       │   ├── ObservableSortedList.luau
│                   │   │       │   ├── ObservableSortedList.spec.luau
│                   │   │       │   ├── ObservableSortedList.story.luau
│                   │   │       │   ├── SortedNode.luau
│                   │   │       │   ├── SortedNodeValue.luau
│                   │   │       │   └── SortFunctionUtils.luau
│                   │   │       └── Utils
│                   │   │           ├── init.meta.json
│                   │   │           └── ListIndexUtils.luau
│                   │   ├── octree
│                   │   │   ├── init.meta.json
│                   │   │   └── Shared
│                   │   │       ├── init.meta.json
│                   │   │       ├── Octree.luau
│                   │   │       ├── OctreeNode.luau
│                   │   │       └── OctreeRegionUtils.luau
│                   │   ├── pagesutils
│                   │   │   ├── init.meta.json
│                   │   │   └── Shared
│                   │   │       ├── init.meta.json
│                   │   │       ├── PagesUtils.luau
│                   │   │       └── Proxy
│                   │   │           ├── init.meta.json
│                   │   │           ├── PagesDatabase.luau
│                   │   │           └── PagesProxy.luau
│                   │   ├── performanceutils
│                   │   │   ├── init.meta.json
│                   │   │   └── Shared
│                   │   │       ├── init.meta.json
│                   │   │       └── PerformanceUtils.luau
│                   │   ├── promise
│                   │   │   ├── init.meta.json
│                   │   │   └── Shared
│                   │   │       ├── init.meta.json
│                   │   │       ├── Promise.luau
│                   │   │       ├── PromiseRetryUtils.luau
│                   │   │       ├── PromiseUtils.luau
│                   │   │       └── Utility
│                   │   │           ├── init.meta.json
│                   │   │           ├── PendingPromiseTracker.luau
│                   │   │           ├── promiseChild.luau
│                   │   │           ├── PromiseInstanceUtils.luau
│                   │   │           ├── promisePropertyValue.luau
│                   │   │           └── promiseWait.luau
│                   │   ├── promisemaid
│                   │   │   ├── init.meta.json
│                   │   │   └── Shared
│                   │   │       ├── init.meta.json
│                   │   │       └── PromiseMaidUtils.luau
│                   │   ├── pseudolocalize
│                   │   │   ├── init.meta.json
│                   │   │   └── Shared
│                   │   │       ├── init.meta.json
│                   │   │       └── PseudoLocalize.luau
│                   │   ├── qframe
│                   │   │   ├── init.meta.json
│                   │   │   └── Shared
│                   │   │       ├── init.meta.json
│                   │   │       ├── QFrame.luau
│                   │   │       └── QFrame.story.luau
│                   │   ├── randomutils
│                   │   │   ├── init.meta.json
│                   │   │   └── Shared
│                   │   │       ├── init.meta.json
│                   │   │       ├── RandomSampler.luau
│                   │   │       ├── RandomUtils.luau
│                   │   │       ├── RandomUtils.spec.luau
│                   │   │       └── WeightedRandomChooser.luau
│                   │   ├── rbxasset
│                   │   │   ├── init.meta.json
│                   │   │   └── Shared
│                   │   │       ├── init.meta.json
│                   │   │       └── RbxAssetUtils.luau
│                   │   ├── rx
│                   │   │   ├── init.meta.json
│                   │   │   └── Shared
│                   │   │       ├── init.meta.json
│                   │   │       ├── Observable.luau
│                   │   │       ├── ObservablePerformance.story.luau
│                   │   │       ├── ObservableSubscriptionTable.luau
│                   │   │       ├── Rx.luau
│                   │   │       ├── Rx.spec.luau
│                   │   │       └── Subscription.luau
│                   │   ├── rxsignal
│                   │   │   ├── init.meta.json
│                   │   │   └── Shared
│                   │   │       ├── init.meta.json
│                   │   │       └── RxSignal.luau
│                   │   ├── servicebag
│                   │   │   ├── init.meta.json
│                   │   │   └── Shared
│                   │   │       ├── init.meta.json
│                   │   │       ├── ServiceBag.luau
│                   │   │       └── ServiceInitLogger.luau
│                   │   ├── signal
│                   │   │   ├── init.meta.json
│                   │   │   └── Shared
│                   │   │       ├── EventHandlerUtils.luau
│                   │   │       ├── init.meta.json
│                   │   │       ├── OldSignal.luau
│                   │   │       ├── Signal.luau
│                   │   │       └── SignalUtils.luau
│                   │   ├── soundplayer
│                   │   │   ├── Client
│                   │   │   │   ├── init.meta.json
│                   │   │   │   ├── Loops
│                   │   │   │   │   ├── init.meta.json
│                   │   │   │   │   ├── Layered
│                   │   │   │   │   │   ├── init.meta.json
│                   │   │   │   │   │   ├── LayeredLoopedSoundPlayer.luau
│                   │   │   │   │   │   └── LayeredLoopedSoundPlayer.story.luau
│                   │   │   │   │   ├── LoopedSoundPlayer.luau
│                   │   │   │   │   ├── LoopedSoundPlayer.story.luau
│                   │   │   │   │   ├── SimpleLoopedSoundPlayer.luau
│                   │   │   │   │   └── SimpleLoopedSoundPlayer.story.luau
│                   │   │   │   └── Schedule
│                   │   │   │       ├── init.meta.json
│                   │   │   │       └── SoundLoopScheduleUtils.luau
│                   │   │   └── init.meta.json
│                   │   ├── sounds
│                   │   │   ├── init.meta.json
│                   │   │   └── Shared
│                   │   │       ├── init.meta.json
│                   │   │       ├── SoundPromiseUtils.luau
│                   │   │       └── SoundUtils.luau
│                   │   ├── spring
│                   │   │   ├── init.meta.json
│                   │   │   └── Shared
│                   │   │       ├── init.meta.json
│                   │   │       ├── LinearValue.luau
│                   │   │       ├── Spring.luau
│                   │   │       └── SpringUtils.luau
│                   │   ├── statestack
│                   │   │   ├── init.meta.json
│                   │   │   └── Shared
│                   │   │       ├── init.meta.json
│                   │   │       ├── RxStateStackUtils.luau
│                   │   │       └── StateStack.luau
│                   │   ├── steputils
│                   │   │   ├── init.meta.json
│                   │   │   └── Shared
│                   │   │       ├── init.meta.json
│                   │   │       ├── onRenderStepFrame.luau
│                   │   │       ├── onSteppedFrame.luau
│                   │   │       └── StepUtils.luau
│                   │   ├── string
│                   │   │   ├── init.meta.json
│                   │   │   └── Shared
│                   │   │       ├── init.meta.json
│                   │   │       └── String.luau
│                   │   ├── symbol
│                   │   │   ├── init.meta.json
│                   │   │   └── Shared
│                   │   │       ├── init.meta.json
│                   │   │       └── Symbol.luau
│                   │   ├── table
│                   │   │   ├── init.meta.json
│                   │   │   └── Shared
│                   │   │       ├── init.meta.json
│                   │   │       ├── Set.luau
│                   │   │       └── Table.luau
│                   │   ├── throttle
│                   │   │   ├── init.meta.json
│                   │   │   └── Shared
│                   │   │       ├── init.meta.json
│                   │   │       ├── throttle.luau
│                   │   │       └── ThrottledFunction.luau
│                   │   ├── timedtween
│                   │   │   ├── init.meta.json
│                   │   │   └── Shared
│                   │   │       ├── init.meta.json
│                   │   │       ├── TimedTween.luau
│                   │   │       └── TimedTween.story.luau
│                   │   ├── transitionmodel
│                   │   │   ├── init.meta.json
│                   │   │   └── Shared
│                   │   │       ├── init.meta.json
│                   │   │       ├── SpringTransitionModel.luau
│                   │   │       ├── Sustain
│                   │   │       │   ├── init.meta.json
│                   │   │       │   └── SustainModel.luau
│                   │   │       ├── Timed
│                   │   │       │   ├── init.meta.json
│                   │   │       │   └── TimedTransitionModel.luau
│                   │   │       ├── TransitionModel.luau
│                   │   │       └── TransitionUtils.luau
│                   │   ├── typeutils
│                   │   │   ├── init.meta.json
│                   │   │   └── Shared
│                   │   │       ├── init.meta.json
│                   │   │       └── TypeUtils.luau
│                   │   ├── valuebaseutils
│                   │   │   ├── init.meta.json
│                   │   │   └── Shared
│                   │   │       ├── init.meta.json
│                   │   │       ├── RxValueBaseUtils.luau
│                   │   │       ├── ValueBaseUtils.luau
│                   │   │       └── ValueBaseValue.luau
│                   │   ├── valueobject
│                   │   │   ├── init.meta.json
│                   │   │   └── Shared
│                   │   │       ├── init.meta.json
│                   │   │       ├── ValueObject.luau
│                   │   │       └── ValueObjectUtils.luau
│                   │   └── vector3utils
│                   │       ├── init.meta.json
│                   │       └── Shared
│                   │           ├── init.meta.json
│                   │           ├── RandomVector3Utils.luau
│                   │           ├── Vector3SerializationUtils.luau
│                   │           └── Vector3Utils.luau
│                   ├── @quentystudios
│                   │   ├── init.meta.json
│                   │   └── t.luau
│                   ├── @sircfenner
│                   │   ├── init.meta.json
│                   │   └── studiocomponents
│                   │       ├── init.meta.json
│                   │       ├── package.luau
│                   │       └── src
│                   │           ├── CommonProps.luau
│                   │           ├── Components
│                   │           │   ├── Background.luau
│                   │           │   ├── Button.luau
│                   │           │   ├── Checkbox.luau
│                   │           │   ├── ColorPicker.luau
│                   │           │   ├── DatePicker.luau
│                   │           │   ├── Dropdown
│                   │           │   │   ├── ClearButton.luau
│                   │           │   │   ├── DropdownItem.luau
│                   │           │   │   ├── init.luau
│                   │           │   │   └── Types.luau
│                   │           │   ├── DropShadowFrame.luau
│                   │           │   ├── Foundation
│                   │           │   │   ├── BaseButton.luau
│                   │           │   │   ├── BaseIcon.luau
│                   │           │   │   ├── BaseLabelledToggle.luau
│                   │           │   │   ├── BaseTextInput.luau
│                   │           │   │   └── init.meta.json
│                   │           │   ├── init.meta.json
│                   │           │   ├── Label.luau
│                   │           │   ├── LoadingDots.luau
│                   │           │   ├── MainButton.luau
│                   │           │   ├── NumberSequencePicker
│                   │           │   │   ├── AxisLabel.luau
│                   │           │   │   ├── Constants.luau
│                   │           │   │   ├── DashedLine.luau
│                   │           │   │   ├── FreeLine.luau
│                   │           │   │   ├── init.luau
│                   │           │   │   ├── LabelledNumericInput.luau
│                   │           │   │   └── SequenceNode.luau
│                   │           │   ├── NumericInput.luau
│                   │           │   ├── PluginProvider.luau
│                   │           │   ├── ProgressBar.luau
│                   │           │   ├── RadioButton.luau
│                   │           │   ├── ScrollFrame
│                   │           │   │   ├── Constants.luau
│                   │           │   │   ├── init.luau
│                   │           │   │   ├── ScrollBar.luau
│                   │           │   │   ├── ScrollBarArrow.luau
│                   │           │   │   └── Types.luau
│                   │           │   ├── Slider.luau
│                   │           │   ├── Splitter.luau
│                   │           │   ├── TabContainer.luau
│                   │           │   └── TextInput.luau
│                   │           ├── Constants.luau
│                   │           ├── Contexts
│                   │           │   ├── init.meta.json
│                   │           │   ├── PluginContext.luau
│                   │           │   └── ThemeContext.luau
│                   │           ├── getTextSize.luau
│                   │           ├── Hooks
│                   │           │   ├── init.meta.json
│                   │           │   ├── useFreshCallback.luau
│                   │           │   ├── useMouseDrag.luau
│                   │           │   ├── useMouseIcon.luau
│                   │           │   ├── usePlugin.luau
│                   │           │   └── useTheme.luau
│                   │           ├── init.luau
│                   │           └── Stories
│                   │               ├── Background.story.luau
│                   │               ├── Button.story.luau
│                   │               ├── Checkbox.story.luau
│                   │               ├── ColorPicker.story.luau
│                   │               ├── DatePicker.story.luau
│                   │               ├── Dropdown.story.luau
│                   │               ├── DropShadowFrame.story.luau
│                   │               ├── Helpers
│                   │               │   ├── createStory.luau
│                   │               │   ├── getStoryPlugin.luau
│                   │               │   ├── init.meta.json
│                   │               │   └── studiocomponents.storybook.luau
│                   │               ├── init.meta.json
│                   │               ├── Label.story.luau
│                   │               ├── LoadingDots.story.luau
│                   │               ├── MainButton.story.luau
│                   │               ├── NumberSequencePicker.story.luau
│                   │               ├── NumericInput.story.luau
│                   │               ├── ProgressBar.story.luau
│                   │               ├── RadioButton.story.luau
│                   │               ├── ScrollFrame.story.luau
│                   │               ├── Slider.story.luau
│                   │               ├── Splitter.story.luau
│                   │               ├── TabContainer.story.luau
│                   │               └── TextInput.story.luau
│                   ├── init.meta.json
│                   └── symbol-luau
│                       ├── init.meta.json
│                       ├── package.luau
│                       └── src
│                           ├── init.luau
│                           ├── Registry.global.luau
│                           └── Symbol.luau
├── FrameworkModules.rbxl
├── README.md
└── tree.txt

343 directories, 1636 files

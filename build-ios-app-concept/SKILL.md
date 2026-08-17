---
name: build-ios-app-concept
description: Create, implement, build, launch, and verify a programmatic UIKit iPhone application from an explicitly approved AppSpec and visual design. Use only after the idea, feature-specific permission copy, permission-review matrix, data inventory, screens, permission UX, visual system, and app icon are approved. Build the smallest permission-centered iOS 15 application with all required permissions, configurable privacy-aware AppMetrica, low mutable static state, Lock Screen widget, notification service/content extensions, Privacy Manifest and entitlement validation, and a minimal working backend. Exclude iPad, Mac, Mac Catalyst, Designed for iPhone/iPad on Mac, visionOS, Apple Vision, storyboards, XIBs, and test targets.
---

# Build iOS App Concept

## Goal

Implement an explicitly design-approved `AppSpec.md` as the smallest working portrait-only iPhone application. Treat the specification and approved design artifacts as the source of truth. Exercise every required authorization through a real, reviewable function and write only the supporting navigation, state, configuration, analytics, privacy, extensions, networking, error handling, and verification code needed to make those functions work.

Do not redesign the product, silently rewrite permission copy, or add unapproved features. Minimize total source files, types, lines, and long-lived state without obscuring resource ownership. This skill verifies local implementation quality but does not replace the later App Store preparation workflow.

## Required handoff

Require:

- `AppSpec.md` with `idea-approved` and `design-status: approved`, or equivalent explicit statuses recorded in the file.
- Approved portrait mockups, screen inventory, permission-to-screen mapping, visual system, accessibility behavior, widget and notification layouts, and app-icon source.
- Exact feature-specific permission and pre-permission copy for all required authorization categories.
- Approved permission-review matrix, data inventory, AppMetrica and ATT behavior, extension roles, and minimal backend contract.
- Destination parent directory or an existing project path.
- Product/module name and bundle identifier or bundle-identifier prefix.

If idea or design approval is missing, stop and propose `generate-ios-app-ideas` or `design-ios-app-concept` as appropriate. Do not perform the missing approval inside this implementation skill.

Before editing, compare the specification, mockups, permission matrix, data inventory, backend contract, and extension roles. Report contradictions instead of resolving them silently. Preserve accepted decisions unless a concrete implementation, platform, privacy, or review conflict requires renewed user approval.

Ask only for missing blocking inputs. Allow an empty configurable AppMetrica key. Request Apple Developer Team details only when device signing or capabilities require them. Treat production backend, privacy-policy, support, Terms, and EULA values as non-blocking `pending` items for the App Store preparation workflow.

Do not require the user to create an empty Xcode project. Create the directory and targets after inspecting the destination. Never overwrite a non-empty directory, existing project, signing settings, or user-owned files without resolving the ambiguity first.

## Permission implementation contract

Implement all 10 authorization categories through visible actions. One coherent feature may cover several permissions; do not create ten disconnected demo buttons. Use the exact approved purpose copy and trigger paths from `AppSpec.md`.

| Capability | Framework and request | Required configuration | Minimum real behavior |
|---|---|---|---|
| Bluetooth | CoreBluetooth with an instance-owned retained `CBCentralManager` | `NSBluetoothAlwaysUsageDescription` | Scan for compatible peripherals and expose an honest concept-specific result; connect or disconnect when the accepted hardware flow supports it |
| Camera | AVFoundation and `AVCaptureDevice.requestAccess(for: .video)` | `NSCameraUsageDescription` | Capture a photo, video, or scan used by the accepted feature |
| Contacts | Contacts with an instance-owned `CNContactStore` | `NSContactsUsageDescription` | Use authorized contact-store data for the accepted feature; a picker-only flow does not justify full Contacts authorization |
| Face ID | LocalAuthentication with an on-demand `LAContext` | `NSFaceIDUsageDescription` | Protect or confirm a meaningful action with passcode and unavailable handling |
| Location | CoreLocation with an instance-owned `CLLocationManager` and when-in-use request | `NSLocationWhenInUseUsageDescription` | Use current location for the accepted nearby or current-location result |
| Microphone | AVFAudio or AVFoundation with an iOS-15-compatible record-permission API | `NSMicrophoneUsageDescription` | Record, stop, save, play, replace, and delete or otherwise use a short clip with visible state |
| Photo-library read | PhotoKit `.readWrite` authorization | `NSPhotoLibraryUsageDescription` | Directly browse or process authorized library content; `PHPicker` alone does not justify full read access |
| Photo-library add | PhotoKit `.addOnly` authorization | `NSPhotoLibraryAddUsageDescription` | Save generated or captured media and show an explicit standard UIKit success or failure alert |
| Advertising tracking | AppTrackingTransparency after the approved explanatory action | `NSUserTrackingUsageDescription` | Gate the approved advertising, attribution, or personalization behavior and keep the app useful when denied |
| Push notifications | UserNotifications authorization with approved options | No usage-description key | Show the approved explanation, notification preferences, and a concept-relevant local or remote notification flow |

Apply these rules:

- Request access only after the user selects its visible feature; never request all permissions at launch.
- Put static purpose strings in the processed Info.plist and localized `InfoPlist.strings`; do not attempt to replace them at runtime.
- Handle `notDetermined`, authorized or limited, denied, restricted, unavailable, and unknown states as applicable. After denial, explain the disabled behavior and offer a deliberate Settings action without pressure or loops.
- Keep controls and status synchronized for microphone recording, saving, saved, playback, replace, and delete states.
- Use direct PhotoKit access only where the approved concept genuinely requires the corresponding read or add authorization.
- Never upload contacts, precise location, photos, recordings, or identifiers merely to demonstrate a permission.
- Keep the runtime behavior, purpose copy, data inventory, ATT state, AppMetrica modules, backend payloads, privacy declarations, and reviewer instructions mutually consistent.
- Return to specification approval if a privacy-preserving picker fully satisfies the feature and makes a required direct-access permission unjustifiable.

## Workflow

### Phase 1: Validate the handoff

Create a compact implementation checklist from `AppSpec.md`: feature and permission mappings, exact copy, denial behavior, data flow, screen placement, extension roles, backend payload, analytics and tracking behavior, app icon, platform settings, and pending external credentials. Resolve only blocking contradictions with the user.

### Phase 2: Create the project

Use repository instructions and its existing project generator when present. Otherwise prefer an installed generator such as XcodeGen or Tuist; if none exists, use available local tooling. Do not install tools or dependencies outside normal project resolution without approval.

Create:

- Main programmatic UIKit Swift target, iPhone iOS 15.0.
- Lock Screen WidgetKit extension, iOS 16.0 because Lock Screen families are unavailable on iOS 15.
- Notification Service Extension, iOS 15.0.
- Programmatic Notification Content Extension, iOS 15.0.
- Shared App Group only where the approved app and widget exchange a compact snapshot.

For every target set the supported Apple platforms as narrowly as the generator permits:

```text
TARGETED_DEVICE_FAMILY = 1
SUPPORTED_PLATFORMS = iphoneos iphonesimulator
SUPPORTS_MACCATALYST = NO
SUPPORTS_MAC_DESIGNED_FOR_IPHONE_IPAD = NO
SUPPORTS_XR_DESIGNED_FOR_IPHONE_IPAD = NO
```

Restrict the main Info.plist to `UIInterfaceOrientationPortrait`. Do not add iPad-specific orientation keys, landscape or upside-down modes, Mac, Catalyst, visionOS, Apple Vision, watchOS, tvOS, or companion targets.

Create all application and extension UI programmatically. Do not add storyboard or XIB files, `UIMainStoryboardFile`, scene storyboard names, or `NSExtensionMainStoryboard`. Prefer `NSExtensionPrincipalClass` for the notification content extension; if the active toolchain makes the approved programmatic approach impossible, stop and report the conflict.

Do not create unit-test or UI-test targets, test files, fixtures, mocks, or test-only infrastructure. Do not run unit or UI tests. Verification consists of builds, launch, backend smoke checks, and direct inspection of the real flows.

Create explicit entitlement files for capabilities the code uses. When a generator owns the project, declare entitlement values in its source specification, such as `project.yml` under `entitlements.properties`; regenerate and inspect emitted files instead of patching only generated output. Configure matching App Group values for the app and widget and Push Notifications for the main app where required. Treat provisioning profiles and signed entitlements as unverified until signing assets are available.

Add `PrivacyInfo.xcprivacy` to every shipped app-owned target that directly uses required-reason APIs. Declare applicable standard `UserDefaults` and App Group reasons; a widget using App Group defaults needs its own manifest with the applicable reason such as `1C8F.1`. Inspect resolved SDK privacy manifests rather than assuming the main app or a dependency covers every target.

Include the approved square 1024×1024 icon source in an `AppIcon` asset set and configure the main target to use it. Do not substitute an SF Symbol, add small text, pre-round, or mask the source.

### Phase 3: Implement the approved application

Default to simple MVC. Prefer one feature-oriented `UIViewController` and extract only instance-owned resource adapters or deterministic helpers that materially reduce complexity, such as `AppConfiguration`, `APIClient`, `AppMetricaAnalyticsClient`, permission framework adapters, Codable models, and pure formatters.

Create one composition root in `SceneDelegate` or an instance-owned `AppFactory` and inject dependencies through initializers. Avoid repositories, use-case layers, coordinators, reactive state stores, service locators, protocol-per-type abstractions, and dependency containers unless the approved design truly needs them.

Implement the approved visual system with programmatic Auto Layout, Dynamic Type text styles, semantic or explicitly approved colors, accessible UIKit controls, deliberate VoiceOver grouping and order, and non-color status cues. Match the approved screen inventory and states; do not interpret supporting code as permission to broaden the MVP.

### Phase 4: Build, launch, and verify

Run the verification section below. Fix implementation drift and build or launch failures without adding product scope.

### Phase 5: Record the handoff

Update the release handoff manifest and report verified behavior, configuration instructions, and external limitations. Do not claim App Store submission readiness while policy, production backend, signing, APNs, or device-only items remain pending.

## Architecture and lifetime rules

Minimize process-wide and long-lived state:

- Do not create app-owned singletons, global mutable variables, mutable `static var`, service locators, or global caches.
- Do not use `NotificationCenter` observers, KVO, Combine state pipelines, or permanent event buses for application state.
- Do not use `URLSession.shared`; inject a configured `URLSession`.
- Allow immutable `static let` constants only when they hold no runtime state.
- Isolate unavoidable framework global entry points such as `UNUserNotificationCenter.current()`, AppTrackingTransparency, or AppMetrica inside small injected adapters.
- Prefer delegates, target-action, scoped closures, and async functions. Capture owners weakly when callbacks can outlive them.
- Give Bluetooth, location, camera, audio, and other delegate-based resources an explicit instance owner and lifecycle. Stop scanning, recording, location updates, timers, and sessions when the feature ends.

Audit app-owned source for mutable static state, singleton declarations or `.shared` calls, observers, KVO, long-lived subscriptions, uncancelled timers, and delegate or closure lifetime leaks. Document required framework globals instead of disguising them. Enforce no unnecessary app-owned process state, not an impossible claim of zero static memory.

## Configuration and AppMetrica

Keep mutable environment choices outside Swift source, preferably in `.xcconfig` values exposed through build-setting substitution:

```text
PRODUCT_BUNDLE_IDENTIFIER
DEVELOPMENT_TEAM
APP_GROUP_IDENTIFIER
APPMETRICA_API_KEY
API_BASE_URL
```

Read values once into an injected immutable `AppConfiguration`. Never bundle APNs private keys, access tokens, or other server secrets.

Before integration, consult current official AppMetrica iOS documentation and package sources. Select and pin a Swift Package version supporting iOS 15 and use its current module and activation API.

- Isolate SDK calls in an instance-owned `AppMetricaAnalyticsClient`; do not expose an application singleton.
- Make `APPMETRICA_API_KEY` replaceable without Swift changes. With an empty or invalid key, disable analytics gracefully and keep the app usable.
- After successful SDK activation, report a custom event named exactly `launch` once per process. Do not duplicate it on scene foreground transitions or report it when activation did not succeed.
- Keep selected modules, data sending, advertising support, and ATT-dependent behavior consistent with `AppSpec.md` and current official SDK controls.
- Report only useful product events such as `launch`, screen open, feature action, permission outcome, and API result. Never send contacts, precise location, media, recordings, advertising identifiers, secrets, or other sensitive payloads as custom event parameters.
- Record SDK-level collection separately from custom event parameters and document that changing the API key may require terminating and relaunching the process.

## Extensions

Implement all approved extensions as real, small targets:

- Lock Screen widget: display the approved glanceable state. Share only a compact Codable snapshot through App Group `UserDefaults` or a small file. Do not observe shared defaults; reload timelines explicitly after writes.
- Notification Service Extension: enrich or transform remote content as approved, keep networking optional and time-bounded, and always call the content handler with the best available content.
- Notification Content Extension: render the approved compact programmatic UI and route actions through notification categories or deep links.

Give targets distinct bundle identifiers and link only their required frameworks and resources. Do not link the complete application graph into an extension.

## Minimal backend and client

Create the approved minimal backend beside the app in `backend/`. Prefer one source file, the simplest installed runtime, standard-library HTTP support, and no third-party packages.

Prefer exactly:

- `GET /health`.
- `POST /sync` carrying one compact idea-specific snapshot.

Let `/sync` also carry an installation identifier, lightweight bearer value, and APNs device token when practical. Split endpoints only when the approved feature cannot work honestly through the merged operation. Use memory or one ignored local JSON file, deterministic Codable-compatible JSON, explicit status codes, and a single documented start command and sample request.

Use an injected configured `URLSession`, timeouts, cancellation, and visible loading and error states. Keep local HTTP allowances debug-only. Allow the production HTTPS URL to remain `pending`, but do not disguise it as a release-ready service. When Apple signing or APNs credentials are unavailable, provide an honest request generator or sender stub and mark remote delivery unverified.

## Privacy and future App Store handoff

Keep permission strings, runtime behavior, AppMetrica, ATT, backend payloads, `PrivacyInfo.xcprivacy`, and the data inventory consistent. Treat mismatches as implementation blockers.

Do not add privacy-policy, support, Terms, or EULA screens unless the user explicitly requests them. Record missing URLs and future in-app entry points as `pending` for the separate App Store preparation skill. Never claim submission readiness while these or production/signing requirements remain pending.

## Verification

Verify in proportion to the available environment:

1. Generate the project, resolve pinned package dependencies, and build the main app and every extension for an available simulator.
2. Build Release without app-owned compiler warnings. Do not suppress warnings merely to pass.
3. Launch the app in a simulator, wait for the meaningful application hierarchy, and inspect all principal approved screens instead of accepting the launch screen as success.
4. Start the backend, call `/health`, and exercise one real `/sync` round trip with the approved models.
5. Search for storyboards, XIBs, test targets, app-owned singletons, mutable static storage, observers, `URLSession.shared`, and unsupported platform settings; fix violations or explain unavoidable framework calls.
6. Exercise every permission feature from its approved visible trigger through authorized or simulator-available behavior and denial recovery. Capture screenshots and the accessibility hierarchy before and after important interactions. Retry a failed simulator interaction once, then classify the limitation honestly. Do not create XCTest or UI-test targets.
7. Verify source, localized, and processed Info.plist purpose strings against `AppSpec.md` verbatim.
8. Verify empty-key AppMetrica behavior. With a valid test key, verify successful activation and one attempted custom `launch` event per process, not per foreground transition.
9. Inspect each app-owned target's Privacy Manifest and resolved SDK manifests against actual APIs and the approved data inventory.
10. Inspect source entitlements and generator configuration for App Group and Push. When signing exists, inspect provisioning profiles and signed products; otherwise list the exact pending Apple Developer steps.
11. Verify distinct extension bundle identifiers and deployment targets, `TARGETED_DEVICE_FAMILY = 1`, iPhone-only supported platforms, disabled Mac/Catalyst/Apple Vision compatibility, and portrait-only processed main-app Info.plist.
12. Verify the approved AppIcon is compiled without missing-icon warnings and inspect it at full size and a small Home Screen-like size.
13. State which Bluetooth, camera, contacts, Face ID, location, microphone, PhotoKit, ATT, remote push, signing, or hardware checks still require a physical device or external credentials.
14. When signing is available, archive Release for Generic iOS Device and inspect signed app and extension entitlements. Otherwise record archive validation as signing-dependent.

Do not broaden the MVP while fixing verification failures.

## AppSpec conformance

Before handoff, compare the built application with every accepted item in `AppSpec.md` and the approved mockups.

For each authorization verify that the visible trigger exists on the approved screen, implemented behavior matches the approved feature, exact copy is present, denial and unavailable behavior matches the design, and accessed, stored, and transmitted data matches the inventory.

Compare screen structure, terminology, control behavior, visual states, accessibility, backend payloads, extension output, AppMetrica and ATT behavior, and the icon with the approved handoff. Do not mark implementation complete while an accepted item is missing or materially different. Fix implementation drift without adding unrelated features.

## Release handoff manifest

Create or update deterministic `Release/release-manifest.json` with:

- Product name, version, build number, and all bundle identifiers.
- App Group, capabilities, entitlement source, and verification status.
- Permission keys, exact localized copy, trigger paths, denial behavior, data handling, and reviewer instructions.
- Data inventory, tracking behavior, AppMetrica modules, and privacy status.
- Backend, privacy-policy, and support URLs or `pending` markers.
- Extension identifiers and roles.
- Deterministic application states intended for future App Store screenshots.
- Device-only, production-backend, signing, APNs, hardware, policy, and archive checks that remain unresolved.

Never include AppMetrica API keys, APNs `.p8` files, access tokens, or other secrets.

## Handoff

Lead with what works. Provide clickable paths to the project, `AppSpec.md`, configuration, backend entry point, approved mockups, app-icon master, app-owned Privacy Manifests, permission localizations, and release manifest. Include exact build and backend-run commands, configurable values, verified targets, Release and archive status, AppSpec conformance, and remaining physical-device, production, policy, credential, or signing limitations.

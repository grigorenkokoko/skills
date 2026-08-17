# App Store Review Pipeline Design

## Goal

Evolve the three iOS skills into a four-stage pipeline that produces a release-ready iPhone application while preserving the product brief's unusual hard requirements: all ten authorization categories, AppMetrica, the minimal backend, Lock Screen widget, Notification Service Extension, and Notification Content Extension remain mandatory.

The pipeline reduces predictable App Review risk but never promises approval. Apple makes the final decision and its requirements change over time.

## Confirmed constraints

- Keep Bluetooth, camera, Contacts, Face ID, location, microphone, Photo Library read, Photo Library add, App Tracking Transparency, and notifications mandatory.
- Keep AppMetrica mandatory, configurable, and privacy-aware.
- Keep the minimal working backend and all three extensions mandatory.
- Add an early App Review feasibility gate without weakening the mandatory capability set.
- Add a shared, machine-readable privacy contract.
- Add conditional policy modules for features such as accounts, third-party login, payments, subscriptions, user-generated content, children, regulated domains, and encryption.
- Make a published privacy policy URL and an accessible in-app privacy-policy entry mandatory.
- Do not create or run unit-test or UI-test targets; optimize for delivery speed.
- Do not make physical-device testing a pipeline status or a `release-ready` gate. Produce a manual device-check list for the user instead.

## Pipeline and statuses

The stages are:

1. `generate-ios-app-ideas`
2. `design-ios-app-concept`
3. `build-ios-app-concept`
4. `prepare-ios-app-store-release`

The status progression is:

```text
idea-draft
  -> policy-approved
  -> design-approved
  -> implementation-verified
  -> archive-validated
  -> release-ready
  -> submitted
```

`device-tested` is deliberately absent. `submitted` is an external action and requires explicit user approval immediately before upload or submission.

## Stage 1: idea and policy feasibility

`generate-ios-app-ideas` continues to require all ten authorization categories. Before producing an approved handoff, it runs an App Review feasibility gate:

- The concept must have adequate lasting utility beyond a permission demonstration.
- Every authorization must be reached through an intentional product action and must support the same coherent recurring scenario.
- Full Contacts and Photo Library access must enable behavior that a privacy-preserving picker cannot provide.
- ATT must gate a disclosed AppMetrica advertising, attribution, or cross-company tracking behavior; denial must not make the app unusable.
- Location must have a manual alternative where the accepted feature permits one.
- The backend and extensions must deliver visible product value rather than empty target shells.
- A concept with decorative or misleading capability use cannot receive `policy-approved`; the skill must revise the concept or report the exact unresolved conflict.

The selected concept produces `AppSpec.md` and `AppPrivacy.yml`. `AppSpec.md` owns product behavior and approved copy. `AppPrivacy.yml` owns machine-readable data collection, transmission, retention, tracking, permission, SDK, domain, privacy-label, and review-disclosure facts.

To keep ideation fast, broad alternatives receive only a compact fit/risk screen. The complete permission-review matrix and privacy contract are generated only for the selected concept.

## Stage 2: design

`design-ios-app-concept` requires `policy-approved` and consumes both source files. It preserves all permission triggers and adds release-relevant surfaces:

- an easily accessible privacy-policy entry;
- consent withdrawal and Settings recovery;
- manual fallbacks where required by the approved feature;
- conditional account deletion, subscription management, reporting/blocking, or other policy UI when a policy module applies;
- reviewer-reachable paths for non-obvious features and required hardware scenarios.

The stage still renders and receives approval for screens, extensions, notification layouts, and the icon. It writes `design-approved` only after explicit user approval.

## Stage 3: implementation

`build-ios-app-concept` requires `policy-approved` and `design-approved`. It implements the approved application and keeps the existing no-storyboard, iPhone-only, portrait-only, programmatic UIKit architecture.

The build stage:

- treats `AppPrivacy.yml` as the privacy source of truth and checks it against Info.plist purpose strings, runtime data flow, AppMetrica configuration, backend payloads, entitlements, and every target's privacy manifest;
- implements an in-app privacy-policy entry, while allowing the final hosted URL to remain unresolved until the release stage;
- activates the policy modules selected during Stage 1;
- does not create test targets or run unit/UI tests;
- builds and launches simulator-compatible flows, exercises the backend, inspects accessibility and permission recovery, and records hardware-only checks for manual execution;
- writes `implementation-verified`, never `release-ready`.

## Stage 4: release preparation

Create `prepare-ios-app-store-release`. It consumes the built project, `AppSpec.md`, `AppPrivacy.yml`, approved design artifacts, and `Release/release-manifest.json`.

At invocation time it consults current primary Apple documentation and records the checked URLs and dates. It must not rely on a permanently hard-coded Xcode, SDK, privacy-manifest reason, age-rating, or App Store Connect requirement.

It prepares and verifies:

- production bundle IDs, signing, entitlements, capabilities, version, and build number;
- a Release archive built with the currently accepted Xcode and SDK;
- archive validation and extension embedding;
- the aggregated Xcode Privacy Report and its consistency with `AppPrivacy.yml` and App Store privacy answers;
- valid privacy-policy and support URLs, with the privacy policy reachable from inside the app;
- App Store metadata, age-rating answers, screenshots, export-compliance answers, content rights, and pricing/business-model disclosures as applicable;
- App Review contact information, review notes, demo credentials or demo mode, sample data, QR codes, and hardware instructions as applicable;
- live production backend reachability from outside the development machine;
- AppMetrica SDK version, privacy manifest/signature status, declared domains, actual configuration, ATT behavior, and disclosure consistency;
- conditional policy-module evidence;
- absence of placeholder content and release-blocking `pending` values.

The release skill produces the metadata and evidence package without automatically changing external state. Uploading a build, changing App Store Connect records, or submitting to review happens only after explicit user approval.

## Shared privacy contract

Add an `AppPrivacy.yml` template with stable semantic fields rather than Apple constants that may change. It covers:

- every authorization and exact purpose/pre-permission copy;
- visible trigger, denied behavior, and reviewer path;
- local, backend, APNs, installation, AppMetrica, advertising, and tracking data;
- collection purpose, linkage, tracking use, retention, deletion, recipients, and domains;
- third-party SDK name, version, modules, manifest/signature status, and declared behavior;
- privacy-policy disclosures and App Store privacy-label mapping;
- applicable conditional policy modules;
- current-documentation checks and unresolved release blockers.

Apple-specific generated values remain derived artifacts. The release stage fails closed when generated manifests, App Store answers, privacy policy, SDK behavior, or runtime configuration disagree with the contract.

## Conditional policy modules

The idea stage selects modules using observable product features. Later stages must implement and verify the selected module:

- account creation: in-app account deletion and data deletion behavior;
- third-party/social login: equivalent login-option review;
- digital goods or subscriptions: StoreKit, restoration, subscription management, and reviewer visibility;
- user-generated content: reporting, blocking, moderation, and support contact;
- children or age-sensitive content: current age-rating and child-safety requirements;
- regulated health, financial, gambling, alcohol, or similar domains: applicable distribution and claim restrictions;
- encryption: export-compliance classification and documentation status;
- special hardware: reviewer instructions, sample data, and a reviewable fallback or demo where feasible.

Modules not triggered by the product remain absent.

## Release-ready definition

`release-ready` means the archive and submission package have no known automated or documentation blocker. It requires:

- `policy-approved`, `design-approved`, `implementation-verified`, and `archive-validated`;
- successful archive validation;
- working production URLs and backend;
- complete signing, metadata, privacy, age-rating, export, reviewer-access, and conditional-policy information;
- privacy consistency across source contract, binary, SDK report, policy, and App Store answers;
- no placeholder text, secrets, or release-blocking `pending` values.

Physical-device checks are listed separately as manual user actions and do not create a pipeline status. App Review approval is not claimed or guaranteed.

## Skill verification

Before editing, create deterministic contract checks that fail against the current repository. They verify the presence of the fourth stage, required status transitions, mandatory capabilities, mandatory AppMetrica, privacy contract, policy modules, privacy-policy requirement, absence of `device-tested`, and absence of test-target requirements. Re-run the same checks after each skill change and perform cross-file consistency review before completion.

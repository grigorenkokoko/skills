---
name: prepare-ios-app-store-release
description: Use when an implementation-verified portrait-only iPhone project must be archived, privacy-audited, documented, or prepared for App Store Connect and App Review under current Apple requirements.
---

# Prepare iOS App Store Release

## Goal

Turn an `implementation-verified` iPhone project into an `archive-validated` and then `release-ready` submission package. Verify the production archive, privacy evidence, AppMetrica behavior, policy modules, metadata, reviewer access, URLs, and backend against current primary Apple requirements.

Reduce known rejection risk without claiming or guaranteeing App Review approval. Apple makes the final decision and may change its requirements. Never write `submitted`, upload a build, change App Store Connect, or submit for review without explicit user approval immediately before that external action.

## Required handoff

Require:

- `AppSpec.md` with `policy-approved` and `design-status: design-approved`.
- `AppPrivacy.yml` matching the implemented permissions, data inventory, AppMetrica, tracking, domains, privacy-policy disclosures, App Store privacy mapping, conditional policy modules, and release blockers.
- `Release/release-manifest.json` with `implementation-verified` status.
- The built Xcode project, approved design artifacts, app icon, permission localizations, backend source, production configuration surface, entitlements, and app-owned privacy manifests.
- Product version, build number, final bundle identifiers, and an Apple Developer team when signing or archive validation requires it.

If implementation evidence is missing or product behavior differs from either source of truth, stop and return the issue to `build-ios-app-concept`. Fix release configuration and disclosure drift here; do not redesign features or silently change permission purposes.

Do not create unit-test or UI-test targets and do not run unit or UI tests. This stage uses archive, static, configuration, service, metadata, and direct launch evidence. Physical-device work remains a **manual device checks** list for the user and creates no pipeline status.

## Current-source rule

Before evaluating compliance, consult **current primary Apple** documentation. Prefer Apple Developer and App Store Connect Help over summaries. At minimum check the current versions of:

- App Review Guidelines and the pre-submission checklist;
- Upcoming Requirements for accepted Xcode and SDK versions;
- privacy manifests, required-reason APIs, SDK signatures, and privacy reports;
- App Store privacy questions and privacy-policy requirements;
- required and localizable metadata, screenshot specifications, and age ratings;
- archive, upload, signing, entitlement, and export-compliance requirements;
- rules activated by the selected conditional policy modules.

Consult current official AppMetrica iOS documentation and the resolved package source for SDK behavior. Do not copy a permanently hard-coded Xcode version, SDK floor, required-reason code, age-rating answer, or App Store Connect field from this skill.

Write `Release/compliance-sources.json` containing each source title, direct URL, date checked, applicable decision, and the artifact or validation it affected. Treat an inaccessible or ambiguous primary requirement as a release blocker rather than guessing.

## Status model

Use only these transitions in this stage:

```text
implementation-verified
  -> archive-validated
  -> release-ready
  -> submitted
```

- `archive-validated` means a correctly signed Release archive passed the currently supported validation path and its embedded products were inspected.
- `release-ready` means the archive and submission package have no known release blocker.
- `submitted` is written only after explicit user approval and confirmed successful submission.

Do not add another status for physical-device testing. Store those checks in `Release/manual-device-checks.md`.

## Workflow

### Phase 1: Reconcile the sources of truth

Compare `AppSpec.md`, `AppPrivacy.yml`, the approved design, source configuration, built products, backend contract, and release manifest. Produce a blocker list with an owner and evidence path for each mismatch.

Verify that all ten mandatory authorization categories remain implemented and reviewer-reachable:

| Capability | Required declaration or evidence |
|---|---|
| Bluetooth | `NSBluetoothAlwaysUsageDescription`, feature trigger, hardware/reviewer instructions |
| Camera | `NSCameraUsageDescription`, capture result, denial path |
| Contacts | `NSContactsUsageDescription`, justified direct-store behavior, denial path |
| Face ID | `NSFaceIDUsageDescription`, meaningful protected action, fallback |
| Location | `NSLocationWhenInUseUsageDescription`, current-location result, accepted manual alternative |
| Microphone | `NSMicrophoneUsageDescription`, record/save/play/replace/delete states |
| Photo Library read | `NSPhotoLibraryUsageDescription`, justified direct read, limited-access behavior |
| Photo Library add | `NSPhotoLibraryAddUsageDescription`, save result and explicit feedback |
| ATT | `NSUserTrackingUsageDescription`, approved AppMetrica behavior, useful denial path |
| Push notifications | App-owned explanation, authorization flow, categories, token handling, reviewer path |

Confirm that the Lock Screen widget, Notification Service Extension, Notification Content Extension, minimal backend, and AppMetrica remain real product features rather than empty release artifacts.

### Phase 2: Resolve production configuration

Use replaceable configuration rather than Swift literals for bundle IDs, team, App Group, AppMetrica key, API URL, privacy-policy URL, and support URL. Never store APNs private keys, App Store Connect API keys, access tokens, demo passwords, or signing secrets in the repository or release manifest.

Require before `release-ready`:

- final production bundle identifiers and versioning;
- matching capabilities, entitlements, and provisioning for the app and every extension;
- a valid production AppMetrica configuration whose activation, modules, ATT behavior, and disclosures match `AppPrivacy.yml`;
- a reachable HTTPS production backend and the approved `/health` and `/sync` behavior;
- a reachable public privacy-policy URL and support URL;
- an easily accessible in-app privacy-policy entry that opens the configured policy;
- complete reviewer credentials, sample data, QR codes, or special-hardware instructions as applicable.

Check production services from outside the development-only localhost path. Record status codes, timestamps, and redacted request shapes without persisting secrets or personal data.

### Phase 3: Archive and validate

Determine the currently accepted Xcode and SDK versions from Apple before building. Preserve the approved deployment targets even when the upload SDK requirement is newer.

Create a clean Release archive for Generic iOS Device using the project's real scheme and production configuration. Use the current Apple-supported archive validation mechanism. Capture commands, tool versions, validation output, warnings, and archive location without exposing credentials.

Inspect the archive, not only source files:

- the main app and exactly the approved embedded extensions;
- distinct bundle identifiers, versions, deployment targets, and supported platforms;
- signed entitlements and matching App Group values;
- processed Info.plist purpose strings and portrait/iPhone restrictions;
- compiled app icon and required resources;
- app-owned and SDK privacy manifests in their resolved bundle locations;
- prohibited placeholders, debug URLs, debug entitlements, unexpected frameworks, and signing drift.

Write `archive-validated` only after validation succeeds and archive inspection has no blocker. A simulator build or unsigned product cannot substitute for this status.

### Phase 4: Privacy and AppMetrica audit

Generate the aggregated **Xcode Privacy Report** from the validated archive using the current supported workflow. Compare it with `AppPrivacy.yml`, all `PrivacyInfo.xcprivacy` files, resolved third-party SDK manifests, actual build configuration, the hosted privacy policy, and proposed App Store privacy answers.

For AppMetrica, verify:

- pinned version and resolved modules;
- official privacy manifest and SDK signature status where currently required;
- SDK-level collected data and contacted domains;
- custom events and parameters contain no contacts, precise location, media, recordings, identifiers, secrets, or user-entered sensitive content;
- ATT-authorized advertising or attribution behavior matches the approved contract;
- ATT denial leaves the core app useful and prevents prohibited tracking behavior;
- disclosures include third-party collection even when custom events are minimal.

Create `Release/app-store-privacy.json` from semantic contract facts and current App Store Connect questions. The contract, binary report, network/domain evidence, policy, and answers must agree. The audit fails closed on mismatch.

### Phase 5: Verify conditional policy modules

Use the observable module selections in `AppPrivacy.yml`. Verify only selected modules:

- account creation: in-app account-deletion initiation, full deletion scope, retention exceptions, and reviewer access;
- third-party login: the currently required equivalent login option and data minimization;
- digital goods or subscriptions: current StoreKit rules, visible products, restoration, subscription management, and review notes;
- user-generated content: moderation, reporting, blocking, support, and deletion;
- children or age-sensitive content: current age-rating, parental, content, and data requirements;
- regulated domains: current claims, eligibility, regional, evidence, and legal requirements;
- encryption: export-compliance answers and documentation status;
- special hardware: complete setup instructions, sample material, and a reviewable fallback or demo where feasible.

A selected module without complete product, metadata, and reviewer evidence is a release blocker. A module marked `not-applicable` must have no contradictory feature in the binary or metadata.

### Phase 6: Prepare App Store and reviewer artifacts

Create a deterministic `Release/app-store-metadata/` package covering every current required field that can be prepared locally:

- localized name, subtitle, description, keywords, promotional text, category, copyright, and business-model explanation;
- accurate screenshots from the implemented application in current accepted sizes, with no nonexistent functionality;
- age-rating answers and content-rights declarations;
- export-compliance answers and documentation status;
- App Store privacy answers and privacy-policy URL;
- support URL and App Review contact fields;
- visible and functional in-app purchases or subscriptions when selected;
- `Release/review-notes.md` with exact steps for every permission, extension, backend flow, non-obvious feature, demo account, sample data, QR code, and special hardware requirement.

Scrub placeholders, stale screenshots, development endpoints, empty websites, generic review notes, and claims not present in the binary. Do not invent legal, contact, account, pricing, or rights information; unresolved required values block `release-ready`.

### Phase 7: Manual device checklist

Write `Release/manual-device-checks.md` for the user. Include hardware-dependent Bluetooth, camera, Contacts, Face ID, location, microphone, PhotoKit, ATT, remote notification, APNs, and accessory checks plus expected results and reset instructions.

This checklist is deliberately manual. Do not add a physical-device pipeline status or make completion of the checklist a `release-ready` gate. Report unchecked items prominently so the user understands the remaining real-world risk.

### Phase 8: Release-ready gate

Write `release-ready` only when all of the following are true:

- prior statuses and `archive-validated` are present;
- the archive validation and embedded-product inspection succeeded;
- privacy manifests, Xcode Privacy Report, AppMetrica, policy, and App Store answers agree;
- production backend, privacy-policy URL, and support URL are reachable;
- signing, entitlements, metadata, screenshots, age rating, export answers, reviewer access, and selected conditional policy evidence are complete;
- no placeholder, secret, debug endpoint, or release-blocking `pending` value remains.

Manual device checks are reported separately and do not change the gate. State clearly that `release-ready` is evidence of preparation, not a guarantee of approval.

## External action gate

Preparing files and read-only inspection do not authorize external mutations. Immediately before uploading a build, editing App Store Connect, starting TestFlight review, or submitting to App Review, summarize the exact action and request **explicit user approval**.

After approval, perform only the approved action. Record identifiers and timestamps after confirmed success. Write `submitted` only after the App Store submission succeeds; a local command, queued upload, or processing build is not submission success.

## Release artifacts

Update or create:

- `Release/release-manifest.json` with statuses, artifact paths, validation evidence, blockers, and no secrets;
- `Release/compliance-sources.json` with current official sources and decisions;
- `Release/archive-validation.json` with toolchain and archive inspection results;
- `Release/app-store-privacy.json` with current privacy answers;
- `Release/app-store-metadata/` with localized metadata and screenshots;
- `Release/review-notes.md` with reviewer instructions;
- `Release/manual-device-checks.md` with non-gating physical-device work.

Keep generated archives, credentials, profiles, and private keys out of version control unless the repository explicitly provides a safe artifact policy.

## Handoff

Lead with the highest verified status: `implementation-verified`, `archive-validated`, `release-ready`, or `submitted`. Provide clickable paths to every release artifact, the validated archive location, current-source record, privacy report, metadata package, review notes, and manual device checklist.

List remaining blockers and manual checks separately. Include exact upload or submission state, but never describe an unapproved or unconfirmed external action as completed and never guarantee App Review approval.

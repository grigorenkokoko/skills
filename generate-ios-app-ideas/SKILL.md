---
name: generate-ios-app-ideas
description: Use when generating, refining, naming, or policy-approving a portrait-only iPhone concept that must satisfy the complete mandatory permissions, AppMetrica, backend, widget, notification-extension, privacy, and App Store review brief before design begins.
---

# Generate iOS App Ideas

## Goal

Generate coherent, buildable, releaseable portrait-only iPhone product ideas in which every mandatory capability has a natural role. Center the MVP on the smallest coherent set of permission-backed user actions. Allow only the supporting navigation, state, configuration, AppMetrica, privacy disclosures, extensions, backend, policy compliance, and error handling required to make those actions work.

Run an **App Review feasibility gate** before approving a concept. A concept may keep every mandatory capability and still fail the gate when one exists only as a demonstration, the product lacks lasting utility, or the privacy and review story is internally inconsistent. Revise the concept or report the exact conflict; never hide it behind generic risk language.

Keep this skill limited to ideation and product specification. Do not create an Xcode project, source code, rendered design, or backend. Use `idea-draft` while exploring. After the user accepts a concept and it passes the gate, create or update `AppSpec.md` and `AppPrivacy.yml` with status `policy-approved` as the handoff to the design skill.

## Inputs

Treat any idea supplied by the user as the primary creative direction. Preserve its core problem, audience, theme, and accepted features while adapting it to satisfy the constraints. Concentrate on developing that idea before contributing original alternatives.

When the user supplies an idea:

- Refine and complete that idea instead of replacing it.
- Proactively suggest concrete improvements to the user's idea when they make it clearer, more coherent, easier to implement, or safer for App Store review.
- When a nearby variation appears materially stronger, present it as an optional close alternative after refining the user's idea. Keep it recognizably based on the user's direction and explain the advantage briefly.
- Resolve missing details with reasonable assumptions.
- Point out a conflict only when a required capability cannot be integrated credibly.
- When the supplied idea is age-gated or based on a high-risk review topic, briefly flag the conflict and adapt its useful core into a general-audience concept instead of following the risky element literally.
- Do not replace the user's direction with unrelated concepts. Generate broader alternatives only when the user explicitly requests them.
- After refining the user's idea and any useful close alternatives, always offer broader alternative generation as an optional next step, even when the current idea is feasible.
- When the user's idea spans multiple Apple platforms or depends on landscape layout, preserve and refine only the iPhone portion and adapt its flows to portrait orientation. Do not add companion experiences for other devices.

Use any theme, audience, number of ideas, tone, or naming preference supplied by the user. When no idea is supplied:

- Generate 5 distinct ideas.
- Generate 5 name variants for each idea.
- Prefer consumer applications with a small, credible MVP.
- Give each alternative only a compact concept, mandatory-capability fit summary, and preliminary review-risk verdict.
- Recommend one alternative, but wait for the user to select or approve a concept before producing the complete permission-review matrix, data inventory, backend contract, extension specification, or `AppPrivacy.yml`.
- Answer in the user's language.

Do not block on missing creative preferences. Make reasonable assumptions and state only assumptions that materially affect the result.

## Hard constraints

Make every idea satisfy all of the following:

1. Actually use every permission or authorization listed below through a reachable, intentional user action. Do not merely declare a purpose string.
2. Keep the user-facing MVP centered on the smallest coherent set of features needed to exercise all required permissions. A single feature may cover several permissions.
3. Do not add unrelated secondary product features. Supporting UI and technical code needed for navigation, state, configuration, analytics, extensions, backend interaction, permission recovery, and error handling are allowed and should be minimal.
4. Produce feature-specific permission copy that clearly states what the app does with the requested access and why that benefits the user. Do not use generic text that could belong to an unrelated app.
5. Include a Lock Screen widget, Notification Service Extension, and Notification Content Extension.
6. Include the smallest backend that can demonstrate one real client-server interaction, synchronization, and push-token handling. Prefer merging responsibilities when that reduces code.
7. Keep the concept suitable for a general audience without age gates or content likely to create a material App Store review obstacle.
8. Make the product exclusively an iOS app for iPhone. Do not propose iPad or iPadOS support, macOS, Mac Catalyst, Designed for iPhone/iPad on Mac distribution, visionOS or Apple Vision, watchOS, tvOS, or cross-platform and companion apps. Treat the widget and notification extensions as parts of the iPhone app.
9. Make the iPhone application portrait-only. Keep every core flow usable without device rotation; do not propose landscape-only screens, interfaces, or features. Treat Lock Screen widget and notification layouts as portrait-oriented surfaces.
10. Include configurable AppMetrica analytics and define its SDK-level collection, custom events, ATT-dependent behavior, retention, and disclosure. The application must remain useful when ATT is denied.
11. Define an easily accessible in-app privacy-policy entry. The public privacy-policy and support URLs may remain release blockers until the release stage, but their required disclosures must be known now.
12. Select every applicable conditional policy module using observable product features. Do not add modules that the product does not trigger.
13. Do not mark a concept `policy-approved` until it passes the feasibility gate below.

Treat the naming pattern as a strong preference, not a hard constraint. Prefer names containing or clearly expanding to «YP», «Y P», or «Я П», but keep a stronger natural name when forcing the pattern would make it unclear or awkward.

Reject or adapt an idea when a permission, extension, or backend exists only to check a box. A permission is not justified merely because the app can display its system prompt. Full Contacts or Photo Library access must enable behavior that cannot honestly be represented by a privacy-preserving system picker alone. Face ID must protect or confirm meaningful data or an action. Advertising tracking must gate a real advertising, attribution, or personalization behavior and the app must remain useful when denied. Bluetooth must have a credible compatible-device scenario. If a required capability cannot be made core and reviewable without unrelated scope, report the conflict rather than disguising it. Avoid duplicating the same product with superficial theme changes.

Avoid concepts centered on adult or sexual content, dating, gambling or betting, alcohol, tobacco, drugs, graphic violence, weapons, hate or extremism, self-harm, anonymous or unmoderated user-generated content, medical diagnosis or treatment claims, real-money speculation, crypto investment, surveillance, stalking, or illegal activity. Avoid requiring identity or age verification merely to access the core product. Treat these rules as review-risk reduction, not a guarantee of App Store approval.

## App Review feasibility gate

Evaluate the selected concept before creating the handoff. Record a pass or an exact unresolved conflict for each item:

1. **Lasting utility**: the application delivers a recurring benefit beyond demonstrating system APIs.
2. **Capability coherence**: all ten authorizations support the same product scenario and none exists as a disconnected demo button.
3. **Data minimization within the brief**: full Contacts and Photo Library access enable approved behavior that a picker cannot provide; the scope of read data is still minimized.
4. **Consent integrity**: requests occur after intentional actions, denial does not create coercive loops, and ATT denial preserves the core application.
5. **Extension value**: the Lock Screen widget and both notification extensions expose accepted, reviewer-reachable product behavior.
6. **Backend value**: the backend enables real synchronization and push-token handling rather than a health-check-only shell.
7. **Privacy consistency**: permission copy, AppMetrica, backend payloads, APNs identifiers, retention, deletion, privacy labels, and policy disclosures tell the same story.
8. **Review access**: non-obvious paths, hardware assumptions, sample data, and manual alternatives can be explained to App Review.
9. **Conditional policy coverage**: every triggered module below has an implementable product and reviewer path.

A failed item prevents `policy-approved`. Refine the concept while preserving the mandatory capability set. If no honest refinement exists, stop with a concise conflict report instead of generating misleading purpose strings.

## Conditional policy modules

Select modules only when the concept contains the observable trigger:

| Module | Trigger | Required handoff decision |
|---|---|---|
| Account deletion | The app creates user accounts | In-app initiation, full deletion scope, retention exceptions, and reviewer path |
| Third-party login | A social or third-party service authenticates the primary account | Equivalent login option and data-minimization behavior |
| Digital goods and subscriptions | The app sells or unlocks digital functionality | StoreKit product, restoration, subscription management, and reviewer visibility |
| User-generated content | Users publish or exchange content | Moderation, reporting, blocking, support contact, and deletion behavior |
| Children or age-sensitive content | Audience or content makes age handling material | Current age-rating answers, parental controls, and data restrictions |
| Regulated domain | Health, financial, gambling, alcohol, or another regulated behavior is retained after the general-audience screen | Claims, eligibility, regional availability, and evidence requirements |
| Encryption | The app or backend uses encryption beyond the platform baseline or needs export classification | Export-compliance status and required documentation |
| Special hardware | A core Bluetooth or accessory path needs uncommon hardware | Reviewer instructions, sample data, and a reviewable fallback or demo where feasible |

Record selected modules and their decisions in both `AppSpec.md` and `AppPrivacy.yml`. Record non-applicable modules explicitly as `not-applicable` so later stages do not invent them.

## Naming rules

Make names concrete enough that a user can infer the theme.

Aim for most name options to visibly contain or expand to one of these exact uppercase patterns: `YP`, `Y P`, or `Я П`. Allow some options outside these patterns when they are clearer, more memorable, or supplied and preferred by the user.

Do not propose compact `ЯП` or Latin `YaP`/`Ya P`/`YA P` constructions. If the user arrives with a name using one of them, preserve it only as the user's working option, explicitly note that this form can draw unnecessary attention to the naming, recommend avoiding it, and offer nearby variants using `YP`, `Y P`, `Я П`, or a natural name without a pattern. Treat this as naming advice, not a reason to reject the underlying idea.

Prefer one of these constructions:

- Compact Latin construction with `YP`: «YP Travel».
- Latin phrase whose prominent words expand to `Y P`: «Your Plan».
- Russian phrase expanding to `Я П`: «Я Путешествую», «Я Планирую», «Я люблю Падел».

For names using a preferred pattern, emphasize its letters with bold Markdown and briefly decode the construction, for example `**Y**our **P**lan` or `**Я** люблю **П**адел`. Keep the target letters uppercase in the displayed name. Present an exceptional name normally and briefly explain why it is stronger without the pattern. Do not force nonsensical grammar merely to obtain the pattern.

## Permission specification

Create exact purpose copy only after the feature mapping is stable. For each capability, write one concise, natural sentence in the product language that names the concrete feature or result and explains the user benefit. Avoid vague phrases such as “для работы функций,” claims about features the MVP does not implement, and lists such as “фото, видео и сканирование” when only one behavior exists.

Map the copy to these surfaces:

| Capability | Copy destination |
|---|---|
| Bluetooth | `NSBluetoothAlwaysUsageDescription` |
| Camera | `NSCameraUsageDescription` |
| Contacts | `NSContactsUsageDescription` |
| Face ID | `NSFaceIDUsageDescription` |
| Location | `NSLocationWhenInUseUsageDescription` |
| Microphone | `NSMicrophoneUsageDescription` |
| Photo-library read | `NSPhotoLibraryUsageDescription` |
| Photo-library add | `NSPhotoLibraryAddUsageDescription` |
| Advertising tracking | `NSUserTrackingUsageDescription` |
| Push notifications | In-app pre-permission explanation; iOS owns the system notification alert copy |

Keep photo-library read access and add-only access separate in copy, rationale, data handling, and user actions. When multiple languages are requested, provide a base value plus localized values suitable for `InfoPlist.strings`; do not pretend runtime code can replace static purpose strings.

## Permission and privacy review

For every required capability, create a permission-to-review row containing:

- exact reachable button, screen, or action that initiates the request;
- concrete feature and user benefit;
- exact purpose or pre-permission copy;
- behavior after authorization, limited access, denial, restriction, and unavailability as applicable;
- data accessed, whether it remains local or is sent to the backend or AppMetrica, and its retention/deletion behavior;
- App Store privacy-label or tracking implication;
- concise reviewer instruction explaining how to exercise the feature.

Then produce one consolidated data inventory covering app data, backend payloads, notification tokens, installation identifiers, and third-party SDK collection. Distinguish data stored only on device from data transmitted off device, data linked to identity, and data used for tracking. Do not claim that no data is collected merely because the app itself does not retain it when an integrated SDK transmits data.

Assign the concept a low, medium, or high App Store review risk. Name the most questionable permissions and the smallest product adjustment that would reduce risk. This is an evidence-based warning, not a guarantee of approval or a reason to discard the user's core idea automatically.

## Expand the selected concept

After the user selects or approves a concept, provide:

1. **Concept**: Describe the product, target user, and primary recurring action in 2–3 sentences.
2. **Names**: Give the requested number of understandable name variants following the naming rules.
3. **MVP**: List the fewest coherent user-facing functions that together exercise all required permissions. Map every function to at least one permission, allow one function to cover several permissions, and exclude unrelated or speculative secondary features.
4. **Permission review matrix**: For all required capabilities, provide the action, benefit, exact feature-specific copy, authorization and denial behavior, data handling, privacy-label implication, and reviewer instruction. Map direct photo-library reading separately from adding media.
5. **Extensions**:
   - Define one glanceable Lock Screen widget using WidgetKit. Use ActivityKit only when the concept has a genuinely live, time-bound state.
   - Define a Notification Service Extension that enriches, decrypts, filters, or attaches media to remote notifications.
   - Define a Notification Content Extension with a compact custom notification interface and at least one relevant action.
6. **Minimal backend**:
   - Name the smallest useful state or entity set.
   - Prefer only `GET /health` and one idea-specific `POST /sync` operation. Let `/sync` accept and return one compact snapshot and carry an installation identifier, lightweight authentication value, and APNs device token when practical.
   - Add or split endpoints only when the concept cannot demonstrate its required client-server or push flow with the merged operation. Keep the total to 1–3 endpoints.
   - Use memory or one JSON file. Avoid separate authentication, device-registration, CRUD, database, queue, admin, or recommendation layers unless they are unavoidable.
7. **Data inventory**: Summarize local data, backend payloads, notification and installation identifiers, AppMetrica data, tracking use, retention, and deletion.
8. **AppMetrica and ATT**: Define SDK modules, custom event names without sensitive parameters, SDK-level collection, advertising or attribution behavior, denial behavior, and the disclosures this creates.
9. **Privacy policy**: Define the in-app entry point and the exact collection, purpose, recipient, retention, deletion, consent-withdrawal, and contact statements the hosted policy must cover. Leave only the final public URL as a release blocker when unavailable.
10. **Conditional policy modules**: Record every module as selected or `not-applicable` and define the accepted behavior for selected modules.
11. **Fit check**: State why all permissions, AppMetrica, extensions, and backend belong to the same releaseable product rather than being decorative.
12. **Feasibility verdict**: Report each gate item, the low/medium/high residual review risk, questionable permissions, accepted mitigations, and any blocking conflict. Only a concept with no blocking conflict may receive `policy-approved`.

## Quality checks

Before creating the approved handoff, silently verify:

- The selected concept covers all 10 required permission or authorization categories, counting photo-library read and add access separately.
- Every required permission is exercised by a reachable user action, not only listed in configuration.
- Every purpose string names the implemented feature and user benefit; no generic or misleading copy remains.
- Every permission has authorization, denial, data-handling, privacy-label, and reviewer-path entries.
- Full Contacts and Photo Library access, Face ID, ATT, and Bluetooth each have a credible core purpose rather than a decorative prompt.
- Every user-facing MVP feature supports at least one required permission; supporting technical behavior is allowed but minimized.
- Aim for most name options to contain or expand to `YP`, `Y P`, or `Я П`; allow exceptions when they are clearer or explicitly preferred by the user.
- Do not generate `ЯП`, `YaP`, `Ya P`, or `YA P` name constructions; when supplied by the user, warn about unnecessary attention to the naming and offer a nearby replacement.
- Names are understandable and related to the concept.
- The selected concept contains all 3 required extension types.
- The backend is minimal, preferably `/health` plus one merged `/sync`, and exposes a concrete reason to exist.
- The data inventory covers on-device, backend, APNs/installation, AppMetrica, and tracking behavior without unsupported “no collection” claims.
- AppMetrica behavior and ATT denial are concrete, disclosed, and consistent with the data inventory.
- The privacy-policy disclosure set covers collection, purposes, recipients, retention, deletion, consent withdrawal, and contact behavior.
- Every conditional policy module is selected with an accepted implementation path or marked `not-applicable` from observable product facts.
- Every App Review feasibility gate item passes; otherwise the handoff remains `idea-draft`.
- The answer contains a review-risk verdict and a smallest risk-reducing adjustment.
- The concepts differ in audience and recurring behavior, not just visual theme.
- Every concept is general-audience, avoids age gates, and is not built around a high-risk App Store review topic.
- Every concept is explicitly iPhone-only and portrait-only, remains fully usable without rotation, and contains no iPad, Mac, Apple Vision, watch, TV, or cross-platform product surface.
- No implementation work has been performed.

## Policy-approved handoff

After the user explicitly accepts an idea, it passes the feasibility gate, and the user wants to continue, prepare `AppSpec.md` and `AppPrivacy.yml` in the current application workspace. If no workspace exists yet, present both complete artifacts in the conversation and write them when a destination becomes available. These two files are the only filesystem outputs allowed in this skill.

Treat `AppSpec.md` as the source of truth for product behavior and approved copy. Treat `AppPrivacy.yml` as the source of truth for machine-readable permission, data, SDK, tracking, domain, retention, deletion, privacy-label, policy-module, and release-blocker facts. Record approved choices exactly and do not silently change them. Mark unavailable release values as release blockers instead of inventing them.

Include in `AppSpec.md`:

- Specification status `policy-approved` and the feasibility-gate verdict.
- Product name, concept, audience, primary recurring action, and permission-centered MVP.
- iPhone-only, portrait-only, and minimum-iOS requirements.
- All 10 authorization categories, counting photo-library read and add separately.
- For every authorization: feature, visible trigger, exact purpose or pre-permission copy, authorization and denial behavior, accessed data, storage and transmission, privacy implication, and reviewer path.
- Consolidated local, backend, APNs/installation, AppMetrica, and tracking data inventory, including retention and deletion behavior.
- Minimal backend endpoints and product-level request/response fields.
- AppMetrica and ATT-dependent behavior.
- Lock Screen widget, Notification Service Extension, and Notification Content Extension roles.
- In-app privacy-policy entry and required hosted-policy disclosures.
- Selected conditional policy modules and accepted behavior.
- App Store review-risk verdict, accepted mitigations, accepted decisions, and release blockers.

Create `AppPrivacy.yml` from `assets/AppPrivacy.template.yml`. Complete every semantic field that is knowable at this stage. Keep changing Apple constants, generated manifest entries, and App Store Connect selections as derived release-stage outputs rather than hard-coding future policy into this specification.

Do not add screen layouts, colors, UIKit structure, Xcode targets, or implementation details that belong to later skills.

## Response shape

When the user brings an idea, lead with the refined version of that idea. Proactively include worthwhile improvements and, when genuinely stronger, a small clearly marked set of close alternatives derived from the same direction; never let them displace the user's concept. End with one concise offer to generate broader alternative concepts in a follow-up, such as: «Если хочешь, могу отдельно предложить несколько более свободных альтернатив». Generate broader or unrelated alternatives only after the user accepts or explicitly asks for them. When generating ideas from scratch, lead with a short comparison list. Then expand each idea using the sections above. Put the feature-specific permission-review matrix once after each complete concept, unless the user asks for permission copy first or requests only one section.

When the user asks only for names, permission texts, extensions, or backend refinements, preserve the accepted parts of the existing idea and return only the requested section.

When the user accepts an idea, pass the feasibility gate, prepare the `AppSpec.md` and `AppPrivacy.yml` handoff, and propose using `design-ios-app-concept`. Do not skip directly to implementation unless an explicitly approved design already exists. Stop before rendering screens or writing code.

# App privacy contract

`AppPrivacy.yml` is the machine-readable privacy source of truth for the complete iOS pipeline. `AppSpec.md` owns product behavior and approved user-facing copy; when the files disagree, stop and resolve the contradiction before design, implementation, or release work.

## Ownership

- `permissions` records the ten mandatory authorization mappings, exact copy, denial behavior, data types, and reviewer path.
- `data_inventory` records every local or transmitted data type, purpose, recipient, linkage, tracking use, retention, and deletion behavior.
- `third_party_sdks` records AppMetrica and any later dependency, including version, modules, collection, manifest, signature, and domains.
- `tracking` records ATT-dependent behavior and the useful non-tracking path after denial.
- `domains` records the production API, privacy-policy, support, and SDK destinations.
- `privacy_policy` records the in-app entry and every disclosure the hosted policy must contain.
- `app_store_privacy` records the semantic answers that later map to current App Store privacy questions.
- `policy_modules` records selected or `not-applicable` compliance modules.
- `approval_log` records explicit user decisions at stage boundaries: stage, decision, UTC timestamp, user actor, authorized next stage or external action, and a short non-sensitive evidence summary.
- `release_blockers` contains unresolved values that prevent `release-ready`.

## Derived artifacts

Info.plist purpose strings, `PrivacyInfo.xcprivacy`, entitlements, Xcode Privacy Report findings, privacy-policy prose, App Store Connect selections, and App Review notes are derived from the contract. Do not store mutable Apple reason codes or version requirements as permanent semantic truth.

The release stage checks current primary Apple documentation, then compares every derived artifact with the contract. The pipeline **fails closed** when runtime behavior, AppMetrica configuration, backend traffic, manifests, policy text, or App Store disclosures disagree.

## Approval rules

A status alone never authorizes later work. Each transition to a new stage requires a matching `approval_log` entry created from an explicit user message after the prior stage gate summary. A blanket request made before the summary, silence, partial feedback, or approval for another artifact is not valid evidence.

If an approved artifact changes materially, treat the matching approval as stale, return to that stage, present the revised gate summary, and request approval again. Keep evidence summaries short and do not copy secrets or sensitive user content into the log.

## Status rules

- `idea-draft`: fields may be `pending` while alternatives are explored.
- `policy-approved`: every product and privacy decision needed for design is complete; only external release values may remain blockers.
- `design-approved`: screen and state locations are recorded without changing the privacy meaning.
- `implementation-verified`: binary behavior and configuration match the contract for simulator-verifiable paths.
- `archive-validated`: the Release archive and aggregated privacy report match the contract.
- `release-ready`: no release blocker remains. Manual device checks may still be listed for the user and are not a pipeline status.

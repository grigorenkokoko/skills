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
- `release_blockers` contains unresolved values that prevent `release-ready`.

## Derived artifacts

Info.plist purpose strings, `PrivacyInfo.xcprivacy`, entitlements, Xcode Privacy Report findings, privacy-policy prose, App Store Connect selections, and App Review notes are derived from the contract. Do not store mutable Apple reason codes or version requirements as permanent semantic truth.

The release stage checks current primary Apple documentation, then compares every derived artifact with the contract. The pipeline **fails closed** when runtime behavior, AppMetrica configuration, backend traffic, manifests, policy text, or App Store disclosures disagree.

## Status rules

- `idea-draft`: fields may be `pending` while alternatives are explored.
- `policy-approved`: every product and privacy decision needed for design is complete; only external release values may remain blockers.
- `design-approved`: screen and state locations are recorded without changing the privacy meaning.
- `implementation-verified`: binary behavior and configuration match the contract for simulator-verifiable paths.
- `archive-validated`: the Release archive and aggregated privacy report match the contract.
- `release-ready`: no release blocker remains. Manual device checks may still be listed for the user and are not a pipeline status.

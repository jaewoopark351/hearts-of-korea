# AGENTS.md

## Scope and mission

This file applies to the repository root and all descendant directories unless a closer `AGENTS.md` or `AGENTS.override.md` provides more specific instructions.

This repository is the authorized successor, restoration, and continued-development project for **하츠 오브 코리아 / Hearts of Korea**.

Project facts:

- Original Steam Workshop item: `2898629778`
- The original creator has passed away, so ordinary upstream maintenance cannot resume.
- The continuation team has been asked to preserve, repair, continue, and publish the mod as a new Steam Workshop item.
- The original item and ID are historical source and credit references only, never this project's upload identity.

Primary objectives:

1. Restore compatibility with the explicitly selected HOI4 version.
2. Preserve the original mod's identity, authorship, intended content, stable IDs, balance, and gameplay behavior during restoration.
3. Fix confirmed defects and recover update-broken content.
4. Continue development, modernization, redesign, or rebalance only when explicitly scoped.
5. Prepare and publish a separately identified successor release when the user explicitly authorizes the concrete publication action.

This is not merely a private maintenance fork, but restoration remains the default priority. Keep compatibility fixes, bug fixes, refactors, balance changes, and new successor content as distinct workstreams. Do not silently turn an update repair into a redesign. More specific instructions may add constraints, but must not weaken the safety, evidence, attribution, or validation rules in this file.

---

## 1. Obey the requested operating mode

Determine the task mode from the user's request before using tools or changing files.

### Review-only

When asked only for review, analysis, planning, comparison, or a verdict:

- Do not edit files or generate patches.
- Do not launch HOI4 or run tests, validators, formatters, or scripts unless requested.
- Do not change Git state, commit, push, publish, or upload.
- Report findings with evidence, file paths, and line numbers where available.

### Diagnostics-only

When diagnostics are authorized but behavior changes are forbidden:

- Preserve gameplay behavior.
- Add only the minimum bounded instrumentation needed to distinguish concrete hypotheses.
- Do not refactor surrounding systems.
- Do not convert a suspected failure directly into a speculative fix.
- Mark temporary diagnostics and state how they should be removed or disabled.

### Implementation

When implementation is explicitly authorized:

- For compatibility or bug repair, make the smallest patch that addresses the demonstrated cause.
- For explicitly requested continuation development, state the intended behavior change and keep it separate from restoration work.
- Keep unrelated cleanup, formatting, and unrequested balance changes out of the diff.
- Preserve IDs, namespaces, filenames, load order, attribution, and save behavior whenever possible; document deliberate migrations.
- Validate the modified subsystem and expand testing according to risk.

### Release preparation

When asked to prepare a release:

- Prepare only the package, descriptors, metadata, credits, changelog, dependency list, and validation record requested.
- Use a clean staging directory or explicit allowlist; exclude `.git`, `AGENTS.md`, editor state, logs, saves, crash dumps, caches, credentials, and private records unless deliberately shipped.
- Keep original Workshop ID `2898629778` as provenance only and remove stale upstream upload identity from the active successor package.
- Stop before any external upload unless that exact action is explicitly requested.

### Publication

Publishing a new successor item is an intended project outcome. When publication or an update is explicitly requested:

- First publication must create a **new** Workshop item.
- Never upload to, overwrite, impersonate, or reuse original Workshop item `2898629778`.
- Later updates may target only the recorded successor item after verifying its ID.
- Credit the original creator and identify the release as a continuation/restoration.
- Do not call it “official” unless the user approves that wording and project records support it.
- Record the source state, release version, dependency set, target HOI4 version, resulting successor item ID, and external actions performed.

Never commit, amend, rebase, merge, reset, clean, push, tag, publish, or upload merely because implementation or preparation was requested. Each Git-changing or external action requires explicit authorization for that action.

---

## 2. Project baseline

Historical upstream baseline:

- Mod: `하츠 오브 코리아 Hearts of Korea`
- Original Workshop ID: `2898629778` (historical reference only)
- Last known upstream version: `1.0.9(1) '강계'`
- Last declared HOI4 compatibility: `1.16`
- Declared required dependency: `Korean Language`
- Scope includes map changes, national focuses, events, decisions, characters, equipment/assets, localisation, and multiplayer-conscious balance.

Successor baseline:

- Project type: authorized continuation, restoration, and new publication project
- Successor Workshop ID: unassigned until first publication; never assume or copy the original ID
- Repository/local development copy: authoritative working source
- Original Workshop copy: read-only historical input
- Original authorship and third-party credits: retained; continuation contributions recorded separately

Treat this continuation mandate as established project context. Do not block routine work by demanding approval from the unavailable original maintainer; escalate only concrete contradictory evidence or a specific third-party restriction.

Do not infer the current target version from memory or from `supported_version` alone. Before compatibility work, record when available:

- exact HOI4 version and build/checksum
- enabled DLC
- launcher playset
- required and optional mods in load order
- language/localisation setup
- operating system and actual HOI4 user-data directory
- repository branch, commit, and working-tree state

When the target version is unknown, perform non-destructive inventory work only and state that version-dependent conclusions remain unproven.

---

## 3. Evidence hierarchy

Use this source order:

1. Exact target-version vanilla files and observed engine behavior.

2. A clean reproduction using the recorded playset.

3. Current runtime logs and crash data.

4. The mod and dependency sources actually loaded by the launcher.

5. Current HOI4 documentation for the target version.

6. Historical examples, forum posts, or model memory.

The installed target-version vanilla files are the canonical syntax and schema reference. Do not import syntax from EU4, CK3, Victoria 3, Stellaris, or another HOI4 era merely because it looks similar.

Classify conclusions:

- `CONFIRMED`: directly demonstrated by source, log, or reproduction.
- `STRONGLY_SUPPORTED`: multiple pieces of evidence agree, but runtime proof is incomplete.
- `UNPROVEN`: plausible hypothesis requiring more evidence.
- `DISPROVEN`: contradicted by observed evidence.

Never present an inference as a confirmed engine fact.

---

## 4. Required inspection before production edits

Before editing a production mod file:

1. Read the task and identify explicit prohibitions.

2. Locate all applicable agent instruction files.

3. Record Git branch, commit, and working-tree state.

4. Inspect `descriptor.mod` and the launcher `.mod` file when available.

5. Identify `supported_version`, dependencies, `replace_path`, and `remote_file_id` entries.

6. Confirm which physical mod copy the launcher loads.

7. Distinguish the repository, local development mod, and Workshop download.

8. Preserve relevant baseline logs before a new launch overwrites them.

9. Reproduce the failure with the smallest valid playset when runtime access is authorized.

10. Find the target-version vanilla counterpart or a known working target-version example.

11. Identify the earliest failure, not merely the largest cluster of cascading errors.

12. When the cause is unclear, form competing hypotheses and define the observation that distinguishes them.

Do not edit the Steam Workshop directory or base-game installation directly. Work in the repository and, when necessary, a separate local development-mod copy.

---

## 5. Root-cause classification

Classify the failure before choosing a fix. Typical categories:

- parser or syntax error
- illegal trigger/effect for the current scope
- changed, removed, or renamed engine key
- missing referenced ID
- duplicate ID or silent override
- file load-order collision
- unsafe `replace_path`
- descriptor, dependency, language-mod, or DLC-gating error
- localisation encoding, header, key, or load-order error
- map, state, province, strategic-region, railway, supply, or adjacency error
- country history, OOB, equipment, technology, character, or bookmark error
- GFX, model, animation, sound, or interface path error
- AI weight, strategy, or evaluation error
- performance or event-spam loop
- save incompatibility
- original upstream bug unrelated to the HOI4 update

Many later errors may be cascades from one early load failure. Fix and retest the earliest proven cause before mass-editing downstream references.

---

## 6. Paradox Script rules

Treat Paradox Script as context-sensitive game logic, not generic configuration text.

### Scope correctness

For every changed trigger or effect, determine:

- expected input scope
- scope produced by each iterator or scope switch
- meaning of `ROOT`, `THIS`, `PREV`, `FROM`, event targets, saved scopes, and variables at that location
- whether the trigger/effect is legal for that scope in the target version

Do not hide a scope error by deleting the condition, adding `always = yes`, changing the target arbitrarily, or wrapping the block in a broad existence check unless that exact change is proven to preserve intent.

### Stable IDs and namespaces

Preserve existing identifiers unless an explicit migration is required, including:

- country tags and cosmetic tags
- event namespaces and IDs
- focus, decision, mission, idea, character, technology, and equipment IDs
- scripted trigger/effect/localisation names
- OOB, template, ship, variant, modifier, flag, variable, and event-target names
- sprite/asset names
- state, province, strategic-region, and supply-network IDs
- localisation keys

Before adding an ID, discover and follow the existing project prefix. If no convention exists, propose one rather than silently polluting the global namespace.

Duplicate definitions may silently override earlier content. Search the mod, required dependencies, and relevant vanilla files before declaring an ID unique.

### Preserve behavior

Do not casually alter:

- `ai_will_do` factors and modifiers
- random-list weights
- focus prerequisites, bypasses, cancellation, mutual exclusion, or rewards
- event cadence, triggers, options, or follow-up chains
- decision visibility, availability, cost, duration, cooldown, cancel, or remove rules
- national spirit and dynamic modifier values
- equipment statistics
- state resources, factories, infrastructure, supply, ownership, cores, or claims
- starting OOB, research, politics, laws, stability, or war support
- shared scripted constants

Compatibility repair, refactoring, rebalance, and successor development are separate tasks. Intentional changes require explicit scope and documentation; a parser-clean file can still be a gameplay regression.

### Editing discipline

- Do not apply broad search-and-replace without reviewing every affected context.
- Do not reformat an entire file for a local fix.
- Preserve comments explaining historical intent or engine quirks.
- Add comments only for non-obvious compatibility constraints.
- Do not delete an unknown key merely to quiet `error.log`; determine whether it was renamed, moved, DLC-gated, or replaced.
- Preserve exact filename and path casing, including on Windows.
- Check braces, quotes, list structure, and block placement after edits.

---

## 7. File-specific critical rules

### Descriptors

For `descriptor.mod` and launcher `.mod` files:

- Changing `supported_version` is not a compatibility fix.
- Preserve dependencies unless migration is explicitly requested.
- Audit every `replace_path`; it can unload broad vanilla databases and cause distant failures.
- Never add `replace_path` merely to hide duplicate or stale content.
- Treat original Workshop ID `2898629778` as provenance only; a successor release must never inherit or target its `remote_file_id`.
- Do not invent a successor `remote_file_id`; record it only after first publication assigns one.
- Do not change successor upload identity or Workshop metadata without an explicit release task.
- Keep launcher, repository, staging, and release descriptors logically consistent while respecting their different path fields.

### `common/`

- Check global ID uniqueness and overwrite behavior.
- Compare changed definitions with the target-version vanilla schema.
- Verify DLC-dependent types and modifiers.
- Trace scripted triggers/effects transitively, not only the immediate caller.
- Treat `on_actions` as high risk because small errors can cause global repeated execution or silently remove callbacks.

### Events, decisions, and focuses

- Preserve namespaces and IDs.
- Verify receiving scope and every scope transition.
- Verify focus prerequisites, bypass, cancel, mutual exclusion, rewards, and AI selection.
- Verify decision visibility separately from availability and completion/removal.
- Check recurring content for accidental daily firing or unbounded event chains.

### History, OOB, characters, and bookmarks

- Preserve date blocks and supported start dates.
- Verify ownership, control, cores, claims, buildings, resources, and victory points.
- Verify character definition, recruitment, roles, traits, portraits, assignment, and retirement/death rules.
- Verify OOB references to templates, equipment, technologies, variants, leaders, states, and provinces.
- Do not solve a missing reference by deleting starting content unless removal is the intended design.

### AI

- Separate “the AI can parse/evaluate this” from “the AI behaves as intended.”
- Inspect the combination of focus weights, strategy plans, templates, equipment, research, diplomacy, and other competing priorities.
- Do not infer final behavior from one isolated factor.
- Avoid unbounded logging in high-frequency AI evaluation paths.

### GFX, interface, models, and sound

- Verify exact asset name, file path, extension, casing, frame count, texture format, and referenced entity.
- Do not mass-convert or recompress binary assets.
- Do not replace missing art with placeholders unless requested.
- Keep asset compatibility changes separate from gameplay changes unless evidence connects them.

---

## 8. Localisation and encoding

HOI4 localisation files are not ordinary YAML. Do not run a generic YAML formatter on them.

- Preserve UTF-8 with BOM for localisation `.yml` files.
- Preserve the project's established language header and its contract with the required Korean language mod.
- Do not invent or replace a locale header without confirming how the active dependency loads it.
- Preserve the expected key form, such as `KEY:0 "Text"`, unless the project has a verified alternative.
- Preserve `$KEY$` substitution, scripted tokens, colour codes, icon tokens, newline escapes, and quote escaping.
- Check duplicate keys and exact casing.
- Keep keys stable for translation and compatibility submods.
- Do not mass-normalize BOMs, encoding, line endings, whitespace, or Unicode.
- Verify Korean text in game, not only in an editor.

Missing text may be a reference or load-order failure rather than a missing string. Trace the caller, key, language header, loaded file, and dependency order.

---

## 9. Map and state work is high risk

Do not modify map-related files unless the task explicitly concerns the map or evidence proves a map definition is the root cause.

Map work includes province definitions/bitmaps, terrain and height data, states, strategic regions, supply nodes, railways, adjacencies, buildings, unit positions, victory points, and ownership.

Required rules:

- Preserve globally unique province IDs and colours.
- Do not renumber state or province IDs casually.
- Verify province-to-state and province-to-strategic-region membership.
- Verify land/sea/lake/coastal classification and adjacency consistency.
- Verify supply, railway, naval-base, and building references after topology changes.
- Verify unit and building positions after geometry changes.
- Nudger output may be written to the HOI4 user-data directory, not the repository. Inspect and copy only intended output.
- Never copy a whole vanilla map folder or add broad `replace_path` as a bandage.
- Main-menu load is insufficient. When authorized, load a country, enter the map, unpause, and inspect affected regions.

---

## 10. Diagnostics and logs

The common Windows user-data location is:

`\<Documents>/Paradox Interactive/Hearts of Iron IV/`

The actual path may be redirected through OneDrive or a custom user directory. Resolve the directory used by the running game.

Relevant evidence may include:

- `logs/error.log`
- `logs/game.log`
- `logs/setup.log`
- `logs/system.log`
- exception and crash logs when present
- launcher logs when discovery or loading fails
- crash dumps
- reproduction-specific saves

Rules:

- Copy or rotate logs before a clean reproduction so stale output is not mistaken for current output.
- Compare against a vanilla or dependency-only control run when possible.
- Separate pre-existing vanilla/DLC/dependency warnings from mod-introduced failures.
- Inspect surrounding and preceding lines; the final message may be a cascade symptom.
- Use `-debug` only when runtime execution is authorized.
- Add script logging only to answer a stated diagnostic question.
- Prefix temporary messages consistently, for example `[HOK][FOCUS][scenario-id]`.
- Log stable identifiers and state transitions, not every daily evaluation.
- Rate-limit or cap repeated diagnostics.
- Remove or disable noisy temporary logging before release unless permanent observability is requested.

Never claim a root cause merely because deleting content made an error disappear.

---

## 11. Compatibility workflow

For each compatibility problem:

1. **Reproduce** using the exact target version and smallest valid playset.

2. **Capture** the earliest relevant log evidence and visible behavior.

3. **Locate** the affected definition and all referenced IDs.

4. **Compare** with a target-version vanilla or known-working example.

5. **Classify** the failure and competing hypotheses.

6. **Patch** the smallest proven incompatibility.

7. **Retest** the exact reproduction before broad smoke testing.

8. **Compare logs** with the baseline/control.

9. **Check behavior**, not merely parsing or launch success.

10. **Review the diff** for accidental ID, balance, encoding, or unrelated changes.

11. **Record uncertainty** and untested paths.

Do not jump from “old mod” to “rewrite with current syntax.” Old syntax may still be valid, and newer syntax may have different semantics.

---

## 12. Validation requirements

Use the smallest relevant subset first, then expand according to risk.

### Static checks

- no unintended additions or deletions
- valid braces, quotes, and block placement
- no newly introduced duplicate IDs
- no broken event/focus/decision/character/idea/equipment/technology/map/asset/localisation references
- descriptor and dependency consistency
- localisation BOM/header/key integrity
- no accidental whole-file encoding or line-ending conversion

### Launcher and load checks

- launcher detects the intended local mod copy
- exact playset and load order are recorded
- the correct physical source is loaded
- main menu loads without a new relevant fatal error
- declared `supported_version` is not confused with demonstrated compatibility

### New-game smoke checks

For every supported bookmark relevant to the change:

- Korea loads in the intended state
- leader, government, parties, laws, ideas, research, and resources load
- focus tree opens and key branches remain connected
- decisions and events appear under intended conditions
- starting OOB and equipment load
- custom states, ownership, cores, claims, supply, and victory points are correct
- portraits, icons, models, names, and localisation resolve
- unpausing does not immediately produce a crash, event spam, or severe error growth

### Targeted and regression checks

- demonstrate the pre-patch failure when possible
- demonstrate the intended post-patch behavior
- test a positive path and an important blocked/negative path
- inspect AI runtime behavior when AI logic changes
- inspect save/load when persistent IDs, flags, variables, history, or map data changes
- check multiplayer checksum/synchronization only when multiplayer compatibility is claimed

Risk examples:

- focus: prerequisites, bypass, cancel, mutual exclusion, rewards, AI path
- event: trigger, scope, options, repeat firing, localisation, follow-up chain
- decision: visibility, availability, cost, duration, cancel/remove, target scope
- character: recruitment, role, portrait, traits, advisor/leader assignment
- map/state: load, unpause, supply, railway, adjacency, ownership, buildings, positions
- equipment/OOB: production, deployment, templates, variants, starting stockpile
- localisation: active language setup and translation-submod key stability

A successful launch is not sufficient evidence that the mod is repaired.

---

## 13. Definition of done

A compatibility fix is complete only when:

- target HOI4 version and test playset are recorded
- original failure is precisely described
- root cause is confirmed, or remaining uncertainty is explicitly bounded
- patch is limited to the demonstrated cause
- intended behavior is preserved, or intentional changes are documented
- the exact reproduction no longer fails
- no new relevant errors appear compared with the baseline/control
- affected IDs, scopes, localisation, dependencies, and load-order effects are reviewed
- diff contains no unrelated cleanup or mass formatting
- runtime validation status is stated honestly

A successor release is ready only when:

- the source commit or immutable source snapshot is recorded
- the staged package contains only intended public/runtime files
- no upload configuration targets original Workshop item `2898629778`
- original authorship, original-item provenance, third-party credits, and continuation contributors are represented accurately
- the description identifies the item as a continuation/restoration without impersonating the original upload
- target version, dependencies, changelog, known limitations, and actual validation status are documented
- first publication remains a new item; later updates target only the recorded successor ID

Not sufficient by itself:

- updating `supported_version`
- reaching the main menu
- reducing raw log-line count
- deleting content until `error.log` becomes quieter
- passing a text parser
- observing one happy path
- renaming and uploading an unverified copy
- inheriting the original `remote_file_id`

---

## 14. File, Git, attribution, and publication safety

- Never modify the base-game installation or use a Workshop-managed copy as the authoritative working tree.
- Never overwrite user saves, playsets, or settings without explicit authorization and backup.
- Do not commit logs, crash dumps, saves, caches, credentials, account data, or personal launcher data unless requested as sanitized fixtures.
- Do not use destructive Git commands such as `git reset --hard`, `git clean`, forced checkout, or force-push.
- Do not discard pre-existing user changes, rename large trees for aesthetics, or mass-convert binary assets.
- Do not add tools, dependencies, generators, or formatters unless approved and materially useful.
- Keep restoration patches small; keep intentional successor changes separately attributable whenever practical.
- Publication of a new continuation item is permitted when explicitly directed.
- Original Workshop item `2898629778` remains a historical reference, never an upload target.
- Do not impersonate the original creator or present inherited code, writing, art, audio, research, or design as newly authored.
- Preserve original names, credits, notices, and third-party attributions; do not invent or remove a licence.
- Mention the creator's death publicly only with user-approved wording, respectfully and never as marketing copy.
- Never expose credentials or perform an upload, update, visibility change, deletion, or metadata mutation without an explicit instruction for that exact target and action.

---

## 15. Reporting format

For implementation or diagnostics work, report:

1. **Scope**: what was and was not authorized.

2. **Baseline**: branch/commit, target version, playset, dependencies, and reproduction.

3. **Evidence**: relevant logs, source locations, and observed behavior.

4. **Root cause**: confirmed fact versus inference.

5. **Changes**: files and logic changed.

6. **Behavior impact**: preserved behavior and intentional differences.

7. **Validation**: checks actually run and results.

8. **Remaining risk**: untested DLC, bookmarks, branches, submods, multiplayer, saves, or map paths.

9. **Git state**: working-tree changes and whether any commit/push occurred.

For release-preparation or publication work, additionally report:

- preparation only, first successor publication, or successor-item update
- source state, package path/hash when practical, release version, and target HOI4 version
- original historical ID and successor target ID, clearly distinguished
- dependency, metadata, credit, changelog, and validation status
- external account/Workshop actions actually performed

For review-only work:

- Put findings first, ordered by severity.
- Cite paths and line numbers where possible.
- Explain concrete failure modes, not style preferences.
- Separate confirmed defects from suggestions.
- State when runtime evidence is missing.
- Do not claim “no issues” when only a subset was inspected.

---

## 16. Hearts of Korea preservation and continuation rules

- Preserve the original vanilla-friendly, multiplayer-conscious balance during restoration unless rebalance is explicitly requested.
- Preserve the Korean identity, alternate-history premise, ideological routes, formables, leaders, names, custom assets, comments, credits, and design history.
- Treat the custom Korean map/state layout as a high-risk subsystem.
- Preserve localisation keys used by translation and compatibility submods whenever possible.
- Preserve the Korean-language-mod contract until a deliberate migration is designed and tested.
- Do not remove content merely because vanilla or a DLC changed; identify the target-version replacement mechanism first.
- Do not collapse custom content into vanilla placeholders merely to make the mod load.
- Distinguish inherited content, restoration fixes, intentional redesigns, and new continuation content in history and release notes.
- Do not imply that inherited work was created by the continuation team or that the original Workshop identity transferred to the new item.
- New content, modernization, and rebalance are allowed when explicitly requested, but must preserve attribution and be tested independently from restoration claims.

---

## 17. Safe stopping conditions

Stop modifying and report the evidence instead of guessing when:

- the exact target version materially affects the fix but cannot be determined
- the launcher loads a different copy than the repository under review
- unknown dependency/load order directly affects the failure
- multiple root causes remain equally plausible
- a fix requires renumbering persistent map IDs
- a `replace_path` migration would unload broad vanilla content
- required binary source/format information is unavailable
- save compatibility needs an explicit migration decision
- an upload command or descriptor would target original Workshop item `2898629778`
- the intended successor item/account/action is unresolved at the external-action boundary
- a concrete third-party licence or attribution conflict is discovered
- the staged package contains credentials, personal data, or files whose publication status cannot be determined safely

Do not stop merely because this is a successor project, a new Workshop item is required, or the original maintainer is unavailable; those are established project conditions.

When blocked, make the safest non-destructive progress possible: inventory the subsystem, identify missing evidence, and provide the next concrete diagnostic or release-preparation step. Do not manufacture certainty to keep moving.

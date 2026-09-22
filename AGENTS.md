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

### Language and evaluation model

Paradox Script is a family of directory- and context-specific declarative DSLs, not a single general-purpose language. Syntax that works in one database, block, or game version is not evidence that it is legal or equivalent in another. Before introducing, moving, or generating syntax, verify the target directory's root schema, loader and merge behavior, lifecycle, and a target-version vanilla example from the same context.

- Treat a script block as an ordered multi-map, not a JSON/YAML object or programming-language dictionary. Repeated keys can be meaningful, and effect order can change behavior. Do not sort, deduplicate, merge, or generically round-trip blocks unless that exact transformation is proven semantics-preserving for that file type.
- Do not import C, C++, or Java operators, statement syntax, or comment syntax. `=` is context-dependent; do not substitute `==`, `&&`, `||`, `!`, semicolons, `//`, or `/* ... */`. Use `#` comments and only syntax demonstrated for the target HOI4 version.
- In ordinary trigger contexts, sibling conditions form a declarative condition set. Do not rely on left-to-right evaluation or short-circuit behavior to make a later condition safe. In effect contexts, earlier commands can change the state or scope used by later commands, so preserve and test command order. A `limit` block remains trigger context even when nested inside an effect construct.
- Brace nesting alone does not prove a scope change. Identify the enclosing command's actual scope contract. Treat `any_*`, `all_*`, `every_*`, and `random_*` constructs as distinct engine operations rather than interchangeable loop forms.
- Treat scripted trigger/effect parameters as context-sensitive expansion, not statically typed function arguments. At every caller, verify required parameters, resulting tokens, entry scope, and the meaning of `ROOT`, `THIS`, `PREV`, and `FROM`.
- Distinguish runtime variables, flags, event targets, saved scopes, and scripted parameters. For state-bearing constructs, verify owning scope, lifetime, unset or default behavior, save persistence, and multiplayer implications. Do not assume lexical block scope or automatic initialization.
- Do not infer numeric semantics from notation alone. For modifiers, weights, costs, durations, and cadences, verify units, additive versus multiplicative behavior, defaults, clamps, and legal ranges against target-version evidence.

### Load and runtime model

Paradox Script has no Java/C++-style compile, type-check, and link barrier. A brace checker, parser, external schema, or linter proves only the conditions it actually checks and may not match the target game version.

- Validate separately that the intended physical file was discovered and loaded, the definition parsed and registered, the block evaluated in the intended runtime scope, and the observable game behavior occurred. A clean parser result or quiet log does not prove all four stages.
- Before splitting, renaming, or duplicating files, determine the target directory's actual accumulation, filename precedence, duplicate-ID, dependency-order, and `replace_path` behavior. Do not assume a later file inherits from or extends an earlier definition.
- Classify the relevant lifecycle: load-time definition, new-game or history initialization, repeated trigger/AI/UI evaluation, sequential effect execution, or localisation/UI rendering. Do not infer runtime execution order merely from file order.
- Before changing a high-frequency trigger, AI weight, decision visibility/availability block, scripted GUI, or `on_action`, identify its call cadence and worst-case scope count. Do not assume caching or short-circuit evaluation without target-version evidence.
- Treat console reload and hot reload as exploratory diagnostics only. Final validation must use a full process restart and a clean run appropriate to the changed subsystem.
- Treat changes to random-selection sites, weights, and ordering as behavior changes rather than harmless refactors. When multiplayer compatibility is claimed, validate synchronized runtime behavior and inspect out-of-sync evidence in addition to comparing checksums.

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

### Focus reward design for continuation content

- For authorized new focus development and reward strengthening, design strong, noticeable rewards that make the focus worth its time and branch commitment. Do not default to token bonuses merely because a focus takes 35 days. Follow [the Korean focus reward guidelines](docs/HOK_KOREAN_FOCUS_REWARD_GUIDELINES.md).
- Preserve existing benefits unless their change is explicitly scoped. Increasing a headline modifier must not silently remove research bonuses, experience, political power, decision unlocks, DLC alternatives, or other secondary effects.
- Treat user-specified reward numbers as final values unless explicitly described as additions. Distinguish flat daily political power, percentage modifiers, research bonus magnitude and uses, and permanent versus temporary benefits.
- Recent approved examples include one industry research bonus of 150%, one electronics research bonus of 100%, factory construction speed of +15%, military factory output of +10%, and flat daily political power of +0.5 or +1.2. These are concrete design references, not a mandatory minimum or a bundle granted to every focus.
- Carry strengthened lower-tier benefits into the matching upper-tier national spirit, preserve its other benefits, and check every mutually exclusive path. Replacing a spirit must not accidentally weaken the selected policy or stack obsolete tiers.
- Evaluate decision costs and opportunity costs against the benefit actually available to the player. When factory costs are explicitly removed, also review availability gates, AI gates, and descriptions; do not extend that removal to unrelated decisions.
- Record branch timing, cumulative rewards, and validation limits. This preference applies within authorized continuation or rebalance work; it does not authorize blanket changes to existing focuses during restoration, compatibility repair, or documentation-only tasks.

### Editing discipline

- Do not apply broad search-and-replace without reviewing every affected context.
- Do not reformat an entire file for a local fix.
- Preserve comments explaining historical intent or engine quirks.
- Any modified production text-code file must include a nearby contributor note in the exact form `#YYYYMMDD_kpopmodder: <brief reason/intent>`. Put it immediately above or at the end of the changed statement or block, keep one note per coherent change, preserve earlier notes, and do not add it to binary, generated, byte-exact, or documentation files.
- For paired localisation files, put the identical contributor note immediately after each locale header and preserve UTF-8 BOM.
- Except for the required contributor note above, add explanatory comments only for non-obvious compatibility constraints.
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

#### Focus placement, x/y, and relative coordinates

Before adding or moving Korean focuses, read [the layout plan](docs/HOK_KOREAN_FOCUS_LAYOUT_PLAN.md), [the coordinate specification](docs/HOK_KOREAN_FOCUS_LAYOUT_COORDINATES.md), and [the compact-layout incident record](docs/incidents/2026-09-21-korean-focus-compact.md). These record the earlier distant parent/child placements, conditional movement mismatches, and the subsequent layout that became excessively wide. Use the current source and latest specification together; do not reuse historical coordinates as current positions.

- Use a small set of stable absolute anchors and `relative_position_id` with relative `x`, `y` for related focuses. A sector root may itself be relative to another anchor; do not require every sector root to be absolute or create dummy focuses solely as anchors. Follow the documented vanilla Japan structure without copying its IDs, coordinates, offsets, or political conditions.
- Declare a relative-position anchor before every focus that references it. An existing ID later in the same file is insufficient: the 2026-09-22 HOI4 1.19.3 baseline logged “Relative focus must be scripted before this” for two Korean focuses. Check declaration order in addition to existence and cycles; if changing anchors, recalculate relative values to preserve the intended base position. See [the second-wave record](docs/HOK_KOREAN_SECOND_WAVE_PLAN.md).
- Focus `x`, `y` values use the focus grid, not screen pixels. Without `relative_position_id`, they specify the base absolute position; with it, they specify displacement from the referenced focus. Resolve the entire anchor chain: `base_position(focus) = base_position(anchor) + (x, y)`. Keep this base position separate from conditional final display positions.
- When converting absolute coordinates to relative coordinates, calculate `relative_xy = desired_base_position - resolved_anchor_base_position`. Do not retain the old absolute numbers or mistake an anchor's own relative numbers for its resolved position. Record the anchor ID, source x/y, resolved base position, and relevant conditional offsets in the layout specification.
- Keep placement references separate from progression. `relative_position_id` does not replace `prerequisite` and need not identify a prerequisite. A focus with several prerequisites still uses one placement anchor; retain all prerequisite groups and their AND/OR structure. For placement-only work, preserve IDs, costs, rewards, mutual exclusions, bypass/cancel/start/visibility conditions, and AI behavior. Do not delete connections or hide branches to conceal layout defects.
- Verify that each anchor ID exists uniquely, no focus references itself, no reference cycle exists, and every chain reaches an absolute anchor. When moving an anchor, inspect every dependent focus, all affected prerequisite and mutual-exclusion connections, and adjacent sectors. Include states where the anchor is hidden or its mutually exclusive alternative was chosen.
- Place new modules near their actual parents within recognizable policy/ideology sectors. Avoid collecting new focuses on distant lower rows or inflating spacing across the whole tree. Account for all parents of a merge, Korean title plates, icon borders, mutual-exclusion marks, and space for connecting lines. Relative coordinates alone do not prevent overlaps or excessive width; compare the overall bounds and scrolling burden before and after the change.
- Trace each `offset` condition and which anchor handles movement. Do not automatically duplicate a parent's offset on its children or bulk-delete offsets. Compare final positions before and after the full conditions become true under both SHOW and HIDE; HIDE alone does not imply that a completion-dependent offset already applies. Check double movement, leftover compensation, and collisions with neighboring sectors. Distinguish hidden focuses from visible but unavailable focuses, which still occupy space.
- Treat `continuous_focus_position` as a separate panel coordinate setting, not the ordinary focus grid. Check panel clearance, shortcut destinations, scroll limits, and access to the full branch after a layout change.
- Check the actual icon/title rectangles and the engine-rendered connections, not just duplicate center coordinates or a straight-line approximation. Prevent unrelated lines from obscuring focuses, minimize unnecessary line crossings, and retain legitimate shared branch/merge lines. Judge spacing at the recorded resolution and GUI scale; a previously successful grid gap is not a universal pixel or font guarantee.
- Update the coordinate documentation and [current machine-readable layout specification](docs/data/HOK_KOREAN_SECOND_WAVE_COORDINATES.json) for implemented changes. Separate static reference/position checks from in-game visual validation. When runtime execution is authorized, inspect affected sectors and their neighbors in initial and post-choice SHOW/HIDE states, including hidden anchors, panels, and shortcuts. Record the states, resolution, GUI scale, and remaining limitations; initial-state screenshots do not prove every later state.

The documented 2026-09-21 compact baseline contains 326 focuses, 7 absolute anchors and 319 relative placements, spanning x0-194 and y0-24. Its four direct offset blocks retain their conditions with movement `(0, 0)`. These are baseline facts, not permanent limits on authorized expansion. Preserve this baseline unless the scoped layout change deliberately updates it. The compact version was visually checked in the initial HIDE state; post-ideology HIDE transitions and SHOW runtime were not rerun, so do not describe them as already validated.

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

#### Images must be stored in this project and referenced by relative path

- Every image explicitly used by this project's content must exist as a physical file inside the repository's runtime asset directories. This includes focus and national-spirit icons, portraits, interface textures, image masks, and image overlays.
- When using an image from vanilla HOI4, a Workshop mod, a dependency, a public asset pack, or any other external location, first copy the selected image into the appropriate project directory, such as `gfx/interface/goals/HOK_KOR/` or `gfx/interface/ideas/HOK_KOR/`. Reference the project copy; do not rely on the external image at runtime. Keep the source installation and Workshop files read-only, and copy only the assets needed for the scoped task.
- Set `texturefile`, `animationmaskfile`, `animationtexturefile`, and equivalent image references to mod-root-relative paths such as `gfx/interface/goals/HOK_KOR/example.dds`. Do not use absolute filesystem paths, external URLs, paths that escape the repository with `..`, or links that resolve to files outside the project.
- Focus `icon = GFX_...` and idea `picture = ...` references must resolve through project-owned sprite definitions to images stored in this project. Merely selecting an existing vanilla or dependency sprite name without a local image and sprite mapping does not satisfy this rule. A relative-looking `gfx/...` path is also insufficient if the file is supplied only by vanilla or another mod.
- Follow the existing `HOK_KOR_` sprite naming convention for new mappings, check for collisions, and avoid overriding a global vanilla sprite merely to redirect one icon. Preserve gameplay IDs and keep image-reference changes separate from behavior changes.
- Preserve the copied image's format, dimensions, alpha, frame layout, and exact path casing unless an intentional asset conversion is part of the task. Record the original source path, applicable reuse basis, original credits, and any subsequent edits; copying an image does not change its authorship or grant additional rights.
- Verify the complete sprite-to-image reference chain, including image masks and overlays: each relative path must resolve to an existing file inside this repository with exact casing. Treat missing project copies as incomplete asset integration, even if the game can find an external fallback.

#### Create and integrate artwork when adding content

When an authorized implementation adds focuses, national spirits, decisions, or other content that needs an image, include suitable artwork creation and integration in that implementation. The user permits both newly drawn/generated artwork (including AI image generation) and copying/adapting open-source or explicitly reusable public artwork; combining the two is also allowed. Choose the method per asset based on subject fit, visual consistency, readability, and effort. External-source research and the existing source-component composer are options, not mandatory prerequisites for new artwork. Save the final assets inside this project and connect them through project-owned GFX and relative paths. Routine drawing/generation, permitted source research/downloads, composition, and integration within authorized implementation do not require a separate artwork request. Review-only and documentation-only requests do not authorize image generation, downloads, asset edits, or game-code changes. Follow [the current artwork policy](docs/HOK_KOREAN_FOCUS_SPIRIT_ICON_PLAN.md).

1. Identify the content's meaning, branch or policy field, central motif, linked focus/spirit relationship, and genuine upgrade stages before selecting artwork. Follow the background-color rules below. Avoid repeating one generic icon for unrelated policies merely because it already exists.
2. For new artwork, draw or generate the needed illustration directly. For reused artwork, search suitable open-source or explicitly reusable public image packs and creators' repositories; the documented Ultimate HOI4 GFX components are one available source, not a required first step. Existing downloaded materials may be reused when their recorded terms cover the use. Use a mixed approach when a new central illustration fits an existing reusable frame or background.
3. For every external image or component reused or adapted, verify that its actual licence or explicit permission covers the intended reuse, modification, and distribution. Public visibility or availability for download alone is not permission. A repository's code licence does not automatically cover its artwork; check artwork-specific terms and third-party exceptions. Keep permission limited to the identified pack/files; do not infer permission for an entire mod or invent a licence. If a candidate cannot be used, select a permitted alternative or create new artwork. Generating or redrawing from a third-party image does not erase that source or its restrictions.
4. Keep selected source files and final selected generated originals in a project-local working directory. Compose or refine them as needed, managing background, frame, central illustration, and stage marks separately where practical. Match the agreed colors, metal treatment, proportions, and small-size readability across directly generated and reused assets. The existing composer remains suitable for component work and background-only recoloring; the earlier choice of that method for the 60-focus/29-spirit recolor does not restrict future new artwork to external components. Preserve source attribution and distinguish new drawing/generation from selection, composition, recoloring, and added marks.
5. Export the finished image to the appropriate runtime directory inside the repository, using the dimensions, alpha, frame layout, and DDS format required by the target-version UI. Keep source downloads and temporary working files separate from runtime outputs. Add or update project-owned sprite mappings, including required local image masks and overlays, and connect the content using the internal relative-path rules above. Do not leave delivery at external sprite references, unintegrated previews, or unrequested placeholders.
6. Record whether each asset is newly drawn/generated, reused, or mixed. For reused parts, retain the source URL/path, fixed revision when available, reuse evidence, contributors, and source hash. For AI-generated parts, record the generation tool, actual model if exposed, date, prompt, reference images if any, and selected original path/hash; label them as AI-generated rather than an open-source download or a named artist's work. For every method, record the content ID, subsequent edits, final project path, sprite reference, and output hash in the relevant documentation and asset manifest. Reuse [the current icon manifest](docs/data/HOK_KOREAN_FOCUS_ICON_MANIFEST.json) pattern where applicable; preserve historical attribution and do not record proposed artwork as already integrated.
7. Inspect the finished artwork at actual display size, compare related focuses and spirits, and check background contrast, central motifs, stage readability, transparency, exact paths, file format, and sprite collisions. Validate in-game states when runtime execution is authorized and record untested states honestly. Keep gameplay logic, existing legacy artwork, and unrelated assets outside the image change unless the task explicitly includes them.

#### Decisions must use dedicated small artwork

When adding or replacing decision-row or decision-category header icons, create a separate small image for the decision UI. Follow the [decision icon size repair](docs/incidents/2026-09-22-korean-decision-icon-size.md) and [small-icon manifest](docs/data/HOK_KOREAN_SMALL_DECISION_ICON_MANIFEST.json).

- Do not point decision/category sprites directly at large focus or national-spirit textures, such as the 100×88 focus DDS. Do not assume the decision UI automatically scales them down. Keep the original focus and spirit images unchanged and export dedicated small DDS files.
- Use **32×32 for individual decision-row icons** and **51×40 for decision-category header icons** as the current project baseline. These sizes fit the inspected HOI4 1.19.3 UI; verify the target UI's row/header bounds, icon anchor, title position, and scaling before using different dimensions or adapting to a changed UI. Keep category description pictures and other UI artwork at their separately verified dimensions. Do not enlarge rows or replace the global decision GUI just to accommodate an oversized icon.
- Recompose the central motif for small-size readability. Preserve the linked content's branch/field colors, recognizable symbols, component aspect ratios, and alpha; simplify large wreaths and ribbons, and retain a visible metal border and transparent margins. Do not merely shrink a detailed focus icon until its subject becomes unreadable, or add I/II/III marks without actual upgrade stages.
- Store the finished assets under `gfx/interface/decisions/HOK_KOR/<module>/` and reference them through project-owned `GFX_HOK_KOR_decision_*` sprites with mod-root-relative paths. Preserve existing sprite names when replacing artwork; keep decision IDs, costs, rewards, durations, unlocks, and AI unchanged during image-only work.
- Record the source, reuse permission or generation method, composition changes, dimensions, sprite mapping, and final hash in the asset documentation. Check DDS format, alpha, exact paths, and actual-size previews against the header/row and nearby text. When runtime validation is authorized, check category, available/unavailable, and active decision displays after a full restart; distinguish static bounds checks from actual game-screen verification.

#### Focus and national-spirit background colors

Use the following background color families for focus and national-spirit artwork. Color represents the focus's political branch or policy field, not the country's current ruling ideology. Shared industry and military icons must not change color when the government changes.

| Political branch or policy field | Background and ornament direction |
|---|---|
| Democracy | Muted deep blue |
| Communism | Deep red rather than vivid primary red |
| Fascism | Brown with black ornaments, or charcoal with bronze ornaments |
| Non-aligned | Light gray and silver rather than pure white |
| Industry and production | Neutral gray with bronze or gold ornaments |
| Education and research | Light gray and silver |
| Army, ordnance, logistics, and staff | Dark green and olive |
| Navy | Navy blue and slate blue-gray |
| Air force | Silver and pale blue |

- Apply political-branch color first to content belonging to a political route. For example, democratic civic/rural education, medical aid, volunteer support, and economic or armaments agreements remain blue. Foreign agreement participant spirits retain the originating branch's color regardless of the recipient's ideology; do not add ideology conditions to implement artwork choices.
- For shared content, use its policy field. Schools, research, and maintenance belonging to a military service retain that service's color. Resolve overlaps from the actual branch, policy, and linked spirit, and record the assignment explicitly; do not infer color solely from an asset recipe's `family` or `category`. The regional Gyeongsang shipbuilding-industry focus uses industry colors.
- Keep linked focuses and national spirits in the same color family and preserve their shared central motif. Use the existing `I`, `II`, and `III` marks for genuine upgrade chains; preserve intentional badge omissions and do not invent stages for unrelated content.
- Edit the background as a separate layer. Preserve the central illustration, metal border, ornaments, stage marks, alpha, and recognizable symbols; do not apply a hue filter to the entire finished icon. Color must complement the central image and shape rather than serve as the only identifier.
- Keep dark backgrounds outlined so they remain visible against the game UI. Preserve shading, contrast, and metallic texture in light gray/silver backgrounds so they do not resemble disabled icons. Distinguish overlapping color families through motifs and frame shapes, including democracy versus navy and education versus air force.
- Record exact palette values, per-ID assignments, original sources, color-processing details, and output hashes in the asset documentation and manifest. Follow [the color plan and applied palette](docs/HOK_KOREAN_FOCUS_ICON_COLOR_PLAN.md) and [the icon manifest](docs/data/HOK_KOREAN_FOCUS_ICON_MANIFEST.json). Check actual-size previews; report in-game locked, available, active, completed, shine, and spirit-display validation separately from static inspection.
- The applied color-work scope is the new 60 focuses and 29 national-spirit definitions. Existing original communist, fascist, and non-aligned focuses and existing spirits remain outside that work. Their palette entries are standards for future explicitly scoped artwork, not authorization to recolor legacy content or change gameplay.

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
- Distinguish a new-save round trip from backward compatibility. To claim existing-save compatibility, load a representative pre-change save in the patched build, advance the game, save again, and reload it. Any one-time migration must be version-gated and idempotent.
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

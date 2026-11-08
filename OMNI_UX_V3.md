# OMNI UX v3 — Project Constellation

**Implemented:** November 8, 2026. **Source baseline:** `92650a83b6d743584ef266196275a2670ba75c04`. Primary goal: reduce interface complexity without dropping a single existing Atlas capability.

## What changed

- The existing inspector now carries three always-reachable tasks: **Explore, Discover, Review**. Its footprint remains fixed; the 3D map is still the main visual surface.
- The Explore entry begins with useful actions: see changes, review experiments, find a project or open the keyboard-accessible repository/connection text index. Original curated evidence route cards and the tour remain.
- Discover is the existing Atlas Pulse with separate browser-check, last-successful-scan and last-evidence-change truths. This release does not change source production or overwrite historical curated descriptions.
- Review is a compact, filtered opportunity queue that retains pinned sources, skeptical objections, experiment/acceptance criteria, cross-project comparison and private Investigate / Shelve / Reject actions. The same private `repo-dex-decisions/v1` code is inlined for genuine standalone offline use; Undo is limited to the latest session action.
- The map-to-Laboratory handoff uses a stable public opportunity ID (`?op=<hex>`). After a validated hosted feed loads, it selects and frames the corresponding mapped relationship. No private decision, user reason or token is inserted in a URL.
- On phones the map inspector expands only after an explicit task selection; an obvious **Map** action collapses it and restores canvas focus. Nav and history touch targets are at least 44 px high on tested phone widths.
- Original map evidence modes, camera, search, filters, source inspector, history, tour, low-effects/flat projection, offline snapshot, graph JSON export/import and Restore remain unchanged in mechanism and reachable from their original controls.

## Zero-loss capability mapping

| Protected IDs | New entry point | Test obligation |
|---|---|---|
| A01–A04, A09 | Explore map/inspector and camera controls | Pointer/keyboard orbit, zoom, select, selection history, frame/reset |
| A05–A07 | Original map modes and Tools filters, global search | Existing evidence modes, family/type filter, keyboard suggestions |
| A08, A10–A11 | Selection inspector, Tour, inventory controls | Source anchors, tour and full-inventory visibility |
| A12–A13 | Discover / Atlas Pulse | Validated public feed, matching separate scan receipt, safe offline failure |
| A14, A21 | Review + private Ledger | Investigate / Shelve / Reject, export/import, Undo, source-change reconsideration |
| A15–A16 | Embedded data, original JSON tools | Offline 201-node startup, export, validated import, Restore |
| A17–A19 | Help, task-specific status and mobile inspector | Keyboard help, error/empty states, mobile expansion and focus |
| A20 | Original graph identity adapter | Stable GitHub IDs and alias continuity on source renames |
| D01–D11 | Independent Repo_Dex and Laboratory site | All original source scanner, source feed, review and legacy browser functions remain available |

This mapping is an acceptance contract, **not an assertion that every physical device, assistive technology or hosted browser has been exercised**.

## Validation and remaining risk

- `python3 qa/verify_ui.py` checks legacy IDs, inline/offline asset structure, source boundaries and new routes.
- Main headless Chromium UX checks exercise the new task flow, source and decision controls, deep-link handling, keyboard textual index, mobile viewport and privacy boundary with a test-only intercepted public feed.
- Existing Atlas continuity checks re-exercise 201-node offline fallback, search, map navigation, source filters, back/forward, Help, JSON export/import and Restore.
- Direct hosted Pages navigation, screen-reader audits and physical touch hardware remain unverified in the sandbox. Hosted status should be manually checked after CI publication. No private decisions are synchronized across unrelated origins or devices.

**Rollback:** revert only the UX HTML and this documentation. Source scanner, public evidence feeds and other repositories are unaffected.

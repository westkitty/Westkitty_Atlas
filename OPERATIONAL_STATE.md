# Operational State — Westkitty_Atlas

Project ID: westkitty/Westkitty_Atlas
Baseline: main c1839cec4440ad4e218981b475fecd679c842591 (observed November 8, 2026)
Active candidate: COOL-20261108-ATLAS-05 / five bounded improvements

## Protected capabilities

- The packaged 201-repository original remains an offline standalone document.
- Existing Canvas 2D orbit, zoom, search, filters, evidence inspector, import/export and keyboard behavior remain.
- Default permanent chrome occupies less than 30% on previously tested target viewports.
- Feed is public-only and source-level declarations never imply verified integration.
- User decisions are private local browser state, never part of public feed/exported graph.

## Verification states

- Verified locally: no-network Chromium tests of previous real public feed, synthetic rename, status receipt, decision ledger, offline fallback and mobile layout.
- Implemented unverified: direct hosted GitHub Pages navigation and physical mobile hardware.

## Pending release gates

- Check current branch baseline before publishing.
- Verify Pages deploy and end-user browser receives new scan/status data.

## 2026-11-08 -- OMNI UX v3: Explore / Discover / Review

- Source baseline: Westkitty_Atlas main `92650a83b6d743584ef266196275a2670ba75c04`. Candidate modifications limited to `index.html`, `qa/verify_ui.py`, documentation and this ledger; no scanner or published feed schema changes.
- Protected user journey: 201-node offline embedded snapshot, Canvas orbit/zoom, evidence-level links, search/filter, camera and keyboard controls, Help, Tour, graph import/export/Restore and private decisions. The existing inspector now has three task entry points; a searchable accessible text index and 44 px phone task/history targets; a self-contained review queue with reversible decisions; and public-ID-only deep link handling.
- Verification: static QA passed 33 original controls, 58 unique IDs and offline guards; 29 focused Chromium checks; 28 legacy parity checks; adapted prior Phase2 real-feed fixture checks; no JS page errors. 320x568 phone collapsed UI chrome remains under 30 percent.
- Unknown: direct hosted live browser transport, physical touch and screen-reader testing are not verified. Private decisions do not automatically synchronize across devices. Expanded inspector may exceed 30 percent only after user action.
- Release gate: compare exact target branch and content blob before committing, verify Pages job success, preserve public-only and offline boundaries, do not misstate historical descriptions as fresh source truth.

## 2026-11-08 — Reviewer keyboard focus and History repair

- Reproduced in headless Chromium: after a private decision in both Atlas and Laboratory, the review list was recreated and keyboard focus fell back to `<body>`. In the Laboratory, History links to reviewed opportunities beyond the first eight results could not find the destination after filtering/pagination reset.
- Bounded repair: preserve focused control using stable public opportunity ID and action label across live review re-renders; fall back to the status filter if the candidate leaves the current filtered list. Focus the newly revealed entry after paginating review/capability/text indexes. Laboratory History now clears its conflicting filters, reveals the requested candidate and focuses it. Repo_Dex scans, content feed, data schemas, privacy ledger and original HTML graph geometry remain unchanged.
- Verified with 15 additional no-network Chromium browser checks (Lab + Atlas), plus existing Repo_Dex Python suite, legacy Atlas parity, new Atlas task-flow suite and JS syntax check. Physical screen reader and public GitHub Pages browser navigation remain unverified in this runtime.
- Release scope: Lab HTML + browser fixture + unit contract tests; Atlas HTML + static guard; documentation/state. Rollback: revert this bounded follow-up commit per repository. Never reset unrelated history.

## 2026-11-08 — Floating Project Workspace

- Approved change: make the Atlas workspace movable, minimizable, dismissible, and resummonable from a labeled top-bar Panel control, without altering Repo_Dex Laboratory.
- Source change: `index.html` published in commit `48e667c3f38dd196e9a6ac1d40a2449a764fe3d8`. The resulting file's Git blob `e1cd51b278d36016aa9d5936f3d06c5126c4999c` matches the GitHub readback.
- Behavior: pointer/touch header dragging, Alt+Arrow keyboard movement, viewport-clamped positioning, minimized title strip, full dismissal, top-bar restoration, responsive mobile window menu with Escape dismissal, and versioned per-breakpoint window preferences stored locally. Selecting a map node or opening Pulse restores a dismissed panel. No private decision data is changed.
- Verified locally: the original static HTML capability guard passed (33 original controls; 65 unique IDs). Node JavaScript syntax passed. Automated Chromium interactions passed at 1108x736, 768x800, 1280x800, 320x568 touch emulation, and 390x844 touch emulation, covering drag, minimize, dismiss, restoration, focus, menu, persistence model and existing task navigation with no page exceptions.
- Verified deployment: a live GitHub Pages HTTP 200 response read from Big Mac had SHA-256 `d4f8682218ba13140c5bd46502aa74bcf5859d75e6ace5418b7963809b9c783b`, exactly matching the locally tested HTML bytes. This establishes deployed source identity, not end-user interaction proof.
- Outstanding: physical mobile touch, screen-reader testing, and direct hosted-browser interaction remain unverified. The local `set_content` harness models localStorage because direct file/local navigation was blocked in the test environment.
- Rollback: revert the bounded Atlas `index.html` change only. Repo_Dex source, scanner, feed, and local decision schema are untouched.

## 2026-11-08 local / 2026-11-09 UTC — Celestial Cartography visual finishing release

- Source: `index.html` at `f868a83217a5269ab79686e2c37cfbda8e720e0c`; Git blob `30886c36f29ed48dab08dece645a461b7aa70e88`.
- User-directed outcome: premium visual finishing of the existing playable Canvas 2D repository atlas; not a new game, renderer framework, gameplay model, or fabricated character/level system.
- Art direction: cinematic astronomic cartography with layered offline starfield, nebula ambience, faint navigation graticule, illuminated crystalline reviewed nodes, restrained dim inventory marks, richer labeled family orbits, and documented-vs-proposed luminous routes.
- CSS/UI: coherent high-contrast dark-sapphire, frosted controls, cyan scientific signals, amber hypotheses, polished panel/toolbar/tabs, visible focus maintained.
- Motion/performance: existing single rAF clock reused and capped near 18 drawn frames/s while idle; no second animation loop. Reduced motion, low-quality mode, hidden pages, and large imported graphs suppress nonessential motion. Static background is prerendered on resize; no external assets or new dependencies.
- Protected verified invariants: 201 original packaged repositories, 45 original links, original inline JSON and local-only RepoDex decision ledger unchanged byte-for-byte. Search, tabs, evidence, views, map interaction, guided tour, tools, import/export/restore, floating workspace preserved.
- Locally verified (Chromium with a modeled storage shim): 33 protected controls / 65 unique element IDs; five viewport interaction journeys; three view modes; orbit, flat, selection, family/relation filters, quality controls, search, review and discover routes; touch-emulated mobile; text index, tour, JSON export, maximum allowed 600-node/3,000-edge synthetic import, and built-in restore. No browser page exceptions observed.
- Render-time observation: headless Chromium rAF wrapper p95 ~1.4–1.6 ms in normal motion during the bounded sample, not an end-user compositor FPS guarantee. Reduced-motion runtime did not persist an idle render loop.
- Deployment verified from Big Mac: GitHub Pages HTTP 200 and live response SHA-256 `e1b9e6abd11013d2fc542b1d236235f331114456f5f60aa6b2908d25f76b6627` exactly matching the packaged source.
- Remaining unverified: physical-device touch, full assistive-tech screen-reader journeys, live interactive browser replay against GitHub Pages. The local tests and exact live file hash do not prove those experiences. Performance evidence is a bounded headless sample, not a field-device benchmark.
- Rollback: revert only the visual `index.html` release commit; Repo_Dex feed and decision schema were not modified.

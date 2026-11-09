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

## 2026-11-08 local / 2026-11-09 UTC — Observatory Survey visual and navigation polish

- User objective: another substantial visual finishing pass on Project Constellation, preserving the existing interactive repository atlas rather than converting it into an unrelated game.
- Baseline: visually finished HTML from `f868a83217a5269ab79686e2c37cfbda8e720e0c`, HTML blob `30886c36f29ed48dab08dece645a461b7aa70e88`.
- Implementation: `index.html` commit `30959a3255a30cf756fa84a5530b8dccd836624c`, blob `d345c219e6ad8f65d3410e9aa72906a6872b582b`, SHA-256 `aec0caa1b0bc59777e12bf9aac9b667a0d46863eccaec713fe2b4ddd7bde9ba0`. Small scope; no external asset or renderer package.
- New visual grammar: an observatory survey chart with a cached stellar river, calibrated azimuth rings and frame ticks, stronger warm-ink interface contrast, family-specific node silhouettes and center glyphs, hover-connected route emphasis, and selection/hover reticles rendered by the existing Canvas clock.
- Protected invariants: all 201 public packaged repositories and 45 mapped relationships, unchanged inline data SHA-256 `9fab02102e0b2ce0ab39e890e9ba5f6c031944af9bf00d287bd8774263881e9d`; unchanged inline RepoDex private-decision helper; preserved search, filters, evidence inspector, tour, text index, graph import/export/restore and movable workspace.
- QA added to repository: `qa/verify_visual_invariants.py` commit `ab57af331bcb11b34efb3c9e9a077e4f1636b7af`. The static original UI guard passed 33 protected controls and 65 unique IDs; workspace interactions passed five viewports; text index, tour, export and full synthetic 600-node/3,000-edge import/restore passed; visual tests passed five viewport modes plus search, filters, orbit/flat, quality and reduced motion. No unexpected page exceptions in those paths.
- Short headless Chromium measurement at 1440x900: previous p95 rAF callback 6.2 ms versus new 4.9 ms; 390x844 in reduced-motion mode retained only two initialization draws. This does not establish physical-device FPS, accessibility compliance or a production performance guarantee.
- Deployment: GitHub default-branch content and hash verified. Live Pages byte readback unavailable because DEX//REACH connector failed and sandbox network DNS was unavailable. Do not upgrade to live-browser proof absent a successful direct test.
- Remaining: physical touch, screen-reader, deployed-page user-journey verification; user feedback on visual direction.
- Rollback: revert the single `index.html` visual-change commit; retain independent QA guard and operational-state history unless invalidated. Repo_Dex itself was not changed.

## 2026-11-08 local / 2026-11-09 UTC — Quiet Sky — reduced clutter and smooth motion

- User-reported defect: previous Observatory Survey release was too dense, the animations looked significantly choppier, and the atmosphere did not read as a proper starfield.
- Baseline source: `index.html` blob `d345c219e6ad8f65d3410e9aa72906a6872b582b`. Root cause confirmed in source and Chromium: `state.lastFrame<55` throttled most ambient redraws to about 15 FPS (66.6 ms median interval at 1108x736, selected state).
- Bounded repair: `index.html` commit `d2f9b3e2605de93730b30b174630ce844cdbb1b6`, blob `3f4ac435c3621587554702545831bf6c658a0413`. Replaced graticule/sector orbits and busy linework with a deterministic cached three-depth starfield and soft galaxy haze. Reduced default route opacity, focused selection/hover connections, reduced label density and unnecessary glows, narrowed hover target to prevent inadvertent emphasis. Retained existing Canvas renderer and one RAF owner; removed 55 ms presentational throttle and stopped idle redraws.
- Protected: original 201 packaged repositories, 45 original relationships and inline graph SHA-256 `9fab02102e0b2ce0ab39e890e9ba5f6c031944af9bf00d287bd8774263881e9d`, evidence/proposal distinction, local decision state, search, Explore/Discover/Review, filters, history, guided tour, mobile, import/export/restore, floating workspace; no external assets or dependencies.
- Validation: all 33 original UI controls and 65 IDs static guard PASS; five viewport workspace/keyboard/drag/persistence journeys PASS; text index, tour, export, synthetic 600-node/3,000-edge import and restore PASS; three browser preview states and reduced-motion behavior PASS without page exceptions.
- Matched headless Chromium drawing measurement at 1108x736: selected previous ~15 FPS (66.6 ms median draw interval), selected Quiet Sky ~58 FPS (16.5 ms median), idle Quiet Sky no sustained redraws, reduced-motion no sustained ambient redraws. This is bounded automation, not a physical-device FPS claim.
- Deployment: live GitHub Pages HTTP 200 from Big Mac, complete HTML SHA-256 `0a4378aee8248c54b00feaafb06ad78540868b5278ec9ec49baaf067531c8038` matching local tested source exactly.
- Regression added: `qa/verify_quiet_sky.py` commit `98399b62d6732466beeb2d9711c27d52755e16ad`, locally executed PASS.
- Remains unverified: real-device browser experience, Brave-specific environment, physical touch, full screen-reader journey, extended-duration thermal performance.
- Rollback: revert only the above `index.html` commit; do not revert graph data, private decisions, unrelated repository changes or QA history.

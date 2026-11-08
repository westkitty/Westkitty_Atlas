# Project Constellation

An offline, interactive relationship atlas for the **public** repositories of [westkitty](https://github.com/westkitty). It renders perspective-projected 3D nodes and evidence-linked connections on Canvas 2D; no WebGL, build step, account, or remote service is required to view the packaged site.

## Launch

- Online: https://westkitty.github.io/Westkitty_Atlas/ (after GitHub Pages deployment is enabled)
- Offline: download `index.html` and open it in a modern browser. All portfolio data and presentation code are embedded in that file.

Rotate by dragging, zoom using the wheel or pinch, select a node or line for the evidence inspector, and use Search / Filters to narrow the graph. The interface includes data export/import, keyboard controls, reduced motion, and a lower-detail view for constrained devices.

## Evidence and coverage

- Snapshot: **2026-11-08**
- **201 public repositories** inventoried; **37** README-reviewed projects
- **45 curated relationships**: **25 documented** against repository files and **20 explicitly hypothetical** opportunities
- Solid lines are documented; dashed lines are proposals. Shared package declarations do not establish shared code, and similar-purpose projects do not establish dependencies.
- No private-repository metadata or files are intentionally included.
- Files: [Source dataset](Project_Constellation_Source_Data.json) · [Chromium browser-test report](Project_Constellation_Browser_Test_Report.json).

The preserved [source JSON](Project_Constellation_Source_Data.json) is the original curated evidence snapshot. On GitHub Pages the atlas now reads the **public-only, versioned Repo_Dex feed** from `https://westkitty.github.io/Repo_Dex/feed/latest.json` when opened, validates repository identities and pinned evidence, and combines newly inspected relationships and clearly unverified experiments with the original graph. The live scan is authored by the independent [Repo_Dex scanner](https://github.com/westkitty/Repo_Dex); it runs on Repo_Dex's GitHub Actions schedule. A scan does not edit the repositories it observes. The local downloaded HTML remains fully functional with its packaged evidence; the online check is skipped offline.

## Deployment

The root `index.html` is deployed by `.github/workflows/pages.yml` on pushes to `main`. GitHub Pages hosts it at https://westkitty.github.io/Westkitty_Atlas/. An online check uses the same GitHub Pages origin and no private token. The packaged offline HTML still works without GitHub, with a retained source snapshot.

## Scope and limitations

This is a source-backed **visual exploration tool**, not a dependency scanner or comprehensive audit. Repository snapshots, links, quality marks, and hypotheses must not be promoted to stronger claims without additional evidence. Browser QA used headless Chromium, not a physical Android device. No third-party runtime libraries or assets are loaded by the HTML file.

## Atlas Pulse integration (2026-11-08)

- The hidden **Observatory controls → Atlas Pulse** section provides a manual feed refresh and an inspector view for observations and proposed experiments.
- Online load checks the Repo_Dex feed automatically when hosted on `westkitty.github.io`. Non-GitHub/offline files never attempt this request.
- Feed validation blocks incomplete inventories, private or foreign repositories and unpinned or off-domain source citations; a rejected feed leaves the packaged graph intact.
- Imported custom graphs stay untouched. Restoring the built-in graph applies the latest accepted public feed if one was received.
- Observations are changes relative to the Repo_Dex snapshot history; the first scan is a **baseline**, not a claim that every project was newly created.
- The public feed is an evidence snapshot, not a verified source-level audit of every repository. Proposed links require manual experiments.

Browser smoke checks were run in isolated headless Chromium using the real Repo_Dex artifact as a mocked fetch response; the environment blocked direct navigation to the public hosted origin. The 17 checks are documented in `ATLAS_LIVE_QA.md`.

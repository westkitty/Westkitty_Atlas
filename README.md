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

The source JSON is an evidence snapshot, **not** an automatically updated inventory. Live GitHub files may change after the snapshot date. The original public repositories were read only.

## Deployment

The root `index.html` is the publishable site. The optional GitHub Pages workflow in `.github/workflows/pages.yml` deploys the root on pushes to `main`, once the repository's **Settings → Pages → Build and deployment → Source** is set to **GitHub Actions**. If workflow publishing is unavailable, select **Deploy from a branch → main → /(root)** instead. The offline HTML works independently of Pages.

## Scope and limitations

This is a source-backed **visual exploration tool**, not a dependency scanner or comprehensive audit. Repository snapshots, links, quality marks, and hypotheses must not be promoted to stronger claims without additional evidence. Browser QA used headless Chromium, not a physical Android device. No third-party runtime libraries or assets are loaded by the HTML file.

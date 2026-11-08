# Living Atlas / Repo_Dex Phase 2

The Atlas remains a standalone, dependency-free, offline-capable HTML document. Hosted copies optionally read the public `../Repo_Dex/feed/latest.json` and **independent** `../Repo_Dex/feed/status.json` from the same GitHub Pages origin.

- Stable numeric GitHub identity protects curated nodes and their original relationship IDs across repository renames; never infer a deletion from a rename.
- Original curated README summaries stay historical. Current public descriptions and pinned capability declarations are displayed separately.
- The two-clock report shows the most recent successful scan only when the status receipt matches the loaded feed digest; otherwise it says the receipt is unavailable.
- Repo_Dex's deterministic skeptical review is a **proposed test**, never a completed integration.
- Hypothesis decisions are private, local to the browser/profile and shared with `Repo_Dex/laboratory.html` through a common same-origin storage key. Portable JSON export/import is manual and should never be committed to public GitHub.
- A shelved or rejected finding stays hidden in the default Pulse view unless its pinned source evidence changes, in which case it becomes a needs-review lead. Evidence changes do not override the user decision.
- Existing 201-node offline snapshot, graph rotation, keyboard navigation, quality fallback, import/export, mobile UI and evidence citations are preserved.

## Validation limits

The local automated suite runs the real HTML in headless Chromium and intercepts a prior real Repo_Dex public snapshot with synthetic valid status receipts. Browser environment blocks direct GitHub Pages navigation. A successful deployment and one later scheduled scan remain separate verification obligations. No physical iPhone/Android check or actual cross-device decision synchronization is claimed.

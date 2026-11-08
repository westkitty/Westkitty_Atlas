# Atlas Pulse integration QA — 2026-11-08

- **Local runtime:** Headless Chromium, 17/17 focused checks passed with an intercepted Repo_Dex scan response.
- **Source feed:** Repo_Dex GitHub Actions run 42514075499; 202 public repositories, 36 source-inspected, 52 source-backed relations, 30 hypotheses; initial baseline, no source errors.
- **Validated:** live inventory updates (201 → 202), original and new edges together, same-origin URL, source-date label, linked project, live status and hypothesis inspector, manual refresh, custom-import preservation, Restore replay, rejecting a private record without replacing packaged data, offline file baseline and mobile inspector availability, no JavaScript page exceptions in the mocked run.
- **Original capabilities protected:** offline source embedded in index.html, Canvas orbit, selection, search, filters, import/export, accessible controls and mobile layout.
- **Scope limit:** The browser sandbox blocks direct network navigation to the live GitHub Pages URL. The startup guard was enabled *in the test copy only* while fetch was mocked with the real GitHub Actions artifact. No physical mobile-device test or exact live-site browser run was performed.
- **Rollout check:** After deploy, confirm the live URL and the Repo_Dex feed are accessible from a normal browser. If the feed is unavailable, the atlas deliberately falls back to its packaged snapshot.

Related source: https://github.com/westkitty/Repo_Dex

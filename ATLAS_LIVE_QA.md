# Atlas Pulse integration QA — 2026-11-08

- **Local runtime:** Headless Chromium, 18/18 focused checks passed with an intercepted Repo_Dex scan response.
- **Source feed:** Repo_Dex GitHub Actions run 42514075499; 202 public repositories, 36 source-inspected, 52 source-backed relations, 30 hypotheses; initial baseline, no source errors.
- **Validated:** live inventory updates (201 → 202), original and new edges together, same-origin URL, source-date label, linked project, live status and hypothesis inspector, manual refresh, custom-import preservation, Restore replay, rejecting a private record without replacing packaged data, offline file baseline and mobile inspector availability, no JavaScript page exceptions in the mocked run, and every generated opportunity opens its corresponding evidence panel.
- **Original capabilities protected:** offline source embedded in index.html, Canvas orbit, selection, search, filters, import/export, accessible controls and mobile layout.
- **Scope limit:** The browser sandbox blocks direct network navigation to the live GitHub Pages URL. The startup guard was enabled *in the test copy only* while fetch was mocked with the real GitHub Actions artifact. No physical mobile-device test or exact live-site browser run was performed.
- **Rollout check:** After deploy, confirm the live URL and the Repo_Dex feed are accessible from a normal browser. If the feed is unavailable, the atlas deliberately falls back to its packaged snapshot.

Related source: https://github.com/westkitty/Repo_Dex

## Pulse visibility correction (2026-11-08)

**Issue reproduced in source:** The live graph was merged but the initial inspector displayed an old curated welcome, previous README summaries stayed primary without freshness labels, the old refresh button did not explain it only fetched a published snapshot, and new findings were buried in Tools. The desktop dock was hidden on narrower screens.

**Fix:** A visible live-applied indicator in the inspector subtitle at all viewport sizes and in the wide-screen dock; immediate report showing the source scan date, 202 vs packaged 201 name comparison, 36/202 source inspection coverage, scanner-backed relationships and experimental hypotheses; explicitly baseline-only change language; separate current GitHub metadata for each project; accurate Reload button label; unchanged-digest fast path; error and import recovery; mobile expandable Pulse report.

**Validation:** 41/41 focused headless Chromium checks passed against the 202-repository Repo_Dex GitHub Actions scan captured on 2026-11-08, with the network response intercepted in a test copy because hosted Pages navigation is blocked in this sandbox. No browser page errors. JavaScript syntax checked with Node. Manual screenshot checks at desktop and phone viewport sizes. Default permanent interface footprint: 27.41% at 320x568, 24.58% at 390x844, 19.69% at 800x1100, and 24.89% at 1400x900. Interactive expansion is temporary and user-invoked.

**Protected:** 201-node offline fallback, orbit/zoom/search/filters, custom import/export, evidence links, 30 source-grounded feed proposals and the no-private-data boundary. **Not verified:** physical mobile browser, direct HTTP/navigation of the publicly hosted Pages site and a later scheduled scan's real delta.

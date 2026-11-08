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

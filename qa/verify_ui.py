"""Dependency-free shape and zero-loss guard for the offline Atlas HTML."""
from html.parser import HTMLParser
from pathlib import Path
import re

class Inventory(HTMLParser):
    def __init__(self):
        super().__init__(); self.ids=[]; self.scripts=[]; self.links=[]
    def handle_starttag(self,tag,attrs):
        d=dict(attrs)
        if 'id' in d: self.ids.append(d['id'])
        if tag=='script': self.scripts.append(d)
        if tag=='link' and d.get('rel')=='stylesheet': self.links.append(d)

html=Path(__file__).resolve().parents[1].joinpath('index.html').read_text(encoding='utf-8')
p=Inventory();p.feed(html)
assert html.lower().startswith('<!doctype html>')
assert len(p.ids)==len(set(p.ids)), 'duplicate DOM IDs'
legacy='scene search search-results topbar panel panelTitle panelSub detail toolBtn toolPopover categoryFilter relationFilter qualitySelect mobileView tourBtn tourMenuBtn backBtn forwardBtn expandPanel collapsePanel pulseOpen flatBtn inventoryBtn resetBtn frameBtn exportBtn importBtn importFile restoreBtn helpDialog helpBtn closeHelp helpDone'.split()
for id_ in legacy:assert id_ in p.ids, f'legacy control missing: {id_}'
for id_ in 'taskNav taskExplore taskDiscover taskReview textIndexBtn mapReturnBtn'.split():assert id_ in p.ids, f'new task control missing: {id_}'
assert all(not d.get('src') for d in p.scripts), 'offline HTML must have inline scripts only'
assert not p.links, 'offline HTML cannot require an external stylesheet'
assert "connect-src 'self'" in html, 'hosted feed must stay origin-restricted'
for token in ('const LIVE_FEED','function graphFromLive','function validateLiveFeed','function showReviewWorkspace','function showAccessibleIndex','function showWelcome','function showSelection','function showLivePulse','function exportJSON','function importJSON','function restore','function tryOpenLinkedOpportunity'):
    assert token in html, f'expected browser capability missing: {token}'
assert 'window.RepoDexDecisions' in html
assert 'documented' in html and 'hypothetical' in html
assert 'prefers-reduced-motion' in html
assert re.search(r'<script[^>]*id="constellation-data"',html)
print(f'PASS: {len(legacy)} protected controls, {len(p.ids)} unique element IDs, task navigation, public-only feed, offline assets')

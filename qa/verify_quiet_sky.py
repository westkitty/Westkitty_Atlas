"""Prevent regression of the calming starfield and responsive map animation."""
from pathlib import Path
import hashlib
import json
import re

html = Path(__file__).resolve().parents[1].joinpath('index.html').read_text(encoding='utf-8')
match = re.search(r'<script type="application/json" id="constellation-data">(.*?)</script>', html, re.S)
assert match, 'Embedded offline graph missing'
graph = json.loads(match.group(1))
assert (len(graph['nodes']), len(graph['edges'])) == (201, 45), 'Original graph inventory changed'
assert hashlib.sha256(match.group(1).encode()).hexdigest() == '9fab02102e0b2ce0ab39e890e9ba5f6c031944af9bf00d287bd8774263881e9d', 'Original graph data modified'
assert 'state.lastFrame<55' not in html, '18 FPS presentation throttle reintroduced'
assert 'function buildBackdrop()' in html and 'state.starCache=b;' in html, 'Cached background missing'
assert 'const dustCount=low?450' in html and 'const sky=g.createRadialGradient' in html, 'Layered starfield missing'
assert 'function drawEdge(e,t,selected,hovered)' in html and "const base=state.view==='all'" in html, 'Connection de-emphasis missing'
assert 'function pick(x,y,forHover=false)' in html, 'Precise hover affordance missing'
assert 'function ambientMotion(t)' in html and 'state.transition||ambientMotion(t)' in html, 'Single animation loop contract missing'
assert 'const WORKSPACE_KEY=' in html and 'function workspaceRestore(' in html, 'Floating workspace lost'
assert 'function importJSON(' in html and 'function exportJSON(' in html and 'function restore(' in html, 'Graph import/export/restore lost'
assert 'window.RepoDexDecisions' in html, 'Private decision ledger lost'
assert not re.search(r'<script[^>]+src=', html), 'External script added to offline artifact'
assert not re.search(r'<link[^>]+rel="stylesheet"', html), 'External stylesheet added'
print('PASS: cached starfield, no 18fps cap, focused routes, original data, offline and workspace invariants')

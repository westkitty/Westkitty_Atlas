"""Static quality regression checks for the self-contained Project Constellation map."""
import hashlib
import json
import re
from pathlib import Path

html = Path(__file__).resolve().parents[1].joinpath('index.html').read_text(encoding='utf-8')
assert html.startswith('<!doctype html>'), 'HTML document missing'
raw = re.search(r'<script type="application/json" id="constellation-data">(.*?)</script>', html, re.S)
assert raw, 'Packaged graph absent'
data = json.loads(raw.group(1))
assert hashlib.sha256(raw.group(1).encode()).hexdigest() == '9fab02102e0b2ce0ab39e890e9ba5f6c031944af9bf00d287bd8774263881e9d', 'Packaged source data unexpectedly changed'
assert (len(data['nodes']), len(data['edges'])) == (201, 45)
assert all(node.get('id') and node.get('url', '').startswith('https://github.com/westkitty/') for node in data['nodes'])
for name in ('function buildBackdrop()', 'function glyphOutline(', 'function sectorGlyph(', 'function drawSurveyFocus(', 'function render(', 'function requestDraw(', 'function pick('):
    assert name in html, f'Missing renderer behavior: {name}'
assert 'drawSurveyFocus(t);drawLabels();' in html, 'Focus reticle not wired into frame'
assert "hovered?.kind==='node'" in html, 'Hover-linked routes not highlighted'
assert 'function ambientMotion(' in html and 'function motionOff(' in html
assert 'prefers-reduced-motion' in html and 'function qualityLow()' in html
assert 'const WORKSPACE_KEY' in html and 'function workspaceRestore(' in html
assert 'window.RepoDexDecisions' in html
assert 'function importJSON(' in html and 'function exportJSON(' in html and 'function restore(' in html
assert "Object.defineProperty(window,'__CONSTELLATION_TEST__'" in html, 'Test hook missing'
assert not re.search(r'<script[^>]+src=', html), 'External JS dependency introduced'
assert not re.search(r'<link[^>]+rel="stylesheet"', html), 'External CSS dependency introduced'
print('PASS: 201/45 original inventory, provenance links, renderer, visual focus, input, motion, offline and private ledger guards')

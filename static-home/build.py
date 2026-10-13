"""Build the static entry page that redirects visitors to the real Django site.

The Django homepage remains authoritative, so it retains its exact design,
database-backed sections, authentication, forms, and routes. Visiting this
static page immediately navigates to the public Django Web Service, which
triggers Render's normal wake-up behavior if the free service is asleep.
"""
import os
from pathlib import Path
from html import escape
from urllib.parse import urlparse

HERE = Path(__file__).resolve().parent
template_path = HERE / "index.template.html"
output_path = HERE / "dist" / "index.html"

backend_url = os.environ.get(
    "BACKEND_BASE_URL", "https://update-it-o0xz.onrender.com"
).strip().rstrip("/")
parsed = urlparse(backend_url)
if parsed.scheme not in ("https", "http") or not parsed.netloc:
    raise SystemExit("BACKEND_BASE_URL must be a full http:// or https:// URL")

html = template_path.read_text(encoding="utf-8")
html = html.replace("__BACKEND_BASE_URL__", escape(backend_url, quote=True))
output_path.parent.mkdir(parents=True, exist_ok=True)
output_path.write_text(html, encoding="utf-8")
print(f"Built static redirect to {backend_url}/")

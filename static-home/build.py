"""Build the Render static landing page from environment-configured public URLs.

Render Static Sites expose environment variables at build time, not in browser
JavaScript. This script safely injects those values into the generated HTML.
"""
import os
from pathlib import Path
from html import escape

HERE = Path(__file__).resolve().parent
template_path = HERE / "index.template.html"
output_dir = HERE / "dist"
output_path = output_dir / "index.html"

values = {
    "__ACADEMY_LOGO_URL__": os.environ.get("ACADEMY_LOGO_URL", "").strip(),
    "__HOME_BANNER_1_IMAGE_URL__": os.environ.get("HOME_BANNER_1_IMAGE_URL", "").strip(),
    "__HOME_BANNER_2_IMAGE_URL__": os.environ.get("HOME_BANNER_2_IMAGE_URL", "").strip(),
    "__HOME_BANNER_3_IMAGE_URL__": os.environ.get("HOME_BANNER_3_IMAGE_URL", "").strip(),
    "__BACKEND_BASE_URL__": os.environ.get(
        "BACKEND_BASE_URL", "https://update-it-o0xz.onrender.com"
    ).strip().rstrip("/"),
}

html = template_path.read_text(encoding="utf-8")
for token, value in values.items():
    html = html.replace(token, escape(value, quote=True))

output_dir.mkdir(parents=True, exist_ok=True)
output_path.write_text(html, encoding="utf-8")
print(f"Built {output_path}")
for key, value in values.items():
    print(f"{key[2:-2]}: {'configured' if value else 'not configured'}")

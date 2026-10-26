# Update Academic Care static entry page

This static site intentionally redirects visitors to the existing Django Web
Service instead of recreating the homepage. That is the reliable way to show
the exact real Update Academic Care design and preserve live database content, login,
forms, notices, results, and the rest of the existing routes.

## Render Static Site settings

- Repository: `rafsanhasanpronoy/Update-IT`
- Root Directory: leave blank
- Build Command: `python static-home/build.py`
- Publish Directory: `static-home/dist`

## Environment variable for the Static Site

Add this in the Static Site's own Environment settings:

- `BACKEND_BASE_URL`: the public URL of your existing Django Web Service,
  for example `https://update-it-o0xz.onrender.com`

The visitor lands on the static URL first; the redirect then requests the
Django homepage. That request wakes a sleeping free Web Service according to
Render's normal behavior. A cold start may take around a minute, and the
static site cannot make Django start instantly or guarantee that every request
succeeds on the first try.

Keep the existing Django Web Service and its templates unchanged. Do not rename
`core/templates/core/home.html` to `index.html`; Django must continue to
render that template.

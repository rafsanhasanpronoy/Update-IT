# Update IT static landing page

This folder is a separate static landing page. It does not replace the Django
homepage or run Django views.

## Render Static Site settings

- Repository: `rafsanhasanpronoy/Update-IT`
- Root Directory: leave blank
- Build Command: `python static-home/build.py`
- Publish Directory: `static-home/dist`

## Environment variables for the Static Site

Add these in the Render Static Site's own Environment settings. Static Site
environment variables are available to the build process; they are not exposed
to browser JavaScript automatically.

- `ACADEMY_LOGO_URL`: public URL of the Update IT logo in Supabase Storage
- `HOME_BANNER_1_IMAGE_URL`: public URL of banner 1
- `HOME_BANNER_2_IMAGE_URL`: public URL of banner 2
- `HOME_BANNER_3_IMAGE_URL`: public URL of banner 3
- `BACKEND_BASE_URL`: existing Django Web Service URL (default in build script:
  `https://update-it-o0xz.onrender.com`)

Use the same public image URLs as the Django service, but add the variables
separately to the Static Site. Changing environment variables triggers a
static-site rebuild/deploy.

The public landing page links admission, about, and notices to Django. Dynamic
database content, login, forms, results, and admin remain on Django.

# Kemuel Swing Academy

A Chino Hills-first youth baseball training ecosystem. **Train the Swing. Track the Growth. Find the Right Coach.**

Static, SEO-focused multi-page website: a 30-day swing challenge, progress dashboard, player growth projection, coach marketplace, batting-cage directory, AA/AAA tryout hub, and training-kit checkout.

## Structure

```
site/
├── *.html              # Generated, deployable pages (open index.html)
├── assets/
│   ├── css/kemuel.css  # Design system (single source of truth)
│   ├── js/kemuel.js    # Nav, accordions, FAQ, toggles
│   └── img/            # Logos + stat screenshots
├── src/                # Per-page body fragments (edit these)
├── build.py            # Wraps fragments in shared nav/footer → *.html
├── sitemap.xml
└── robots.txt
```

## Editing & building

The navbar and SEO footer live once in `build.py`. Page content lives in `src/<page>.html`. After editing, regenerate the deployable pages:

```bash
python3 build.py
```

`foundation.html` is an internal design-system reference (excluded from sitemap/robots).

## Design system

Midnight Navy `#071E3D` · Power Red `#D62828` · Clay Orange `#E76524` · Trophy Gold `#C99700` · Off White `#FAF7F0` · Ink Black `#111827` · Steel Gray `#64748B`. Type: Anton / Barlow Condensed / Inter.

## Disclaimers

Kemuel Swing Academy does not guarantee home runs, scholarships, roster spots, tryout selection, or injury prevention. Public coach/cage/club listings are based on publicly available information and are not endorsements unless claimed and verified. Youth training should be parent- or coach-supervised. Sleep and nutrition guidance is educational, not medical advice.

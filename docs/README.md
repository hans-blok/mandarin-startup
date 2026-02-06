# MkDocs Publicatie - Mandarin Startup

Dit document beschrijft hoe je de MkDocs documentatie kunt bouwen en bekijken.

## Vereisten

- Python 3.9 of hoger
- pip (Python package manager)

## Installatie

Installeer MkDocs en het Material theme:

```bash
pip install mkdocs
pip install mkdocs-material
```

Of gebruik requirements.txt als die beschikbaar is:

```bash
pip install -r requirements.txt
```

## Lokaal ontwikkelen

Start de development server om de documentatie live te bekijken:

```bash
mkdocs serve
```

De documentatie is dan beschikbaar op: http://127.0.0.1:8000/

Wijzigingen in Markdown-bestanden worden automatisch herladen.

## Bouwen

Bouw de statische website:

```bash
mkdocs build
```

Dit genereert de site in de `site/` folder.

## Publiceren

### GitHub Pages

Als je GitHub Pages gebruikt:

```bash
mkdocs gh-deploy
```

Dit bouwt en publiceert automatisch naar de `gh-pages` branch.

## Documentatie Structuur

```
mandarin-startup/
├── mkdocs.yml                    # MkDocs configuratie
├── docs/                         # Documentatie bron
│   ├── index.md                 # Homepage
│   ├── fundamentele-hypothese.md
│   ├── strategische-intenties.md
│   └── styles/
│       └── mandarin.css         # Custom Mandarin stylesheet
└── site/                        # Gegenereerde site (na build)
```

## Stylesheet

De site gebruikt de custom **Mandarin stylesheet** met:
- Mandarin-oranje topbalk (#e55039)
- Segoe UI lettertype
- WCAG 2.1 AA toegankelijkheid
- Responsive design

Zie `templates/docs/mandarin-stylesheet-guide.md` voor meer informatie over de stylesheet.

## Content Toevoegen

1. Maak nieuwe Markdown-bestanden aan in `docs/`
2. Voeg ze toe aan de navigatie in `mkdocs.yml`:

```yaml
nav:
  - Home: index.md
  - Strategie:
      - Fundamentele Hypothese: fundamentele-hypothese.md
      - Strategische Intenties: strategische-intenties.md
      - Nieuw Document: nieuw-document.md  # <- voeg hier toe
```

3. Test met `mkdocs serve`

## Troubleshooting

### MkDocs niet gevonden

```bash
pip install --upgrade mkdocs mkdocs-material
```

### Stylesheet wordt niet toegepast

Controleer of `docs/styles/mandarin.css` bestaat en dat het pad in `mkdocs.yml` klopt:

```yaml
extra_css:
  - styles/mandarin.css
```

### Build errors

Controleer de console output voor specifieke fouten. Vaak helpt:

```bash
mkdocs build --clean
```

## Verantwoordelijkheid

- **MkDocs configuratie**: Publicatie Steward
- **Stylesheet**: Presentatie Architect
- **Content**: Diverse agents (Hypothese Vormer, Strategisch Analist, etc.)

---

**Laatst bijgewerkt**: 2026-02-06  
**Versie**: 1.0

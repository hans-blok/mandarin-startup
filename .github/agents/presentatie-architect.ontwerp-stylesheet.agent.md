# Agent Contract - presentatie-architect.ontwerp-stylesheet

**Agent**: presentatie-architect
**Intent**: ontwerp-stylesheet
**Omschrijving**: Genereert CSS/SCSS stylesheets met branding en layout

## Input

- **Branding-richtlijnen**:
  - Primary color: `#e55039` (Mandarin-oranje)
  - Single font family: Segoe UI (met system fallbacks)
  - Topbalk hoogte: 64px
  - Design filosofie: Clean, minimalistisch, toegankelijk

- **Toegankelijkheidseisen**:
  - WCAG 2.1 AA compliant
  - Kleurcontrast minimaal 4.5:1
  - Keyboard navigation support
  - Screen reader friendly

- **Responsive vereisten**:
  - Mobile-first approach
  - Breakpoints: 768px (tablet), 1024px (desktop), 1440px (large desktop)

## Output

### Bestanden gegenereerd

1. **`templates/css/mandarin.css`** - Hoofdstylesheet
   - Design tokens (CSS custom properties)
   - Base styles (typography, colors, spacing)
   - Mandarin topbalk (#e55039)
   - Component styling (buttons, tables, code blocks)
   - Responsive breakpoints (mobile-first)
   - Print stylesheet
   - Accessibility enhancements

2. **`templates/docs/mandarin-stylesheet-guide.md`** - Documentatie
   - Overzicht en kernkenmerken
   - Design tokens referentie
   - MkDocs integratie instructies
   - Component documentatie met voorbeelden
   - Best practices
   - Troubleshooting

### Kenmerken

- **Single font family**: Segoe UI, system-ui fallbacks
- **Primary color**: `#e55039` voor topbalk en branding
- **WCAG 2.1 AA**: Alle kleurcontrasten gevalideerd
- **Responsive**: Mobile-first met 4 breakpoints
- **Print-ready**: Dedicated print styles
- **Toegankelijk**: Focus states, skip-to-content, reduced motion support

## Validatie

✅ CSS-syntax correct (W3C compliant)  
✅ WCAG 2.1 AA kleurcontrast (4.5:1 voor normale tekst)  
✅ Responsive breakpoints werkend (mobile-first)  
✅ Print-stylesheet aanwezig  
✅ Single font family geïmplementeerd  
✅ Mandarin-oranje topbalk (#e55039)

## Foutafhandeling

- **Fallback fonts**: Segoe UI → system-ui → sans-serif
- **Browser compatibility**: CSS custom properties met fallback values
- **Missing resources**: Graceful degradation bij ontbrekende fonts

## Gebruik in MkDocs

```yaml
# mkdocs.yml
extra_css:
  - css/mandarin.css
```

Plaats stylesheet in: `docs/css/mandarin.css`

## Herkomstverantwoording

- Gegenereerd door: agent-smeder → presentatie-architect
- Bron: agent-boundaries/presentatie-architect.boundary.md
- Branding-input: Mandarin huisstijl (oranje #e55039, single font)
- Datum: 2026-02-06
- Versie: 1.0
- Laatst uitgevoerd: 2026-02-06

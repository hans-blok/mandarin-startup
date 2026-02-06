# Mandarin Stylesheet Guide

**Verantwoordelijke**: Presentatie Architect  
**Versie**: 1.0  
**Datum**: 2026-02-06  
**Status**: Actief

## Overzicht

Dit document beschrijft het gebruik van de Mandarin stylesheet (`mandarin.css`) voor publicaties in de Mandarin huisstijl. De stylesheet implementeert een clean, professioneel ontwerp met één consistent lettertype en de karakteristieke Mandarin-oranje topbalk.

## Kernkenmerken

### Branding
- **Primary color**: `#e55039` (Mandarin-oranje)
- **Font family**: Segoe UI (systeem fallback naar system-ui, sans-serif)
- **Karakteristieke topbalk**: 64px hoog, altijd bovenaan sticky
- **Design filosofie**: Clean, minimalistisch, toegankelijk

### Toegankelijkheid
- **WCAG 2.1 AA compliant**: Alle kleurcontrasten voldoen aan de 4.5:1 ratio voor normale tekst
- **Keyboard navigation**: Focus indicators op alle interactieve elementen
- **Screen reader friendly**: Semantische HTML-structuur, skip-to-content link
- **Reduced motion**: Respecteert `prefers-reduced-motion` voorkeur
- **High contrast**: Ondersteunt high contrast modus

### Responsive Design
- **Mobile-first**: Basis styles voor mobiel, progressive enhancement
- **Breakpoints**:
  - Mobiel: < 768px (basis)
  - Tablet: 768px - 1023px
  - Desktop: 1024px - 1439px
  - Large Desktop: ≥ 1440px

## Design Tokens

### Kleuren

```css
--mandarin-primary: #e55039           /* Hoofdkleur (topbalk, headings) */
--mandarin-primary-dark: #c23616      /* Donkere variant (hover states) */
--mandarin-primary-light: #ff6348     /* Lichte variant (accenten) */

--mandarin-text: #2c3e50              /* Basis tekstkleur */
--mandarin-text-light: #546e7a        /* Lichte tekstkleur (secondary) */
--mandarin-background: #ffffff         /* Achtergrond */
--mandarin-background-alt: #f8f9fa    /* Alternatieve achtergrond */
--mandarin-border: #dee2e6            /* Randen */
```

### Typografie

```css
--mandarin-font-family: 'Segoe UI', system-ui, sans-serif
--mandarin-font-size-base: 16px (mobiel), 17px (tablet), 18px (desktop)
--mandarin-line-height: 1.6
```

### Spacing

```css
--mandarin-spacing-xs: 0.5rem   (8px)
--mandarin-spacing-sm: 1rem     (16px)
--mandarin-spacing-md: 1.5rem   (24px)
--mandarin-spacing-lg: 2rem     (32px)
--mandarin-spacing-xl: 3rem     (48px)
```

## Integratie met MkDocs

### Configuratie in mkdocs.yml

```yaml
theme:
  name: "material"
  language: "nl"
  palette:
    primary: "deep-orange"  # Wordt overschreven door custom CSS
  features:
    - navigation.instant
    - navigation.sections
    - navigation.top
    - navigation.tabs

extra_css:
  - css/mandarin.css
```

### Bestandslocatie

Plaats `mandarin.css` in de volgende locatie relatief aan je `mkdocs.yml`:

```
project-root/
├── mkdocs.yml
└── docs/
    └── css/
        └── mandarin.css
```

## Componenten

### Topbalk (Header)

De Mandarin-topbalk is het meest herkenbare element:

```html
<header class="mandarin-header">
  <h1 class="mandarin-header__title">Project Naam</h1>
</header>
```

**Styling**:
- Achtergrondkleur: `#e55039` (Mandarin-oranje)
- Hoogte: 64px
- Position: sticky (blijft bovenaan bij scrollen)
- Box shadow voor diepte

**MkDocs Material theme**: De stylesheet overschrijft automatisch `.md-header` styling.

### Typografie

#### Headings

```html
<h1>Hoofdtitel</h1>           <!-- 2.25rem, border-bottom primary -->
<h2>Sectietitel</h2>           <!-- 1.875rem, border-bottom grijs -->
<h3>Subsectie</h3>             <!-- 1.5rem -->
<h4>Paragraaftitel</h4>        <!-- 1.25rem -->
```

**Opmerking**: H1 krijgt een oranje onderlijn, H2 een grijze onderlijn.

#### Paragrafen en Links

```html
<p>Normale tekst met <a href="#">een link</a>.</p>
```

**Links**:
- Kleur: Mandarin-oranje (#e55039)
- Hover: Donkerder oranje + underline
- Focus: 2px outline voor keyboard navigation

### Code Blocks

#### Inline code

```html
<p>Gebruik <code>mandarin.css</code> voor styling.</p>
```

**Styling**: Lichtgrijze achtergrond, oranje tekstkleur.

#### Code blocks

```html
<pre><code>
def hello():
    print("Hello, Mandarin!")
</code></pre>
```

**Styling**: Lichtgrijze achtergrond, oranje left-border (4px).

### Tabellen

```html
<table>
  <thead>
    <tr>
      <th>Kolom 1</th>
      <th>Kolom 2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Data 1</td>
      <td>Data 2</td>
    </tr>
  </tbody>
</table>
```

**Styling**:
- Header: Mandarin-oranje achtergrond, witte tekst
- Hover: Lichtgrijze achtergrond op rijen
- Borders: Subtiele grijze borders

### Buttons

```html
<button class="mandarin-button">Klik hier</button>
```

**Styling**:
- Achtergrond: Mandarin-oranje
- Hover: Donkerder oranje
- Focus: Outline voor toegankelijkheid

### Admonitions / Callouts

Voor MkDocs Material theme:

```markdown
!!! note "Let op"
    Dit is een belangrijk bericht.
```

**Styling**: Automatisch gestyled met oranje left-border en lichtgrijze achtergrond.

## Gebruik in Custom HTML

Als je custom HTML/Jinja2 templates maakt:

### Basis structuur

```html
<!DOCTYPE html>
<html lang="nl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="css/mandarin.css">
  <title>{{ page_title }}</title>
</head>
<body>
  <a href="#main-content" class="skip-to-main">Spring naar hoofdinhoud</a>
  
  <header class="mandarin-header">
    <h1 class="mandarin-header__title">{{ site_name }}</h1>
  </header>
  
  <main id="main-content" class="mandarin-content">
    {{ content }}
  </main>
</body>
</html>
```

### CSS Custom Properties gebruiken

```css
/* In je eigen stylesheet */
.mijn-component {
  background-color: var(--mandarin-primary);
  padding: var(--mandarin-spacing-md);
  font-family: var(--mandarin-font-family);
  border-radius: var(--mandarin-border-radius);
}
```

## Best Practices

### 1. Eén lettertype

De stylesheet gebruikt consequent **één font family** (Segoe UI met fallbacks). Introduceer geen andere fonts tenzij absoluut noodzakelijk.

### 2. Kleurconsistentie

Gebruik alleen de gedefinieerde Mandarin-kleuren:
- ✅ Primary: `#e55039`
- ❌ Niet: willekeurige andere oranje tinten

### 3. Spacing

Gebruik de gedefinieerde spacing tokens:
```css
/* Goed */
margin: var(--mandarin-spacing-md);

/* Vermijd */
margin: 23px;  /* Willekeurige waarde */
```

### 4. Toegankelijkheid

- Gebruik semantische HTML (`<nav>`, `<main>`, `<article>`, `<aside>`)
- Zorg voor voldoende kleurcontrast (minimaal 4.5:1)
- Voeg alt-tekst toe aan afbeeldingen
- Test keyboard navigation

### 5. Responsive Design

Test op minimaal deze breakpoints:
- 375px (iPhone SE)
- 768px (iPad portrait)
- 1024px (iPad landscape / klein desktop)
- 1920px (full HD desktop)

## Print Styling

De stylesheet bevat dedicated print styles:
- Header en navigatie worden verborgen
- Links tonen hun URLs in print
- Pagina-breaks worden slim ingezet
- Kleuren worden aangepast voor zwart-wit print

Test print output met: `Ctrl+P` / `Cmd+P` in browser.

## Troubleshooting

### Topbalk heeft niet de juiste kleur

**Probleem**: De Material theme overschrijft de kleur.

**Oplossing**: Zorg dat `mandarin.css` *na* de Material theme wordt geladen:

```yaml
extra_css:
  - css/mandarin.css  # Komt na theme CSS
```

### Font wordt niet toegepast

**Probleem**: Segoe UI niet beschikbaar op systeem.

**Oplossing**: De stylesheet heeft fallbacks. Controleer of `font-family` correct cascadet:

```css
body {
  font-family: var(--mandarin-font-family);
}
```

### Responsive breakpoints werken niet

**Probleem**: Viewport meta tag ontbreekt.

**Oplossing**: Voeg toe aan `<head>`:

```html
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

## Versioning en Updates

### Wijzigingen documenteren

Bij updates aan `mandarin.css`:
1. Update versienummer in dit document
2. Documenteer wijzigingen in changelog
3. Test backwards compatibility
4. Communiceer breaking changes

### Changelog

#### v1.0 (2026-02-06)
- Initiële release
- Mandarin-oranje topbalk (#e55039)
- Single font family (Segoe UI)
- WCAG 2.1 AA compliant
- Responsive mobile-first design
- Print stylesheet

## Gerelateerde Documenten

- **Presentatie Architect Charter**: `artefacten/fnd.02.presentatie-architect/presentatie-architect.charter.md`
- **MkDocs Template**: `templates/publicatie-steward.mkdocs.template.md`
- **Design Tokens**: (TODO: `templates/design-tokens.yml`)

## Contact & Governance

**Eigenaar**: Presentatie Architect  
**Governance**: Workspace-doctrine v1.4.0  
**Vragen**: Via workspace-steward

---

*Laatst bijgewerkt: 2026-02-06*

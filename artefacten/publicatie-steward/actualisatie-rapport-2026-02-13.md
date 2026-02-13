# Actualisatie-rapport mkdocs.yml — 2026-02-13

**Agent**: Publicatie-steward  
**Scope**: Aanpassen mkdocs-configuratie aan actuele structuur in `docs/` en corrigeren links

---

## Wijzigingsoverzicht

**Aangepaste onderdelen**
- Navigatieblok `Strategie` in `mkdocs.yml`
- Navigatieblok `Investerings-Pitches` in `mkdocs.yml`
- Nieuwe navigatiesectie `Concurrentie` in `mkdocs.yml`
- Verwijzingen op de homepage `docs/index.md`
- Interne verwijzing in `docs/publish/onze strategie/strategische-spanningsvelden.md`

**Nieuwe content opgenomen in navigatie**
- `docs/publish/onze strategie/click-hypohese.md`
- `docs/publish/onze strategie/hypothese-probleemkader-mandarin.md`
- `docs/concurrentie/Dataiku.md`

**Verouderde/broken verwijzingen gecorrigeerd**
- Verwijzing naar niet-bestaand `publish/onze strategie/fundamentele-hypothese.md` vervangen door actuele hypothese-bestanden
- Verwijzingen naar pitches onder `publish/onze strategie/` aangepast naar `publish/pitches/`

---

## Detail: Navigatie vóór/na (samenvatting)

### Strategie
- **Voor**:
  - Overzicht → `publish/onze strategie/strategische-intenties.md`
  - Strategische Intenties → `publish/onze strategie/strategische-intenties.md`
  - Fundamentele Hypothese → `publish/onze strategie/fundamentele-hypothese.md`
  - Strategische Spanningsvelden → `publish/onze strategie/strategische-spanningsvelden.md`
  - De drie vragen in de bestuurskamer → `publish/onze strategie/de-drie-vragen-in-de-bestuurskamer.md`

- **Na**:
  - Overzicht → `publish/onze strategie/strategische-intenties.md`
  - Strategische Intenties → `publish/onze strategie/strategische-intenties.md`
  - Hypothese (Click-formaat) → `publish/onze strategie/click-hypohese.md`
  - Hypothese Probleemkader → `publish/onze strategie/hypothese-probleemkader-mandarin.md`
  - Strategische Spanningsvelden → `publish/onze strategie/strategische-spanningsvelden.md`
  - De drie vragen in de bestuurskamer → `publish/onze strategie/de-drie-vragen-in-de-bestuurskamer.md`

### Investerings-Pitches
- **Voor**:
  - Uitgebreide Pitch → `publish/onze strategie/investerings-pitch-mandarin.md`
  - 30-Seconden Pitch → `publish/onze strategie/30-seconden-pitch-mandarin.md`

- **Na**:
  - Uitgebreide Pitch → `publish/pitches/investerings-pitch-mandarin.md`
  - 30-Seconden Pitch → `publish/pitches/30-seconden-pitch-mandarin.md`

### Concurrentie
- **Nieuw**:
  - Dataiku als spanningsveld → `concurrentie/Dataiku.md`

---

## Detail: Linkcorrecties in content

### `docs/index.md`
- Strategisch blok:
  - Verwijzing naar `Fundamentele Hypothese` vervangen door links naar de twee nieuwe hypothese-pagina's:
    - `publish/onze strategie/click-hypohese.md`
    - `publish/onze strategie/hypothese-probleemkader-mandarin.md`
- Investerings-pitches blok:
  - Links naar `publish/onze strategie/investerings-pitch-mandarin.md` en `publish/onze strategie/30-seconden-pitch-mandarin.md` aangepast naar `publish/pitches/...`

### `docs/publish/onze strategie/strategische-spanningsvelden.md`
- Interne link naar `fundamentele-hypothese.md` aangepast naar `hypothese-probleemkader-mandarin.md`.

---

## Waarnemingen en aandachtspunten

- Er is geen `fundamentele-hypothese.md` meer in `docs/publish/onze strategie/`; de actuele hypothese-artefacten zijn `click-hypohese.md` en `hypothese-probleemkader-mandarin.md`.
- De pitches zijn nu logisch gegroepeerd onder `docs/publish/pitches/`; navigatie en homepage-links zijn hierop afgestemd.
- Nieuwe content onder `docs/concurrentie/` (Dataiku) is nu zichtbaar in de hoofdnav onder een aparte sectie `Concurrentie`.

Deze actualisatie blijft binnen de bestaande structuur en naming-conventies, en is beperkt tot het corrigeren van paden en het toevoegen van nieuwe inhoud aan de navigatie.

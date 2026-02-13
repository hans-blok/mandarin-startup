---
workspace: <workspace-naam>
value_stream: <vs-code>
canon_github_url: https://github.com/hans-blok/mandarin-canon.git

# Grondslagen-patronen per value stream voor canon consultatie
# BELANGRIJK: De grondslagen-map hieronder moet alle value streams bevatten die in deze workspace gebruikt worden
grondslagen:
  aeo: "grondslagen/.algemeen/*,grondslagen/aeo/*"
  sfw: "grondslagen/.algemeen/*,grondslagen/sfw/*"
  aod: "grondslagen/.algemeen/*,grondslagen/aod/*"
  kvl: "grondslagen/.algemeen/*,grondslagen/kvl/*"
  miv: "grondslagen/.algemeen/*,grondslagen/miv/*"
  fnd: "grondslagen/.algemeen/*,grondslagen/fnd/*"
---

# Beleid voor de <WORKSPACE-NAAM> workspace

Deze workspace hoort bij de waardestroom **<VALUE-STREAM-NAAM>**.

## Verplichte leesvolgorde van grondslagen

Elke geautomatiseerde rol, agent of runner hanteert bij aanvang van zijn functioneren de volgende verplichte leesvolgorde:

**In de centrale canon repository** (`https://github.com/hans-blok/mandarin-canon.git`):
1. `grondslagen/.algemeen/constitutie.md`
2. overige algemene grondslagen binnen `grondslagen/.algemeen/`
3. grondslagen van de expliciet toegewezen value stream

**In deze workspace**:
4. workspace-specifiek beleid (dit bestand)

Het overslaan, herordenen of impliciet toepassen van deze leesvolgorde is niet toegestaan.

**Zonder aantoonbare toepassing van de constitutie is handelen ongeldig.**

## Dit beleid is workspace-specifiek

Dit beleid beschrijft alleen de workspace-specifieke scope. Voor alle regels, uitzonderingen, details en constitutionele bepalingen volgen we volledig de richtlijnen in `hans-blok/mandarin-canon`.

De constitutie, algemene regels en governance voor alle workspaces staan in:
- https://github.com/hans-blok/mandarin-canon.git

## Canon Repository Synchronisatie

In alle geautomatiseerde en handmatige processen wordt de centrale canon repository geraadpleegd. Dit gebeurt altijd eerst met een `git pull` om te waarborgen dat de meest recente grondslagen worden gebruikt.

**Foutmelding**: Wanneer de mandarin-canon-repository niet bereikbaar is of niet kan worden gevonden, wordt een foutmelding gegeven en stopt het proces.

## Scope

### Wat we in deze workspace vastleggen

<Beschrijf hier 5-10 kernactiviteiten of artefacten die in deze workspace horen. Bijvoorbeeld:>

- **<Activiteit 1>**: <Beschrijving van wat deze workspace doet of vastlegt>
- **<Activiteit 2>**: <Beschrijving van wat deze workspace doet of vastlegt>
- **<Activiteit 3>**: <Beschrijving van wat deze workspace doet of vastlegt>

### Wat niet in deze workspace hoort

Andere domeinen vallen buiten deze workspace en horen in andere repositories. Voorbeelden hiervan zijn:

<Lijst met voorbeelden van wat NIET in deze workspace hoort, verwijs naar andere value streams. Bijvoorbeeld:>

- **Business domeinlogica**: Specifieke bedrijfsprocessen, domeinkennis en business rules horen in domein-specifieke workspaces
- **Software ontwikkeling**: Applicatie-code, databases, API's en technische implementaties horen in SFW-workspaces (Software-ontwikkeling)
- **Enterprise architectuur**: C4-modellen, ArchiMate-diagrammen en architectuur-artefacten horen in AOD-workspaces (Architectuur- en Oplossingsontwerp)
- **Content en publicaties**: Artikelen, essays, handleidingen en communicatie-materiaal horen in KVL-workspaces (Kennisverwerving en -verspreiding)
- **Strategische analyse**: Marktonderzoek, business cases en investeringsbeslissingen horen in MIV-workspaces (Markt- en Investeringsvorming)
- **Infrastructuur en tooling**: Server-configuratie, deployment-pipelines en basis-tooling horen in FND-workspaces (Foundation)

## Workspace-specifieke aanvullingen

<Voeg hier workspace-specifieke regels, conventies en aanvullingen toe. Voorbeelden:>

- **<Conventie 1>**: <Beschrijving, bijvoorbeeld naamgeving-conventies>
- **<Conventie 2>**: <Beschrijving, bijvoorbeeld kwaliteitsnormen>
- **<Conventie 3>**: <Beschrijving, bijvoorbeeld logging/audit requirements>

---

*Laatste update: <datum> door <auteur>*

---

## 📋 Instructies voor gebruik van dit template

### Stap 1: YAML Frontmatter invullen

In de YAML frontmatter bovenaan dit bestand:

1. **workspace**: Vervang `<workspace-naam>` met de technische naam (lowercase-with-hyphens), bijv. `kennispublicatie` of `architectuur-ontwerp`

2. **value_stream**: Vervang `<vs-code>` met de 3-letter value stream code (lowercase):
   - `aeo` = Agent Ecosysteem Ontwikkeling
   - `sfw` = Software-ontwikkeling
   - `aod` = Architectuur- en Oplossingsontwerp
   - `kvl` = Kennisverwerving en -verspreiding
   - `miv` = Markt- en Investeringsvorming
   - `fnd` = Foundation

3. **canon_github_url**: Laat staan tenzij je een andere canon repository gebruikt

4. **grondslagen**: 
   - Behoud alleen de value streams die in deze workspace gebruikt worden
   - Voeg nieuwe value streams toe indien nodig met patroon: `<vs>: "grondslagen/.algemeen/*,grondslagen/<vs>/*"`

### Stap 2: Workspace naam en beschrijving

1. Vervang `<WORKSPACE-NAAM>` (in titel) met de leesbare naam, bijv. "KENNISPUBLICATIE" of "ARCHITECTUUR-ONTWERP"
2. Vervang `<VALUE-STREAM-NAAM>` met de volledige naam, bijv. "KENNISVERWERVING EN -VERSPREIDING (KVL)"

### Stap 3: Scope invullen

1. **Wat we in deze workspace vastleggen**: 
   - Beschrijf 5-10 concrete activiteiten of artefacten
   - Gebruik bullet points met vette titels
   - Wees specifiek over wat WEL in deze workspace hoort

2. **Wat niet in deze workspace hoort**:
   - Pas de voorbeelden aan of gebruik ze als-is
   - Verwijs naar andere value streams voor out-of-scope items
   - Voorkom scope creep door duidelijk te zijn over wat niet hoort

### Stap 4: Workspace-specifieke aanvullingen

Voeg workspace-specifieke regels toe, zoals:
- Naamgeving-conventies
- Kwaliteitsnormen (bijv. B1-taalniveau, schema-validatie)
- Logging en audit requirements
- Template-gebruik
- Version control practices
- Specifieke tools of processen

### Stap 5: Metadata bijwerken

1. Vervang `<datum>` met huidige datum (YYYY-MM-DD formaat)
2. Vervang `<auteur>` met je naam

### Stap 6: Verwijder instructies

Verwijder deze gehele instructiesectie (van "📋 Instructies" tot einde) voordat je het beleid-bestand commit.

### ℹ️ Extra informatie

**Waarom YAML frontmatter?**
- **Single Source of Truth**: Canon URL en grondslagen-patronen centraal beheerd
- **Automatisering**: Scripts zoals `run_prompt.py` lezen deze configuratie automatisch
- **SOLID principe**: Minimale configuratie in prompt bestanden, centraal in beleid

**Bekende Value Streams**:
- **AEO** (Agent Ecosysteem Ontwikkeling): Het ontwerpen, bouwen en beheren van agents
- **SFW** (Software-ontwikkeling): Software architectuur, development, testen
- **AOD** (Architectuur- en Oplossingsontwerp): Enterprise architectuur, C4-modellen, ArchiMate
- **KVL** (Kennisverwerving en -verspreiding): Publicaties, artikelen, essays, communicatie
- **MIV** (Markt- en Investeringsvorming): Strategie, marktverkenning, business cases
- **FND** (Foundation): Basis tooling, workspace management, engineering support

**Zie ook**:
- [docs/README-PROMPT-ARCHITECTURE.md](../docs/README-PROMPT-ARCHITECTURE.md) - Architectuur principes
- [scripts/run_prompt.py](../scripts/run_prompt.py) - Script dat beleid-workspace.md gebruikt


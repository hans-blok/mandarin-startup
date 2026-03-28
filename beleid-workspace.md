---
workspace: mandarin-startup
value_stream: miv
value_stream-fasen: ["miv.01", "miv.02", "miv.07"]
canon_github_url: https://github.com/hans-blok/mandarin-canon.git

# Grondslagen-patronen per value stream voor canon consultatie
# BELANGRIJK: De grondslagen-map hieronder moet alle value streams bevatten die in deze workspace gebruikt worden
grondslagen:
  miv: "grondslagen/.algemeen/*,grondslagen/miv/*"
---

# Beleid voor de MANDARIN-STARTUP workspace

Deze workspace hoort bij de waardestroom **MARKT- EN INVESTERINGSVORMING (MIV)**.

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

## Charter & Template Repository Configuratie

Deze workspace gebruikt externe agents uit de `mandarin-agents` repository. Charters en templates blijven in die repository; alleen prompts en agent-contracten worden hier gefetcht.

```yaml
external_agent_resources:
  # Primaire agent repository (schaalt automatisch voor alle agents)
  agent_repository:
    type: github  # Gebruik 'github' voor productie, 'local' voor development
    base_url: https://raw.githubusercontent.com/hans-blok/mandarin-agents/main/artefacten
    # BELANGRIJK: base_url is niet direct browseable, maar wordt gebruikt als prefix
    # voor individuele charter- en template-paden. Bijvoorbeeld:
    # {base_url}/aod/aod.02.core-framework-architect/core-framework-architect.charter.md
    # {base_url}/aod/aod.02.core-framework-architect/templates/core-framework-architect.structureer-gedrag.template.md
    
    # Voor lokale development (comment out base_url en gebruik):
    # type: local
    # local_path: ../mandarin-agents/artefacten
  
  # Pad-conventies (gebruikt door run_prompt.py om resources te vinden)
  # Variabelen: {vs} = value stream code, {fase} = fase nummer, {agent} = agent naam, {intent} = intent naam
  conventions:
    charter: "{vs}/{vs}.{fase}.{agent}/{agent}.charter.md"
    template: "{vs}/{vs}.{fase}.{agent}/templates/{agent}.{intent}.template.md"
  
  # Alleen uitzonderingen hier definiëren (optioneel)
  # Gebruik dit alleen voor agents die afwijken van de standaard pad-conventies
  exceptions: {}
    # voorbeeld:
    # legacy-agent:
    #   charter_path: special/path/legacy-agent.charter.md
    #   templates:
    #     legacy-intent: special/path/legacy.template.md
```

**Voorbeeld resource-opbouw voor agent `core-framework-architect` met `value_stream_fase: aod.02` en `intent: structureer-gedrag`:**
- Parse: `vs=aod`, `fase=02`, `agent=core-framework-architect`, `intent=structureer-gedrag`
- Charter pad via conventie: `aod/aod.02.core-framework-architect/core-framework-architect.charter.md`
- Template pad via conventie: `aod/aod.02.core-framework-architect/templates/core-framework-architect.structureer-gedrag.template.md`
- Volledige URLs:
  - Charter: `{base_url}/aod/aod.02.core-framework-architect/core-framework-architect.charter.md`
  - Template: `{base_url}/aod/aod.02.core-framework-architect/templates/core-framework-architect.structureer-gedrag.template.md`

**Development workflow:**
1. **Lokaal ontwikkelen**: Zet `type: local` en gebruik `local_path: ../mandarin-agents/artefacten`
2. **Na commit**: Zet `type: github` en gebruik `base_url` naar main branch

Nieuwe agents die de conventies volgen hoeven niet geconfigureerd te worden!

## Scope

### Wat we in deze workspace vastleggen

- **Strategische intenties en waardehypotheses**: Kernpositionering, waardeproposities en probleemkaders voor Mandarin als startup
- **Markt- en investeringsnarratieven**: Pitches, 4F-profielen, investeringsverhalen en positionering voor verschillende doelgroepen
- **Spanningsveld-analyses**: Identificatie en analyse van aannames, risico's en strategische dilemma's
- **Concept-ontwikkeling**: Uitwerking van kernconcepten zoals tractie, strategische intentie en andere fundamentele bouwstenen
- **Hypothese-vorming**: Geformuleerde en toetsbare hypotheses over markt, product-marktfit en investeringsstrategie
- **Strategische gespreksverslagen**: Documentatie van belangrijke strategische discussies en besluitvorming
- **Werkversies governance**: Voorbereidende versies van beleids- en governance-afspraken die later elders worden verankerd
- **Publicatie-gereed materiaal**: Uitgewerkte presentaties, essays en verhalen voor externe communicatie

### Wat niet in deze workspace hoort

Andere domeinen vallen buiten deze workspace en horen in andere repositories. Voorbeelden hiervan zijn:

- **Business domeinlogica**: Specifieke bedrijfsprocessen, domeinkennis en business rules horen in domein-specifieke workspaces
- **Software ontwikkeling**: Applicatie-code, databases, API's en technische implementaties horen in SFW-workspaces (Software-ontwikkeling)
- **Enterprise architectuur**: C4-modellen, ArchiMate-diagrammen en architectuur-artefacten horen in AOD-workspaces (Architectuur- en Oplossingsontwerp)
- **Content en publicaties**: Artikelen, essays, handleidingen en communicatiemateriaal horen in KVL-workspaces (Kennisverwerving en -verspreiding)
- **Infrastructuur en tooling**: Server-configuratie, deployment-pipelines en basis-tooling horen in FND-workspaces (Foundation)
- **Operationele dossiers**: Dagelijkse uitvoering, runbooks, incidentafhandeling en klantcases
- **Definitieve beslisarchieven**: Contracten, formele juridische of financiele documenten en bindende besluiten
- **Marketing in productie**: Actieve website, campagnes, CRM-uitvoering en saleskanalen

## Workspace-specifieke aanvullingen

- **Taal en stijl**: Documentatie is primair in helder B1/B2-Nederlands, met waar nodig Engelstalige termen uit de canon. We schrijven concreet, toetsbaar en vermijden marketingtaal in bronartefacten
- **Vorm en structuur**: Alle inhoud wordt vastgelegd in gestructureerde markdown-bestanden binnen `artefacten/` en `docs/`, met expliciete bron- en versieverantwoording
- **Rol van de workspace**: Alleen denkwerk in wording en strategische explicitering; geen definitieve besluiten, operationele instructies of uitvoerende taken
- **Traceerbaarheid**: Substantiële wijzigingen aan strategische artefacten worden waar mogelijk gelogd via agent-logs in `logs/` of wijzigingslogs in de betreffende markdown-bestanden
- **Werkgeheugen-functie**: De workspace fungeert als expliciete, herleidbare analyse-omgeving voor input naar latere, formele besluitvorming in andere repositories
- **Agent-samenwerking**: Geoptimaliseerd voor gebruik door gespecialiseerde agents zoals strategisch-analist, hypothese-vormer, investerings-verteller en publicatie-steward
- **Iteratieve ontwikkeling**: Concepten en hypotheses worden gradueel uitontwikkeld door verschillende agent-rollen in samenwerking

---

*Laatste update: 2026-03-28 door GitHub Copilot*

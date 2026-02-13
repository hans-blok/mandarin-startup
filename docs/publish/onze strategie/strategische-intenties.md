# Strategische Intenties — Mandarin

**Tijdshorizon**: 2026–2031  
**Datum**: 2026-02-08  
**Versie**: 2.0 (herijking op basis van Edwin's input + marktcontext)

---

## Context van deze Herijking

Deze versie integreert:
1. **Edwin's strategische input** (2026-02-07): Governance als kernwaarde, determinisme, TLX-roadmap, wetenschappelijke basis
2. **The Agentic AI Advantage** (The Economist, 2025): Marktbehoefte aan governance, data-infrastructuur, ROI-denken
3. **Eerdere strategische intenties** (v1.0): Product, fundament, licentiemodel

De herijking expliciteert **wat impliciete aannames waren**, scherpt **spanningsvelden** aan en voegt **nieuwe strategische keuzeruimte** toe zonder richting te kiezen.

---

## Geëxpliciteerde Intenties

### Intentie 1: Governance-Native Agentic Platform

**Waarom**: Mandarin onderscheidt zich door governance, traceerbaarheid en voorspelbaarheid als **kern van het product**, niet als plugin of afterthought. De ambitie is om het expliciet gebrek aan AI governance in de markt (73% van organisaties heeft geen framework, Gartner 2025) te adresseren met een platform waarin elke artefact verklaarbaar en herleidbaar is.

**Horizon**: 2026–2031

**Scope**:
- **WEL**: Audit trails, expliciet contract per agent, traceability van beslissingen, deterministische pipelines waar mogelijk, AI-intent alleen waar effectief, compliance-by-design, accountability zonder blame.
- **NIET**: Blackbox AI-systemen, governance als toevoeging achteraf, technologie zonder transparantie, tools zonder verantwoordingsplicht.

**Onderliggende aannames**:
- **Marktaanname**: CTO's en compliance officers accepteren AI-adoption alleen met governance (bevestigd door Economist: "without governance, organizations will avoid scale").
- **Architectuuraanname**: Deterministisch systeem met AI-intent alleen waar het sterk is, leidt tot voorspelbaarheid zonder innovatie te belemmeren.
- **Concurrentieaanname**: Bestaande tools (GitHub Copilot, etc.) hebben governance niet als DNA, waardoor Mandarin first-mover-voordeel heeft.
- **Klantaanname**: IT-professionals willen "sleep better" (predictability, traceability, accountability), niet alleen snellere tools.
- **Risico-aanname**: Sectoren met compliance-eisen (finance, healthcare, government) zijn early adopters voor governance-native tooling.

**Spanningsveld**: 
- Governance kan worden gezien als bottleneck (bureaucratie) vs. enabler (vertrouwen). Mandarin moet beide percepties adresseren.
- Determinisme vs. AI-flexibiliteit: te strikt = geen innovatie, te los = geen controle.

**Bronnen**: Edwin input (2026-02-07), The Economist (governance gap), 4 F's framework (Flair: governance-native)

---

### Intentie 2: Practice-First Productvolwassenheid via TLX

**Waarom**: Mandarin wordt gedurende 2 jaar (2026–2028) ontwikkeld en bewezen binnen TLX als complexe praktijkomgeving. Dit is geen pilot maar een **volledige implementatie** om architectuur, governance en processen te valideren voordat commercialisatie start. De ambitie is geen vaporware te verkopen, maar een product met aantoonbare tractie, stabiliteit en overdraagbare kennis.

**Horizon**: 2026–2028 (bouw & bewijs), 2028→ (commercialisatie)

**Scope**:
- **WEL**: 
  - **Q2 2026**: **Bouw & Fundament** — UI-generator operationeel, KEYSTONE module met abonnementen/endpoints/Keycloak, TLX klantportaal (API-laag, canoniek model)
  - **Q3 2026**: **CI/CD & Support** — Veranderverkenning UI, geoptimaliseerde pipeline (requirements → OAS), TLX in acceptatie, eerste zelfstandige gebruikersinterface
  - **Q4 2026**: **TLX Compleet & Pre-Sales** — Mandarin v1.0 voor definitiefase (OAS, DDL output), pre-sales leadgeneratie, TLX bouw volledig afgerond
  - **Q1 2027**: **Sales Start** — Volledige automatisering (feature → deployment), JIRA-integratie, complete traceability, **commercieel**: sales launch, TLX productie (True Logic uitfasering)
- **NIET**: Commercialisatie zonder praktijkbewijs, product zonder volwassenheid, verkoop van experimenten, premature scaling.

**Uitgewerkte roadmap**: Voor een overzichtelijke tabel met alle mijlpalen per kwartaal, zie [Mijlpalen](../mijlpalen/mijlpalen.md). Deze roadmap toont de parallelle ontwikkeling van TLX (als testomgeving) en Mandarin (als commercieel product) van Q2 2026 tot Q1 2027, met als hoogtepunt de start van commerciële verkoop in Q1 2027.

**Onderliggende aannames**:
- **TLX-aanname**: TLX biedt voldoende complexiteit (APIs, canonieke modellen, multi-systeem integratie) om Mandarin te testen.
- **Jan Dalm-aanname**: TLX heeft interne salescapability (Jan Dalm) waardoor early feedback mogelijk is zonder eigen salesorganisatie.
- **Timeline-aanname**: 2 jaar is voldoende voor productvolwassenheid (tegen marktdruk om sneller te gaan).
- **Investering-aanname**: €20K (2026-2028) is voldoende voor practice-first fase zonder externe druk tot ROI. Edwin en Hans zijn voldoende beschikbaar voor ontwikkeling en kunnen Niek nuttig inzetten.
- **Learning-aanname**: Praktijkervaring in TLX is generaliseerbaar naar andere organisaties.

**Spanningsveld**:
- **Snelheid vs. Gronddigheid**: Markt wil snelle innovatie, Mandarin kiest bewust voor 2 jaar bewijs → risico op achterstand vs. concurrentie die sneller commercialiseert.
- **TLX-focus vs. Generalisatie**: Diep in TLX duiken kan leiden tot TLX-specifieke oplossingen die niet overdraagbaar zijn.

**Bronnen**: Edwin roadmap (Q2 2026–Q1 2027), Fase 1 (Fundament), 4 F's (Practice-first differentiator)

---

### Intentie 3: Wetenschappelijk Gefundeerde Architectuur

**Waarom**: Mandarin ontwikkelt samen met een **universiteit** een wetenschappelijke basis voor het agent-ecosysteem. De ambitie is geloofwaardigheid, gedegen architectuurkeuzes en een theoretisch kader dat bredere adoptie ondersteunt en intellectueel eigendom beschermt.

**Horizon**: 2026–2028 (parallel aan TLX-praktijk)

**Scope**:
- **WEL**: Academische samenwerking, publiceerbare architectuurkaders, peer-reviewed validatie van governance-modellen, expliciete agent-contracten, formele definities van traceability en accountability.
- **NIET**: Ivoren-toren-onderzoek zonder praktijkrelevantie, vertraging van TLX-ontwikkeling door academische cycles, papers schrijven als doel op zich.

**Onderliggende aannames**:
- **Geloofwaardigheidsaanname**: Academische fundering verhoogt vertrouwen bij enterprise buyers (vooral in regulated industries).
- **IP-aanname**: Wetenschappelijke basis leidt tot defensible IP (moeilijker te kopiëren door concurrenten).
- **Talent-aanname**: Universiteit levert toegang tot onderzoekstalent en student-interns voor doorontwikkeling.
- **Publicatie-aanname**: Papers in erkende tijdschriften versterken thought leadership positie van Mandarin.
- **Cost-benefit-aanname**: Tijd en geld geïnvesteerd in universiteit levert ROI via differentiatie en IP-bescherming.

**Spanningsveld**:
- **Pragmatisme vs. Academie**: TLX-praktijk vereist snelle iteratie, universiteit vraagt om methodische rigour → risico op vertraging of fricties.
- **Openheid vs. Concurrentie**: Publiceren vergroot zichtbaarheid maar kan ook concurrenten helpen.

**Bronnen**: Edwin input (universiteit als sidenote), The Economist (need for robust frameworks)

---

### Intentie 4: Data-Centric Enterprise Interoperability

**Waarom**: Mandarin adresseert de data-infrastructuur bottleneck die enterprise AI-adoptie blokkeert (22% van organisaties heeft adequate architectuur, Economist 2025). De ambitie is dat Mandarin agents naadloos integreren met bestaande enterprise systemen (ERP, CRM, databases) en data-kwaliteit, -interoperability en -governance garanderen.

**Horizon**: 2026→ (vanaf Q3 2026 via TLX-integraties)

**Scope**:
- **WEL**: API-first design, canonieke datamodellen, multi-systeem data-synchronisatie, RAG-architectuur voor data-grounding, verifieerbare databronnen, expliciete herkomstmetadata, koppelingen met JIRA/andere tools.
- **NIET**: Siloed agents zonder data-toegang, blackbox data-transformaties, afhankelijkheid van één ERP/CRM vendor, data-integratie als afterthought.

**Onderliggende aannames**:
- **Marktaanname**: Data-infrastructuur is grootste belemmering voor AI-schaal (Economist bevestigt dit).
- **RAG-aanname**: Retrieval Augmented Generation levert betrouwbaardere output dan pure LLM-prompts.
- **Interoperability-aanname**: Enterprise waarde ontstaat pas bij cross-systeem agents (niet losse point solutions).
- **Datakwaliteit-aanname**: "Garbage in, landfill out" (Economist) — hoogwaardige input is voorwaarde voor success.
- **Orkestratie-aanname**: Agents moeten gecoördineerd werken (niet fragmentatie met 15+ tools zoals nu).

**Spanningsveld**:
- **Vendor Lock-in vs. Neutraliteit**: Hoe diep integreren zonder afhankelijk te worden van specifieke platforms?
- **Data Access vs. Security**: Agents hebben data nodig, maar security/privacy eisen beperkingen.
- **Canonical Model vs. Flexibility**: Standaardisatie helpt, maar elke klant heeft unieke datastroomen.

**Bronnen**: The Economist (data bottleneck), Edwin input (API's, canoniek model, APEX-integratie), KEYSTONE module

---

### Intentie 5: Licentieerbaar Product met Enterprise Support

**Waarom**: Mandarin wordt vanaf Q1 2027 een **licentieerbaar B2B SaaS product** dat organisaties zelf kunnen inzetten met tiered support. De ambitie is schaalbaarheid (70-100 klanten tegen 2031), €5-8M ARR, en exit-valuation van €25-40M (5x ARR).

**Horizon**: 2028–2031 (na practice-first bewijs)

**Scope**:
- **WEL**: Licenties (€500-2000/seat/jaar), tiered support (basic/premium/enterprise), training (€10-50K/org), consulting (€50-200K/governance impl), governance-templates, onboarding-pakketten, white-label mogelijkheden.
- **NIET**: Full-service consulting model (niet schaalbaar), klanten volledig afhankelijk van Mandarin-team, product zonder documentatie/self-service, premature exit onderhandelingen.

**Onderliggende aannames**:
- **Productvolwassenheid-aanname**: 2 jaar TLX is voldoende voor enterprise-ready product.
- **Markt-sizing-aanname**: DevOps tooling markt ($15B+, 20% CAGR) is groot genoeg voor Mandarin's niche.
- **Pricing-aanname**: €500-2000/seat/jaar is competitief maar premium (governance is waardevol).
- **Sales-aanname**: Sales capability (currently missing, spanningsveld 7) wordt ontwikkeld tussen 2026-2028.
- **Churn-aanname**: Practice-first leidt tot lage churn (betere product-market fit).
- **Exit-aanname**: 5x ARR valuation is realistisch voor SaaS met <20% churn.

**Spanningsveld**:
- **Self-Service vs. High-Touch**: Licentiemodel vereist self-service, maar governance-implementatie is complex.
- **Standardization vs. Customization**: Governance-templates moeten generiek genoeg zijn, maar elke org heeft unieke compliance-eisen.

**Bronnen**: Edwin business model, Fase 2 (Licentieverkoop), Scenario A, 4 F's (Facts)

---

### Intentie 6: First-Mover Advantage in Tijdgevoelige Markt

**Waarom**: Agentic AI-adoptie groeit explosief (25% van Gen AI-gebruikers in 2025 → 50% in 2027, Gartner). De ambitie is **early positioning** als governance-native speler voordat concurrenten dit gat dichten, zonder te compromitteren op kwaliteit door te vroeg te commercialiseren.

**Horizon**: 2026–2028 (kritieke window)

**Scope**:
- **WEL**: Pre-sales vanaf Q4 2026, thought leadership (blogs, papers, conferenties), early adopter-programma, pilotklanten naast TLX, reputatieopbouw als "de governance player", netwerk met investeerders opbouwen.
- **NIET**: Haastwerk dat kwaliteit ondermijnt, "me-too" productpositie, premature feature-explosion zonder focus, marketing zonder proof.

**Onderliggende aannames**:
- **Window-aanname**: 2026-2028 is uniek moment (markt erkent governance-gap, maar weinig oplossingen).
- **Concurrentie-aanname**: Grote spelers (Microsoft, GitHub) voegen governance toe als feature, niet als DNA → blijvende differentiatie mogelijk.
- **Thought Leadership-aanname**: Vroeg positie innemen via content/papers verhoogt inbound leads.
- **Network Effect-aanname**: Eerste klanten worden ambassadeurs (NPS 30+, evangelists).
- **Investor Timing-aanname**: Funding rounds zijn makkelijker tijdens hype-cycle (2026-2027) dan erna.

**Spanningsveld**:
- **Speed vs. Quality**: Markt beweegt snel, Mandarin kiest bewust traag → risico markt te missen.
- **Hype vs. Substance**: Agentic AI is buzzword, Mandarin moet hype gebruiken zonder slachtoffer te worden van verwachtingen.

**Bronnen**: The Economist (adoption curve), Edwin (sales start Q1 2027), 4 F's (eerste-mover in governance-native)

---

## Relaties tussen Intenties

### Versterkingen
1. **Intentie 1 (Governance) ↔ Intentie 2 (Practice-first)**: TLX-praktijk valideert governance-architectuur; governance maakt TLX-resultaten overdraagbaar.
2. **Intentie 2 (Practice-first) ↔ Intentie 3 (Wetenschappelijk)**: Praktijk levert casussen voor academisch onderzoek; wetenschap valideert architectuurkeuzes.
3. **Intentie 3 (Wetenschappelijk) ↔ Intentie 1 (Governance)**: Academische fundering verhoogt geloofwaardigheid van governance-claims.
4. **Intentie 4 (Data-Centric) ↔ Intentie 1 (Governance)**: Data-interoperability is voorwaarde voor enterprise governance (geen audit zonder data-trails).
5. **Intentie 2 (Practice-first) → Intentie 5 (Licentie)**: TLX-bewijs is noodzakelijk voor licentieverkoop (geen product zonder proof).
6. **Intentie 6 (First-Mover) ← Intentie 1 (Governance)**: Governance-focus is basis voor first-mover positie.

### Uitsluitingen / Spanningen
1. **Intentie 6 (First-Mover) ⚡ Intentie 2 (Practice-first)**: Snelheid vs. gronddigheid → Markt wil snel, Mandarin kiest 2 jaar bewijs. **Risiko**: Concurrenten zijn in 2027 al verkocht zonder bewijs.
2. **Intentie 3 (Wetenschappelijk) ⚡ Intentie 2 (Practice-first)**: Academische rigour vs. pragmatische iteratie → **Risiko**: Vertraging door publicatie-cycli.
3. **Intentie 5 (Licentie self-service) ⚡ Intentie 1 (Governance complexity)**: Standaardisatie vs. complexiteit → **Risiko**: Klanten kunnen governance niet zelfstandig implementeren.
4. **Intentie 4 (Data-interoperability) ⚡ Intentie 5 (Vendor-agnostic)**: Diep integreren vs. neutraal blijven → **Risiko**: Te generiek = geen waarde, te specifiek = vendor lock-in.

---

## Nieuwe Spanningsvelden (Expliciet Zichtbaar Gemaakt)

Deze herijking maakt **7 strategische spanningsvelden** expliciet die in v1.0 impliciet waren:

1. **Speed-to-Market vs. Practice-First** (Intentie 6 vs. 2)
2. **Governance-as-Control vs. Governance-as-Enabler** (Intentie 1, perceptie-risico)
3. **TLX-Specifiek vs. Generaliseerbaar** (Intentie 2, learning transfer)
4. **Academic Rigour vs. Pragmatic Iteration** (Intentie 3 vs. 2)
5. **Self-Service vs. High-Touch Implementation** (Intentie 5, operationeel model)
6. **Vendor Lock-in vs. Interoperability** (Intentie 4, architectuurkeuze)
7. **Sales Capability Gap** (Intentie 5/6, execution risk)

→ Deze spanningsvelden worden verder uitgewerkt in `spanningsvelden.md` (volgende agent-iteratie).

---

## Bronverwijzingen

### Primaire Bronnen
- **Edwin Input (2026-02-07)**: Governance-focus, determinisme, TLX-roadmap Q2 2026–Q1 2027, wetenschappelijke basis, 4 F's framework
- **The Agentic AI Advantage (The Economist, 2025)**: Governance gap (73%), data-infrastructuur bottleneck (22%), ROI-denken (3.7:1), first-mover advantage, workforce augmentation
- **Strategische Intenties v1.0 (2026-02-06)**: Product, fundament, licentie (herijkt en uitgebreid)

### Secundaire Bronnen
- Fundamentele hypothese (probleemkader Mandarin)
- Investerings-pitch (business model, financials)
- Doctrine agent-charter normering (governance-principes)

---

## Wijzigingslog

**v2.0 (2026-02-08)**:
- ✅ **Intentie 1 herijkt**: Governance niet als feature maar als DNA (was impliciet in v1.0)
- ✅ **Intentie 2 uitgebreid**: Concrete TLX-roadmap Q2 2026–Q1 2027 (was abstract in v1.0)
- ✅ **Intentie 3 toegevoegd**: Wetenschappelijke basis (nieuw)
- ✅ **Intentie 4 toegevoegd**: Data-centric interoperability (nieuw, was impliciet)
- ✅ **Intentie 5 (voorheen 3)**: Licentiemodel verfijnd met pricing, support tiers
- ✅ **Intentie 6 toegevoegd**: First-mover timing (nieuw, marktcontext)
- ✅ **Spanningsvelden geëxpliciteerd**: 7 spanningen zichtbaar gemaakt (was 2 in v1.0)
- ✅ **Aannames verrijkt**: Markt-, architectuur-, timing-, risico-aannames per intentie

**v1.0 (2026-02-06)**:
- Initiële explicitering: 3 intenties (Product, fundament, licentie)
- Basis relaties en aannames

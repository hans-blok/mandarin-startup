# Mandaryn Investor Visual - Mermaid Diagram

## Context: Brooks' Law of Complexity

```
┌────────────────────────────────────────────────┐
│ ESSENTIAL COMPLEXITY: inherent domein          │
│         ↓                                      │
│ ACCIDENTAL COMPLEXITY: tooling/infrastructuur  │
│         ↓                                      │
│ Nieuwe tech reduceert accidental...            │
│ MAAR essential blijft                          │
│         ↓                                      │
│ → Ambitieuzere systemen                        │
│ → Scope groeit                                 │
│ → Nieuwe abstracties                           │
│ → Nieuwe accidental complexity                 │
│                                                │
│ CONCLUSIE: COMPLEXITEIT GROEIT                 │
│           ER IS GEEN PLAYBOOK                  │
└────────────────────────────────────────────────┘
```

---

## Mandaryn Ecosystem

```mermaid
graph TD
    %% Styling
    classDef coreStyle fill:#ffffff,stroke:#e55039,stroke-width:3px,color:#000000
    classDef brandStyle fill:#e55039,stroke:#c0392b,stroke-width:2px,color:#ffffff
    classDef problemStyle fill:#ecf0f1,stroke:#34495e,stroke-width:1px,color:#000000
    classDef solutionStyle fill:#ffffff,stroke:#e55039,stroke-width:2px,color:#000000
    classDef resultStyle fill:#e55039,stroke:#c0392b,stroke-width:2px,color:#ffffff
    
    %% Core
    CORE["<b>KERN</b><br/>In 2030 wordt de meeste<br/>software met Agentic AI gemaakt"]
    
    %% Brand
    BRAND["<b>MANDARYN</b><br/>Governance-Native Agent Ecosysteem"]
    
    %% Problems Layer
    P1["<b>Wie is aanspreekbaar?</b><br/>Geen escalatiepad,<br/>geen eigenaarschap,<br/>geen audit basis"]
    P2["<b>Kwaliteit & Compliance?</b><br/>Dynamisch gedrag<br/>botst met statische governance"]
    P3["<b>Zijn kosten houdbaar?</b><br/>Van pilot naar 1000 agents<br/>= OPEX-explosie?"]
    P4["<b>Grip op ROI?</b><br/>Welke waarde per euro<br/>AI-investering?"]
    P5["<b>Wat met mijn data?</b><br/>Privacy-compliance<br/>+ RAG = haalbaar?"]
    
    %% Solutions Layer
    S1["<b>Governance-Native</b><br/>Constitutie + contracten<br/>in systeem-DNA"]
    S2["<b>AI waar waardevol</b><br/>Deterministisch<br/>waar mogelijk"]
    S3["<b>60 jaar architectuur</b><br/>2x30 jaar ervaring<br/>complexe systemen"]
    S4["<b>Traceability by design</b><br/>Volledige audit trail<br/>ingebouwd"]
    S5["<b>Practice-first: TLX</b><br/>2 jaar bewijs<br/>vóór commercie"]
    S6["<b>Data-centrisch</b><br/>On-premise +<br/>open standaarden"]
    
    %% Results Layer
    R1["<b>Voorspelbaar & Traceerbaar</b><br/>Van intentie tot<br/>deployment herleidbaar"]
    R2["<b>Data-soevereiniteit</b><br/>RAG zonder data-lekkage,<br/>AVG-compliant"]
    R3["<b>Beheerste AI-kosten</b><br/>Transparant kostenmodel,<br/>geen OPEX-verrassingen"]
    R4["<b>Sneller zonder tech debt</b><br/>Governance als accelerator"]
    R5["<b>Defensible moat</b><br/>2+ jaar<br/>architectuur-voorsprong"]
    R6["<b>Geen achterblijver</b><br/>Early mover<br/>governance-native AI"]
    
    %% Connections
    CORE --> BRAND
    
    BRAND --> P1
    BRAND --> P2
    BRAND --> P3
    BRAND --> P4
    BRAND --> P5
    
    P1 --> S1
    P2 --> S2
    P3 --> S3
    P4 --> S4
    P5 --> S5
    BRAND --> S6
    
    S1 --> R1
    S2 --> R2
    S3 --> R3
    S4 --> R4
    S5 --> R5
    S6 --> R6
    
    %% Apply Styles
    class CORE coreStyle
    class BRAND brandStyle
    class P1,P2,P3,P4,P5 problemStyle
    class S1,S2,S3,S4,S5,S6 solutionStyle
    class R1,R2,R3,R4,R5,R6 resultStyle
```

---

## Alternatieve weergave: Layered flowchart

```mermaid
flowchart TD
    subgraph VISION["🎯 VISIE 2030"]
        V1["In 2030 wordt de meeste software<br/>met Agentic AI gemaakt"]
    end
    
    subgraph BRAND["🟠 MANDARYN"]
        B1["Governance-Native Agent Ecosysteem"]
    end
    
    subgraph PROBLEMS["⚠️ 5 PROBLEMEN"]
        P1["Wie is aanspreekbaar?"]
        P2["Kwaliteit & Compliance?"]
        P3["Zijn kosten houdbaar?"]
        P4["Grip op ROI?"]
        P5["Wat met mijn data?"]
    end
    
    subgraph SOLUTIONS["✅ 6 OPLOSSINGEN"]
        S1["Governance-Native"]
        S2["AI waar waardevol"]
        S3["60 jaar architectuur"]
        S4["Traceability by design"]
        S5["Practice-first: TLX"]
        S6["Data-centrisch"]
    end
    
    subgraph RESULTS["🚀 6 RESULTATEN"]
        R1["Voorspelbaar & Traceerbaar"]
        R2["Data-soevereiniteit"]
        R3["Beheerste AI-kosten"]
        R4["Sneller zonder tech debt"]
        R5["Defensible moat"]
        R6["Geen achterblijver"]
    end
    
    VISION --> BRAND
    BRAND --> PROBLEMS
    PROBLEMS --> SOLUTIONS
    SOLUTIONS --> RESULTS
    
    style VISION fill:#ffffff,stroke:#e55039,stroke-width:3px
    style BRAND fill:#e55039,stroke:#c0392b,stroke-width:3px,color:#ffffff
    style PROBLEMS fill:#ecf0f1,stroke:#34495e
    style SOLUTIONS fill:#ffffff,stroke:#e55039,stroke-width:2px
    style RESULTS fill:#e55039,stroke:#c0392b,color:#ffffff
```

---

## Simpele basis diagram (uitgebreid)

```mermaid
graph TD
    %% Styling
    classDef kernStyle fill:#ffffff,stroke:#e55039,stroke-width:4px,color:#000000,font-weight:bold
    classDef brandStyle fill:#e55039,stroke:#c0392b,stroke-width:3px,color:#ffffff,font-weight:bold
    classDef headerStyle fill:#34495e,stroke:#2c3e50,stroke-width:2px,color:#ffffff
    classDef problemStyle fill:#ecf0f1,stroke:#34495e,stroke-width:1px,color:#000000
    classDef solutionStyle fill:#ffffff,stroke:#e55039,stroke-width:2px,color:#000000
    classDef resultStyle fill:#e55039,stroke:#c0392b,stroke-width:2px,color:#ffffff
    
    %% Kern
    KERN["In 2030 wordt de meeste<br/>software met Agentic AI gemaakt"]
    
    %% Brand
    BRAND["MANDARYN<br/>Governance-Native Agent Ecosysteem"]
    
    %% Headers
    PROB_H["5 PROBLEMEN"]
    SOL_H["6 OPLOSSINGEN"]
    RES_H["6 RESULTATEN"]
    
    %% Problemen
    P1["1. Wie is aanspreekbaar?<br/><small>Geen escalatiepad, eigenaarschap, audit basis</small>"]
    P2["2. Kwaliteit & Compliance?<br/><small>Dynamisch gedrag vs statische governance</small>"]
    P3["3. Zijn kosten houdbaar?<br/><small>Van pilot naar 1000 agents = OPEX-explosie?</small>"]
    P4["4. Grip op ROI?<br/><small>Welke waarde per euro AI-investering?</small>"]
    P5["5. Wat met mijn data?<br/><small>Privacy-compliance + RAG = haalbaar?</small>"]
    
    %% Oplossingen
    S1["1. Governance-Native<br/><small>Constitutie + contracten in systeem-DNA</small>"]
    S2["2. AI waar waardevol<br/><small>Deterministisch waar mogelijk</small>"]
    S3["3. 60 jaar architectuur<br/><small>2x30 jaar ervaring complexe systemen</small>"]
    S4["4. Traceability by design<br/><small>Volledige audit trail ingebouwd</small>"]
    S5["5. Practice-first: TLX<br/><small>2 jaar bewijs vóór commercie</small>"]
    S6["6. Data-centrisch<br/><small>On-premise + open standaarden</small>"]
    
    %% Resultaten
    R1["1. Voorspelbaar & Traceerbaar<br/><small>Van intentie tot deployment herleidbaar</small>"]
    R2["2. Data-soevereiniteit<br/><small>RAG zonder data-lekkage, AVG-compliant</small>"]
    R3["3. Beheerste AI-kosten<br/><small>Transparant kostenmodel, geen OPEX-verrassingen</small>"]
    R4["4. Sneller zonder tech debt<br/><small>Governance als accelerator</small>"]
    R5["5. Defensible moat<br/><small>2+ jaar architectuur-voorsprong</small>"]
    R6["6. Geen achterblijver<br/><small>Early mover governance-native AI</small>"]
    
    %% Verbindingen
    KERN --> BRAND
    BRAND --> PROB_H
    BRAND --> SOL_H
    BRAND --> RES_H
    
    PROB_H --> P1
    PROB_H --> P2
    PROB_H --> P3
    PROB_H --> P4
    PROB_H --> P5
    
    SOL_H --> S1
    SOL_H --> S2
    SOL_H --> S3
    SOL_H --> S4
    SOL_H --> S5
    SOL_H --> S6
    
    RES_H --> R1
    RES_H --> R2
    RES_H --> R3
    RES_H --> R4
    RES_H --> R5
    RES_H --> R6
    
    %% Apply Styles
    class KERN kernStyle
    class BRAND brandStyle
    class PROB_H,SOL_H,RES_H headerStyle
    class P1,P2,P3,P4,P5 problemStyle
    class S1,S2,S3,S4,S5,S6 solutionStyle
    class R1,R2,R3,R4,R5,R6 resultStyle
```

## Compacte versie (zonder details)

```mermaid
graph TD
    %% Styling
    classDef kernStyle fill:#ffffff,stroke:#e55039,stroke-width:4px,color:#000000,font-weight:bold
    classDef brandStyle fill:#e55039,stroke:#c0392b,stroke-width:3px,color:#ffffff,font-weight:bold,font-size:16px
    classDef categoryStyle fill:#34495e,stroke:#2c3e50,stroke-width:2px,color:#ffffff
    
    KERN["2030:<br/>Meeste software met Agentic AI"]
    BRAND["MANDARYN"]
    PROB["5 PROBLEMEN<br/><small>Aanspreekbaarheid • Compliance<br/>Kosten • ROI • Data</small>"]
    SOL["6 OPLOSSINGEN<br/><small>Governance-Native • Traceability<br/>60yr Architectuur • Practice-First</small>"]
    RES["6 RESULTATEN<br/><small>Voorspelbaar • Data-soeverein<br/>Beheerste kosten • Defensible moat</small>"]
    
    KERN --> BRAND
    BRAND --> PROB
    BRAND --> SOL
    BRAND --> RES
    
    class KERN kernStyle
    class BRAND brandStyle
    class PROB,SOL,RES categoryStyle
```

---

## Hoe te gebruiken

### In MkDocs:
Deze diagrammen worden automatisch gerenderd in de MkDocs site dankzij de Mermaid extensie.

### Export als PNG/SVG:
1. Ga naar https://mermaid.live
2. Kopieer één van de Mermaid code blocks
3. Download als PNG/SVG voor gebruik in PowerPoint of andere presentaties

### In VS Code:
1. Open dit bestand in VS Code
2. Druk op Ctrl+Shift+V voor preview
3. De Mermaid diagrammen worden automatisch gerenderd

---

## Welke versie gebruiken?

- **Mandaryn Ecosystem**: Meest gedetailleerd, alle 5+6+6 punten zichtbaar
- **Layered flowchart**: Cleaner, overzichtelijke groepering
- **Simpele basis (uitgebreid)**: Beste balans tussen detail en leesbaarheid
- **Compacte versie**: Voor quick overview of executive summary

Kies de versie die het beste past bij jouw presentatie-context!

# Behoefteprofiel: TLX hosting en technisch applicatiebeheer

## 1. Doel en scope

Dit behoefteprofiel legt de functionele en niet-functionele behoeften vast voor hosting en technisch applicatiebeheer van TLX.

Het profiel dient als objectieve basis voor latere leveranciersselectie. Het selectiedoel in deze opdracht is: beoordelen of BaseTide voor zijn prijs de juiste partij is.

## 2. Context

hosting van TLX een transportsysteem met 30 gebruikers. Alleen ondersteuning tijdens kantooruren. Chauffeurs die geen toegang hebben moeten snel worden geholpen.

De leverancier moet hosting en technisch applicatiebeheer als samenhangende dienst kunnen uitvoeren, met nadruk op operationele continuiteit en snelle ondersteuning bij toegangsproblemen.

## 3. Functionele behoeften

- **F-01**: Hosting Entoli-run: draai de productie-omgeving van Entoli-run inclusief alle benodigde middleware en databases.
- **F-02**: Private GitLab-omgeving: lever en beheer een geisoleerde GitLab-instantie (CI/CD, container registry, artefact-opslag).
- **F-03**: Release-uitvoering: provider voert alle software-releases en patches uit volgens afgesproken vensters en rollback-procedures.
- **F-04**: Backup & Recovery: verzorg dagelijkse back-ups van alle workloads (Entoli-run, GitLab, databases) en hersteltests.
- **F-05**: Certificaten-beheer: aanvragen, vernieuwen en uitrollen van TLS-certificaten (inclusief private GitLab).
- **F-06**: Incident & Change-management: registreer, prioriteer en behandel tickets; wijzigingen via gestandaardiseerd CAB-proces.
- **F-07**: Consultancy-uur: minimaal 1 uur per maand expertadvies over performance-optimalisatie of architectuurvragen.
- **F-08**: Kantooruren-support: eerste- en tweedelijns ondersteuning op werkdagen 08:00-18:00 CET via telefoon en portal.
- **F-09**: Mobiele app-ondersteuning: garandeer bereikbaarheid van de chauffeur-app voor 15 chauffeurs (Android + iOS).
- **F-10**: Self-service rapportage: maandelijkse SLA-rapportages (uptime, incidenten, changes, consultancy-gebruik).

## 4. Niet-functionele eisen

### Capaciteit & Schaalbaarheid

- N-01: minimaal 20 gelijktijdige gebruikers (15 chauffeurs + 5 staff) met groeipad 2x binnen 3 jaar.
- N-02: verticale of horizontale schaal zonder downtime.

### Beschikbaarheid

- N-03: minimaal 99,5% maandelijkse uptime voor Entoli-run.
- N-04: geplande maintenance maximaal 2 uur per maand, aangekondigd minimaal 5 dagen vooraf.

### Backup & DR

- N-05: dagelijkse back-up, retentie 30 dagen.
- N-06: RPO maximaal 24 uur, RTO maximaal 4 uur.
- N-07: kwartaal-restore-test met rapportage.

### Performance

- N-08: p95 API-respons maximaal 500 ms (intra-EU).
- N-09: Git clone/push bandbreedte minimaal 50 Mbit/s.

### Beveiliging

- N-10: data-in-transit TLS 1.3, data-at-rest AES-256.
- N-11: ISO 27001-aligned maatregelen; jaarlijkse pen-test.
- N-12: role-based access control, MFA verplicht voor admins.

### Compliance

- N-13: verwerkersovereenkomst volgens GDPR.
- N-14: logging & auditing met 12 maanden bewaartermijn.

### Onderhoudbaarheid

- N-15: CI/CD pipelines (GitLab) volledig geautomatiseerd.
- N-16: IaC-definities toegankelijk voor klantreview.

### Service & Support

- N-17: response SLA: P1 maximaal 30 minuten, P2 maximaal 2 uur tijdens kantooruren.
- N-18: dedicated service-manager, kwartaalservice-review.

### Documentatie

- N-19: actuele runbook, architectuurschema's en contactmatrix.
- N-20: wijzigingslog van releases en configuraties.

## 5. Randvoorwaarden

- Ondersteuning is minimaal nodig tijdens kantooruren.
- Chauffeurs die geen toegang hebben, moeten snel worden geholpen.
- Private GitLab en technisch applicatiebeheer vallen binnen de gevraagde dienstverlening.
- Het profiel is bedoeld voor leveranciersvergelijking en niet voor contractuele eindredactie.

## 6. Afbakening

- Geen leveranciersbeoordeling, rangorde of keuze.
- Geen contractonderhandeling of prijsbeoordeling.
- Geen implementatie- of migratieplan.
- Geen operationele inrichting buiten de vastgelegde behoeften.

## 7. Herkomstverantwoording

### Gebruikte bronnen

- `temp/hosting/FenNF.md`

### Operationele context

- hosting van TLX een transportsysteem met 30 gebruikers. Alleen ondersteuning tijdens kantooruren. Chauffeurs die geen toegang hebben moeten snel worden geholpen.

### Expliciete aannames

- De operationele context met 30 gebruikers is leidend voor de huidige behoeftebepaling en scherpt de eerdere referentie van 20 gelijktijdige gebruikers aan.
- Het selectiedoel noemt BaseTide als latere beoordelingscontext, maar dit document bevat geen leveranciersoordeel.

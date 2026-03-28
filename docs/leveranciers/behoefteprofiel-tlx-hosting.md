# Behoefteprofiel: TLX hosting en technisch applicatiebeheer

## 1. Doel en scope

Dit behoefteprofiel legt de functionele en niet-functionele behoeften vast voor hosting en technisch applicatiebeheer van TLX, een transportsysteem met 30 gebruikers.

Het profiel is bedoeld als objectieve basis voor latere leveranciersselectie, in het bijzonder om te beoordelen of BaseTide, gegeven prijs en dienstverlening, passend is voor deze behoefte.

De scope omvat:

- hosting van de productie-omgeving van het TLX-platform
- technisch applicatiebeheer op productiecomponenten en ondersteunende systemen
- beheer van private GitLab-voorzieningen voor CI/CD en artefacten
- back-up, herstel, certificaten, releases, incidenten en wijzigingsbeheer
- ondersteuning tijdens kantooruren met nadruk op snelle hulp bij toegangsproblemen voor chauffeurs

## 2. Context

TLX is een transportsysteem waarin chauffeurs en ondersteunende medewerkers dagelijks afhankelijk zijn van continue beschikbaarheid van applicatie en beheerketen.

De operationele context voor dit profiel is:

- totaal circa 30 gebruikers
- ondersteuning alleen tijdens kantooruren
- chauffeurs die geen toegang hebben, moeten snel worden geholpen
- mobiele bereikbaarheid voor chauffeurs blijft bedrijfskritisch

De leverancier moet daarom niet alleen infrastructuur leveren, maar ook aantoonbaar in staat zijn om hosting en technisch applicatiebeheer als samenhangende dienst uit te voeren.

## 3. Functionele behoeften

### 3.1 Hosting en platformdiensten

- Hosting van de productie-omgeving van Entoli-run, inclusief alle benodigde middleware en databases.
- Levering en beheer van een geisoleerde private GitLab-instantie, inclusief CI/CD, container registry en artefact-opslag.
- Ondersteuning van de mobiele chauffeur-app op Android en iOS, met nadruk op bereikbaarheid en continu gebruik.

### 3.2 Beheer en wijziging

- Uitvoering van software-releases en patches binnen afgesproken onderhoudsvensters.
- Aanwezigheid van rollback-procedures bij releases en wijzigingen.
- Registratie, prioritering en afhandeling van incidenten via een gestandaardiseerd incidentproces.
- Afhandeling van wijzigingen via een gestructureerd change- of CAB-proces.

### 3.3 Continuiteit en beveiliging

- Dagelijkse back-ups van alle relevante workloads, inclusief applicatie, GitLab en databases.
- Uitvoering van hersteltests om de bruikbaarheid van back-ups aantoonbaar te maken.
- Beheer van TLS-certificaten, inclusief aanvraag, vernieuwing en uitrol.

### 3.4 Rapportage en ondersteuning

- Maandelijkse SLA-rapportage met ten minste uptime, incidenten, changes en gebruik van consultancy.
- Eerste- en tweedelijns ondersteuning op werkdagen tussen 08:00 en 18:00 CET via telefoon en portal.
- Minimaal 1 uur per maand consultancy voor performance-optimalisatie of architectuurvragen.

## 4. Niet-functionele eisen

### 4.1 Capaciteit en schaalbaarheid

- De oplossing moet minimaal 30 gelijktijdige gebruikers ondersteunen in de huidige context.
- De oplossing moet schaalbaar zijn zonder downtime, verticaal of horizontaal.
- Er moet ruimte zijn voor groei in gebruik zonder fundamentele herinrichting van de dienst.

### 4.2 Beschikbaarheid en onderhoud

- Doelwaarde voor maandelijkse uptime van Entoli-run is minimaal 99,5%.
- Geplande maintenance bedraagt maximaal 2 uur per maand.
- Geplande maintenance wordt minimaal 5 dagen vooraf aangekondigd.
- Onderhoudsvensters mogen de operationele inzet van chauffeurs niet onnodig verstoren.

### 4.3 Back-up en disaster recovery

- Dagelijkse back-up met een retentie van 30 dagen.
- RPO maximaal 24 uur.
- RTO maximaal 4 uur.
- Minimaal eenmaal per kwartaal een restore-test met rapportage.

### 4.4 Performance

- p95 API-respons binnen intra-EU gebruik maximaal 500 ms.
- Git clone- en push-bandbreedte minimaal 50 Mbit/s.
- De gebruikerservaring voor chauffeurs en kantoorfuncties moet stabiel blijven bij normaal gelijktijdig gebruik.

### 4.5 Beveiliging en toegang

- Data in transit via TLS 1.3.
- Data at rest via AES-256 of aantoonbaar gelijkwaardig beschermingsniveau.
- ISO 27001-aligned maatregelen.
- Jaarlijkse penetratietest of aantoonbaar vergelijkbare beveiligingscontrole.
- Role-based access control.
- MFA verplicht voor beheerders.

### 4.6 Compliance en logging

- Verwerkersovereenkomst conform GDPR.
- Logging en auditing met een bewaartermijn van 12 maanden.
- Logging moet geschikt zijn voor incidentanalyse en beheercontrole.

### 4.7 Onderhoudbaarheid en overdraagbaarheid

- GitLab CI/CD pipelines volledig geautomatiseerd.
- IaC-definities beschikbaar voor klantreview.
- Actuele runbooks, architectuurschema's en contactmatrix beschikbaar.
- Wijzigingslog van releases en configuraties aantoonbaar bijgehouden.

### 4.8 Service en support

- Response SLA tijdens kantooruren: P1 maximaal 30 minuten, P2 maximaal 2 uur.
- Dedicated service-manager beschikbaar.
- Kwartaalservice-review ingericht.
- Toegangsproblemen voor chauffeurs worden behandeld als tijdkritisch operationeel issue.

## 5. Randvoorwaarden en afhankelijkheden

- Leverancier moet hosting en technisch applicatiebeheer als samenhangende dienst kunnen leveren.
- Ondersteuning buiten kantooruren is geen eis in dit profiel, maar verstoringen met impact op chauffeurs binnen kantooruren moeten snel worden opgepakt.
- Private GitLab is onderdeel van de gevraagde dienstverlening en geen losse nevenvoorziening.
- De oplossing moet toepasbaar zijn binnen een Europese context, gezien eisen rond performance, privacy en gegevensverwerking.
- Behoeften in dit profiel zijn bedoeld voor leveranciersvergelijking en nog niet voor contractuele eindredactie.

## 6. Afbakening

Dit behoefteprofiel doet het volgende niet:

- geen beoordeling van BaseTide of andere leveranciers
- geen prijsvergelijking of rangschikking van aanbiedingen
- geen contractonderhandeling of SLA-eindredactie
- geen technisch implementatieontwerp voor migratie of transitie
- geen operationeel runbook voor interne uitvoering

Dit profiel is uitsluitend een vastlegging van behoeften die later als selectiegrond gebruikt kan worden.

## 7. Herkomstverantwoording

### Gebruikte bronnen

- Bronbestand: `temp/hosting/FenNF.md`
- Aanvullende operationele context uit opdracht:
  - TLX is een transportsysteem met 30 gebruikers
  - alleen ondersteuning tijdens kantooruren
  - chauffeurs zonder toegang moeten snel worden geholpen
- Selectiedoel uit opdracht:
  - beoordelen of BaseTide voor zijn prijs de juiste partij is

### Expliciete aannames

- De operationele context met 30 gebruikers vervangt de eerdere minimumreferentie van 20 gelijktijdige gebruikers uit het bronbestand voor de huidige behoeftebepaling.
- De in het bronbestand genoemde mobiele app-ondersteuning voor 15 chauffeurs blijft relevant, maar valt binnen een bredere gebruikscontext van 30 totale gebruikers.
- Omdat het selectiedoel expliciet een latere leveranciersbeoordeling noemt, is in dit document alleen de behoefte vastgelegd en geen oordeel over BaseTide opgenomen.

### Kwaliteitscontrole

- Functionele behoeften expliciet vastgelegd
- Niet-functionele eisen expliciet vastgelegd
- Randvoorwaarden en afbakening benoemd
- Herleidbaarheid naar bron en aanvullende context aanwezig
- Geen leveranciersoordeel opgenomen
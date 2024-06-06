En liten guide til deg som skal se på koden

Dette prosjektet er et enkelt system for håndtering av banktransaksjoner, inkludert innskudd, uttak, tvister, løsninger på tvister, og tilbakebetalinger

- **Innskudd (Deposit)**: Legger til midler på kundens konto.
- **Uttak (Withdraw)**: Tar ut midler fra kundens konto, hvis det er nok tilgjengelige midler.
- **Tvist (Dispute)**: Reserverer midler som er under tvist.
- **Løsning (Resolve)**: Flytter midler fra reservert tilbake til tilgjengelig saldo etter at en tvist er løst.
- **Tilbakebetaling (Chargeback)**: Fjerner midler som var under tvist og fryser kundens konto.

Installasjon

1. Klon repoet

2. I dag ligger det en input.csv fil med litt data som du kan bruke, eller så akn du oppdatere den

3. Kjør python readTransactions.py input.csv

4. Se resultatene i output.csv filen

Tester

- Testene ligger i filen output.csv

1.  Kjør python -m unittest test_bank.py

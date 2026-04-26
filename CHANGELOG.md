# Changelog

## v0.2.2 — 2026-04-27
- Salvare în Cloud: Devizele sunt acum salvate automat în Google Sheets, eliminând riscul pierderii datelor din browser.
- Arhivă & Recuperare: Adăugată funcția „Load” care permite reîncărcarea oricărui deviz salvat anterior folosind numărul de înmatriculare.
- PWA (App Mode): Site-ul poate fi instalat acum ca o aplicație nativă pe telefon, oferind un spațiu de lucru mai mare și acces rapid.

## v0.2.1 — 2026-04-24
### Update: Optimizare mobil (public)
- HUB, COnsumabile, Telefoane clienti optimizate mobil
- Corectat erori

## v0.2.0 — 2026-04-22
### Release: Telefoane clienti (public)
- Pagina finalizată și stabilizată.
- Publicată în folderul public.
- Include toate optimizările din v0.1.0.

## v0.1.0 — 2026-04-19
### Release: Stoc Consumabile (public)
- Pagina finalizată și stabilizată.
- Publicată în folderul public.
- Include toate optimizările din v0.0.9.

# v0.0.9 — Flota Auto (API + Listă Mașini)
**Data:** 14.04.2026  
**Tip:** Feature Release + API Integration

## 🚀 Funcționalități noi
- Implementare **API Flota Auto** (Google Apps Script Web App).
- Adăugat **doGet()** pentru citirea tuturor mașinilor în format JSON.
- Adăugat **doPost()** pentru adăugare și modificare mașini.
- Structură JSON completă: nr, VIN, marcă, RCA, ITP, Rovinietă, link acte, observații, rowIndex.
- Creare **Web App nou (deployment v2)** cu acces „Anyone”.
- Integrare completă HUB → API prin `fetch()`.

## 🧩 Pagini noi / actualizate
### `lista_auto.html` (nou)
- Pagina principală a modulului Flota Auto.
- Header premium „Flota Auto”.
- Afișare carduri pentru fiecare mașină.
- VIN afișat sub număr (copy‑friendly).
- Culori dinamice pentru expirări (verde / galben / roșu).
- Butoane:
  - **✏️ Modifică**
  - **📁 Acte**
- Sortare logică: expirate → aproape expirate → restul.

### Structură folder simplificată
- `lista_auto.html`
- `adauga.html`
- `modifica.html` (în pregătire)

## 🛠️ Optimizări & Fix-uri
- Eliminat pagini inutile din modulul Flota Auto.
- Corectat deploy-ul Web App (versiune veche fără `doGet()`).
- Mutat scriptul în proiectul corect (`verificaExpirari`).
- Rezolvat eroarea „Script function not found: doGet”.
- Stabilizat fluxul API (GET + POST).
- Confirmat funcționarea JSON în browser.

## 🎨 UI/UX
- Carduri premium, aerisite, optimizate pentru mobil și PC.
- VIN vizibil și ușor de copiat.
- Culori intuitive pentru expirări.
- Layout consistent cu restul HUB-ului.

## 📁 Fișiere modificate
- `modules/flota/lista_auto.html` (nou)
- `modules/flota/adauga.html` (actualizat pentru API)
- `modules/flota/modifica.html` (urmează)
- `Cod.gs` (Google Apps Script):
  - `doGet()` — nou
  - `doPost()` — actualizat
  - `verificaExpirari()` — nemodificat

## 🧭 Ce urmează în v0.1.0
- Pagina `modifica.html` cu preluare automată a datelor.
- Căutare rapidă în lista de mașini.
- Filtru după expirări.
- Sortare manuală.
- Export PDF pentru fișa unei mașini (opțional).

## v0.0.8 — 13 April 2026
### Adăugat
- manifest.json cu nume aplicație, iconițe și setări pentru instalare pe Android/iPhone/PC
- service worker (sw.js) pentru cache și actualizare automată
- suport complet pentru instalarea HUB-ului ca aplicație (PWA)

### Modificat
- index.html actualizat cu referințe la manifest și înregistrarea service worker-ului

### Observații
- aplicația se actualizează automat la fiecare deschidere
- pregătit pentru instalare pe toate platformele


## v0.0.7 — 13 April 2026
### Adăugat
- Footer premium cu blur, shadow și accent mov
- Linie mov subtilă (glass edge) pentru un look modern
- Sistem de versiuni afișat în footer

### Improved
- Contrast Light Mode (text vizibil, fundal optimizat)
- theme.js: adăugată clasa `light-mode` pentru funcționare corectă
- Grid-ul din dashboard (aliniere și spacing mai curat)
- Header neon mov (optimizare vizuală)

### Fixed
- Footer care nu se vedea în Light Mode
- Probleme minore de spacing în layout

---

## v0.0.6 — 12 April 2026
#### Adăugat
- Header neon mov
- Iconițe noi pentru carduri
- Optimizări pentru mobile

### Improved
- Layout general și spațiere
- Vizibilitatea elementelor în Dark Mode
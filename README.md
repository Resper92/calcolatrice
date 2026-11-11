# Raccolta Progetti Python (Mini-Games & Utilities)

Una raccolta di script e mini-applicazioni sviluppate in Python, comprendente giochi classici ed utilità grafiche e da riga di comando.

---

## 📁 Struttura del Progetto

- **`calcolatrice.py`**: Calcolatrice con interfaccia grafica (GUI) realizzata tramite la libreria standard `tkinter`. Supporta operazioni aritmetiche (`+`, `-`, `*`, `/`, `%`), gestione delle parentesi e calcolo dinamico.
- **`tetris.py`**: Il classico gioco del Tetris sviluppato con `pygame`. Presenta tutti i tetramini ufficiali, colori distinti, rotazione dei blocchi, rilevamento collisioni, sidebar informativa e calcolo del punteggio.
- **`tris.py`**: Gioco del Tris (Tic-Tac-Toe) per 2 giocatori su terminale, con input delle coordinate per posizionare `X` e `O`.
- **`idor.py`**: Semplice script per la conversione rapida di emoticon testuali (come `:)` e `:(`) nelle rispettive emoji grafiche (`🙂`, `🙁`).

---

## 🚀 Requisiti e Installazione

### 1. Prerequisiti
- **Python 3.8+** installato sul proprio computer.

### 2. Creazione dell'ambiente virtuale (consigliato)
Apri un terminale nella cartella del progetto:

```bash
# Su Windows
python -m venv .venv
.\.venv\Scripts\activate

# Su Linux/macOS
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Installazione delle dipendenze
Installa le librerie richieste (in particolare per Tetris):

```bash
pip install -r requirements.txt
```

---

## 🎮 Come Avviare gli Script

### Calcolatrice GUI
```bash
python calcolatrice.py
```

### Tetris
```bash
python tetris.py
```
**Comandi di gioco**:
- Freccia Sinistra / Destra: Sposta il blocco
- Freccia Su: Ruota il blocco
- Freccia Giù: Accelera la caduta
- Barra Spaziatrice: Hard drop (caduta immediata)

### Tris
```bash
python tris.py
```
Inserisci le coordinate `x` (colonna da 0 a 2) e `y` (riga da 0 a 2) a turno.

### Convertitore Emoticon
```bash
python idor.py
```

---

## 📦 Pubblicazione su GitHub

Se stai caricando questo progetto su una nuova repository GitHub, segui questi passaggi:

1. Crea una nuova repository vuota su [GitHub](https://github.com/new) (es. `python-mini-projects` o `calcolatrice`).
2. Collega la repository remota ed effettua il push:
   ```bash
   git remote add origin https://github.com/<TUO-USERNAME>/<NOME-REPO>.git
   git branch -M main
   git push -u origin main
   ```


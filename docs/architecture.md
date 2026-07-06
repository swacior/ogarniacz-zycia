# Architektura projektu

## Cel

Ogarniacz Życia będzie inteligentnym asystentem AI pomagającym użytkownikowi planować życie, podejmować decyzje i zarządzać codziennymi obowiązkami.

## Główne elementy systemu

### 1. Interfejs użytkownika (UI)

Odpowiada za komunikację z użytkownikiem.

Przykłady:
- ekran dnia,
- kalendarz,
- zadania,
- ustawienia,
- rozmowa z AI.

Technologia:
- Kivy

---

### 2. Baza danych

Przechowuje dane użytkownika.

Przykłady:
- zadania,
- wydarzenia,
- cele,
- preferencje,
- historia decyzji.

Technologia:
- SQLite

---

### 3. Model użytkownika

System przechowujący informacje o użytkowniku.

Uwzględnia:
- zainteresowania,
- cele,
- zwyczaje,
- preferencje,
- relacje,
- sposób działania.

---

### 4. Planner

Odpowiada za tworzenie i zarządzanie planami.

Zakres:
- plan dnia,
- plan tygodnia,
- plan miesiąca,
- cele długoterminowe,
- priorytety.

Planner współpracuje z Life Engine, który analizuje kontekst i proponuje najlepsze rozwiązania.

---

### 4. Life Engine

Główny silnik planowania.

Odpowiada za:
- analizę zadań,
- tworzenie planów,
- zmianę harmonogramu,
- wykrywanie konfliktów.

---

### 5. AI Assistant

Warstwa sztucznej inteligencji.

Odpowiada za:
- analizę kontekstu,
- rozmowę z użytkownikiem,
- sugestie,
- pomoc w decyzjach.

---

### 6. Integracje

Połączenia z zewnętrznymi usługami.

Przykłady:
- pogoda,
- kalendarz,
- rozpoznawanie głosu.

---

## Ogólny przepływ danych

Użytkownik

↓

Interfejs aplikacji

↓

Life Engine

↓

Analiza danych

↓

AI Assistant

↓

Sugestia dla użytkownika
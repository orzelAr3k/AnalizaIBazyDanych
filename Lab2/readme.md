# Lab 2 - TIER protocol i tidy data

## Instalacja

Użyj menedżera pakietów [pip](https://pip.pypa.io/en/stable/).

Ustawienie środowiska.
```
conda env create -f environment.yml
```
lub
```
pip install -r requirements.txt
```


Aktywacja środowiska:

Window: ```
        conda activate TIER```

Linux, MacOS: ```
                source activate TIER```


## Opis danych
Dzienne dane pogodowe z Global Historical Climatology Network dla jednej stacji pogodowej (MX17004) w Meksyku przez pięć miesięcy w 2010 roku. Posiada zmienne w poszczególnych kolumnach (id, rok, miesiąc), rozłożone na kolumny (dzień, d1 – d31) i w poprzek rzędy (tmin, tmax) (temperatura minimalna i maksymalna. Miesiące z mniej niż 31 dni mają strukturalne brakujące wartości dla ostatniego dnia (dni) miesiąca. Kolumna element nie jest zmienną; przechowuje nazwy zmiennych.

*Orginalne dane weather.txt dostępne w folderze /OriginalData. W celu oparacji na danych dokonano skopjowania pliku do folderu /AnalysisData.*

*Skrypt wykonywany na danych dostępny w folderze /CommandFiles/Lab2.ipynb, wraz z komentarzami w kodzie.*

## Etap operacji na danych
1. Dane zostały poddane oczyszczeniu i uporządkowaniu poprzez zastosowanie wyrażeń regularnych
```
weather = re.sub(r"[OSD]|I(?![A-Z])", "", weather)
# usunięcie spacji
weather = re.sub(r" +", " ", weather)
# usunięcie połączonych napisów z danymi
weather = re.sub(r"(?<=[A-Z])\-", " -", weather)
```
2. Utworzono odpowiedni obiekt *DataFrame* oraz sformatowano tabelę
3. Znormalizowano danę poprzez podzielenie wartości tabeli przez 10
```
weather.iloc[:, 4:].div(10, axis=1)
```
4. Usunięto błędę dane 
5. Przegrupowano dane za pomocą funkcji *melt()*
6. Utworzony wykresy zależności temperatur


**Dane po analizie dostępne:**
- 'Name' - string, [nazwa urządzenia ]
- 'Year' - string, [rok, w którym został dokonany pomiar]
- 'Month' - string, [miesiąc, w którym został dokonany pomiar]
- 'Element' - string, [rodzaj pomiaru]
- 'd1' ... 'd31' - float, [pomiar wiekości mierzonej (zakres 0 - 100)]



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

**Dane po analizie dostępne:**
** 'Name' - string, [nazwa urządzenia ]
** 'Year' - string, [rok, w którym został dokonany pomiar]
** 'Month' - string, [miesiąc, w którym został dokonany pomiar]
** 'Element' - string, [rodzaj pomiaru]
** 'd1' ... 'd31' - float, [pomiar wiekości mierzonej (zakres 0 - 100)]



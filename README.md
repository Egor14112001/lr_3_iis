# Описание проекта
Проект посвящен решеню задачи предсказания цен на машины
https://www.kaggle.com/datasets/vijayaadithyanvg/car-price-predictionused-cars?resource=download

# Запуск
Для запуска проекта необходимо выполнить команды:
```
git clone https://github.com/Egor14112001/IIS_Lr_1
cd IIS_Lr_1
установка окружения - python -m venv .venv_proj
активация окружения - .venv_proj/scripts/Activate
установка зависимостей - pip install -r requirements.txt
```

# Исследование данных
В ходе исследования были проведены действия:
 * Очистка данных не производилась, так как после проверки все данные оказались валидын
 * Был создан новый признак - 'Driven_run' - уровень пробега автомобиля
 * Для столбцов 'Driven_kms', 'Year' изменен тип данных на int32
Закономерности, выявлены по графикам, которые могут быть полезны в дальнейшем для решния задачи:
 * В основном машины меньшего года выпуска стоят дешевле.
 * Дизельные автомобили стоят в основном дороже, что соответсвует правде.
 * Были продемонстрированы более дорогие модели машин.
 * Был сделан вывод, что машины с салона стоят дороже, чем с рук.
 * Стоимосить машины больше всего коррелирует с годом выпуска.

Обработанная выборка сохранена в файл `./data/clean_data.pkl`

# Запуск MLFlow
* Перейти в директорию mlflow
```
cd mlflow
```
* Выполинть в терминале следующую команду
```
source start_mlflow.sh
```
Или выполнить команду
```
mlflow server --backend-store-uri sqlite:///mlruns.db
```
После чего можно проверить, что фреймворк успешно запустился, пройдя в браузере на http://localhost:5000/
# Результаты исследования
Лучший результат показала модель на основе fe_sklearn:
Метрики полученные при обучении модели следующие:
* mae: 0.16
* mape: 0.05
* mse: 0.08
Параметры модели:
* depth: 8
* max_features: 0.5052449805697352
* n_estimators': 3
RunID финальной модели: 76998f40b5ac47809ed494edf6f68dda
### Описание разработанного сервиса
Этот сервис предоставляет API для выполнения предсказаний с использованием модели машинного обучения. Модель была обучена ранее, сохранена через MLflow, и интегрирована в данный сервис.

**Основные файлы:**
- api_handler.py включает в себя функции, необходимые для работы модели в FastAPI (загрузка, обработка и т.п.)
- Dockerfile включает в себя необходимые команды для сборки контейнера с определёнными параметрами
- main.py содержит основные функции для создания предсказаний
- requirements.txt содержит необходимые для работы сервиса библиотеки
- файл get_model.py берёт необходимую модель из mlflow и записывает её в формат pickle
- model.pkl содержит модель, полученную в предыдушем пункте

  
### Команды для создания Docker-образа
Сборка образа выполняется с помощью команды:
```
docker build . --tag lr_3_model:0
```

### Команда для запуска контейнера
Для запуска контейнера с пробросом порта и подключением модели выполните следующую команду:
```
docker run -p 8001:8000 -v $(pwd)/../models:/models lr_3_model:0
```
### Проверка работоспособности сервиса
1. Перейдите на страницу документации FastAPI по адресу:
   [http://localhost:8001/docs](http://localhost:8001/docs)

2. Выполните запрос к эндпоинту `/api/prediction`:
   **Пример тела запроса**:
```  
{"Car_Name":"ritz",
"Year":2014,
"Present_Price":5.59,
"Driven_kms":27000,
"Fuel_Type":"Petrol",
"Selling_type":"Dealer",
"Transmission":"Manual",
"Owner":0,
"Driven_run":"mid"
}
```

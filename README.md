### Запуск
Необходимо
1. Клонировать репозиторий
   ```sh
   git clone https://github.com/ilyazhokhovets/validation_form.git
   ```
2. Активировать виртуальное окружение

    MacOS и Linux
   ```sh
   cd validation_form/venv
   source bin/activate
   ```

   Windows
   ```sh
   cd validation_form/venv
   .\Scripts\activate
   ```

3. Запустить сервер flask
```sh
cd ..
python app.py
```

4. Запустить скрипт с тестовыми запросами

```sh
node validation_form/script.js
```

### Дополнительно
Чтобы перезаписать базу, надо изменить данные в файле db_fill.py и запустить его

```sh
python db_fill.py
```

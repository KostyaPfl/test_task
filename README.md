# Test_task
## В проекте рализованны тесты из тестового задания на позицию разработчика в тестировании (Программист-тестировщик).
## Список ререализованных проверок:
### <u>Первый сценарий:</u>
1. **test_the_power_is_in_people_block:** Проверка присутствия блока "Сила в людях" на странице https://tensor.ru/
2. **test_open_tenzor_about_page:** Проверка открытия страницы https://tensor.ru/about при нажатии кнопки "Подробнее" в блоке "Сила в людях"
3. **test_photo_size:** Проверка что фотографии в хронологии раздела "Работаем" имеют одинаковый размер
### <u>Второй сценарий:</u>
1. **test_selected_region:** Проверка выбора по умолчанию домашнего региона и наличие списка партнеров
2. **test_changing_region:** Проверка изменения региона и списка партнеров при выборе другого региона
3. **test_url_and_title_changing_region:** Проверка поставления в url и title выбранного региона
### <u>Третий сценарий:</u>
1. **test_file_size_is_equal_to_the_specified:** Проверка соответствия размера скачанного файла с плагином с указанным на сайте

Запуск всех тестов с генерацией отчетов командой: python -m pytest --alluredir allure-results

Просмотреть полученные отчеты командой: allure serve allure-results
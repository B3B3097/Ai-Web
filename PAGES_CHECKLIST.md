# ✅ Чек-лист настройки GitHub Pages

Пройдитесь по всем пунктам для успешной настройки!

---

## 1️⃣ Создание репозитория

- [ ] Перешли на https://github.com/new
- [ ] Название репозитория: `vless-configs`
- [ ] **Visibility: Public** (🔓 публичный)
- [ ] Репозиторий создан

---

## 2️⃣ Включение GitHub Pages

- [ ] Открыли Settings в репозитории
- [ ] Нашли раздел Pages (в левом меню)
- [ ] Выбрали Source: `Deploy from a branch`
- [ ] Branch: `main`
- [ ] Folder: `/ (root)`
- [ ] Нажали Save
- [ ] Подождали 1-2 минуты

**Ваш URL:** `https://ВАШ_USERNAME.github.io/vless-configs/`

---

## 3️⃣ Создание GitHub Token

- [ ] Перешли на https://github.com/settings/tokens
- [ ] Нажали "Generate new token (classic)"
- [ ] Note: `vless-bot`
- [ ] Expiration: `No expiration`
- [ ] ✅ Отметили scope `repo`
- [ ] Нажали "Generate token"
- [ ] **СКОПИРОВАЛИ ТОКЕН** (начинается с `ghp_`)

---

## 4️⃣ Получение Telegram Bot Token

- [ ] Открыли @BotFather в Telegram
- [ ] Отправили `/newbot`
- [ ] Придумали имя бота
- [ ] Придумали username бота (должен заканчиваться на `bot`)
- [ ] **СКОПИРОВАЛИ ТОКЕН** (формат: `123456:ABC-DEF...`)

---

## 5️⃣ Настройка .env файла

- [ ] Открыли файл `/workspace/.env`
- [ ] Заменили `BOT_TOKEN` на свой из @BotFather
- [ ] Заменили `GITHUB_TOKEN` на свой (начинается с `ghp_`)
- [ ] Заменили `CONFIG_REPO` на `ВАШ_USERNAME/vless-configs`
- [ ] Заменили `PAGES_REPO` на `ВАШ_USERNAME/vless-configs` (**такой же!**)
- [ ] Указали свой `VLESS_ADDRESS`
- [ ] Указали свой `VLESS_SNI`
- [ ] Сохранили файл

---

## 6️⃣ Первый запуск бота

- [ ] Перешли в `/workspace`
- [ ] Запустили: `python bot/main.py`
- [ ] Бот запустился без ошибок
- [ ] В Telegram отправили `/start`
- [ ] Появились кнопки "🔑 Get Proxy" и "🔄 Update"

---

## 7️⃣ Генерация первого конфига

- [ ] Нажали кнопку "🔑 Get Proxy"
- [ ] Бот ответил конфигом
- [ ] Проверили репозиторий на GitHub:
  - [ ] Появилась папка `configs/`
  - [ ] Внутри файл `Weleredz_YYYYMMDD_HHMMSS.txt`
  - [ ] Появился файл `index.html` в корне

---

## 8️⃣ Проверка GitHub Pages

- [ ] Открыли в браузере: `https://ВАШ_USERNAME.github.io/vless-configs/`
- [ ] Видите таблицу с конфигом
- [ ] Кнопка Download работает
- [ ] Конфиг скачивается

---

## 🎉 Всё готово!

Если все пункты отмечены - поздравляем! 🎊

Ваш бот полностью настроен и готов к работе!

---

## ❌ Если что-то не работает

### Проблема: Страница 404
**Решение:** Подождите ещё 2-3 минуты, GitHub Pages активируется не сразу

### Проблема: Ошибка "Bad credentials"
**Решение:** Пересоздайте GITHUB_TOKEN с правами `repo`

### Проблема: configs/ не создаётся
**Решение:** Создайте вручную файл `configs/.gitkeep` в репозитории

### Проблема: Бот не отвечает
**Решение:** Проверьте BOT_TOKEN и убедитесь что ваш username @Weleredz

---

**Нужна помощь?** Откройте один из файлов:
- `QUICK_START_PAGES.md` - пошаговая инструкция
- `ENV_SETUP_GUIDE.md` - как заполнить .env
- `GITHUB_PAGES_SETUP.md` - полное руководство

# ⚙️ Настройка .env для GitHub Pages

## 📋 Что нужно заполнить

Откройте файл `.env` и замените значения на свои:

```bash
# Telegram Bot
BOT_TOKEN=1234567890:ABCdefGHIjklMNOpqrsTUVwxyz

# GitHub
GITHUB_TOKEN=ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
CONFIG_REPO=your-username/vless-configs
PAGES_REPO=your-username/vless-configs

# VLESS Server
VLESS_ADDRESS=your-domain.com
VLESS_PORT=443
VLESS_PATH=/vless
VLESS_SNI=your-domain.com
```

---

## 🔑 Где взять каждое значение

### 1. BOT_TOKEN
**Где получить:** Telegram бот @BotFather

**Инструкция:**
1. Откройте @BotFather в Telegram
2. Отправьте `/newbot`
3. Придумайте имя и username для бота
4. Скопируйте полученный токен

**Пример:** `1234567890:ABCdefGHIjklMNOpqrsTUVwxyz`

---

### 2. GITHUB_TOKEN
**Где получить:** https://github.com/settings/tokens

**Инструкция:**
1. Перейдите по ссылке выше
2. Нажмите "Generate new token" → "Generate new token (classic)"
3. Заполните:
   - **Note:** `vless-bot`
   - **Expiration:** `No expiration`
   - **Scopes:** ✅ `repo` (полный доступ)
4. Нажмите "Generate token"
5. **Скопируйте токен!** (больше не увидите)

**Пример:** `ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`

---

### 3. CONFIG_REPO и PAGES_REPO
**Формат:** `ВАШ_USERNAME/НАЗВАНИЕ_РЕПОЗИТОРИЯ`

**Инструкция:**
1. Создайте репозиторий на GitHub: https://github.com/new
2. Название: `vless-configs` (или любое другое)
3. Visibility: **Public** (обязательно!)
4. Скопируйте полное имя: `ваш-username/vless-configs`

**Важно:** Оба параметра должны указывать на **один и тот же** репозиторий!

**Пример:**
```bash
CONFIG_REPO=Weleredz/vless-configs
PAGES_REPO=Weleredz/vless-configs
```

---

### 4. VLESS_ADDRESS и VLESS_SNI
**Что это:** Домен вашего VLESS сервера

**Где взять:** Из вашей панели управления сервером или DNS записей

**Пример:**
```bash
VLESS_ADDRESS=proxy.mydomain.com
VLESS_SNI=proxy.mydomain.com
```

---

### 5. VLESS_PORT
**Что это:** Порт VLESS сервера

**Обычно:** `443` (для HTTPS)

---

### 6. VLESS_PATH
**Что это:** Путь для VLESS подключения

**Обычно:** `/vless` или любой другой

---

## ✅ Проверка перед запуском

Пройдитесь по чек-листу:

- [ ] BOT_TOKEN начинается с цифр и содержит `:`
- [ ] GITHUB_TOKEN начинается с `ghp_`
- [ ] CONFIG_REPO в формате `username/repo`
- [ ] PAGES_REPO = CONFIG_REPO
- [ ] Репозиторий **публичный**
- [ ] GitHub Pages включён в Settings репозитория
- [ ] VLESS_ADDRESS и VLESS_SNI указаны правильно

---

## 🚀 Пример готового .env

```bash
# Telegram Bot
BOT_TOKEN=1234567890:ABCdefGHIjklMNOpqrsTUVwxyz

# GitHub
GITHUB_TOKEN=ghp_AbCdEfGhIjKlMnOpQrStUvWxYz123456
CONFIG_REPO=Weleredz/vless-configs
PAGES_REPO=Weleredz/vless-configs

# VLESS Server
VLESS_ADDRESS=proxy.example.com
VLESS_PORT=443
VLESS_PATH=/vless
VLESS_SNI=proxy.example.com
```

---

## 🆘 Если что-то не работает

### Ошибка: "Bad credentials"
→ Проверьте GITHUB_TOKEN, возможно он истёк или скопирован неправильно

### Ошибка: "Not Found"
→ Проверьте CONFIG_REPO, убедитесь что репозиторий существует

### Ошибка: "Unauthorized"
→ У токена нет прав `repo`, создайте новый с правильными правами

### Страница 404
→ Подождите 2-3 минуты после первого коммита, GitHub Pages активируется не сразу

---

**Готово! Теперь можно запускать бота:**
```bash
python bot/main.py
```

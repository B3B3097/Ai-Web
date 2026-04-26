# 🚀 Быстрая настройка GitHub Pages - ПОШАГОВАЯ ИНСТРУКЦИЯ

## ⏱️ Время настройки: 5-7 минут

---

## ШАГ 1: Создание репозитория (2 мин)

### 1.1 Откройте GitHub
Перейдите на: https://github.com/new

### 1.2 Заполните данные:
```
Repository name: vless-configs
Visibility: 🔓 Public (ОБЯЗАТЕЛЬНО!)
✅ Initialize with README (можно отметить)
```

### 1.3 Нажмите "Create repository"

---

## ШАГ 2: Включение GitHub Pages (2 мин)

### 2.1 Перейдите в Settings
В созданном репозитории нажмите вкладку **Settings**

### 2.2 Найдите раздел Pages
В левом меню прокрутите вниз до раздела **Pages**

### 2.3 Настройте Source:
```
Build and deployment:
  • Source: Deploy from a branch
  • Branch: main → / (root)
```

### 2.4 Нажмите Save

⏳ **Подождите 1-2 минуты** пока GitHub активирует Pages

### 2.5 Запомните ваш URL:
```
https://ВАШ_USERNAME.github.io/vless-configs/
```

---

## ШАГ 3: Создание GitHub Token (2 мин)

### 3.1 Перейдите к токенам
https://github.com/settings/tokens

### 3.2 Нажмите "Generate new token" → "Generate new token (classic)"

### 3.3 Настройте токен:
```
Note: vless-bot-token
Expiration: No expiration (или выберите срок)
Scopes: ✅ repo (полный доступ)
```

### 3.4 Нажмите "Generate token"

### 3.5 СКОПИРУЙТЕ ТОКЕН!
```
ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```
⚠️ **Больше вы его не увидите!**

---

## ШАГ 4: Настройка .env файла (1 мин)

### 4.1 Откройте файл .env в проекте:
```bash
nano /workspace/.env
```

### 4.2 Заполните данными:
```bash
# Telegram Bot (получите у @BotFather)
BOT_TOKEN=1234567890:ABCdefGHIjklMNOpqrsTUVwxyz

# GitHub Token (который создали в Шаге 3)
GITHUB_TOKEN=ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# ВАШ репозиторий (одинаковые значения!)
CONFIG_REPO=ВАШ_USERNAME/vless-configs
PAGES_REPO=ВАШ_USERNAME/vless-configs

# Ваш сервер VLESS
VLESS_ADDRESS=your-domain.com
VLESS_PORT=443
VLESS_PATH=/vless
VLESS_SNI=your-domain.com
```

### 4.3 Сохраните файл (Ctrl+O, Enter, Ctrl+X)

---

## ШАГ 5: Проверка работы (1 мин)

### 5.1 Запустите бота:
```bash
cd /workspace
python bot/main.py
```

### 5.2 В Telegram нажмите /start

### 5.3 Нажмите кнопку "🔑 Get Proxy"

### 5.4 Проверьте результат:

#### ✅ В репозитории должны появиться:
- Папка `configs/`
- Файл `configs/Weleredz_YYYYMMDD_HHMMSS.txt`
- Файл `index.html`

#### ✅ GitHub Pages должен работать:
Откройте в браузере:
```
https://ВАШ_USERNAME.github.io/vless-configs/
```

Вы должны увидеть таблицу с конфигом!

---

## 🔍 Проверочный чек-лист

Пройдитесь по пунктам:

- [ ] Репозиторий создан и **публичный**
- [ ] GitHub Pages включён в Settings
- [ ] Тоken создан с правами **repo**
- [ ] В .env указаны правильные данные
- [ ] CONFIG_REPO = PAGES_REPO (один репозиторий!)
- [ ] Бот запускается без ошибок
- [ ] В репозитории появился `index.html`
- [ ] Страница GitHub Pages открывается

---

## ❌ Частые проблемы и решения

### Проблема 1: Страница 404
**Решение:**
- Подождите 2-3 минуты после первого коммита
- Проверьте, что `index.html` в корне репозитория
- Убедитесь, что Pages включён для ветки `main`

### Проблема 2: Ошибка при загрузке конфига
**Решение:**
- Проверьте токен (должен начинаться с `ghp_`)
- Убедитесь, что у токена есть право `repo`
- Проверьте формат: `USERNAME/repo-name`

### Проблема 3: configs/ не создаётся
**Решение:**
- Бот создаёт автоматически при первой загрузке
- Если нет - создайте вручную файл `configs/.gitkeep`

### Проблема 4: Репозиторий приватный
**Решение:**
- Бесплатный GitHub Pages работает **только с публичными** репозиториями
- Измените visibility на Public в Settings

---

## 📋 Шпаргалка по URL

После настройки ваши конфиги будут доступны по:

| Тип | URL |
|-----|-----|
| Главная страница | `https://username.github.io/vless-configs/` |
| Конкретный конфиг | `https://username.github.io/vless-configs/configs/Weleredz_20240126_123456.txt` |
| Raw-версия | `https://raw.githubusercontent.com/username/vless-configs/main/configs/Weleredz_20240126_123456.txt` |

---

## 🎯 Итоговая архитектура

```
ОДИН репозиторий: username/vless-configs
├── configs/              ← Сюда бот загружает конфиги
│   ├── .gitkeep
│   └── Weleredz_timestamp.txt
├── index.html            ← Бот автоматически обновляет
└── README.md

GitHub Pages: https://username.github.io/vless-configs/
└── Показывает таблицу со всеми конфигами
```

---

## 🆘 Нужна помощь?

Если что-то не работает:
1. Проверьте логи бота в терминале
2. Проверьте вкладку **Actions** в репозитории
3. Убедитесь, что все шаги выполнены по порядку

---

**Удачи в настройке! 🚀**

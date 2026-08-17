# Build Minimal iOS App for App Store Review

Один Codex-скилл для создания минимального portrait-only iPhone-приложения и подготовки его к App Store Review: идея, дизайн, реализация и релизный пакет в одном возобновляемом процессе.

Скилл уменьшает число предсказуемых причин отклонения, но не гарантирует одобрение Apple. Финальное решение принимает App Review, а проверки на физическом iPhone выполняются владельцем приложения вручную.

## Как работает пайплайн

| Этап | Результат | Статус после проверки |
| --- | --- | --- |
| Идея и политика | `AppSpec.md`, `AppPrivacy.yml`, App Review feasibility gate | `policy-approved` |
| Дизайн | Экраны, permission UX, widget, notification UI и иконка | `design-approved` |
| Реализация | Xcode-проект, extensions, AppMetrica, backend и release manifest | `implementation-verified` |
| Релиз | Архив, privacy report, metadata и review notes | `archive-validated`, затем `release-ready` |

Между этапами скилл показывает артефакты, решения и блокеры, затем останавливается. Следующий этап начинается только после нового явного сообщения пользователя, которое утверждает текущий результат и разрешает конкретный следующий этап.

Начальная просьба «сделай всё», молчание, неоднозначная похвала или старое разрешение не считаются аппрувом. При запросе изменений скилл остаётся на текущем этапе и повторно запрашивает подтверждение после обновлённого результата.

Отправка сборки, изменение App Store Connect и отправка на App Review требуют ещё одного отдельного разрешения непосредственно перед внешним действием.

## Обязательный продуктовый brief

Пайплайн рассчитан на UIKit и iOS 15 для основного приложения, iOS 16 для Lock Screen widget, iPhone-only portrait interface и кодовую вёрстку без Storyboard/XIB. Unit- и UI-test targets не создаются; проверка реализации использует сборку, запуск, статическую инспекцию, backend smoke checks и ручной device checklist.

Каждое приложение должно честно и через реальную пользовательскую функцию использовать:

- Bluetooth;
- камеру;
- контакты;
- Face ID;
- геолокацию;
- микрофон;
- чтение Фото;
- добавление в Фото;
- App Tracking Transparency;
- push-уведомления;
- AppMetrica;
- минимальный HTTPS backend;
- Lock Screen widget;
- Notification Service Extension;
- Notification Content Extension.

Если обязательную возможность нельзя органично встроить в продукт, скилл останавливает feasibility gate, а не создаёт декоративный запрос разрешения.

## Установка в Codex

Codex обнаруживает скиллы в `.agents/skills` текущего репозитория и в `$HOME/.agents/skills` пользователя. Символические ссылки позволяют обновлять этот репозиторий без ручного копирования файлов.

### Для одного проекта

В корне проекта выполните:

```bash
mkdir -p .agents/skills
ln -s /absolute/path/to/skills/build-minimal-ios-app-for-app-store-review .agents/skills/build-minimal-ios-app-for-app-store-review
```

### Для всех проектов пользователя

```bash
mkdir -p "$HOME/.agents/skills"
ln -s /absolute/path/to/skills/build-minimal-ios-app-for-app-store-review "$HOME/.agents/skills/build-minimal-ios-app-for-app-store-review"
```

Замените `/absolute/path/to/skills` на абсолютный путь к клону репозитория. Если скилл не появился автоматически, перезапустите Codex. Подробнее: [официальная документация OpenAI по скиллам](https://learn.chatgpt.com/docs/build-skills).

## Пошаговый сценарий

Скилл можно выбрать через `/skills`, упомянуть как `$build-minimal-ios-app-for-app-store-review` или вызвать естественным запросом. Работайте в папке конкретного приложения, а не внутри репозитория `skills`: все спецификации, дизайн и исходный код создаются в workspace приложения.

Каждый шаг заканчивается gate summary. В нём скилл перечисляет готовые артефакты, принятые решения, незакрытые блокеры и один конкретный вопрос об аппруве. Не отправляйте следующий большой prompt: ответьте на этот вопрос либо перечислите изменения.

### Шаг 0. Открыть рабочую папку приложения

Создайте пустую папку будущего приложения или откройте существующий проект в Codex. Подключите скилл одним из способов из раздела установки.

Для нового приложения не нужно заранее создавать пустой Xcode-проект: build-stage создаст папки и targets сам. Если workspace уже содержит проект, скилл сначала проверит его и не должен перезаписывать пользовательские файлы без разрешения.

Начальный запрос со своей идеей:

```text
$build-minimal-ios-app-for-app-store-review
Хочу приложение для совместного планирования семейных поездок. Начни с проверки идеи для App Review. Не переходи к дизайну без моего аппрува.
```

Если идеи нет:

```text
$build-minimal-ios-app-for-app-store-review
Предложи идеи простого потребительского iPhone-приложения и начни только этап выбора идеи.
```

### Шаг 1. Утвердить идею

Скилл уточняет или предлагает концепцию, связывает все обязательные разрешения с реальными пользовательскими функциями, описывает AppMetrica, backend и extensions, составляет privacy inventory и проводит App Review feasibility gate.

**Что создаёт скилл:** до аппрува — концепцию, варианты названия, MVP, permission-review matrix, privacy решения и оценку review risk. После аппрува — `AppSpec.md`, `AppPrivacy.yml`, запись в `approval_log` и статус `policy-approved`.

**Что проверить пользователю:**

- приложение даёт постоянную пользу, а не демонстрирует системные API;
- Bluetooth, камера, Contacts, Face ID, location, microphone, Photo read/add, ATT и push нужны продукту;
- purpose copy честно соответствует функциям;
- передаваемые данные, AppMetrica и backend описаны правильно;
- review risk и conditional policy modules приемлемы.

**Как продолжить:**

```text
Утверждаю эту идею и разрешаю перейти к дизайну.
```

Если нужны изменения:

```text
Идею пока не утверждаю. Убери аккаунты, оставь локальный профиль и заново покажи feasibility gate.
```

Скилл не должен начинать дизайн, пока не получит явное утверждение текущей версии идеи.

### Шаг 2. Утвердить дизайн

После аппрува идеи отдельная команда не требуется: сообщение «разрешаю перейти к дизайну» уже авторизует design-stage. Скилл читает `AppSpec.md` и `AppPrivacy.yml`, создаёт минимальную навигацию, все permission states, privacy surfaces, widget, notification UI, accessibility behavior и app icon.

**Что создаёт скилл:** утверждаемые файлы в `Design/`, описание экранов и состояний, permission-to-screen mapping, visual system и accessibility specification. Xcode-проект на этом шаге не создаётся.

**Что проверить пользователю:**

- все основные функции доступны на показанных экранах;
- разрешения запрашиваются после понятного действия, а не при запуске;
- видны состояния denied, limited, unavailable, loading и error;
- privacy policy и Settings recovery легко найти;
- widget, notification UI и иконка соответствуют приложению;
- интерфейс реально собрать на UIKit для portrait-only iPhone.

**Как продолжить:**

```text
Дизайн и иконку утверждаю. Начинай реализацию.
Название проекта: YP Journey.
Bundle ID: com.example.ypjourney.
Создай проект в текущей папке.
```

Если название проекта, bundle ID или папка назначения ещё не указаны, скилл должен запросить только эти блокирующие данные.

Для доработки:

```text
Дизайн не утверждаю. Сделай главный экран компактнее, перенеси privacy policy в видимый раздел и повторно покажи mockup.
```

### Шаг 3. Проверить реализацию

После аппрува дизайна скилл создаёт и проверяет приложение по утверждённым источникам правды. Он не должен самостоятельно менять функции, permission copy или дизайн ради удобства реализации.

**Что создаёт скилл:**

- programmatic UIKit app для iPhone iOS 15;
- Lock Screen WidgetKit extension;
- Notification Service Extension;
- programmatic Notification Content Extension;
- privacy manifests, entitlements и конфигурационные значения;
- AppMetrica integration с безопасным поведением при пустом ключе;
- минимальный backend в `backend/`;
- `Release/release-manifest.json` со статусом `implementation-verified` и блокерами следующего этапа.

Скилл собирает и запускает приложение в доступном simulator, проверяет extensions, `/health`, `/sync`, purpose strings, privacy manifests и основные состояния. Unit- и UI-test targets не создаются.

**Что проверить пользователю:**

- build и simulator launch действительно прошли;
- приложение соответствует утверждённым mockups и текстам;
- backend smoke check выполнен;
- перечислены ограничения simulator и ручные device checks;
- отсутствующие signing, APNs, production URLs и ключи честно записаны как release blockers.

**Как продолжить:**

```text
Реализацию принимаю. Разрешаю подготовить релизный пакет, но ничего не загружай и не меняй в App Store Connect.
```

Для исправления:

```text
Реализацию пока не принимаю. Исправь расхождение экрана разрешений с Design/mockup.png и повтори build verification.
```

### Шаг 4. Подготовить релиз

Release-stage начинается только после принятия реализации. Скилл проверяет актуальные первичные требования Apple, production configuration, signing, archive, privacy evidence, AppMetrica, metadata и reviewer access.

Перед этим шагом можно сразу передать известные значения:

```text
Версия: 1.0.0, build: 1.
Apple Developer Team: <team id>.
Production API: https://api.example.com.
Privacy Policy: https://example.com/privacy.
Support: https://example.com/support.
AppMetrica настроена через локальную конфигурацию; секреты в репозиторий не добавляй.
```

**Что создаёт скилл:**

- `Release/compliance-sources.json`;
- `Release/archive-validation.json`;
- `Release/app-store-privacy.json`;
- `Release/app-store-metadata/`;
- `Release/review-notes.md`;
- `Release/manual-device-checks.md`;
- обновлённый `Release/release-manifest.json`.

**Что проверить пользователю:**

- какой archive был проверен и какими инструментами;
- совпадают ли privacy contract, binary report, privacy policy и App Store answers;
- доступны ли production backend, privacy policy и support URL;
- готовы ли screenshots, metadata, age rating, export compliance и review notes;
- какие ручные проверки на реальном iPhone ещё не выполнены;
- остались ли release blockers.

Статус `release-ready` означает отсутствие известных блокеров в проверенных артефактах, но не гарантирует решение App Review и не означает, что сборка уже загружена.

### Шаг 5. Разрешить внешнее действие

Загрузка build и отправка на review — разные внешние действия. Каждое требует отдельного разрешения после того, как скилл назвал точное приложение, build, account/team и ожидаемый результат.

Разрешить только загрузку:

```text
Разрешаю загрузить archive <путь> для приложения <название>, build 1, в App Store Connect команды <team>. Не отправляй на App Review.
```

После успешной загрузки отдельно разрешить submission:

```text
Разрешаю отправить обработанный build 1 приложения <название> на App Review с подготовленными metadata и review notes.
```

Скилл записывает `submitted` только после подтверждённой успешной отправки. Формирование локальной команды, upload в обработке или добавление build в TestFlight не равны submission.

## Полный пример диалога

| Ход | Пользователь | Что делает скилл |
| --- | --- | --- |
| 1 | `$build-minimal-ios-app-for-app-store-review Придумай приложение для семейных поездок` | Предлагает идеи, раскрывает выбранную концепцию и показывает idea gate |
| 2 | `Уменьши MVP и не используй аккаунты` | Пересматривает текущую идею и повторяет gate без перехода дальше |
| 3 | `Утверждаю идею, переходи к дизайну` | Записывает `policy-approved`, создаёт контракты и готовит дизайн |
| 4 | `Дизайн утверждаю. Bundle ID: com.example.trip. Начинай реализацию` | Записывает `design-approved`, создаёт и simulator-проверяет проект |
| 5 | `Реализацию принимаю, готовь релиз без загрузки` | Сохраняет `implementation-verified`, проверяет release package и показывает блокеры |
| 6 | `Вот production URLs и signing values; продолжи release validation` | Проверяет archive и доводит пакет до `release-ready`, если блокеров нет |
| 7 | `Разрешаю загрузить build 1, но не отправлять на review` | Выполняет только upload и сообщает подтверждённый результат |
| 8 | `Разрешаю отправить build 1 на App Review` | Выполняет submission и только после успеха записывает `submitted` |

## Если нужна доработка

До аппрува просто перечислите изменения: скилл обязан остаться на текущем этапе и показать новый gate summary.

После аппрува укажите, какое принятое решение меняется. Материальное изменение делает соответствующий аппрув и зависящие от него поздние результаты устаревшими. Скилл должен вернуться к самому раннему затронутому этапу, обновить источники правды и снова пройти последующие gates.

Пример:

```text
Вернись к этапу идеи: теперь приложение должно создавать аккаунт. Обнови privacy contract и conditional policy modules. Дизайн и реализацию пока не продолжай.
```

Не используйте фразу «всё одобряю заранее»: она не разрешает будущие этапы и внешние действия.

## Как продолжить после паузы

Откройте ту же папку приложения и напишите:

```text
$build-minimal-ios-app-for-app-store-review
Продолжи с первого незавершённого или неутверждённого этапа. Сначала покажи найденные статусы, approval log, артефакты и блокеры.
```

Скилл читает `AppSpec.md`, `AppPrivacy.yml`, `Design/` и `Release/release-manifest.json`. Валидный статус должен иметь соответствующую запись в `approval_log`. При противоречии скилл останавливается и объясняет, какой gate нужно повторить.

Если проект был создан старой версией без `approval_log`, скилл не повторяет работу автоматически: он показывает последний найденный результат и просит свежее подтверждение перед следующим этапом.

## Когда понадобятся внешние данные

| Данные | Когда нужны | Можно ли отложить |
| --- | --- | --- |
| Идея, аудитория, язык, бизнес-модель | Idea-stage | Да, скилл может предложить варианты |
| Визуальные предпочтения | Design-stage | Да, скилл выберет минимальное направление |
| Название модуля, bundle ID или prefix, папка проекта | Перед build-stage | Нет для создания итоговой структуры проекта |
| AppMetrica API key | Build/release | В build-stage допустим пустой конфиг; для release-ready нужен production вариант |
| Apple Developer Team, signing и provisioning | Archive validation | Нет для подписанного release archive |
| APNs configuration | Production push verification | Можно отложить, но это останется release blocker |
| Production backend URL | Release-stage | Нет для `release-ready` |
| Privacy Policy и Support URL | Release-stage | Нет для `release-ready` |
| Version, build number и финальные bundle identifiers | Release-stage | Нет для archive и metadata |
| Review contact, demo account, sample data, hardware instructions | Release-stage | Только если соответствующий сценарий не нужен приложению |
| Доступ к App Store Connect и точное внешнее действие | Upload/submission | Нужны непосредственно перед действием |

Не сохраняйте AppMetrica keys, APNs `.p8`, App Store Connect API keys, access tokens, пароли и signing secrets в `AppPrivacy.yml`, release manifests или git. Передавайте их через безопасную локальную конфигурацию или существующее хранилище секретов.

## Ожидаемые файлы в workspace приложения

```text
AppSpec.md
AppPrivacy.yml
Design/
backend/
<Xcode project and application sources>
Release/
├── release-manifest.json
├── compliance-sources.json
├── archive-validation.json
├── app-store-privacy.json
├── app-store-metadata/
├── review-notes.md
└── manual-device-checks.md
```

Некоторые release-файлы появляются только на четвёртом этапе. Отсутствие будущего артефакта на раннем этапе не является ошибкой.

## Статусы

```text
idea-draft
  -> policy-approved
  -> design-approved
  -> implementation-verified
  -> archive-validated
  -> release-ready
  -> submitted
```

Ручные проверки Bluetooth, камеры, Contacts, Face ID, геолокации, микрофона, PhotoKit, ATT, APNs, push и специального оборудования записываются в `Release/manual-device-checks.md`. Они не создают отдельного статуса.

## AppPrivacy.yml

`AppPrivacy.yml` — machine-readable source of truth для:

- разрешений, feature triggers и purpose copy;
- локальных и передаваемых данных;
- AppMetrica и других SDK;
- ATT и tracking behavior;
- backend и публичных доменов;
- privacy policy и App Store Privacy;
- conditional policy modules;
- release blockers;
- журнала явных пользовательских аппрувов.

Файл не должен содержать API keys, токены, сертификаты, пароли и другие секреты.

## Структура

```text
build-minimal-ios-app-for-app-store-review/
├── SKILL.md
├── scripts/
│   └── validate_skill.py
├── references/
│   ├── idea-stage.md
│   ├── design-stage.md
│   ├── build-stage.md
│   ├── release-stage.md
│   ├── app-privacy-contract.md
│   └── AppPrivacy.template.yml
└── version.json
```

`SKILL.md` отвечает за triggers, usage, определение этапа и approval gates. Подробные требования каждого этапа загружаются из `references/` только тогда, когда этот этап разрешён. `version.json` содержит версию, changelog, категорию и автора.

## Проверка скилла

После изменения файлов выполните из корня репозитория:

```bash
python3 build-minimal-ios-app-for-app-store-review/scripts/validate_skill.py
```

Валидатор проверяет единственность устанавливаемого скилла, обязательные файлы, frontmatter, stage routing, approval contract, разрешения, privacy schema, README и `version.json`.

## Что потребуется перед релизом

- актуальные Xcode и iOS SDK;
- Apple Developer Team, signing и provisioning;
- настроенные APNs и AppMetrica;
- доступный production HTTPS backend;
- опубликованные privacy policy и support page;
- данные App Store Connect;
- reviewer account, sample data или инструкции к оборудованию, когда они нужны;
- ручная проверка релизной сборки на физическом iPhone.

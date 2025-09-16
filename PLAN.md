Есть unify nvr c api. Хочу сделать приложение на питоне, которое будет делать следующее. gui на freesimplegui. Приложение стартует, логинимся по кредам из энва. Получаем список камер. Есть режим просмотра текущего. Можно выбрать камеры которые хочу смотреть а какие нет (чекбоксами) В нем просто получаем поток ото всех камер и показываем на одном экране. Везде звук выключен, можно включить звук камеры которую хочу. Есть режим просмотра всех камер в одиновом масштабе, а есть режим просмотра конкрентной камеры крупным планом.  Второй режим. Задаю период который хочу смотреть и камеры которые хочу смотреть (чекбоксами). Есть один ползунок, который показывает на каком времени мы сейчас смотрим записи. Соответсвенно когда включаю плей все камеры где есть запись в это время показываем свой поток. Идея в том, чтобы я мог выбрать время которое хочу смотреть и у меня пошел просмотр со всех камер. Камеры пишутся в режиме моушен детекшена, соответсвенно если в какой-то момент нет записей ни откуда, то нужно такое скипать. 
ChatGPT сказал:

Отличная идея 👍 Давай разложим по шагам, чтобы у тебя получился рабочий план для приложения.

Архитектура

API-слой

Используем Unifi Protect (NVR) API для:

авторизации (/api/auth),

получения списка камер (/api/cameras),

получения RTSP-ссылок на стримы (у каждой камеры есть несколько профилей качества),

запросов записей (motion events, таймлайны).

GUI-слой

PySimpleGUI для управления:

авторизацией,

списком камер с чекбоксами,

режимами просмотра (live / playback),

включением/выключением звука,

масштабированием.

Видео-слой

opencv-python или ffmpeg (через aiortc/ffpyplayer) для отображения RTSP-стримов.

Для многопоточности: threading или asyncio, чтобы каждая камера обрабатывалась независимо.

Логика режимов

Live режим:

чекбоксами выбираем камеры → запускаем поток → выводим в едином окне (грид).

звук по умолчанию off, включается только на одной выбранной.

Playback режим:

выбираем камеры,

указываем интервал дат/времени,

получаем список motion events (там есть start/end),

ползунок времени → синхронно ищем кадры для каждой камеры,

при Play движемся по таймлайну, пропуская пустые промежутки.

Основные вызовы API (примерно)
import os
import requests

BASE_URL = os.getenv("NVR_URL")
USER = os.getenv("NVR_USER")
PASS = os.getenv("NVR_PASS")

session = requests.Session()

def login():
    resp = session.post(f"{BASE_URL}/api/auth/login", json={
        "username": USER,
        "password": PASS
    }, verify=False)
    resp.raise_for_status()

def get_cameras():
    resp = session.get(f"{BASE_URL}/api/cameras")
    return resp.json()

def get_events(start_ts, end_ts):
    resp = session.get(f"{BASE_URL}/api/events", params={
        "start": start_ts,
        "end": end_ts,
        "types": "motion"
    })
    return resp.json()

GUI (набросок)
import PySimpleGUI as sg

layout = [
    [sg.Text("Выберите режим:"), sg.Radio("Live", "mode", default=True, key="live"),
     sg.Radio("Playback", "mode", key="playback")],
    [sg.Text("Камеры:"), sg.Column([ [sg.Checkbox("Cam1", key="cam1")],
                                     [sg.Checkbox("Cam2", key="cam2")] ])],
    [sg.Button("Start"), sg.Button("Exit")]
]

window = sg.Window("Unifi NVR Viewer", layout)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, "Exit"):
        break
    if event == "Start":
        if values["live"]:
            print("Live режим...")
        else:
            print("Playback режим...")

Потенциальные сложности

RTSP-стримы: напрямую через OpenCV могут лагать. Лучше использовать ffpyplayer или aiortc.

Синхронизация playback: придётся строить общий таймлайн по событиям всех камер, чтобы правильно «перескакивать» пустые промежутки.

Звук: OpenCV не тянет звук, поэтому для аудио придётся отдельно запускать ffmpeg-процесс или использовать vlc-python.

Хочешь, я соберу минимальный рабочий прототип (только Live-режим, выбор камер, вывод картинок без звука) на PySimpleGUI + OpenCV, чтобы у тебя было сразу с чего стартовать?

Вы сказали:
не, надо со звуком сразу
ChatGPT сказал:

Окей, тогда OpenCV сразу отбрасываем — он умеет только картинку, без звука. Для твоей задачи лучше взять VLC Python bindings (python-vlc).

Почему VLC

Умеет и RTSP/RTMP/HLS стримы от UniFi Protect.

Поддерживает аудио + видео.

Можно встроить видео в PySimpleGUI (через tkinter-handle окна).

Легко включать/отключать звук у отдельных камер.

Архитектура для Live режима со звуком

Авторизация в NVR → получаем RTSP URL для каждой камеры.

Для каждой камеры: создаём VLC MediaPlayer.

Видео без звука → set_mute(True).

У выбранной камеры → set_mute(False).

В GUI: чекбоксы для выбора камер + radio/combobox для выбора, с какой включить звук.

Для Playback: берём сегменты записей (events) → по RTSP можно запрашивать отрезки (если Protect это поддерживает) либо дергать API для mp4-файлов → VLC их тоже крутит.

Минимальный пример Live со звуком
import os
import vlc
import PySimpleGUI as sg

# RTSP ссылки камер (обычно получаются из NVR API)
CAMERAS = {
    "Cam1": "rtsp://user:pass@192.168.1.10:7447/abcd123",
    "Cam2": "rtsp://user:pass@192.168.1.10:7447/efgh456",
}

players = {}

def start_player(cam_name, rtsp_url, frame):
    instance = vlc.Instance("--no-xlib")  # для Linux без X
    player = instance.media_player_new()
    media = instance.media_new(rtsp_url)
    player.set_media(media)
    player.set_hwnd(frame.Widget.winfo_id())  # встраиваем в PySimpleGUI
    player.audio_set_mute(True)
    player.play()
    players[cam_name] = player

layout = [
    [sg.Text("Выберите камеры для просмотра:")],
    [sg.Checkbox(cam, key=cam) for cam in CAMERAS],
    [sg.Text("Камера со звуком:"), sg.Combo(list(CAMERAS.keys()), key="audio_cam")],
    [sg.Button("Start"), sg.Button("Exit")],
    [sg.Frame(cam, [[sg.Canvas(key=f"canvas_{cam}")]]) for cam in CAMERAS]
]

window = sg.Window("UniFi NVR Viewer", layout, finalize=True)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, "Exit"):
        break
    if event == "Start":
        for cam, url in CAMERAS.items():
            if values[cam]:
                start_player(cam, url, window[f"canvas_{cam}"])
        if values["audio_cam"]:
            for cam, player in players.items():
                player.audio_set_mute(cam != values["audio_cam"])

Что дальше

Для Playback:

UniFi Protect API отдаёт event clips (.mp4).

Их можно точно так же грузить через player.set_media().

Для синхронизации нескольких камер нужен общий таймлайн + seek (player.set_time(ms)).

Для переключения звука на лету:

player.audio_set_mute(False)
other.audio_set_mute(True)


Хочешь, я распишу структуру классов (NVRClient, CameraPlayer, PlaybackController), чтобы у тебя код был не спагетти, а расширяемый?
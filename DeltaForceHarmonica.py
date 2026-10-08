# -*- coding: utf-8 -*-
"""Delta Force Harmonica Auto Player | Credit: huuhoa43

Reads all mappings, settings and song events from config.json next to this file.
If config.json is missing, the built-in default config is recreated automatically.
"""

import base64
import json
import os
import sys
import threading
import time
import zlib
from pathlib import Path

try:
    import pydirectinput
    from pynput.keyboard import Listener, Key
except ModuleNotFoundError as exc:
    missing = exc.name or "a required package"
    print(f"Thiếu thư viện: {missing}")
    print("Cài thư viện bằng lệnh: python -m pip install pydirectinput pynput")
    raise SystemExit(1)

APP_NAME = "Delta Force Harmonica Auto Player"
CREDIT = "huuhoa43"

_DEFAULT_CONFIG_B64 = "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"


def get_app_dir():
    """Return the folder beside the .py file or packaged .exe."""
    if getattr(sys, "frozen", False):
        return Path(sys.executable).resolve().parent
    return Path(__file__).resolve().parent


APP_DIR = get_app_dir()
CONFIG_PATH = APP_DIR / "config.json"


def load_config_file():
    if not CONFIG_PATH.exists():
        try:
            raw = zlib.decompress(base64.b64decode(_DEFAULT_CONFIG_B64)).decode("utf-8")
            CONFIG_PATH.write_text(raw, encoding="utf-8")
            print(f"Đã tạo config mặc định tại: {CONFIG_PATH}")
        except Exception as exc:
            raise RuntimeError(f"Không thể tạo config.json: {exc}") from exc

    try:
        with CONFIG_PATH.open("r", encoding="utf-8-sig") as f:
            data = json.load(f)
    except json.JSONDecodeError as exc:
        raise RuntimeError(
            f"config.json bị sai định dạng JSON (dòng {exc.lineno}, cột {exc.colno}). "
            "Sửa lại dấu phẩy/dấu ngoặc hoặc khôi phục config.json mẫu."
        ) from exc
    except OSError as exc:
        raise RuntimeError(f"Không đọc được config.json: {exc}") from exc

    validate_config(data)
    return data


def validate_config(data):
    if not isinstance(data, dict):
        raise ValueError("Cấu hình gốc phải là JSON object.")
    if data.get("schema_version") != 1:
        raise ValueError("schema_version không được hỗ trợ. Hãy dùng config.json đi kèm bản này.")

    settings = data.get("settings")
    if not isinstance(settings, dict):
        raise ValueError("Thiếu object settings trong config.json.")
    speed = float(settings.get("speed_multiplier", 1.0))
    delay = float(settings.get("startup_delay_seconds", 1.0))
    pause = float(settings.get("pydirectinput_pause_seconds", 0.001))
    if speed <= 0 or speed > 10:
        raise ValueError("settings.speed_multiplier phải lớn hơn 0 và không quá 10.")
    if delay < 0 or delay > 30:
        raise ValueError("settings.startup_delay_seconds phải nằm trong khoảng 0..30.")
    if pause < 0 or pause > 1:
        raise ValueError("settings.pydirectinput_pause_seconds phải nằm trong khoảng 0..1.")

    hotkeys = data.get("hotkeys")
    if not isinstance(hotkeys, dict):
        raise ValueError("Thiếu object hotkeys trong config.json.")
    for action in ("play_pause", "next_song", "exit"):
        if action not in hotkeys:
            raise ValueError(f"Thiếu hotkeys.{action} trong config.json.")
        parse_hotkey(hotkeys[action])
    normalized_hotkeys = [str(hotkeys[k]).upper() for k in ("play_pause", "next_song", "exit")]
    if len(set(normalized_hotkeys)) != len(normalized_hotkeys):
        raise ValueError("Ba hotkey play_pause, next_song và exit phải khác nhau.")

    note_map = data.get("note_map")
    if not isinstance(note_map, dict) or not note_map:
        raise ValueError("note_map phải là object không rỗng.")
    if any(not isinstance(k, str) or not isinstance(v, str) or not v for k, v in note_map.items()):
        raise ValueError("Mỗi giá trị trong note_map phải là tên phím dạng chuỗi.")

    mouse_map = data.get("mouse_map")
    if not isinstance(mouse_map, dict):
        raise ValueError("mouse_map phải là object.")
    for label, button in mouse_map.items():
        if str(label).upper() not in ("LEFT", "MIDDLE", "RIGHT") or str(button).lower() not in ("left", "middle", "right"):
            raise ValueError(f"Mouse mapping không hợp lệ: {label}: {button}")

    songs = data.get("songs")
    if not isinstance(songs, dict) or not songs:
        raise ValueError("songs phải có ít nhất một bài nhạc.")
    for title, events in songs.items():
        if not isinstance(title, str) or not title:
            raise ValueError("Tên bài hát phải là chuỗi không rỗng.")
        if not isinstance(events, list) or not events:
            raise ValueError(f"Bài '{title}' chưa có event nào.")
        for index, event in enumerate(events, start=1):
            if not isinstance(event, list) or len(event) != 4:
                raise ValueError(f"{title}, event {index}: phải có dạng [note, hold, gap, mouse_buttons].")
            note, hold, gap, buttons = event
            if not isinstance(note, str):
                raise ValueError(f"{title}, event {index}: note phải là chuỗi.")
            try:
                hold, gap = float(hold), float(gap)
            except (TypeError, ValueError) as exc:
                raise ValueError(f"{title}, event {index}: hold/gap phải là số.") from exc
            if hold < 0 or gap < 0:
                raise ValueError(f"{title}, event {index}: hold/gap không thể âm.")
            if not isinstance(buttons, list):
                raise ValueError(f"{title}, event {index}: mouse_buttons phải là danh sách.")
            for button in buttons:
                if str(button).upper() not in mouse_map:
                    raise ValueError(f"{title}, event {index}: nút chuột '{button}' chưa có trong mouse_map.")
            if note.upper() == "REST" and buttons:
                raise ValueError(f"{title}, event {index}: REST không được kèm chuột.")


def parse_hotkey(name):
    """Convert F8/ESC/SPACE or a single printable character to a key token."""
    label = str(name).strip().upper()
    aliases = {"ESC": "esc", "ESCAPE": "esc", "SPACE": "space", "ENTER": "enter", "TAB": "tab"}
    key_name = aliases.get(label, label.lower())
    if len(label) == 1 and label.isprintable():
        return label.lower()
    if hasattr(Key, key_name):
        return getattr(Key, key_name)
    raise ValueError(f"Hotkey không hỗ trợ: {name}. Dùng F1-F12, ESC, SPACE, ENTER, TAB hoặc 1 ký tự.")


try:
    CONFIG = load_config_file()
except Exception as exc:
    print("LỖI CONFIG:", exc)
    print("Đặt config.json cùng thư mục với file .py/.exe rồi thử lại.")
    raise SystemExit(1)

SETTINGS = CONFIG["settings"]
NOTE_MAP = {str(k): str(v).lower() for k, v in CONFIG["note_map"].items()}
MOUSE_MAP = {str(k).upper(): str(v).lower() for k, v in CONFIG["mouse_map"].items()}
SONGS = CONFIG["songs"]
HOTKEYS = {action: parse_hotkey(value) for action, value in CONFIG["hotkeys"].items()}

pydirectinput.PAUSE = float(SETTINGS.get("pydirectinput_pause_seconds", 0.001))
pydirectinput.FAILSAFE = bool(SETTINGS.get("failsafe", False))

is_playing = False
current_song_index = 0
run_token = 0
state_lock = threading.RLock()


def is_active(token):
    with state_lock:
        return is_playing and token == run_token


def precise_wait(target_time, token):
    """Wait until target time, stopping quickly after F8/F7/F9."""
    while True:
        if not is_active(token):
            return False
        remaining = target_time - time.perf_counter()
        if remaining <= 0:
            return True
        if remaining > 0.004:
            time.sleep(min(remaining - 0.001, 0.01))
        else:
            # Tiny final wait for lower scheduling jitter.
            time.sleep(min(remaining, 0.001))


def normalize_event(event):
    note, hold, gap, buttons = event
    return str(note), float(hold), float(gap), [str(x).upper() for x in buttons]


def song_stats(events):
    speed = float(SETTINGS.get("speed_multiplier", 1.0))
    total = 0.0
    count = 0
    for note, hold, gap, _buttons in events:
        total += (float(hold) + float(gap)) / speed
        if str(note).upper() != "REST":
            count += 1
    return count, total


def play_event(note, hold, buttons, token):
    """Press keyboard note and all requested mouse modifiers together."""
    speed = float(SETTINGS.get("speed_multiplier", 1.0))
    hold_seconds = float(hold) / speed

    if str(note).upper() == "REST":
        return precise_wait(time.perf_counter() + hold_seconds, token)

    key = NOTE_MAP.get(str(note))
    if key is None and str(note).lower() in ("z", "x", "c", "v", "b", "n", "m", ","):
        key = str(note).lower()
    if key is None:
        raise ValueError(f"Không có mapping cho nốt '{note}' trong note_map.")

    actual_buttons = []
    key_is_down = False
    try:
        for modifier in buttons:
            actual = MOUSE_MAP.get(str(modifier).upper())
            if actual is None:
                raise ValueError(f"Không có mouse_map cho '{modifier}'.")
            pydirectinput.mouseDown(button=actual)
            actual_buttons.append(actual)

        pydirectinput.keyDown(key)
        key_is_down = True
        precise_wait(time.perf_counter() + max(0.001, hold_seconds), token)
    finally:
        if key_is_down:
            try:
                pydirectinput.keyUp(key)
            except Exception:
                pass
        for button in reversed(actual_buttons):
            try:
                pydirectinput.mouseUp(button=button)
            except Exception:
                pass

    return is_active(token)


def show_status(message=None):
    if bool(SETTINGS.get("clear_console", True)):
        os.system("cls" if os.name == "nt" else "clear")
    with state_lock:
        song_names = list(SONGS.keys())
        song_name = song_names[current_song_index] if song_names else "(không có bài)"
        playing = is_playing
    print("=" * 68)
    print(f"  {APP_NAME} | Credit: {CONFIG.get('credit', CREDIT)}")
    print("=" * 68)
    print(f"Bài hiện tại: {song_name}")
    print("Phím kèn: " + "  ".join(f"{n}={k}" for n, k in NOTE_MAP.items()))
    print("Modifier chuột: LEFT / MIDDLE / RIGHT (có thể kết hợp theo từng event)")
    print("-" * 68)
    print(f"{CONFIG['hotkeys']['next_song']} : Đổi bài")
    print(f"{CONFIG['hotkeys']['play_pause']} : Bắt đầu / dừng bài")
    print(f"{CONFIG['hotkeys']['exit']} : Thoát")
    print(f"Tốc độ: {float(SETTINGS.get('speed_multiplier', 1.0)):.2f}x")
    print("-" * 68)
    print("Trạng thái: " + ("ĐANG PHÁT" if playing else "DỪNG"))
    if message:
        print(message)
    print("=" * 68)


def play_music(token, song_name, events):
    speed = float(SETTINGS.get("speed_multiplier", 1.0))
    normalized = [normalize_event(event) for event in events]
    note_count, total_time = song_stats(normalized)
    show_status(f"Đang phát: {song_name} | {note_count} nốt | {len(events)} event | ~{total_time:.1f}s")

    startup_delay = float(SETTINGS.get("startup_delay_seconds", 1.0))
    target = time.perf_counter() + startup_delay
    if not precise_wait(target, token):
        return

    try:
        for note, hold, gap, buttons in normalized:
            if not is_active(token):
                break
            if not precise_wait(target, token):
                break
            if not play_event(note, hold, buttons, token):
                break
            target += (hold + gap) / speed
    except Exception as exc:
        print(f"\nLỗi khi phát bài '{song_name}': {exc}")
    finally:
        with state_lock:
            if token == run_token:
                is_playing = False
        show_status("Đã kết thúc hoặc dừng bài." if not is_active(token) else None)


def toggle_play():
    global is_playing, run_token
    with state_lock:
        if is_playing:
            is_playing = False
            run_token += 1
            message = "Đã dừng bài. Nhấn phím phát để chạy lại từ đầu."
            should_start = False
        else:
            if not SONGS:
                print("config.json không có bài hát.")
                return
            is_playing = True
            run_token += 1
            token = run_token
            song_names = list(SONGS.keys())
            song_name = song_names[current_song_index]
            events = SONGS[song_name]
            message = "Đang chuẩn bị phát..."
            should_start = True
    show_status(message)
    if should_start:
        threading.Thread(target=play_music, args=(token, song_name, events), daemon=True).start()


def switch_song():
    global current_song_index, is_playing, run_token
    with state_lock:
        is_playing = False
        run_token += 1
        song_names = list(SONGS.keys())
        current_song_index = (current_song_index + 1) % len(song_names)
    show_status("Đã chuyển sang bài kế tiếp.")


def key_matches(pressed, expected):
    if isinstance(expected, str):
        try:
            return getattr(pressed, "char", None) is not None and pressed.char.lower() == expected.lower()
        except Exception:
            return False
    return pressed == expected


def on_press(key):
    global is_playing, run_token
    if key_matches(key, HOTKEYS["play_pause"]):
        toggle_play()
    elif key_matches(key, HOTKEYS["next_song"]):
        switch_song()
    elif key_matches(key, HOTKEYS["exit"]):
        with state_lock:
            is_playing = False
            run_token += 1
        print("\nĐã thoát chương trình. Credit: " + str(CONFIG.get("credit", CREDIT)))
        return False


def main():
    print("Đã nạp config:", CONFIG_PATH)
    print("Số bài:", len(SONGS))
    show_status("Đưa Delta Force về cửa sổ nhận input kèn trước khi phát.")
    with Listener(on_press=on_press) as listener:
        listener.join()


if __name__ == "__main__":
    main()

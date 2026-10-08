# Delta Force Harmonica Auto Player

[English](#english) | [Tiếng Việt](#tiếng-việt)

---

<a id="english"></a>
# EN English

**Credit:** huuhoa43

An automated tool to play the harmonica in Delta Force.

## 1. Included Files
- **.exe file**: The executable program (if provided separately).
- **config.json**: Configuration file for settings, hotkeys, key mapping, and the song list.
- **README.md**: This documentation.
- **PROMPT_AI_TAO_BAI_HAT.txt**: A sample prompt to ask AI to create more songs.
- **DeltaForceHarmonica.py**: The Python source code (only needed if you want to view/run from the source).

> **Note:** If you received the EXE file separately, keep the EXE and `config.json` in the same folder. Do not rename `config.json`. Extract the ZIP file before running; do not run the EXE directly from inside the ZIP preview window.

## 2. How to Run (Recommended)
1. Extract the files into a folder, e.g., `Desktop\DeltaForceHarmonica`.
2. Ensure the EXE file and `config.json` are next to each other in the same folder.
3. Right-click on the EXE file.
4. Select **"Run as administrator"**.
5. If the Windows User Account Control (UAC) dialog appears, click **Yes** (only if you trust the file source).
6. Open *Delta Force* and navigate to the interface/mode that accepts Harmonica input.
7. Use the hotkeys (see section 3) to select and play songs.

*You do not need to install Python or Visual Studio Code if you are only running the EXE file. If the game is running as administrator but the bot doesn't recognize input, make sure to run the bot with the same privileges. Only open files from trusted sources; do not disable Windows Defender or antivirus arbitrarily.*

## 3. In-Game Usage
- Open *Delta Force* and switch to the harmonica input interface.
- Keep the bot window running, then switch focus back to the game before playing music.
- **F7**: Skip to the next song.
- **F8**: Play or Pause the current song.
- **F9**: Exit the program.
- When you pause in the middle of a song, the next time you press play, it will restart from the beginning.
- *Tip: Try it in a safe area first, as the bot will automatically press keyboard and mouse buttons.*

Default hotkeys can be changed in `config.json`. If you have modified them, check the `hotkeys` section in the config file to see the currently assigned keys.

## 4. What is `config.json` for?
The program reads `config.json` located in the same folder as the `.py` or `.exe` file. After editing `config.json`, save the file and restart the program to apply the changes. It is highly recommended to create a backup of `config.json` before making edits.

**Main fields:**
- `settings.speed_multiplier`: `1.00` = original speed; `1.10` = 10% faster; `0.90` = 10% slower.
- `settings.startup_delay_seconds`: Delay (in seconds) before the song starts playing.
- `settings.pydirectinput_pause_seconds`: Small pause between `pydirectinput` actions.
- `settings.failsafe`: Enable/disable `pydirectinput` failsafe.
- `settings.clear_console`: Clear the console screen when updating status.
- `hotkeys`: Change `play_pause`, `next_song`, and `exit` hotkeys. Supports F1-F12, ESC, SPACE, ENTER, TAB, or a single character. The three hotkeys must be unique.
- `note_map`: Maps note numbers to keyboard keys.
- `mouse_map`: Maps LEFT/MIDDLE/RIGHT to mouse buttons.
- `songs`: The playlist. You can add, edit, or delete songs here.

**Event structure format:**
```json
["5", 0.25, 0.0, ["MIDDLE"]]
```
- `"5"`: Note number in `note_map`. Use `"REST"` to pause without pressing a key.
- `0.25`: Hold duration in seconds.
- `0.0`: Gap duration after the note in seconds.
- `["MIDDLE"]`: Hold the middle mouse button while pressing the note.
- `[]`: No mouse modifier needed.
- `["LEFT", "MIDDLE"]`: Hold both left and middle mouse buttons.
- Example of a 0.5-second rest: `["REST", 0.5, 0.0, []]`.

**Important JSON Rules:**
- JSON does not support comments (like `#`).
- Use correct double quotes, commas, and square brackets.
- Do not delete required fields like `schema_version`, `settings`, `hotkeys`, `note_map`, `mouse_map`, and `songs`.
- Ensure new song names are unique.

## 5. Adding New Songs to `config.json`
1. Make a backup copy of `config.json`.
2. Open `config.json` using Notepad or a code editor (do not use Microsoft Word).
3. Find the `"songs"` section. Each song is a key-value pair of the song name and an event list.
4. Add the new song at the same level as the others. If inserting after an existing song, remember to add a comma `,` after the previous song's closing bracket.
5. Format each event as `["note", hold, gap, ["MOUSE"]]`.
6. Save the file as **UTF-8** and keep the name `config.json`.
7. Restart the bot. If the JSON is invalid, the program will show a configuration error.

**Short Example:**
```json
"Sample Song": [
  ["5", 0.25, 0.0, []],
  ["6", 0.25, 0.0, ["MIDDLE"]],
  ["REST", 0.5, 0.0, []]
]
```

### Asking AI to Generate Songs
Open the `PROMPT_AI_TAO_BAI_HAT.txt` file, copy the prompt, and send it to an AI along with a MIDI file (`.mid` / `.midi`), sheet music/notation, or a clear audio source. The prompt instructs the AI to return JSON events matching the `config.json` schema.

*For the best timing accuracy, prioritize providing a MIDI file. If you only provide audio/video/sheet music, ask the AI to specify which timings are estimated and instruct it not to invent notes. Always review notes, mappings, and modifiers in-game before sharing.*

## 6. Troubleshooting
- **EXE opens but doesn't press keys in-game:** Check window focus, ensure you are in the harmonica UI, verify mappings in `config.json`, and try running the bot as administrator.
- **Privilege issues:** If the game runs as administrator, the bot may need the same privileges to send inputs successfully.
- **Config.json errors:** Check for missing commas, incorrect quotes, or mismatched brackets. Restore your backup if necessary.
- **Wrong keys/notes played:** Check `note_map`, `mouse_map`, and the song's events.
- **New song not showing up:** Ensure the song is inside the `"songs"` object, the JSON is valid, the file is saved as `config.json` next to the EXE, and you have restarted the program.
- **Windows SmartScreen warning:** Only proceed if you trust the creator of the file. Do not arbitrarily disable your antivirus.

## 7. Credits
Created and arranged by **huuhoa43**.
*This is a fan-made tool, not affiliated with, sponsored by, or endorsed by Delta Force.*
*This tool was developed with the assistance of AI.*

---
---

<a id="tiếng-việt"></a>
# 🇻🇳 Tiếng Việt

**Credit:** huuhoa43

Công cụ tự động chơi kèn Harmonica trong game Delta Force.

## 1. Các file trong bộ cài
- **File .exe**: Chương trình để mở (nếu được gửi kèm riêng).
- **config.json**: Cấu hình, hotkey, mapping và danh sách bài nhạc.
- **README.md**: Tài liệu hướng dẫn này.
- **PROMPT_AI_TAO_BAI_HAT.txt**: Prompt mẫu để nhờ AI tạo thêm bài nhạc.
- **DeltaForceHarmonica.py**: Mã nguồn Python, chỉ cần nếu muốn xem/chạy source.

> **Lưu ý:** Nếu bạn nhận file EXE riêng, hãy để EXE và `config.json` trong cùng một thư mục. Không đổi tên `config.json`. Nên giải nén trước khi chạy, không chạy EXE trực tiếp bên trong cửa sổ xem trước của file ZIP.

## 2. Chạy file EXE (Khuyến nghị)
1. Giải nén bộ file vào một thư mục, ví dụ `Desktop\DeltaForceHarmonica`.
2. Kiểm tra file EXE và `config.json` nằm cạnh nhau trong cùng thư mục.
3. Nhấn chuột phải vào file EXE.
4. Chọn **“Run as administrator”** / “Chạy bằng quyền quản trị”.
5. Nếu Windows hiện hộp thoại User Account Control, chỉ chọn **Yes** khi bạn tin tưởng nguồn file.
6. Mở *Delta Force* và vào giao diện/chế độ có thể nhận input kèn Harmonica.
7. Dùng hotkey trong mục 3 để chọn bài và phát nhạc.

*Không cần cài Python hay Visual Studio Code nếu bạn chỉ chạy file EXE. Nếu game đang chạy bằng quyền administrator mà bot không nhận input, hãy chạy bot bằng quyền tương đương. Chỉ mở file từ nguồn bạn tin tưởng; không tắt phần mềm bảo vệ Windows một cách tùy tiện.*

## 3. Sử dụng trong game
- Mở *Delta Force* và chuyển đến giao diện nhận input kèn.
- Để cửa sổ bot đang chạy; sau đó chuyển focus về game trước khi phát nhạc.
- **F7**: Chuyển sang bài tiếp theo.
- **F8**: Bắt đầu phát hoặc dừng bài đang phát.
- **F9**: Thoát chương trình.
- Khi dừng giữa bài, lần phát tiếp theo bắt đầu lại từ đầu bài.
- *Mẹo: Nên thử ở khu vực an toàn trước, vì bot có thể tự động bấm phím và nút chuột.*

Các hotkey mặc định có thể đổi trong `config.json`. Nếu bạn đã đổi hotkey, hãy xem mục `hotkeys` trong `config.json` để biết phím đang được gán.

## 4. `config.json` dùng để làm gì?
Chương trình đọc `config.json` nằm cùng thư mục với file `.py` hoặc `.exe`. Sau khi sửa `config.json`, hãy lưu file và đóng/mở lại chương trình để áp dụng. Nên tạo bản sao `config.json` trước khi sửa.

**Các trường chính:**
- `settings.speed_multiplier`: `1.00` = tốc độ gốc; `1.10` = nhanh hơn khoảng 10%; `0.90` = chậm hơn khoảng 10%.
- `settings.startup_delay_seconds`: Số giây chờ trước khi bắt đầu phát bài.
- `settings.pydirectinput_pause_seconds`: Khoảng dừng nhỏ giữa các thao tác `pydirectinput`.
- `settings.failsafe`: Bật/tắt failsafe của `pydirectinput`.
- `settings.clear_console`: Xóa màn hình console khi cập nhật trạng thái.
- `hotkeys`: Đổi phím `play_pause`, `next_song` và `exit`. Hỗ trợ F1-F12, ESC, SPACE, ENTER, TAB hoặc một ký tự đơn; ba hotkey phải khác nhau.
- `note_map`: Ánh xạ số nốt sang phím bàn phím.
- `mouse_map`: Ánh xạ LEFT/MIDDLE/RIGHT sang nút chuột.
- `songs`: Danh sách bài nhạc. Có thể thêm, sửa hoặc xóa bài trong JSON.

**Mỗi event của bài hát có dạng:**
```json
["5", 0.25, 0.0, ["MIDDLE"]]
```
- `"5"`: Số nốt trong `note_map`. Dùng `"REST"` để nghỉ mà không bấm phím.
- `0.25`: Hold, thời gian giữ nốt tính bằng giây.
- `0.0`: Gap, khoảng nghỉ sau nốt tính bằng giây.
- `["MIDDLE"]`: Giữ chuột giữa trong lúc bấm nốt.
- `[]`: Không cần modifier chuột.
- `["LEFT", "MIDDLE"]`: Giữ đồng thời chuột trái và chuột giữa.
- Ví dụ nghỉ 0.5 giây: `["REST", 0.5, 0.0, []]`.

**Lưu ý JSON:**
- JSON không hỗ trợ chú thích bằng dấu `#`.
- Dùng đúng dấu ngoặc kép, dấu phẩy và ngoặc vuông.
- Không xóa các trường bắt buộc như `schema_version`, `settings`, `hotkeys`, `note_map`, `mouse_map` và `songs`.
- Đổi tên bài nhạc cần đảm bảo không trùng tên bài đã có.

## 5. Thêm bài nhạc mới vào `config.json`
1. Tạo bản sao `config.json` để dự phòng.
2. Mở `config.json` bằng Notepad hoặc một trình soạn thảo văn bản. Không nên sửa bằng Microsoft Word.
3. Tìm mục `"songs"`. Mỗi bài là một cặp tên bài và danh sách event.
4. Thêm bài mới cùng cấp với các bài khác trong `"songs"`. Nếu chèn sau một bài đã có, nhớ đặt dấu phẩy `,` sau phần kết thúc bài trước nó.
5. Mỗi event dùng format `["note", hold, gap, ["MOUSE"]]`.
6. Lưu file dạng **UTF-8**, giữ nguyên tên `config.json`.
7. Đóng và mở lại bot. Nếu JSON sai, chương trình sẽ báo lỗi cấu hình.

**Ví dụ một bài ngắn:**
```json
"Bai Mau": [
  ["5", 0.25, 0.0, []],
  ["6", 0.25, 0.0, ["MIDDLE"]],
  ["REST", 0.5, 0.0, []]
]
```
*(Trong ví dụ trên, nốt 5 được bấm 0.25 giây; nốt 6 bấm cùng với chuột giữa; sau đó nghỉ 0.5 giây. Đây chỉ là ví dụ format, không phải bản nhạc đầy đủ).*

### Prompt mẫu để nhờ AI tạo thêm bài nhạc
Mở file `PROMPT_AI_TAO_BAI_HAT.txt`, sao chép prompt trong đó và gửi cho AI kèm file MIDI (`.mid` / `.midi`), bản nhạc/notation, hoặc nguồn âm thanh rõ ràng. Prompt yêu cầu AI trả về event JSON đúng schema của `config.json`.

*Để timing chính xác nhất, ưu tiên gửi file MIDI. Nếu chỉ gửi audio/video hoặc ảnh sheet, hãy yêu cầu AI nói rõ chỗ nào là timing ước lượng và không được tự chế nốt. Bạn cần kiểm tra lại nốt, mapping và modifier trong game trước khi chia sẻ.*

## 6. Sự cố thường gặp
- **EXE mở nhưng không bấm trong game:** Kiểm tra focus, giao diện kèn, mapping trong `config.json` và thử chạy bot bằng quyền administrator.
- **Quyền truy cập:** Nếu game chạy bằng quyền administrator, bot cũng có thể cần chạy bằng quyền tương đương để input được nhận.
- **Lỗi `config.json`:** Kiểm tra dấu phẩy, dấu ngoặc kép và ngoặc vuông; phục hồi bản sao nếu cần.
- **Phát sai phím/nốt:** Kiểm tra `note_map`, `mouse_map` và event của bài.
- **Không thấy bài mới:** Đảm bảo bài nằm bên trong object `"songs"`, JSON hợp lệ, lưu đúng file `config.json` cạnh EXE và khởi động lại chương trình.
- **Cảnh báo Windows khi mở EXE:** Chỉ tiếp tục nếu bạn tin tưởng nguồn tạo file. Không tắt phần mềm bảo vệ một cách tùy tiện.

## 7. Credit
Created and arranged by **huuhoa43**.
*Đây là công cụ fan-made, không liên kết với và không được Delta Force bảo trợ/chứng thực.*
*Công cụ này có sự hỗ trợ của AI.*

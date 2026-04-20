<!--
Document : INSTALL.md
Auteur : Bruno DELNOZ
Email : bruno.delnoz@protonmail.com
Version : v1.0.0
Date : 2026-04-20 00:00
-->
# Installation Guide

## 1. System Prerequisites

Install required tools before running scripts:

- `bash`
- `python3`
- `pip3`
- `git`
- `cmake`
- `make`
- `ffmpeg` (includes `ffprobe`)
- `bc`

Example (Debian/Ubuntu):

```bash
sudo apt update
sudo apt install -y python3 python3-pip python3-venv git cmake make ffmpeg bc
```

## 2. Installer Script

Grant execution permission and run installer:

```bash
chmod +x install_whisper.sh
./install_whisper.sh
```

Installer actions:

1. Checks tool prerequisites.
2. Creates `whisper_env` virtual environment.
3. Installs `openai-whisper`.
4. Clones or updates `whisper.cpp`.
5. Builds `whisper.cpp` binaries.
6. Verifies `whisper.cpp/build/bin/whisper-cli`.
7. Downloads `models/ggml-base.bin` if missing.

## 3. Installer Maintenance Modes

```bash
./install_whisper.sh --help
./install_whisper.sh --clean
./install_whisper.sh --reinstall
./install_whisper.sh --test /path/audio.wav
```

## 4. Validate Transcription Tool

```bash
chmod +x transcribe_mp4.2.3.sh
./transcribe_mp4.2.3.sh --help
./transcribe_mp4.2.3.sh --file "/path/video.mp4" --analyze
./transcribe_mp4.2.3.sh --file "/path/video.mp4" --exec
```

## 5. Batch Execution

```bash
./transcribe_mp4.2.3.sh --folder "/path/videos" --exec --model large-v3 --lang en
```

## 6. Expected Paths

- Whisper executable: `./whisper.cpp/build/bin/whisper-cli`
- Models directory: `./whisper.cpp/models/`
- Python environment: `./whisper_env`

## 7. Troubleshooting

- If model file is missing, rerun installer or manually download with `whisper.cpp/models/download-ggml-model.sh`.
- If analysis fails, confirm `ffprobe` and `bc` are installed.
- If build fails, verify C/C++ toolchain and `cmake` setup.

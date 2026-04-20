<!--
Document : README_DeepEcho.md
Auteur : Bruno DELNOZ
Email : bruno.delnoz@protonmail.com
Version : v3.0.0
Date : 2026-04-20 00:00
-->
# DeepEcho Documentation Snapshot

This document aligns with the scripts currently present in the repository and keeps a concise project view.

## Functional Components Present in Repository

1. `install_whisper.sh`
   - Full install/cleanup/reinstall/test workflow for Python Whisper + `whisper.cpp`.
2. `transcribe_mp4.2.3.sh`
   - Single-file and folder transcription.
   - Optional deep audio diagnostics.
   - Optional generated-file cleanup.
3. Historical transcription variants
   - `transcribe_mp4.v1.7.sh`
   - `transcribe_mp4.1.9.sh`
   - `transcribe_mp4.2.1.sh`
   - `transcribe_mp4.bof.sh`
4. Embedded `whisper.cpp`
   - Local source tree used by the transcription toolchain.

## Operational Flow

1. Run installer:

```bash
./install_whisper.sh
```

2. Validate with analyzer mode:

```bash
./transcribe_mp4.2.3.sh --file "/path/video.mp4" --analyze
```

3. Execute transcription:

```bash
./transcribe_mp4.2.3.sh --file "/path/video.mp4" --exec
```

4. Batch mode:

```bash
./transcribe_mp4.2.3.sh --folder "/path/videos" --exec
```

## Important Technical Notes

- Script output formats are controlled by `--output-format`.
- `--exec` is required to trigger real transcription; otherwise the script stays in simulation/informational mode.
- Audio analysis mode depends on `ffprobe` and `bc`.
- Default runtime expects:
  - `./whisper.cpp/build/bin/whisper-cli`
  - `./whisper.cpp/models/`

## Documentation Map

- `README.md` → Main project readme.
- `INSTALL.md` → Installation and validation procedures.
- `WHY.md` → Design rationale and retained structure.
- `CHANGELOG.md` → Documentation update history.

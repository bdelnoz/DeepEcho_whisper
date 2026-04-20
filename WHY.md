<!--
Document : WHY.md
Auteur : Bruno DELNOZ
Email : bruno.delnoz@protonmail.com
Version : v1.0.0
Date : 2026-04-20 00:00
-->
# Why This Repository Exists

## Goal

Provide practical, script-first automation for speech transcription from video files using a local Whisper runtime.

## Design Choices

### 1) Keep installation and transcription separate

- `install_whisper.sh` handles environment/bootstrap.
- `transcribe_mp4.2.3.sh` focuses on operational transcription and diagnostics.

This separation simplifies maintenance and issue isolation.

### 2) Keep multiple script generations

Historical versions are kept in-repo to:

- compare behavior changes,
- recover previous workflows,
- audit evolution of options and diagnostics.

### 3) Use embedded `whisper.cpp`

Bundling `whisper.cpp` inside repository enables:

- local/offline execution patterns,
- deterministic path assumptions in scripts,
- easier onboarding for non-expert users.

### 4) Prioritize diagnostics before execution

Audio analysis mode (`--analyze`) gives actionable ffmpeg fixes before running heavy transcription jobs.

### 5) Preserve command-line usability

Scripts include direct CLI help and modes for real execution vs. simulation behavior.

## Intended Audience

- Users needing fast transcription operations from video files.
- Operators preferring shell scripts over larger application stacks.
- Users requiring `whisper.cpp` + simple repeatable command flows.

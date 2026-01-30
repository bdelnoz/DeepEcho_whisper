# DeepEcho_whisper
Il permet de transformer vos enregistrements en texte clair, prêt pour la recherche, la documentation ou l’archivage.
## 🚀 Fonctionnalités principales
- Transcription automatique des fichiers .mp4
- Traitement récursif de dossiers complets
- Détection de la langue automatique
- Sauvegarde des transcriptions au format .txt ou .md
- Logs détaillés avec statistiques de succès/échec
## ⚙️ Installation
bash
git clone https://github.com/votre-nom/DeepEcho.git
cd DeepEcho
chmod +x deepecho.sh

## 🧩 Utilisation
bash
./deepecho.sh --input /chemin/videos --output /chemin/transcriptions

| Argument | Description |
|-----------|--------------|
| --input | Fichier ou dossier contenant les .mp4 |
| --output | Dossier de destination des fichiers texte |
| --language | (Optionnel) Forcer la langue fr, en, etc.) |
| --verbose | Active le mode verbeux |
## 🧠 Exemple concret
bash
./deepecho.sh --input ~/Videos/overlook --output ~/Transcripts

Transcrit tous les fichiers .mp4 du dossier et enregistre les textes dans ~/Transcripts.
## 🧾 Licence
Ce projet est distribué sous licence MIT.
---
**Auteur :** Bruno Delnoz  
**Version :** 2.5.0  
**Nom de code :** DeepEcho  
**Description :** Transcription WhisperCPP automatisée pour vidéos MP4.

Afficher plus
22:01
DeepEcho
🧠 Overview
DeepEcho is an automatic analysis and transcription tool for .mp4 videos, based on WhisperCPP.
It allows you to transform your recordings into clear text, ready for search, documentation, or archiving.

🚀 Key Features
Automatic transcription of .mp4 files
Recursive processing of entire folders
Automatic language detection
Transcription saved in .txt or .md format
Detailed logs with success/failure statistics
⚙️ Installation
bash
git clone https://github.com/your-name/DeepEcho.git
cd DeepEcho
chmod +x deepecho.sh
🧩 Usage
bash
./deepecho.sh --input /path/to/videos --output /path/to/transcriptions
Argument	Description
--input	File or folder containing .mp4 files
--output	Destination folder for text files
--language	(Optional) Force language (fr, en, etc.)
--verbose	Enable verbose mode
🧠 Practical Example
bash
./deepecho.sh --input ~/Videos/overlook --output ~/Transcripts
Transcribes all .mp4 files in the folder and saves the text files in ~/Transcripts.

🧾 License
This project is distributed under the MIT License.

Author: Bruno Delnoz
Version: 2.5.0
Code name: DeepEcho
Description: Automated WhisperCPP transcription for MP4 videos.

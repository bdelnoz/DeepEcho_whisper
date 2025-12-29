# DeepEcho

## 🧠 Présentation

**DeepEcho** est un outil d’analyse et de transcription automatique de vidéos `.mp4`, basé sur **WhisperCPP**.  
Il permet de transformer vos enregistrements en texte clair, prêt pour la recherche, la documentation ou l’archivage.

## 🚀 Fonctionnalités principales

- Transcription automatique des fichiers `.mp4`
- Traitement récursif de dossiers complets
- Détection de la langue automatique
- Sauvegarde des transcriptions au format `.txt` ou `.md`
- Logs détaillés avec statistiques de succès/échec

## ⚙️ Installation

```bash
git clone https://github.com/votre-nom/DeepEcho.git
cd DeepEcho
chmod +x deepecho.sh
```

## 🧩 Utilisation

```bash
./deepecho.sh --input /chemin/videos --output /chemin/transcriptions
```

| Argument | Description |
|-----------|--------------|
| `--input` | Fichier ou dossier contenant les `.mp4` |
| `--output` | Dossier de destination des fichiers texte |
| `--language` | (Optionnel) Forcer la langue (`fr`, `en`, etc.) |
| `--verbose` | Active le mode verbeux |

## 🧠 Exemple concret

```bash
./deepecho.sh --input ~/Videos/overlook --output ~/Transcripts
```

Transcrit tous les fichiers `.mp4` du dossier et enregistre les textes dans `~/Transcripts`.

## 🧾 Licence

Ce projet est distribué sous licence MIT.

---

**Auteur :** Bruno Delnoz  
**Version :** 2.5.0  
**Nom de code :** DeepEcho  
**Description :** Transcription WhisperCPP automatisée pour vidéos MP4.

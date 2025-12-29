import sys, wave, json
from vosk import Model, KaldiRecognizer

wavfile = sys.argv[1]
model_path = sys.argv[2]
outfile = sys.argv[3]

wf = wave.open(wavfile, "rb")
model = Model(model_path)
rec = KaldiRecognizer(model, wf.getframerate())
texte = ""

while True:
    data = wf.readframes(4000)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        res = json.loads(rec.Result())
        texte += res.get("text", "") + " "

res = json.loads(rec.FinalResult())
texte += res.get("text", "")

with open(outfile, "w", encoding="utf-8") as f:
    f.write(texte)

print(f"[OK] {wavfile} → {outfile}")

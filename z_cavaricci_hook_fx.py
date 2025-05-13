
import librosa
import soundfile as sf
from pydub import AudioSegment, effects
import os

# === CONFIGURATION ===
input_path = "your_recording.m4a"
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

# === STEP 1: Load + Normalize with Pydub ===
raw = AudioSegment.from_file(input_path)
normalized = effects.normalize(raw)
normalized.export(f"{output_dir}/01_normalized.wav", format="wav")

# === STEP 2: Convert to 44.1kHz Mono for processing ===
y, sr = librosa.load(f"{output_dir}/01_normalized.wav", sr=44100, mono=True)
sf.write(f"{output_dir}/02_librosa_clean.wav", y, sr)

# === STEP 3: Pitch correction (Mock-up: plug in real autotune externally)
sf.write(f"{output_dir}/03_pitch_corrected.wav", y, sr)

# === STEP 4: Stereo doubling with pydub ===
clean = AudioSegment.from_wav(f"{output_dir}/03_pitch_corrected.wav")
double = clean.overlay(clean - 6, delay=20)
double.export(f"{output_dir}/04_doubled.wav", format="wav")

# === STEP 5: Add basic reverb by overlaying echoes ===
reverb = clean.overlay(clean - 12, delay=100)
reverb = reverb.overlay(clean - 18, delay=200)
reverb.export(f"{output_dir}/05_fx_reverb.wav", format="wav")

# === STEP 6: Final stylized mix ===
final = double.overlay(reverb - 6)
final.export(f"{output_dir}/Z_Cavaricci_Hook_Stylized.wav", format="wav")

# === Optional: Export stems ===
clean.export(f"{output_dir}/stem_dry.wav", format="wav")
double.export(f"{output_dir}/stem_doubled.wav", format="wav")
reverb.export(f"{output_dir}/stem_reverb.wav", format="wav")

print("✅ Stylized vocal processed and exported to:", output_dir)

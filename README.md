
# Z Cavaricci Hook FX Processor

This Python script processes a vocal recording into a stylized, auto-tune-ready hook inspired by early RiFF RAFF and Lil Debbie vibes. It simulates doubling, reverb, and prepares stems for Cubasis or any DAW.

## Requirements
- Python 3.8+
- ffmpeg installed and in system PATH
- `pip install pydub librosa soundfile`

## Usage
1. Place your voice recording as `your_recording.m4a` in the project root.
2. Run the script:
```bash
python z_cavaricci_hook_fx.py
```
3. Outputs go to `/output`, including final WAV and vocal stems.

## Files Generated
- `Z_Cavaricci_Hook_Stylized.wav`: The final polished hook.
- `stem_dry.wav`: Dry voice
- `stem_doubled.wav`: Stereo widened version
- `stem_reverb.wav`: Reverb trail

Customize the script as needed for your vocal chain or DAW integration.

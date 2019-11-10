#! /usr/bin/env python3


def load_file(in_file):
    import librosa
    print("Loading file " + in_file)
    real_sr = librosa.get_samplerate(in_file)
    signal, sr = librosa.load(in_file, sr=real_sr)
    print("Sample rate: {0}".format(sr))
    return signal, sr


def extract_rms(signal, window=2048):
    import librosa.feature
    print("Extracting RMS loudness...")
    # We don't want overlap, so frame_length == hop_length
    rms_vals = librosa.feature.rms(y=signal, frame_length=window, hop_length=window)
    print(rms_vals)
    return rms_vals


def get_onsets(signal, sr=48000):
    import librosa.onset
    onset_pos = librosa.onset.onset_detect(signal, sr, units='frames')
    print(onset_pos)
    return onset_pos, sr

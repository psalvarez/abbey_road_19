#! /usr/bin/env python3
import argparse
import librosa
import librosa.feature


def load_file(in_file):
    print("Loading file " + in_file)
    real_sr = librosa.get_samplerate(in_file)
    signal, sr = librosa.load(in_file, sr=real_sr)
    print("Sample rate: {0}".format(sr))
    return signal, sr


def extract_rms(signal, window=2048):
    print("Extracting RMS loudness...")
    # We don't want overlap, so frame_length == hop_length
    rms_vals = librosa.feature.rms(y=in_signal, frame_length=window, hop_length=window)
    print(rms_vals)
    return rms_vals


def menu():
    parser = argparse.ArgumentParser(description='Extract features from audio signal')
    parser.add_argument('-f', '--file', default='sounds/annoying_arp.wav')
    parser.add_argument('-l', '--frame-length', default=2048)
    args = parser.parse_args()

    return args


if __name__ == "__main__":
    params = menu()
    in_signal, sr = load_file(params.file) 
    rms_vals = extract_rms(in_signal, window=int(params.frame_length))
    print("Done")

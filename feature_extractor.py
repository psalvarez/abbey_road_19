#! /usr/bin/env python3
import argparse
import librosa
import librosa.feature


def load_file(in_file):
    print("Loading file " + in_file)
    real_sr = librosa.get_samplerate(in_file)
    signal, sr = librosa.load(in_file, sr=real_sr)
    return signal, sr


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Extract features from audio signal')
    parser.add_argument('-f', '--file', default='sounds/annoying_arp.wav')
    parser.add_argument('-l', '--frame-length', default=2048)
    args = parser.parse_args()

    in_signal, sr = load_file(args.file) 
    window = int(args.frame_length)
    # We don't want overlap, so frame_length == hop_length
    rms_vals = librosa.feature.rms(y=in_signal, frame_length=window, hop_length=window)

    print(rms_vals)
    print(sr)

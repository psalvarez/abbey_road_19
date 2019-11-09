#! /usr/bin/env python3
import argparse
import librosa
import librosa.feature


def load_file(in_file):
    real_sr = librosa.get_samplerate(in_file)
    signal, sr = librosa.load(in_file, sr=real_sr)
    return signal, sr


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Extract features from audio signal')
    parser.add_argument('-f', '--file', default='sounds/annoying_arp.wav')
    args = parser.parse_args()

    signal, sr = load_file(args.file) 
    print(sr)


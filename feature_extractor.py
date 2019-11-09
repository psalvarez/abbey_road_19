#! /usr/bin/env python3
import argparse
import librosa
import librosa.feature

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Extract features from audio signal')
    parser.add_argument('-f', '--file', default='sounds/annoying_arp.wav')
    args = parser.parse_args()

    sr = librosa.get_samplerate(args.file)
    signal, sr = librosa.load(args.file, sr=sr)
    print(sr)

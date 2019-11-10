#! /usr/bin/env python3
import argparse
import librosa
import librosa.display
import matplotlib.pyplot as plt

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', required=True)
    args = parser.parse_args()
    
    real_sr = librosa.get_samplerate(args.f)
    y, sr = librosa.load(args.f, sr=real_sr)
    print([i for i in range(len(y)) if y[i] != 0])
    librosa.display.waveplot(y, sr)
    plt.show()

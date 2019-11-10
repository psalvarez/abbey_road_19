#! /usr/bin/env python3
import write_wav_file
import numpy as np
import feature_extractor

import os


def menu():
    import argparse
    parser = argparse.ArgumentParser(description='Extract features from audio signal')
    parser.add_argument('-f', '--file', default='sounds/annoying_arp_mono.wav')
    parser.add_argument('-l', '--frame-length', default=2048, type=int)
    parser.add_argument('--rms', action='store_true')
    parser.add_argument('--onset', action='store_true')
    args = parser.parse_args()

    return args


def feature_select(params):
    in_signal, sr = load_file(params.file)
    if params.rms:
        out_signal, sr = extract_feature(in_signal, window=frame_length)
    elif params.onsets:
        out_signal, sr = extract_feature(in_signal, sr=sr)
    else:
        print("You didn't choose anything, you moron")

    return out_signal, sr


if __name__ == '__main__':
    params = menu()
    rms_values, sample_rate = feature_extractor.main(params.file, params.frame_length)
    rms_wav_filename = "{0}_rms.wav".format(os.path.basename(os.path.splitext(params.file)[0]))
    write_wav_file.write_wav_file(rms_wav_filename, rms_values, sample_rate, params.frame_length)


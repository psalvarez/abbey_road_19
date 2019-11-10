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


def feature_select(params, in_signal, sr):
    feat_name = ""
    if params.rms:
        out_signal = feature_extractor.extract_rms(in_signal, window=params.frame_length)
        feat_name = "rms"
    elif params.onset:
        out_signal = feature_extractor.get_onsets(in_signal, sr=sr)
        feat_name = "onset"
    else:
        print("You didn't choose anything, you moron")
        return False

    return out_signal, feat_name


if __name__ == '__main__':
    params = menu()
    in_signal, sr = feature_extractor.load_file(params.file)
    c_signal, feat_name = feature_select(params, in_signal, sr)
    c_wav_filename = "{0}_{1}.wav".format(os.path.basename(os.path.splitext(params.file)[0]), feat_name)
    write_wav_file.write_wav_file(c_wav_filename, c_signal, feat_name, sr, frame_length=params.frame_length, input_stream=in_signal)


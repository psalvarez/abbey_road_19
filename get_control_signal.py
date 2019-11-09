import write_wav_file
import numpy as np
import feature_extractor

import os


def menu():
    import argparse
    parser = argparse.ArgumentParser(description='Extract features from audio signal')
    parser.add_argument('-f', '--file', default='sounds/annoying_arp.wav')
    parser.add_argument('-l', '--frame-length', default=2048, type=int)
    args = parser.parse_args()

    return args


if __name__ == '__main__':
    params = menu()
    rms_values, sample_rate = feature_extractor.main(params.file, params.frame_length)
    rms_wav_filename = "{0}_rms.wav".format(os.path.basename(os.path.splitext(params.file)[0]))
    write_wav_file.write_wav_file(rms_wav_filename, rms_values, sample_rate, params.frame_length)


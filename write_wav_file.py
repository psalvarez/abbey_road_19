import soundfile
import numpy as np
import sys
import os

"""
Given sample rate (input and output), frame length, and the data array (1-D)
"""


def write_wav_file(file_name, data, sample_rate=48000, frame_length=1):
    if os.path.splitext(file_name)[0] != 'wav':
        file_name = file_name.replace(os.path.splitext(file_name)[0], 'wav')
    if frame_length != 1:
        output_data = np.zeros(sample_rate * frame_length)
        for i in range(len(data)):
            for j in range(frame_length):
                print(i*j+j)
                output_data[(i*j)+j] = data[i]
    else:
        output_data = data
    print('Output data, with dimensions {}, looks like...'.format(output_data.shape))
    print(output_data)
    soundfile.write(file_name, output_data, sample_rate)


if __name__ == '__main__':
    rms_values = np.random.rand(10)
    write_wav_file('test_output.wav', rms_values, 10, 3)

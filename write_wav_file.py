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
    data_dims = data.shape[0]
    if frame_length != 1:
        output_data = np.zeros((data_dims, sample_rate * frame_length))
        for dim in range(data_dims):
            for i in range(len(data[dim])):
                for j in range(frame_length):
                    output_data[dim, (i*frame_length)+j] = data[dim][i]
    else:
        output_data = data
    print('Output data, with dimensions {}, looks like...'.format(output_data.shape))
    print(output_data)
    soundfile.write(file_name, output_data, sample_rate)


if __name__ == '__main__':
    rms_values = np.random.rand(1, 10)
    write_wav_file('test_output.wav', rms_values, 10, 3)

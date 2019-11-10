import soundfile
import numpy as np
import sys
import librosa
import os

"""
Given sample rate (input and output), frame length, and the data array (1-D)
"""


def generate_rms_output(data, frame_length):
    data_dims = data.shape[0]
    if frame_length != 1:
        output_data = np.zeros((data_dims, len(data[0]) * frame_length))
        for dim in range(data_dims):  # Looping through no. of channels (expect 1 for mono)
            for i in range(len(data[dim])):
                for j in range(frame_length):  # Looping through data array, repeating value for each frame
                    output_data[dim, (i*frame_length)+j] = data[dim][i]
    else:
        output_data = data
    output_data = output_data.transpose()
    return output_data


def generate_offset_output(data, input_stream):
    output_data = np.zeros((len(input_stream), 1))
    for i in data:
        output_data[i][0] = 1

    return output_data


def write_wav_file(file_name, data, feature, sample_rate=48000, frame_length=2048, input_stream=None):
    if feature == 'rms':
        output_data = generate_rms_output(data, frame_length)
    elif feature == 'onset':
        output_data = generate_offset_output(data, input_stream)
    print('Output data, with dimensions {}, looks like...'.format(output_data.shape))
    print(output_data)
    # soundfile.write(file_name, output_data, sample_rate)
    print(file_name)
    librosa.output.write_wav(file_name, output_data, sample_rate)


if __name__ == '__main__':
    rms_values = np.random.rand(1, 10)
    write_wav_file('test_output.wav', rms_values, 10, 3)

import librosa
import speech_recognition as sr
import os
import numpy as np
# import tensorflow as tf

train_audio_path = "C:/Users/Hashara/Downloads/sdgp_wav"


def get_file_paths(dirname):
    file_paths = []
    for root, directories, files in os.walk(dirname):
        for filename in files:
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)
            print("loading files")
    return file_paths


def recognize_multiple(file):
    r = sr.Recognizer()
    with sr.WavFile(file) as source:  # use "test.wav" as the audio source
        audio = r.record(source)  # extract audio data from the file
        print("In Recognize_multiple method")

        # r = sr.Recognizer()
        # with sr.Microphone() as source:
        #     print("Say something!")
        #     audio = r.listen(source)
    try:
        print("lol")
        print("Transcription: " + r.recognize_google(audio))  # recognize speech using Google Speech Recognition
        sentence = r.recognize_google(audio)
        tokens = list(sentence.lower().split()) 
        print(len(tokens))
        

        vocab, index = {}, 1
        vocab['<pad>'] = 0  # add a padding token
        
        for token in tokens:
            if token not in vocab:
                vocab[token] = index
                index += 1
        vocab_size = len(vocab)
        print(vocab)

        inverse_vocab = {index: token for token, index in vocab.items()}
        print(inverse_vocab)

        example_sequence = [vocab[word] for word in tokens]
        print(example_sequence)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:  # speech is unintelligible
        print("Could not request results from Google Speech Recognition service; {0}".format(e))


def main():
    print("njfeiw")
    files = get_file_paths(train_audio_path)
    for file in files:  # execute for each file
        (filepath, ext) = os.path.splitext(file)  # get the file extension
        file_name = os.path.basename(file)  # get the basename for writing to output file
        print(file_name)  # only interested if extension is '.wav'
        recognize_multiple(file)


if __name__ == '__main__':
    main()

# import speech_recognition as sr
# import os
#
# r = sr.Recognizer()
# with sr.AudioFile("C:/Users/Ieshitha Wijetunge/Downloads/Audio/F_0101_14y8m_1.wav") as source:     # use "test.wav" as the audio source
#     audio = r.record(source)                        # extract audio data from the file
#     print("yo")
#     try:
#         print("lol")
#         print("Transcription: " + r.recognize_google(audio))   # recognize speech using Google Speech Recognition
#     except sr.UnknownValueError:
#         print("Google Speech Recognition could not understand audio")
#     except sr.RequestError as e:  # speech is unintelligible
#         print("Could not request results from Google Speech Recognition service; {0}".format(e))

# sentence = r.recognize_google(audio)
# tokens = list(sentence.lower().split())
# print(len(tokens))
#
# vocab, index = {}, 1
# vocab['<pad>'] = 0   # add a padding token
# for token in tokens:
#   if token not in vocab:
#     vocab[token] = index
#     index += 1
# vocab_size = len(vocab)
# print(vocab)
#
# inverse_vocab = {index: token for token, index in vocab.items()}
# print(inverse_vocab)
#
# example_sequence = [vocab[word] for word in tokens]
# print(example_sequence)


# model = tf.keras.Sequential([
#     example_sequence,
#     tf.keras.layers.Embedding(
#         input_dim=len(example_sequence.get_vocabulary()),
#         output_dim=64,
#         # Use masking to handle the variable sequence lengths
#         mask_zero=True),
#     tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(64)),
#     tf.keras.layers.Dense(64, activation='relu'),
#     tf.keras.layers.Dense(1)
# ])
# print([layer.supports_masking for layer in model.layers])
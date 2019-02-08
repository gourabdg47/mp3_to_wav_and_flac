from pydub import AudioSegment
import argparse
import os

def convert(format, folder_path):
    for a,b,mp in os.walk(folder_path):
        for files in mp:
            if files.endswith(('mp3')):

                sound = os.path.join(a,files)

                if format == 'both':
                    sound_wav = sound.split('.')[0]
                    sound_wav = sound_wav + '.wav'
                    sound_conv_wav = AudioSegment.from_mp3(sound)
                    sound_conv_wav.export(sound_wav, format="wav")

                    print(sound_wav)
                    
                    sound_wav = sound.split('.')[0]
                    sound_wav = sound_wav + '.flac'
                    sound_conv_flac = AudioSegment.from_mp3(sound)
                    sound_conv_flac.export(sound_wav,format = "flac")

                    print(sound_wav)

                elif format == 'wav':

                    sound_wav = sound_wav + '.wav'
                    sound_conv_wav = AudioSegment.from_mp3(sound)
                    sound_conv_wav.export(sound_wav, format="wav")
                    #print(sound_wav)

                elif format == 'flac':

                    sound_wav = sound_wav + '.flac'
                    sound_conv_flac = AudioSegment.from_mp3(sound)
                    sound_conv_flac.export(sound_wav,format = "flac")
                    #print(sound_wav)



test_arg = argparse.ArgumentParser()

test_arg.add_argument('--format', type=str, default='both', help="both, wav, flac")
test_arg.add_argument('--folder_path', type=str, default='data/7008089991', help="Raw/noisy wav file/folder")

args = test_arg.parse_args()

convert(args.format, args.folder_path)
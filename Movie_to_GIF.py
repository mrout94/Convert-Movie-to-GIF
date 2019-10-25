import imageio
import os
import sys

SPEED_MULTIPLIER = 5
MOVIE_FILE = 'movie_case007.mpg'

def convertFile(inputpath, targetFormat):
    outputpath = os.path.splitext(inputpath)[0] + targetFormat
    print("You are converting\r\n\t{0}\r\nto\r\n\t{1}. Thanks for using my program.".format(inputpath, outputpath))

    movie_file = imageio.get_reader(inputpath)
    fps = movie_file.get_meta_data()['fps']

    gif_file = imageio.get_writer(outputpath, fps=fps)
    for i,im in enumerate(movie_file):
        if i % SPEED_MULTIPLIER == 0:
            sys.stdout.write("\rProcessing Frame number {0}".format(i))
            sys.stdout.flush()
            gif_file.append_data(im)
    gif_file.close()
    return outputpath

cwd = os.getcwd()
Video_file = os.path.join(cwd, MOVIE_FILE)
gif_path = convertFile(Video_file, ".gif")

command = 'gifsicle --optimize ' + gif_path + ' --colors 256 --output ' + os.path.join(cwd, 'optimized_gif.gif')
bat_file = os.path.join(cwd, 'GIF_OPTIMIZER.bat')
with open(bat_file, 'w+') as f:
    f.write(command)

print("\nDone.")

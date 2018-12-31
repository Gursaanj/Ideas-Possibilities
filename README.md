# Ideas-Possibilities

In this Branch

I create some audio tools that I could use to pipeline any sounds files I might want to tackle with future projects

I was thinking of making a rhythm game for Unity, and wanted to create "power-ups" or things of that nature where the music or certain sound effects would be effected as a consequence from the player's actions.

In this case I wanted to alter the rate (BPM) and pitch of the sounds depending on how responsive the player was (a more distortive pitch would indicate lower the acceptable performance).

So I created some python script that would take the output sounds file that is generated at periodic times and use that information to either quicken, deepen, or demonize the voice. The sound file (wav) was regenerated and ready to be imported to the appropriate file system (and delete the generated file in the process).

The Fourier transform file was for more general approaches to wave transformation. In this case, I intend to use it (haven't not used it as of yet) to take sound file or a wavelength of color and output and Fourier transform in phase space or vice versa. One application I see this being used for is in color objectification.

for example, If I were to create to take certain sounds (say generated from the player) I could turn them into sinusoidal waves that would correspond with a color and amplitude, A visualizer inn real time. So a louder voice with higher pitch will correspond a wave with larger amplitude and high frequency (so something more bluer). This transform will be useful and easy to integrate to certain pipelines. 

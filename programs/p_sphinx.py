from pocketsphinx import LiveSpeech

speech = LiveSpeech(lm=False, keyphrase='forward', kws_threshold=1e+20)
for phrase in speech:
    print(phrase.segments(detailed=True))

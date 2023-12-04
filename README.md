# Expert-Novice dataset with augmentations

This is the augmented Expert-Novice dataset from paper [Expert and Novice Evaluations of Piano Performances](https://ismir2023program.ismir.net/poster_129.html) by Dr. Jiang, with original dataset in [zenodo](https://zenodo.org/records/8392772). This augmentation includes:  

1. Transcription into MIDI files by the [Bytedance high-resolution model](https://github.com/tangjjbetsy/ATEPP/tree/master/piano_transcription-master) (original wav not included in this repo). 
    - [X] Manually check each transcription file to ensure the onset are correct. Overall the quality is pretty good as the pieces are simple.
2. GPT4 cleaned instructor and rater feedback with question-answers in ```evaluation_qa.csv``` 
3. Annotated the error regions in the same fashion as the Burgmuller set (Separate MIDI track with pitch 0 covering the error region), according to the rater feedback. New tracks are ```*-annot.mid```, ones without annotations are free of salient mistake regions. The type of mistake is briefly discussed in ```mistake_notes.pdf```


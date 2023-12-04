# move the annotation into note 0 of the other track
import glob
from mido import MidiFile


mid_annotations = glob.glob("**/TheBlues-15-annot.mid", recursive=True)

for ma_path in mid_annotations:
	mid = MidiFile(ma_path)
	for message in mid.tracks[2]:
		if message.type in ['note_on', 'note_off']:
			message.note = 0

	mid.save(ma_path)

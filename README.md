# Basic usage
1. Type subject ID, KID ID, date, or experiment ID into the subject field. This will update a list of matching subjects as you type.
2. Select subject from list, and press <Enter>
3. Type keywords into variable field to search for .mat or .csv files.
4. Select and press <Enter> on filenames to draw onto plot.
5. Select and press <Enter> on video files to load them.

# Playback
- On stream plot, move and resize the red/black bar to set the window viewing position.
- Click the stream plot to seek the videos to a new position.
- Press `<Space>` to toggle the playback of videos.
- `<Right Arrow>` to go to next frame.
- `<Left Arrow>` to go 0.25 seconds backward.
- `<Down Arrow>` to go 10 seconds forward.
- `<Up Arrow>` to go 10 seconds backward.
- Click the variable name on the stream plot to close that variable.

# Additional notes
- derived/ folder is the default working folder. You can specify a different working directory by typing another location into the “variable” entry field and pressing <Enter>.
..* e.g. type “extra_p/” to view and select files from extra_p/ folder
- You can load a subject that is not on multiwork by typing out the full path location into the subject field and press <Enter>.
..* e.g. “c:/users/multisensory/desktop/subject0001/”
- You can save the current video layout by pressing <SaveLayout> button. This saves to config/layout.txt in the vislite.exe folder. Next time you load video files, it will place the videos into the saved positions. To go back to default layout, just delete config/layout.txt.
- You can add or remove “favorites” files by editing config/favorites.txt.

# Requirements
- Subjects must have the following:
..*  derived/ folder
....*  cevent_trials.mat
....* timing.mat with two required fields,
......* trialInfo.camRate
......* trialInfo.camTime
....* extract_range.txt file in either supporting_files/ or extra_p/
......* This file contains the offset between the beginning of the video file and 30sec mark in the .mat files.
..* .mat files must be saved as a matlab structure, with the data located in the structure, sdata.data
..* .csv files must be comma separated, no headers
..* Video files must be synchronized. They can have different frame rates however. Note that if they have different frame rates, navigating with <Right Arrow> will not be synchronized.



Contact info:
Seth Foster
fosterbseth@gmail.com

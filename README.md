# Speech-Perception-Experiment-Programming
jsPsych/Cognition.run speech-perception experiment with audio playback, drag-and-drop classification, and behavioral data collection.

# Speech Perception Free Classification Task

JavaScript/jsPsych implementation of an interactive speech-perception free-classification experiment designed for deployment in Cognition.run.

Participants listen to speech stimuli and arrange sound tokens spatially according to their perceived similarity. Final x/y coordinates are saved for later analysis of perceptual grouping and category structure.

## Task Structure

The experiment includes:

- Participant ID entry
- Experimental condition and phase tracking
- Instruction screen
- One practice classification screen with 6 stimuli
- Five experimental classification screens
- 12 stimuli per experimental screen
- 60 total experimental placements
- Completion screen

## Experimental Conditions

The script supports multiple experimental conditions through URL parameters:

- `VOT_Bimodal`
- `VOT_Unimodal`
- `Voicing_Bimodal`
- `Voicing_Unimodal`

It also supports:

- Pretest
- Posttest
- Preview mode

Condition, phase, participant ID, and day are automatically stored with the behavioral data.

## Free-Classification Interface

Each experimental screen displays speech stimuli as colored dots arranged around a large classification circle.

Participants can:

- Hover over a dot to hear its associated speech stimulus
- Click a dot to replay the stimulus
- Drag individual dots into the classification area
- Position perceptually similar sounds closer together
- Position perceptually different sounds farther apart

The starting locations of the dots are randomized while the stimulus composition of each screen remains fixed.

## Stimulus Structure

Each experimental screen contains 12 speech tokens representing:

- Voiceless unaspirated stops
- Voiceless aspirated stops
- Voiced unaspirated stops
- Naturally produced breathy-voiced stops
- Prevoicing diagnostic stimuli
- VOT diagnostic stimuli

Tokens from two speakers are represented on each screen.

## Data Collection

The script saves one structured data row for each classification screen.

For every stimulus, the output includes:

- Audio filename
- Token label
- Stop category
- Speaker
- Stimulus class
- Final x-coordinate
- Final y-coordinate
- Number of stimulus plays

Additional trial-level information includes:

- Participant ID
- Experimental condition
- Experimental phase
- Day
- Practice/experimental status
- Screen number
- Stimulus set
- Number of items
- Screen completion time

The resulting coordinate data can be used for later spatial-similarity, clustering, or perceptual-category analyses.

## Programming Features

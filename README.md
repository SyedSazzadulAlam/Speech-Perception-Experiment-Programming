# Speech Perception and Production Experiment Programming

Experimental programming for behavioral speech research using **PsychoPy/Python** and **jsPsych/Cognition.run**.

This repository contains custom code developed for speech-perception and speech-production experiments, including stimulus management, randomization, audio presentation, response collection, interactive classification, timing, condition handling, and structured behavioral data output.

## Technologies

- Python
- PsychoPy
- JavaScript
- jsPsych 7
- Cognition.run
- HTML/CSS

## PsychoPy Experiments

### Production Task

Python/PsychoPy implementation of a speech-production task.

Custom code includes:

- Automatic loading of production-picture stimuli
- Image-file filtering
- Validation of the expected stimulus set
- Randomization of presentation order
- Trial/stimulus indexing
- Experimental sanity checks and debugging output
- Integration with the PsychoPy experiment workflow

For example, the experiment verifies that all expected production stimuli are available before starting and randomizes their order for each run.

Additional PsychoPy tasks in this repository may include speech-perception, exposure, and discrimination experiments.

## Free-Classification Task

The Cognition.run/jsPsych implementation provides an interactive free-classification experiment in which participants listen to speech stimuli and arrange sound tokens spatially according to perceived similarity.

### Task Structure

The experiment includes:

- Participant ID entry
- Experimental condition and phase tracking
- Instruction screen
- One practice classification screen with 6 stimuli
- Five experimental classification screens
- 12 stimuli per experimental screen
- 60 total experimental placements
- Completion screen

### Experimental Conditions

The script supports:

- `VOT_Bimodal`
- `VOT_Unimodal`
- `Voicing_Bimodal`
- `Voicing_Unimodal`

It also supports pretest, posttest, and preview modes.

## Interactive Classification Interface

Participants can:

- Hover over a stimulus to hear its associated speech sound
- Click to replay the stimulus
- Drag stimuli into a classification circle
- Position perceptually similar sounds closer together
- Position perceptually different sounds farther apart

Starting positions are randomized while the stimulus composition of each screen remains controlled.

## Data Collection

The experimental scripts collect structured behavioral data including, where relevant:

- Participant and condition information
- Experimental phase
- Stimulus identity
- Speaker
- Stimulus category
- Response accuracy
- Reaction time
- Presentation order
- Audio play counts
- Final spatial coordinates
- Trial/screen completion information

These outputs can be used for subsequent statistical, perceptual-similarity, clustering, and category-learning analyses.

## Programming Features

The repository demonstrates:

- Experimental programming in Python and JavaScript
- PsychoPy experiment development
- jsPsych/Cognition.run deployment
- Stimulus-file management
- Input and stimulus validation
- Randomization
- Trial sequencing
- Audio presentation
- Interactive HTML/CSS interfaces
- Mouse-event handling
- Custom drag-and-drop behavior
- Timing measurement
- Behavioral data collection
- Error handling
- Reproducible experimental workflows

## Repository Structure

```text
Speech-Perception-Experiment-Programming/
├── README.md
├── cognition/
│   └── free_classification_cognition_run.js
└── psychopy/
    └── production_task.py
```

Additional PsychoPy experiment scripts can be added as the repository develops.

## Research Context

These tasks were developed for experimental research in speech perception, speech production, non-native sound-category learning, and perceptual category formation.

The repository focuses on the **programming and experimental-design components** of the research. Participant data and restricted research stimuli are not included.

## Data and Stimuli

Audio files, participant data, and restricted experimental stimuli are excluded from the public repository where research ethics, licensing, or data-sharing restrictions apply.

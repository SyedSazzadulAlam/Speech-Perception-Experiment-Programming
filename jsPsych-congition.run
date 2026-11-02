// ======================================================
// FREE CLASSIFICATION TASK
// Cognition.run / jsPsych 7
//
// SIMPLE CSV VERSION
// - Participant ID screen
// - Instruction screen
// - 1 practice grouping screen with 6 sound dots
// - 5 real grouping screens
// - 12 dots per real screen = 60 total real placements
// - Clean CSV output
// - One row per screen
// - Only final x/y coordinates saved
// - Speaker saved for each stimulus
// - Stimulus class saved for each stimulus
// - Moves properly from practice to screen 1 to 2 to 3 to 4 to 5
// ======================================================


// -------------------- BASIC SETTINGS --------------------

const urlParams = new URLSearchParams(window.location.search);

let PARTICIPANT_ID = urlParams.get("participant") || "";

const CONDITION = urlParams.get("condition") || "PREVIEW";

const VALID_CONDITIONS = [
  "VOT_Bimodal",
  "VOT_Unimodal",
  "Voicing_Bimodal",
  "Voicing_Unimodal",
  "PREVIEW"
];

if (!VALID_CONDITIONS.includes(CONDITION)) {
  throw new Error(
    `Invalid condition "${CONDITION}".`
  );
}

const PHASE = urlParams.get("phase") || "PREVIEW";

const VALID_PHASES = [
  "pretest",
  "posttest",
  "PREVIEW"
];

if (!VALID_PHASES.includes(PHASE)) {
  throw new Error(
    `Invalid phase "${PHASE}". This task only supports pretest and posttest.`
  );
}

const DAY =
  PHASE === "pretest" ? 1 :
  PHASE === "posttest" ? 2 :
  "PREVIEW";

// -------------------- INITIALIZE JSPSYCH --------------------

const jsPsych = initJsPsych({
  on_finish: function () {
    // Cognition.run should save the data automatically.
  }
});


// -------------------- PARTICIPANT ID SCREEN --------------------

const participantIdTrial = {
  type: jsPsychHtmlKeyboardResponse,
  choices: "NO_KEYS",

  stimulus: `
    <div style="font-family: Arial, sans-serif; max-width: 800px; margin: 70px auto; text-align: center;">
      <h2>Participant Information</h2>

      <p style="font-size: 20px; line-height: 1.5;">
        Please enter the participant number assigned by the researcher.
      </p>

      <p style="font-size: 18px; line-height: 1.5;">
        Current condition: <strong>${CONDITION}</strong><br>
        Current phase: <strong>${PHASE}</strong><br>
        Current day code: <strong>${DAY}</strong>
      </p>

      <input
        id="participant-id-input"
        type="text"
        placeholder="Example: VOTB001"
        style="font-size: 22px; padding: 10px; width: 280px; text-align: center;"
      />

      <br><br>

      <button
        id="participant-id-submit"
        type="button"
        style="font-size: 20px; padding: 12px 28px;"
      >
        Continue
      </button>

      <div
        id="participant-id-warning"
        style="color: darkred; font-size: 18px; margin-top: 20px; font-weight: bold;"
      ></div>
    </div>
  `,

  on_load: function () {
    const input = document.getElementById("participant-id-input");
    const button = document.getElementById("participant-id-submit");
    const warning = document.getElementById("participant-id-warning");

    if (PARTICIPANT_ID !== "") {
      input.value = PARTICIPANT_ID;
    }

    button.addEventListener("click", function (e) {
      e.preventDefault();

      const enteredId = input.value.trim();

      if (enteredId === "") {
        warning.innerText = "Please enter a participant number.";
        return;
      }

      PARTICIPANT_ID = enteredId;

      jsPsych.data.addProperties({
        participant_id: PARTICIPANT_ID,
        condition: CONDITION,
        phase: PHASE,
        day: DAY
      });

      jsPsych.finishTrial({
        task_type: "participant_id_entry",
        participant_id: PARTICIPANT_ID,
        condition: CONDITION,
        phase: PHASE,
        day: DAY
      });
    });
  }
};


// -------------------- PRACTICE STIMULI --------------------

// IMPORTANT:
// Replace these example practice audio names later with your actual
// 6 practice audio files.
//
// These should ideally NOT be part of your real experimental stimulus set.

const practiceScreenInfo = {
  screen_number: "practice",
  word_set: "practice",
  stimuli: [
    {
      token_label: "practice1",
      stop_type: "practice",
      speaker: "practice",
      stimulus_class: "practice",
      audio: "ba.wav"
    },
    {
      token_label: "practice2",
      stop_type: "practice",
      speaker: "practice",
      stimulus_class: "practice",
      audio: "bha.wav"
    },
    {
      token_label: "practice3",
      stop_type: "practice",
      speaker: "practice",
      stimulus_class: "practice",
      audio: "pa.wav"
    },
    {
      token_label: "practice4",
      stop_type: "practice",
      speaker: "practice",
      stimulus_class: "practice",
      audio: "pha.wav"
    },
    {
      token_label: "practice5",
      stop_type: "practice",
      speaker: "practice",
      stimulus_class: "practice",
      audio: "bha1.wav"
    },
    {
      token_label: "practice6",
      stop_type: "practice",
      speaker: "practice",
      stimulus_class: "practice",
      audio: "pha1.wav"
    }
  ]
};


// -------------------- REAL STIMULUS STRUCTURE --------------------
//
// EACH SCREEN HAS:
//
// 2 x pa       = A + R
// 2 x pha      = A + R
// 2 x ba       = A + R
// 2 x natural bha = A + R
// 2 x PV diagnostic = A + R
// 2 x VOT diagnostic = A + R
//
// TOTAL = 12 stimuli per screen
//
// The stimuli are assigned permanently to their particular screen.
// Their starting positions around the circle are randomized below.
// ---------------------------------------------------------------

const stimuliByScreen = [

  // ==================================================
  // SCREEN 1
  // ==================================================
  {
    screen_number: 1,
    word_set: "set1",

    stimuli: [

      // ---------- PA ----------
      {
        token_label: "pa_A",
        stop_type: "p",
        speaker: "A",
        stimulus_class: "natural",
        audio: "pa1A.wav"
      },
      {
        token_label: "pa_R",
        stop_type: "p",
        speaker: "R",
        stimulus_class: "natural",
        audio: "pa1R.wav"
      },

      // ---------- PHA ----------
      {
        token_label: "pha_A",
        stop_type: "pʰ",
        speaker: "A",
        stimulus_class: "natural",
        audio: "pha1A.wav"
      },
      {
        token_label: "pha_R",
        stop_type: "pʰ",
        speaker: "R",
        stimulus_class: "natural",
        audio: "pha1R.wav"
      },

      // ---------- BA ----------
      {
        token_label: "ba_A",
        stop_type: "b",
        speaker: "A",
        stimulus_class: "natural",
        audio: "ba1A.wav"
      },
      {
        token_label: "ba_R",
        stop_type: "b",
        speaker: "R",
        stimulus_class: "natural",
        audio: "ba1R.wav"
      },

      // ---------- NATURAL BHA ----------
      {
        token_label: "bha_A",
        stop_type: "bʱ",
        speaker: "A",
        stimulus_class: "natural",
        audio: "bha5040A.wav"
      },
      {
        token_label: "bha_R",
        stop_type: "bʱ",
        speaker: "R",
        stimulus_class: "natural",
        audio: "bha5060R.wav"
      },

      // ---------- PV DIAGNOSTIC ----------
      {
        token_label: "PVdiag_A",
        stop_type: "bʱ",
        speaker: "A",
        stimulus_class: "PV_diagnostic",
        audio: "bha_PVdiagnostic1A.wav"
      },
      {
        token_label: "PVdiag_R",
        stop_type: "bʱ",
        speaker: "R",
        stimulus_class: "PV_diagnostic",
        audio: "bha_PVdiagnostic1R.wav"
      },

      // ---------- VOT DIAGNOSTIC ----------
      {
        token_label: "VOTdiag_A",
        stop_type: "bʱ",
        speaker: "A",
        stimulus_class: "VOT_diagnostic",
        audio: "bha_VOTdiagnostic1A.wav"
      },
      {
        token_label: "VOTdiag_R",
        stop_type: "bʱ",
        speaker: "R",
        stimulus_class: "VOT_diagnostic",
        audio: "bha_VOTdiagnostic1R.wav"
      }
    ]
  },


  // ==================================================
  // SCREEN 2
  // ==================================================
  {
    screen_number: 2,
    word_set: "set2",

    stimuli: [

      // ---------- PA ----------
      {
        token_label: "pa_A",
        stop_type: "p",
        speaker: "A",
        stimulus_class: "natural",
        audio: "pa2A.wav"
      },
      {
        token_label: "pa_R",
        stop_type: "p",
        speaker: "R",
        stimulus_class: "natural",
        audio: "pa2R.wav"
      },

      // ---------- PHA ----------
      {
        token_label: "pha_A",
        stop_type: "pʰ",
        speaker: "A",
        stimulus_class: "natural",
        audio: "pha2A.wav"
      },
      {
        token_label: "pha_R",
        stop_type: "pʰ",
        speaker: "R",
        stimulus_class: "natural",
        audio: "pha2R.wav"
      },

      // ---------- BA ----------
      {
        token_label: "ba_A",
        stop_type: "b",
        speaker: "A",
        stimulus_class: "natural",
        audio: "ba2A.wav"
      },
      {
        token_label: "ba_R",
        stop_type: "b",
        speaker: "R",
        stimulus_class: "natural",
        audio: "ba2R.wav"
      },

      // ---------- NATURAL BHA ----------
      {
        token_label: "bha_A",
        stop_type: "bʱ",
        speaker: "A",
        stimulus_class: "natural",
        audio: "bha5050A.wav"
      },
      {
        token_label: "bha_R",
        stop_type: "bʱ",
        speaker: "R",
        stimulus_class: "natural",
        audio: "bha6040R.wav"
      },

      // ---------- PV DIAGNOSTIC ----------
      {
        token_label: "PVdiag_A",
        stop_type: "bʱ",
        speaker: "A",
        stimulus_class: "PV_diagnostic",
        audio: "bha_PVdiagnostic2A.wav"
      },
      {
        token_label: "PVdiag_R",
        stop_type: "bʱ",
        speaker: "R",
        stimulus_class: "PV_diagnostic",
        audio: "bha_PVdiagnostic2R.wav"
      },

      // ---------- VOT DIAGNOSTIC ----------
      {
        token_label: "VOTdiag_A",
        stop_type: "bʱ",
        speaker: "A",
        stimulus_class: "VOT_diagnostic",
        audio: "bha_VOTdiagnostic2A.wav"
      },
      {
        token_label: "VOTdiag_R",
        stop_type: "bʱ",
        speaker: "R",
        stimulus_class: "VOT_diagnostic",
        audio: "bha_VOTdiagnostic2R.wav"
      }
    ]
  },


  // ==================================================
  // SCREEN 3
  // ==================================================
  {
    screen_number: 3,
    word_set: "set3",

    stimuli: [

      // ---------- PA ----------
      {
        token_label: "pa_A",
        stop_type: "p",
        speaker: "A",
        stimulus_class: "natural",
        audio: "pa3A.wav"
      },
      {
        token_label: "pa_R",
        stop_type: "p",
        speaker: "R",
        stimulus_class: "natural",
        audio: "pa3R.wav"
      },

      // ---------- PHA ----------
      {
        token_label: "pha_A",
        stop_type: "pʰ",
        speaker: "A",
        stimulus_class: "natural",
        audio: "pha3A.wav"
      },
      {
        token_label: "pha_R",
        stop_type: "pʰ",
        speaker: "R",
        stimulus_class: "natural",
        audio: "pha3R.wav"
      },

      // ---------- BA ----------
      {
        token_label: "ba_A",
        stop_type: "b",
        speaker: "A",
        stimulus_class: "natural",
        audio: "ba3A.wav"
      },
      {
        token_label: "ba_R",
        stop_type: "b",
        speaker: "R",
        stimulus_class: "natural",
        audio: "ba3R.wav"
      },

      // ---------- NATURAL BHA ----------
      {
        token_label: "bha_A",
        stop_type: "bʱ",
        speaker: "A",
        stimulus_class: "natural",
        audio: "bha6050A.wav"
      },
      {
        token_label: "bha_R",
        stop_type: "bʱ",
        speaker: "R",
        stimulus_class: "natural",
        audio: "bha6050R.wav"
      },

      // ---------- PV DIAGNOSTIC ----------
      {
        token_label: "PVdiag_A",
        stop_type: "bʱ",
        speaker: "A",
        stimulus_class: "PV_diagnostic",
        audio: "bha_PVdiagnostic3A.wav"
      },
      {
        token_label: "PVdiag_R",
        stop_type: "bʱ",
        speaker: "R",
        stimulus_class: "PV_diagnostic",
        audio: "bha_PVdiagnostic3R.wav"
      },

      // ---------- VOT DIAGNOSTIC ----------
      {
        token_label: "VOTdiag_A",
        stop_type: "bʱ",
        speaker: "A",
        stimulus_class: "VOT_diagnostic",
        audio: "bha_VOTdiagnostic3A.wav"
      },
      {
        token_label: "VOTdiag_R",
        stop_type: "bʱ",
        speaker: "R",
        stimulus_class: "VOT_diagnostic",
        audio: "bha_VOTdiagnostic3R.wav"
      }
    ]
  },


  // ==================================================
  // SCREEN 4
  // ==================================================
  {
    screen_number: 4,
    word_set: "set4",

    stimuli: [

      // ---------- PA ----------
      {
        token_label: "pa_A",
        stop_type: "p",
        speaker: "A",
        stimulus_class: "natural",
        audio: "pa4A.wav"
      },
      {
        token_label: "pa_R",
        stop_type: "p",
        speaker: "R",
        stimulus_class: "natural",
        audio: "pa4R.wav"
      },

      // ---------- PHA ----------
      {
        token_label: "pha_A",
        stop_type: "pʰ",
        speaker: "A",
        stimulus_class: "natural",
        audio: "pha4A.wav"
      },
      {
        token_label: "pha_R",
        stop_type: "pʰ",
        speaker: "R",
        stimulus_class: "natural",
        audio: "pha4R.wav"
      },

      // ---------- BA ----------
      {
        token_label: "ba_A",
        stop_type: "b",
        speaker: "A",
        stimulus_class: "natural",
        audio: "ba4A.wav"
      },
      {
        token_label: "ba_R",
        stop_type: "b",
        speaker: "R",
        stimulus_class: "natural",
        audio: "ba4R.wav"
      },

      // ---------- NATURAL BHA ----------
      {
        token_label: "bha_A",
        stop_type: "bʱ",
        speaker: "A",
        stimulus_class: "natural",
        audio: "bha7040A.wav"
      },
      {
        token_label: "bha_R",
        stop_type: "bʱ",
        speaker: "R",
        stimulus_class: "natural",
        audio: "bha6060R.wav"
      },

      // ---------- PV DIAGNOSTIC ----------
      {
        token_label: "PVdiag_A",
        stop_type: "bʱ",
        speaker: "A",
        stimulus_class: "PV_diagnostic",
        audio: "bha_PVdiagnostic4A.wav"
      },
      {
        token_label: "PVdiag_R",
        stop_type: "bʱ",
        speaker: "R",
        stimulus_class: "PV_diagnostic",
        audio: "bha_PVdiagnostic4R.wav"
      },

      // ---------- VOT DIAGNOSTIC ----------
      {
        token_label: "VOTdiag_A",
        stop_type: "bʱ",
        speaker: "A",
        stimulus_class: "VOT_diagnostic",
        audio: "bha_VOTdiagnostic4A.wav"
      },
      {
        token_label: "VOTdiag_R",
        stop_type: "bʱ",
        speaker: "R",
        stimulus_class: "VOT_diagnostic",
        audio: "bha_VOTdiagnostic4R.wav"
      }
    ]
  },


  // ==================================================
  // SCREEN 5
  // ==================================================
  {
    screen_number: 5,
    word_set: "set5",

    stimuli: [

      // ---------- PA ----------
      {
        token_label: "pa_A",
        stop_type: "p",
        speaker: "A",
        stimulus_class: "natural",
        audio: "pa5A.wav"
      },
      {
        token_label: "pa_R",
        stop_type: "p",
        speaker: "R",
        stimulus_class: "natural",
        audio: "pa5R.wav"
      },

      // ---------- PHA ----------
      {
        token_label: "pha_A",
        stop_type: "pʰ",
        speaker: "A",
        stimulus_class: "natural",
        audio: "pha5A.wav"
      },
      {
        token_label: "pha_R",
        stop_type: "pʰ",
        speaker: "R",
        stimulus_class: "natural",
        audio: "pha5R.wav"
      },

      // ---------- BA ----------
      {
        token_label: "ba_A",
        stop_type: "b",
        speaker: "A",
        stimulus_class: "natural",
        audio: "ba5A.wav"
      },
      {
        token_label: "ba_R",
        stop_type: "b",
        speaker: "R",
        stimulus_class: "natural",
        audio: "ba5R.wav"
      },

      // ---------- NATURAL BHA ----------
      {
        token_label: "bha_A",
        stop_type: "bʱ",
        speaker: "A",
        stimulus_class: "natural",
        audio: "bha7060A.wav"
      },
      {
        token_label: "bha_R",
        stop_type: "bʱ",
        speaker: "R",
        stimulus_class: "natural",
        audio: "bha7050R.wav"
      },

      // ---------- PV DIAGNOSTIC ----------
      {
        token_label: "PVdiag_A",
        stop_type: "bʱ",
        speaker: "A",
        stimulus_class: "PV_diagnostic",
        audio: "bha_PVdiagnostic5A.wav"
      },
      {
        token_label: "PVdiag_R",
        stop_type: "bʱ",
        speaker: "R",
        stimulus_class: "PV_diagnostic",
        audio: "bha_PVdiagnostic5R.wav"
      },

      // ---------- VOT DIAGNOSTIC ----------
      {
        token_label: "VOTdiag_A",
        stop_type: "bʱ",
        speaker: "A",
        stimulus_class: "VOT_diagnostic",
        audio: "bha_VOTdiagnostic5A.wav"
      },
      {
        token_label: "VOTdiag_R",
        stop_type: "bʱ",
        speaker: "R",
        stimulus_class: "VOT_diagnostic",
        audio: "bha_VOTdiagnostic5R.wav"
      }
    ]
  }
];


// -------------------- BUILD STIMULI FOR EACH SCREEN --------------------

function buildStimuliForCircle(screenInfo) {

  const stimuli = screenInfo.stimuli.map((item, index) => {

    return {
      stimulus_id: `screen${screenInfo.screen_number}_${item.token_label}_${index + 1}`,
      word_set: screenInfo.word_set,

      token_label: item.token_label,
      stop_type: item.stop_type,

      speaker: item.speaker,
      stimulus_class: item.stimulus_class,

      audio: item.audio
    };

  });

  // IMPORTANT:
  // This randomizes the starting LOCATION of the stimuli,
  // but does NOT change which stimuli belong to which screen.

  return jsPsych.randomization.shuffle(stimuli);
}


// -------------------- DOT POSITIONING --------------------

function getCircularDotPositions(
  nDots,
  centerX,
  centerY,
  orbitRadius,
  dotSize
) {

  let positions = [];

  for (let i = 0; i < nDots; i++) {

    const angle =
      -Math.PI / 2 +
      (2 * Math.PI * i) / nDots;

    const xCenter =
      centerX +
      orbitRadius * Math.cos(angle);

    const yCenter =
      centerY +
      orbitRadius * Math.sin(angle);

    positions.push({
      left: xCenter - dotSize / 2,
      top: yCenter - dotSize / 2
    });
  }

  return positions;
}


// -------------------- INSTRUCTION SCREEN --------------------

const instructionTrial = {

  type: jsPsychHtmlKeyboardResponse,

  choices: "NO_KEYS",

  stimulus: `

    <div
      style="
        font-family: Arial, sans-serif;
        max-width: 850px;
        margin: 60px auto;
        text-align: center;
      "
    >

      <h2>Free classification task</h2>

      <p
        style="
          font-size: 20px;
          line-height: 1.5;
        "
      >
        You will see colored dots around a large circle. 
        When you move your mouse over a dot, it will play a sound. 
      </p>

      <p
        style="
          font-size: 20px;
          line-height: 1.5;
        "
      >
        Drag all the dots into the circle. 
        Focus on the first consonant in the sound played by each dot. 
        Place dots that seem to have similar initial consonants closer together. 
        Place dots that seem to have different initial consonants farther apart. 
        Do not cluster the dots according to the similarity of the speakers you hear in their sounds. 
      </p>

      <p
        style="
          font-size: 20px;
          line-height: 1.5;
        "
      >
        You should arrange the dots however you perceive their similarity with one another. 
        There are no right or wrong answers.
      </p>

      <p
        style="
          font-size: 20px;
          line-height: 1.5;
        "
      >
        You will first complete a short practice screen
        before the real task begins.
      </p>

      <button
        id="start-fc"
        type="button"
        style="
          font-size: 20px;
          padding: 12px 28px;
          margin-top: 25px;
        "
      >
        Start practice
      </button>

    </div>
  `,

  on_load: function () {

    document
      .getElementById("start-fc")
      .addEventListener("click", function (e) {

        e.preventDefault();

        jsPsych.finishTrial({

          task_type:
            "free_classification_instructions",

          participant_id:
            PARTICIPANT_ID,

          condition:
            CONDITION,

          phase:
            PHASE,

          day:
            DAY
        });

      });

  }

};


// -------------------- FREE CLASSIFICATION SCREEN --------------------

function createFreeClassificationTrial(
  screenInfo,
  isPractice = false
) {

  return {

    type:
      jsPsychHtmlKeyboardResponse,

    choices:
      "NO_KEYS",


    // --------------------------------------------------
    // STIMULUS HTML
    // --------------------------------------------------

    stimulus: function () {

      const stimuli =
        buildStimuliForCircle(screenInfo);

      window.currentFCStimuli =
        stimuli;


      // ---------- SCREEN SIZE ----------

      const wrapperWidth =
        1000;

      const wrapperHeight =
        900;


      // ---------- LARGE CLASSIFICATION CIRCLE ----------

      const circleSize =
        500;

      const circleRadius =
        circleSize / 2;

      const circleCenterX =
        wrapperWidth / 2;

      const circleCenterY =
        440;

      const circleLeft =
        circleCenterX -
        circleRadius;

      const circleTop =
        circleCenterY -
        circleRadius;


      // ---------- DOT SETTINGS ----------

      const dotSize =
        15;

      const orbitRadius =
        circleRadius + 30;


      const dotPositions =
        getCircularDotPositions(

          stimuli.length,

          circleCenterX,

          circleCenterY,

          orbitRadius,

          dotSize
        );


      // ---------- DOT COLORS ----------

      const dotColors = [

        "#4E79A7",

        "#F28E2B",

        "#E15759",

        "#76B7B2",

        "#59A14F",

        "#EDC948",

        "#B07AA1",

        "#FF9DA7",

        "#9C755F",

        "#BAB0AC",

        "#6B6ECF",

        "#8CD17D"
      ];


      // --------------------------------------------------
      // RETURN SCREEN HTML
      // --------------------------------------------------

      return `

        <style>

          #fc-wrapper {

            width:
              ${wrapperWidth}px;

            height:
              ${wrapperHeight}px;

            margin:
              0 auto;

            position:
              relative;

            font-family:
              Arial, sans-serif;

            user-select:
              none;
          }


          #fc-title {

            position:
              absolute;

            top:
              10px;

            left:
              0;

            width:
              100%;

            text-align:
              center;
          }


          #fc-title h2 {

            margin:
              0 0 18px 0;

            font-size:
              26px;
          }


          #fc-title p {

            margin:
              0;

            font-size:
              20px;

            line-height:
              1.4;
          }


          #circle-area {

            width:
              ${circleSize}px;

            height:
              ${circleSize}px;

            border:
              3px solid #333;

            border-radius:
              50%;

            position:
              absolute;

            left:
              ${circleLeft}px;

            top:
              ${circleTop}px;

            background:
              rgba(245,245,245,0.4);
          }


          .sound-dot {

            width:
              ${dotSize}px;

            height:
              ${dotSize}px;

            border-radius:
              50%;

            position:
              absolute;

            cursor:
              grab;

            border:
              3px solid white;

            box-shadow:
              0 2px 8px rgba(0,0,0,0.35);
          }


          .sound-dot:active {

            cursor:
              grabbing;
          }


          #finish-button {

            position:
              absolute;

            top:
              820px;

            left:
              390px;

            font-size:
              20px;

            padding:
              12px 28px;
          }


          #warning {

            position:
              absolute;

            top:
              875px;

            left:
              0;

            width:
              100%;

            text-align:
              center;

            color:
              darkred;

            font-size:
              18px;

            font-weight:
              bold;
          }

        </style>


        <div id="fc-wrapper">

          <div id="fc-title">

            <h2>
              ${
                isPractice
                  ? "Practice screen"
                  : "Grouping screen " +
                    screenInfo.screen_number +
                    " of 5"
              }
            </h2>

            <p>
              Hover over each dot to hear the sound.
              Drag all dots into the circle.
              Similar initial consonant should be closer together.
            </p>

          </div>


          <div id="circle-area"></div>


          ${
            stimuli.map((stim, i) => {

              const pos =
                dotPositions[i];

              const color =
                dotColors[
                  i % dotColors.length
                ];


              return `

                <div

                  class="sound-dot"

                  id="dot-${i}"

                  data-index="${i}"

                  data-stimulus-id="${stim.stimulus_id}"

                  data-audio="${stim.audio}"

                  data-token-label="${stim.token_label}"

                  data-stop-type="${stim.stop_type}"

                  data-speaker="${stim.speaker}"

                  data-stimulus-class="${stim.stimulus_class}"

                  data-dot-color="${color}"

                  style="
                    left: ${pos.left}px;
                    top: ${pos.top}px;
                    background-color: ${color};
                  "

                ></div>

              `;

            }).join("")
          }


          <button
            id="finish-button"
            type="button"
          >
            ${
              isPractice
                ? "Finish practice"
                : "Finish this screen"
            }
          </button>


          <div id="warning"></div>

        </div>
      `;
    },


    // --------------------------------------------------
    // ON LOAD
    // --------------------------------------------------

    on_load: function () {

      const wrapper =
        document.getElementById(
          "fc-wrapper"
        );

      const finishButton =
        document.getElementById(
          "finish-button"
        );

      const warning =
        document.getElementById(
          "warning"
        );

      const dots =
        Array.from(
          document.querySelectorAll(
            ".sound-dot"
          )
        );


      // ---------- START TIME ----------

      const startTime =
        performance.now();


      // ---------- AUDIO COUNTS ----------

      const playCounts =
        {};

      let currentAudio =
        null;


      // ---------- DRAG VARIABLES ----------

      let activeDot =
        null;

      let offsetX =
        0;

      let offsetY =
        0;


      // --------------------------------------------------
      // SET UP EACH DOT
      // --------------------------------------------------

      dots.forEach((dot) => {

        playCounts[
          dot.dataset.stimulusId
        ] = 0;


        // ---------- LOAD AUDIO ----------

        const audioPath =
          dot.dataset.audio;

        const audioObj =
          new Audio(audioPath);

        audioObj.preload =
          "auto";

        dot.audioObj =
          audioObj;


        // ---------- AUDIO ERROR ----------

        audioObj.addEventListener(
          "error",
          function () {

            console.log(
              "FAILED AUDIO FILE:",
              audioPath
            );

            warning.innerText =
              "Audio file failed to load: " +
              audioPath;

          }
        );


        // ---------- PLAY ON HOVER ----------

        dot.addEventListener(
          "mouseenter",
          function () {

            if (currentAudio) {

              currentAudio.pause();

              currentAudio.currentTime =
                0;
            }


            currentAudio =
              dot.audioObj;

            currentAudio.currentTime =
              0;


            currentAudio
              .play()
              .catch(function (error) {

                console.log(
                  "Audio did not play:",
                  audioPath,
                  error
                );

                warning.innerText =
                  "Audio did not play: " +
                  audioPath +
                  ". Check file name and extension.";

              });


            playCounts[
              dot.dataset.stimulusId
            ] += 1;

          }
        );


        // ---------- STOP WHEN LEAVING DOT ----------

        dot.addEventListener(
          "mouseleave",
          function () {

            if (currentAudio) {

              currentAudio.pause();

              currentAudio.currentTime =
                0;
            }

          }
        );


        // ---------- ALSO PLAY ON CLICK ----------

        dot.addEventListener(
          "click",
          function () {

            if (currentAudio) {

              currentAudio.pause();

              currentAudio.currentTime =
                0;
            }


            currentAudio =
              dot.audioObj;

            currentAudio.currentTime =
              0;


            currentAudio
              .play()
              .catch(function (error) {

                console.log(
                  "Audio did not play on click:",
                  audioPath,
                  error
                );

                warning.innerText =
                  "Audio did not play: " +
                  audioPath +
                  ". Check file name and extension.";

              });


            playCounts[
              dot.dataset.stimulusId
            ] += 1;

          }
        );


        // ---------- START DRAGGING ----------

        dot.addEventListener(
          "mousedown",
          function (e) {

            activeDot =
              dot;

            const dotRect =
              dot.getBoundingClientRect();

            offsetX =
              e.clientX -
              dotRect.left;

            offsetY =
              e.clientY -
              dotRect.top;

            dot.style.zIndex =
              1000;

            e.preventDefault();

          }
        );

      });


      // --------------------------------------------------
      // DRAG MOVEMENT
      // --------------------------------------------------

      function mouseMoveHandler(e) {

        if (!activeDot) {
          return;
        }


        const wrapperRect =
          wrapper.getBoundingClientRect();


        let newLeft =
          e.clientX -
          wrapperRect.left -
          offsetX;


        let newTop =
          e.clientY -
          wrapperRect.top -
          offsetY;


        // Do not allow dot to leave wrapper

        newLeft =
          Math.max(
            0,
            Math.min(
              wrapper.offsetWidth -
              activeDot.offsetWidth,
              newLeft
            )
          );


        newTop =
          Math.max(
            0,
            Math.min(
              wrapper.offsetHeight -
              activeDot.offsetHeight,
              newTop
            )
          );


        activeDot.style.left =
          `${newLeft}px`;

        activeDot.style.top =
          `${newTop}px`;

      }


      // --------------------------------------------------
      // STOP DRAGGING
      // --------------------------------------------------

      function mouseUpHandler() {

        if (activeDot) {

          activeDot.style.zIndex =
            10;

          activeDot =
            null;
        }

      }


      document.addEventListener(
        "mousemove",
        mouseMoveHandler
      );


      document.addEventListener(
        "mouseup",
        mouseUpHandler
      );


      // --------------------------------------------------
      // COLLECT SIMPLE WIDE-FORM DATA
      // --------------------------------------------------

      function getSimpleWideData() {

        let wideData =
          {};


        dots.forEach(
          (dot, index) => {


            const dotNum =
              String(index + 1)
                .padStart(
                  2,
                  "0"
                );


            const dotLeft =
              parseFloat(
                dot.style.left
              );


            const dotTop =
              parseFloat(
                dot.style.top
              );


            const dotCenterX =
              dotLeft +
              dot.offsetWidth / 2;


            const dotCenterY =
              dotTop +
              dot.offsetHeight / 2;


            const stim =
              window.currentFCStimuli[
                parseInt(
                  dot.dataset.index
                )
              ];


            // ------------------------------
            // SAVE STIMULUS INFORMATION
            // ------------------------------

            wideData[
              `dot${dotNum}_audio`
            ] =
              stim.audio;


            wideData[
              `dot${dotNum}_label`
            ] =
              stim.token_label;


            wideData[
              `dot${dotNum}_stop_type`
            ] =
              stim.stop_type;


            wideData[
              `dot${dotNum}_speaker`
            ] =
              stim.speaker;


            wideData[
              `dot${dotNum}_stimulus_class`
            ] =
              stim.stimulus_class;


            // ------------------------------
            // SAVE FINAL COORDINATES
            // ------------------------------

            wideData[
              `dot${dotNum}_x`
            ] =
              dotCenterX;


            wideData[
              `dot${dotNum}_y`
            ] =
              dotCenterY;


            // ------------------------------
            // SAVE NUMBER OF PLAYS
            // ------------------------------

            wideData[
              `dot${dotNum}_play_count`
            ] =
              playCounts[
                stim.stimulus_id
              ];

          }
        );


        return wideData;

      }


      // --------------------------------------------------
      // FINISH BUTTON
      // --------------------------------------------------

      finishButton.addEventListener(
        "click",
        function (e) {

          e.preventDefault();

          e.stopPropagation();


          try {

            finishButton.disabled =
              true;

            finishButton.innerText =
              "Saving...";

            warning.innerText =
              "";


            // ---------- GET DATA ----------

            const simpleWideData =
              getSimpleWideData();


            const completionTimeMs =
              Math.round(
                performance.now() -
                startTime
              );


            // ---------- REMOVE LISTENERS ----------

            document.removeEventListener(
              "mousemove",
              mouseMoveHandler
            );


            document.removeEventListener(
              "mouseup",
              mouseUpHandler
            );


            // ---------- STOP AUDIO ----------

            if (currentAudio) {

              currentAudio.pause();

              currentAudio.currentTime =
                0;
            }


            // ---------- BUILD FINAL TRIAL ROW ----------

            const trialData =
              Object.assign(

                {

                  task_type:
                    isPractice
                      ? "free_classification_practice_screen"
                      : "free_classification_screen",


                  participant_id:
                    PARTICIPANT_ID,


                  condition:
                    CONDITION,


                  phase:
                    PHASE,


                  day:
                    DAY,


                  is_practice:
                    isPractice,


                  screen_number:
                    screenInfo.screen_number,


                  word_set:
                    screenInfo.word_set,


                  n_items:
                    dots.length,


                  screen_completion_time_ms:
                    completionTimeMs

                },

                simpleWideData

              );


            // ---------- FINISH TRIAL ----------

            jsPsych.finishTrial(
              trialData
            );


          } catch (error) {

            console.log(
              "ERROR WHILE SAVING SCREEN:",
              error
            );


            warning.innerText =
              "There was an error saving this screen. Please tell the researcher.";


            finishButton.disabled =
              false;


            finishButton.innerText =
              isPractice
                ? "Finish practice"
                : "Finish this screen";

          }

        }
      );

    }

  };

}


// -------------------- COMPLETION SCREEN --------------------

const endTrial = {

  type:
    jsPsychHtmlKeyboardResponse,

  choices:
    "NO_KEYS",

  trial_duration:
    3000,


  stimulus: `

    <div
      style="
        font-family: Arial, sans-serif;
        max-width: 800px;
        margin: 80px auto;
        text-align: center;
      "
    >

      <h2>
        Task complete
      </h2>

      <p
        style="
          font-size: 20px;
        "
      >
        Thank you.
        You have completed this task.
      </p>

      <p
        style="
          font-size: 20px;
        "
      >
        You may now close this page.
      </p>

    </div>
  `,


  on_finish: function (data) {

    data.task_type =
      "free_classification_end";

    data.participant_id =
      PARTICIPANT_ID;

    data.condition =
      CONDITION;

    data.phase =
      PHASE;

    data.day =
      DAY;

  }

};


// -------------------- RUN TIMELINE --------------------

let timeline =
  [];


// Participant ID

timeline.push(
  participantIdTrial
);


// Instructions

timeline.push(
  instructionTrial
);


// Practice screen with 6 sound dots

timeline.push(
  createFreeClassificationTrial(
    practiceScreenInfo,
    true
  )
);


// Real experimental screens

stimuliByScreen.forEach(
  (screenInfo) => {

    timeline.push(
      createFreeClassificationTrial(
        screenInfo,
        false
      )
    );

  }
);


// Completion screen

timeline.push(
  endTrial
);


// -------------------- START EXPERIMENT --------------------

jsPsych.run(
  timeline
);

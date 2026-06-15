# Anti-air missile guidance rebalance — 2026-06-15

## Scope

All 178 weapon definitions whose `Type = AAMissile` now receive seeker- and era-aware guidance values instead of the previous universal `TickEndHoming = -1` and `MaxDegreeOfMissile = 160` values. The repeatable mapping is implemented in `tools/realistify_aamissiles.py`.

## Interpretation of the fields

- `MaxLockOnRange` is a gameplay lock envelope in blocks. Literal real-world ranges (often tens or hundreds of kilometres) are not usable on normal Minecraft maps, so values use an approximately 1:100 compressed scale while preserving the ordering between MANPADS, dogfight missiles, medium-range missiles, long-range SAMs, and ABMs.
- `AntiFlareCount` is treated as countermeasure-resistance time in ticks. It is not a flare count or a probability. Early seekers receive little or no persistence; modern IRCCM, monopulse/digital radar seekers, and dual-mode point-defense missiles receive progressively more.
- `ActiveRadar` is enabled only for missiles represented as having an onboard active radar seeker. SARH and command-guided missiles remain false.
- `ScanInterval` represents seeker update cadence in ticks. Modern active or imaging seekers update most frequently; early and externally guided systems update less frequently.
- `CanLockMissile` is reserved for weapons with a credible anti-missile/point-defense role (ABMs, modern naval area-defense missiles, RAM/ESSM-class systems). It is not enabled merely because a weapon is radar guided.
- `EnableBVR` is enabled for radar-guided AAMs and medium/long-range SAMs, but not short-range IR dogfight missiles, MANPADS, or terminal point-defense weapons.
- `IsHeatSeekerMissile` and `IsRadarMissile` describe the onboard seeker and therefore the appropriate countermeasure. Command-guided SAMs are neither, even when the launcher tracks targets with radar. MICA is represented as dual-mode where the asset name does not specify RF or IR.
- `TickEndHoming` now represents a finite seeker/guidance battery and useful flight life at 20 ticks per second. Values range from 18 seconds for early short-range IR weapons to 130 seconds for strategic interceptors. Guidance no longer lasts forever.
- `MaxDegreeOfMissile` is used by the backend as a maneuverability/overload proxy, not as a literal published seeker angle. The blanket value of 160 made every missile exceptionally agile. New values range from 28 for strategic interceptors to 100 for modern high-off-boresight dogfight missiles.

## Capability bands

| Band | Lock range | Homing life | Turn proxy | Typical examples |
|---|---:|---:|---:|---|
| Early rear-aspect IR | 80–120 | 360–440 ticks | 32–42 | AIM-9B/E, K-13, R-3S |
| All-aspect / IRCCM IR | 180–240 | 520–640 ticks | 58–82 | AIM-9L/M, R-60M, Magic II, R-73 |
| Imaging-IR / HOBS | 280 | 700 ticks | 100 | AIM-9X, IRIS-T, ASRAAM |
| MANPADS / short IR SAM | 100–150 | 420–520 ticks | 55–62 | Stinger, Igla, Type 91 |
| SARH AAM | 240–650 | 700–1400 ticks | 32–45 | K-5, AIM-7, R-24/R-27/R-33 |
| Active-radar AAM | 800–1050 | 1500–1800 ticks | 58–65 | AIM-120, R-77, Meteor, AAM-4 |
| Command-guided SAM | 300 | 900 ticks | 46 | 57E6, 9M311, VT-1 |
| Radar SAM | 600–950 | 1400–1900 ticks | 48–58 | HAWK, SM-2, Patriot, SM-6 |
| Point defense | 260 | 700 ticks | 78 | RAM/SeaRAM, ESSM |
| Strategic/ABM | 1400 | 2600 ticks | 28 | SM-3, 77N6 |

## Data basis and limitations

The classification uses public seeker type, role, generation, and broad engagement-envelope data. Useful public references include:

- U.S. Air Force AIM-120 fact sheet: <https://www.af.mil/About-Us/Fact-Sheets/Display/Article/104576/aim-120-amraam/>
- U.S. Navy AIM-9X fact file: <https://www.navy.mil/Resources/Fact-Files/Display-FactFiles/Article/2168989/aim-9x-sidewinder-missile/>
- U.S. Navy Standard Missile fact file: <https://www.navy.mil/Resources/Fact-Files/Display-FactFiles/Article/2169011/standard-missile/>
- MBDA Meteor: <https://www.mbda-systems.com/product/meteor/>
- MBDA ASRAAM: <https://www.mbda-systems.com/product/asraam/>
- War Thunder missile characteristics are used only as a secondary comparative reference where public real-world details are classified or ambiguous: <https://wiki.warthunder.com/weapon/>

Exact seeker processing, counter-countermeasure effectiveness, battery life, and no-escape envelopes are commonly classified. Consequently, these values are conservative gameplay approximations rather than claims of exact real-world performance. Duplicate aircraft-specific files intentionally receive the same family profile.

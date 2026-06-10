# Plane flight tuning audit

This pass audits every `assets/mcheli/planes/*.txt` aircraft config and documents the intended relative scale between prop aircraft and jets. The BF-109 remains the prop-fighter reference: usable WWII props keep roughly `Speed` 0.9-1.15, `ThrottleAcceleration` 0.018, and torque around 0.35 unless a file already had a special legacy feel. Jets should not fall below that baseline by default.

## Balance logic

| Class | Intended feel | Typical tuned ranges |
| --- | --- | --- |
| WWII props / piston aircraft | Preserved as the baseline; BF-109-style handling stays responsive without jet-level acceleration. | `Speed` ~0.4-1.15, `ThrottleAcceleration` ~0.018, prop drag retained. |
| Early jets / jet drones | Faster than props, better throttle response, but not modern-fighter agility. | `Speed` >=1.55, `ThrottleAcceleration` 0.026, moderate pitch/roll/yaw authority. |
| Jet strike / attackers | Powerful acceleration and climb with heavier handling than fighters. | `Speed` >=1.45 or existing higher value, `ThrottleAcceleration` 0.030, moderate-high control authority. |
| Modern fighters | Clear step above props and early jets with strong roll/pitch response and lower high-speed drag. | `Speed` >=3.20 or existing higher value, `ThrottleAcceleration` 0.034, strong control authority. |
| Agile / 5th-gen fighters | Best fighter response without UFO turning; high speed retention and fast throttle response. | `Speed` >=3.60, `ThrottleAcceleration` 0.038, highest pitch/roll profile. |
| Heavy jets / large transports / bombers | Stronger acceleration than props, high speed and climb, but deliberately slower turn response. This includes large turboprop transports that need the same heavy-airframe feel. | `Speed` >=1.45 or existing higher value, `ThrottleAcceleration` 0.024, high damping/inertia. |
| Superfast recon/interceptors | Highest straight-line performance with intentionally heavy control feel at speed. | `Speed` ~4.0+, `ThrottleAcceleration` 0.030-0.032, low-moderate authority, high damping. |

The pass uses the extended realistic-flight-model fields already parsed by the plane loader: `ThrottleAcceleration`, `EngineDrag`, `BaseDrag`, `InducedDrag`, `ControlSurfaceDrag`, `ClimbEnergyLoss`, `DiveEnergyGain`, `IdleDrag`, `MaxLevelSpeed`, `StallSpeed`, `StallRecoverySpeed`, `CompressibilitySpeed`, `MaxSafeSpeed`, `PitchTorque`, `RollTorque`, `YawTorque`, `PitchDamping`, `RollDamping`, `YawDamping`, `MobilityYaw`, `MobilityPitch`, `MobilityRoll`, and `InertiaMultiplier`. Optional fields are only added to jet/large-airframe configs that needed explicit safe values; prop aircraft are left on their existing baseline so older configs continue to load normally.

## Aircraft audit table

| File | Aircraft | Audit class | Speed | ThrottleAccel | Pitch/Roll/Yaw torque | Action |
| --- | --- | --- | ---: | ---: | --- | --- |
| `a-10.txt` | A-10 Thunderbolt II | jet strike / attack | 1.45 | 0.030 | 0.39/0.42/0.29 | rebalanced profile |
| `a4.txt` | A-4E Skyhawk Early | jet strike / attack | 1.884 | 0.030 | 0.39/0.42/0.29 | rebalanced profile |
| `a400m.txt` | Airbus A400M Atlas | heavy jet / large transport / bomber | 1.45 | 0.024 | 0.25/0.25/0.18 | rebalanced profile |
| `a6.txt` | A-6 Intruder | jet strike / attack | 1.81 | 0.030 | 0.39/0.42/0.29 | rebalanced profile |
| `a6m2.txt` | A6M5 Zero Type 21 | prop / piston / turboprop | 0.927 | 0.018 | 0.35/0.35/0.262 | unchanged: prop baseline preserved |
| `a6m2n.txt` | A6M2-N Rufe | prop / piston / turboprop | 0.76 | 0.018 | 0.35/0.35/0.262 | unchanged: prop baseline preserved |
| `a7.txt` | A-7 Corsair | jet strike / attack | 1.931 | 0.030 | 0.39/0.42/0.29 | rebalanced profile |
| `ac-130.txt` | AC-130H Spectre | prop / piston / turboprop | 1.03 | 0.018 | 0.2/0.2/0.15 | unchanged: prop baseline preserved |
| `ac-47.txt` | Douglas AC-47 Spooky "Puff, the Magic Dragon" | prop / piston / turboprop | 0.626 | 0.018 | 0.25/0.25/0.188 | unchanged: prop baseline preserved |
| `an2.txt` | An-2 | prop / piston / turboprop | 0.449 | 0.018 | 0.27/0.27/0.203 | unchanged: prop baseline preserved |
| `au23.txt` | Fairchild AU-23A Peacemaker | prop / piston / turboprop | 0.475 | 0.018 | 0.28/0.28/0.21 | unchanged: prop baseline preserved |
| `b-1.txt` | B-1B Lancer (Conventional Payload) | heavy jet / large transport / bomber | 2.323 | 0.024 | 0.25/0.25/0.18 | rebalanced profile |
| `b-1nuclear.txt` | B-1B Lancer (Nuclear Payload) | heavy jet / large transport / bomber | 2.323 | 0.024 | 0.25/0.25/0.18 | rebalanced profile |
| `b-2a.txt` | B-2A Spirit (Conventional) | heavy jet / large transport / bomber | 1.757 | 0.024 | 0.25/0.25/0.18 | rebalanced profile |
| `b-2a2.txt` | B-2A Spirit (GBU-57 MOP) | heavy jet / large transport / bomber | 1.757 | 0.024 | 0.25/0.25/0.18 | rebalanced profile |
| `b-2a3.txt` | B-2A Spirit (Mixed Nuclear Loadout) | heavy jet / large transport / bomber | 1.757 | 0.024 | 0.25/0.25/0.18 | rebalanced profile |
| `b-2a4.txt` | B-2A Spirit (Full Nuclear Loadout) | heavy jet / large transport / bomber | 1.757 | 0.024 | 0.25/0.25/0.18 | rebalanced profile |
| `b29.txt` | B-29 Superfortress | prop / piston / turboprop | 0.999 | 0.018 | 0.22/0.22/0.165 | unchanged: prop baseline preserved |
| `b29sp.txt` | B-29 Superfortress (Silverplate Program) | prop / piston / turboprop | 0.999 | 0.018 | 0.22/0.22/0.165 | unchanged: prop baseline preserved |
| `b52.txt` | B-52H Stratofortress (Conventional) | heavy jet / large transport / bomber | 1.822 | 0.024 | 0.25/0.25/0.18 | rebalanced profile |
| `b52d.txt` | B-52D Big Belly | heavy jet / large transport / bomber | 1.822 | 0.024 | 0.25/0.25/0.18 | rebalanced profile |
| `b52n.txt` | B-52H Stratofortress (Nuclear Loadout) | heavy jet / large transport / bomber | 1.822 | 0.024 | 0.25/0.25/0.18 | rebalanced profile |
| `bayraktar tb 2.txt` | Baykar Bayraktar TB2 | prop/low-speed UAV | 0.386 | 0.018 | 0.3/0.3/0.225 | unchanged: prop/low-speed drone baseline already usable |
| `bf109.txt` | Bf.109 | prop / piston / turboprop | 1.114 | 0.018 | 0.35/0.35/0.262 | unchanged: prop baseline preserved |
| `bqm_74e.txt` | BQM-74E CHUKAR III (Target Drone) | early jet / jet drone | 1.55 | 0.026 | 0.38/0.42/0.28 | rebalanced profile |
| `bv138.txt` | BV-138 C-1 | prop / piston / turboprop | 0.496 | 0.018 | 0.22/0.22/0.165 | unchanged: prop baseline preserved |
| `c-47.txt` | Douglas C-47 Skytrain | prop / piston / turboprop | 0.626 | 0.018 | 0.25/0.25/0.188 | unchanged: prop baseline preserved |
| `c5.txt` | C5A galaxy | heavy jet / large transport / bomber | 1.489 | 0.024 | 0.25/0.25/0.18 | rebalanced profile |
| `c5m.txt` | C5M Super Galaxy | heavy jet / large transport / bomber | 1.489 | 0.024 | 0.25/0.25/0.18 | rebalanced profile |
| `e767.txt` | E767 AWACS | heavy jet / large transport / bomber | 1.479 | 0.024 | 0.25/0.25/0.18 | rebalanced profile |
| `emb314.txt` | EMB 314 Super Tucano | prop / piston / turboprop | 1.027 | 0.018 | 0.34/0.34/0.255 | unchanged: prop baseline preserved |
| `eurofighter_typhoon_2.txt` | Eurofighter Typhoon II (Storm Shadow) | agile / 5th-gen fighter | 4.341 | 0.038 | 0.46/0.52/0.34 | rebalanced profile |
| `eurofighter_typhoon_2_t.txt` | Eurofighter Typhoon II (Taurus) | agile / 5th-gen fighter | 4.341 | 0.038 | 0.46/0.52/0.34 | rebalanced profile |
| `f-104.txt` | f-104 | fast interceptor | 3.70 | 0.032 | 0.38/0.42/0.28 | rebalanced profile |
| `f-15e.txt` | F-15E Strike Eagle | modern fighter | 4.62 | 0.034 | 0.43/0.48/0.32 | rebalanced profile |
| `f-15s_mtd.txt` | F-15 S/MTD | agile / 5th-gen fighter | 4.62 | 0.038 | 0.46/0.52/0.34 | rebalanced profile |
| `f-35a.txt` | F-35A Lightning II | agile / 5th-gen fighter | 3.65 | 0.038 | 0.46/0.52/0.34 | rebalanced profile |
| `f-35b.txt` | F-35B Lightning II | agile / 5th-gen fighter | 3.55 | 0.038 | 0.46/0.52/0.34 | rebalanced profile |
| `f-35c.txt` | F-35C Lightning II | agile / 5th-gen fighter | 3.60 | 0.038 | 0.46/0.52/0.34 | rebalanced profile |
| `f-5e.txt` | F-5E Tiger II | fast interceptor | 3.40 | 0.032 | 0.38/0.42/0.28 | rebalanced profile |
| `f-80.txt` | Lockheed P-80/F-80 Shooting Star | early jet / jet drone | 1.663 | 0.026 | 0.38/0.42/0.28 | rebalanced profile |
| `f-86f.txt` | F-86F Sabre | early jet / jet drone | 1.55 | 0.026 | 0.38/0.42/0.28 | rebalanced profile |
| `f117.txt` | F-117 Nighthawk (GBU-12 Paveway II) | jet strike / attack | 2.05 | 0.030 | 0.39/0.42/0.29 | rebalanced profile |
| `f117gbu27.txt` | F-117 Nighthawk (GBU-27 Paveway III) | jet strike / attack | 2.05 | 0.030 | 0.39/0.42/0.29 | rebalanced profile |
| `f117nuc.txt` | F-117 Nighthawk (B61 Nuclear Bombs) | jet strike / attack | 2.05 | 0.030 | 0.39/0.42/0.29 | rebalanced profile |
| `f14.txt` | F-14D Tomcat | modern fighter | 4.324 | 0.034 | 0.43/0.48/0.32 | rebalanced profile |
| `f14d.txt` | F-14D Tomcat (alt) | modern fighter | 3.20 | 0.034 | 0.43/0.48/0.32 | rebalanced profile |
| `f16c.txt` | F-16C | modern fighter | 3.80 | 0.034 | 0.43/0.48/0.32 | rebalanced profile |
| `f1m.txt` | Mitsubishi F1M "Pete" | prop / piston / turboprop | 0.644 | 0.018 | 0.34/0.34/0.255 | unchanged: prop baseline preserved |
| `f22a.txt` | F-22A Raptor | agile / 5th-gen fighter | 4.2 | 0.038 | 0.46/0.52/0.34 | rebalanced profile |
| `f4a.txt` | F-4A Phantom II | fast interceptor | 4.124 | 0.032 | 0.38/0.42/0.28 | rebalanced profile |
| `f8f.txt` | F8F-1B Bearcat | prop / piston / turboprop | 1.18 | 0.018 | 0.35/0.35/0.262 | unchanged: prop baseline preserved |
| `fa18e.txt` | F/A-18E Super Hornet | modern fighter | 3.65 | 0.034 | 0.43/0.48/0.32 | rebalanced profile |
| `fa18fold.txt` | F/A-18F Super Hornet | modern fighter | 3.65 | 0.034 | 0.43/0.48/0.32 | rebalanced profile |
| `fa50.txt` | FA-50 | modern fighter | 3.20 | 0.034 | 0.43/0.48/0.32 | rebalanced profile |
| `fuel_truck.txt` | Fuel Truck | ground support | 0 | - | -/-/- | unchanged: not an aircraft flight profile |
| `geran2.txt` | Geran 2 | prop / piston / turboprop | 0.322 | 0.018 | 0.32/0.32/0.24 | unchanged: prop baseline preserved |
| `h6k.txt` | Xi'an H-6K "God Of War" | heavy jet / large transport / bomber | 1.45 | 0.024 | 0.25/0.25/0.18 | rebalanced profile |
| `h8k.txt` | Kawanishi H8K "Emily" | prop / piston / turboprop | 0.809 | 0.018 | 0.23/0.23/0.173 | unchanged: prop baseline preserved |
| `harrier.txt` | AV-8B Harrier II | jet strike / attack | 2.046 | 0.030 | 0.39/0.42/0.29 | rebalanced profile |
| `harrier_en.txt` | BAe Harrier II | jet strike / attack | 2.046 | 0.030 | 0.39/0.42/0.29 | rebalanced profile |
| `il28sh.txt` | Il-28Sh | early jet / jet drone | 1.569 | 0.026 | 0.38/0.42/0.28 | rebalanced profile |
| `il76ua.txt` | Il-76MD-90A | heavy jet / large transport / bomber | 1.566 | 0.024 | 0.25/0.25/0.18 | rebalanced profile |
| `j11b.txt` | J-11B | modern fighter | 4.35 | 0.034 | 0.43/0.48/0.32 | rebalanced profile |
| `j15.txt` | J-15 Fly Shark | modern fighter | 4.176 | 0.034 | 0.43/0.48/0.32 | rebalanced profile |
| `j8.txt` | Shenyang J-8 II | fast interceptor | 4.07 | 0.032 | 0.38/0.42/0.28 | rebalanced profile |
| `jas39.txt` | jas39 | modern fighter | 3.20 | 0.034 | 0.43/0.48/0.32 | rebalanced profile |
| `ju87.txt` | Ju-87D-3 Stuka | prop / piston / turboprop | 0.679 | 0.018 | 0.35/0.35/0.262 | unchanged: prop baseline preserved |
| `kf-21.txt` | KF-21 Boramae | agile / 5th-gen fighter | 3.828 | 0.038 | 0.46/0.52/0.34 | rebalanced profile |
| `m2000-5.txt` | Mirage 2000-5F | modern fighter | 4.065 | 0.034 | 0.43/0.48/0.32 | rebalanced profile |
| `m2000c.txt` | Mirage 2000C | modern fighter | 4.065 | 0.034 | 0.43/0.48/0.32 | rebalanced profile |
| `mc130.txt` | MC-130H Combat Talon II | prop / piston / turboprop | 1.03 | 0.018 | 0.2/0.2/0.15 | unchanged: prop baseline preserved |
| `mc130j.txt` | MC-130J Commando II | prop / piston / turboprop | 1.168 | 0.018 | 0.2/0.2/0.15 | unchanged: prop baseline preserved |
| `md90.txt` | MD-90-30 | heavy jet / large transport / bomber | 1.609 | 0.024 | 0.25/0.25/0.18 | rebalanced profile |
| `mig-15.txt` | Mikoyan-Gurevich MiG-15 (No Payload) | early jet / jet drone | 1.872 | 0.026 | 0.38/0.42/0.28 | rebalanced profile |
| `mig-19s.txt` | MiG-19S Farmer | early jet / jet drone | 2.53 | 0.026 | 0.38/0.42/0.28 | rebalanced profile |
| `mig-21pf.txt` | MiG-21PF Fishbed | fast interceptor | 3.784 | 0.032 | 0.38/0.42/0.28 | rebalanced profile |
| `mig17f.txt` | MIG-17 F | early jet / jet drone | 1.992 | 0.026 | 0.38/0.42/0.28 | rebalanced profile |
| `mig21.txt` | Mig-21 F-13 | fast interceptor | 3.698 | 0.032 | 0.38/0.42/0.28 | rebalanced profile |
| `mig23.txt` | MIG-23MLD | fast interceptor | 4.254 | 0.032 | 0.38/0.42/0.28 | rebalanced profile |
| `mig25.txt` | Mikoyan-Gurevich MiG-25 | fast interceptor | 5.22 | 0.032 | 0.38/0.42/0.28 | rebalanced profile |
| `mig29.txt` | MiG-29 Fulcrum | modern fighter | 4.263 | 0.034 | 0.43/0.48/0.32 | rebalanced profile |
| `mig3.txt` | MiG-3-15 | prop / piston / turboprop | 1.114 | 0.018 | 0.35/0.35/0.262 | unchanged: prop baseline preserved |
| `mig31.txt` | MiG-31 Foxhound | superfast recon/interceptor | 4.00 | 0.030 | 0.24/0.26/0.18 | rebalanced profile |
| `mig31k.txt` | Mig-31K | superfast recon/interceptor | 3.95 | 0.030 | 0.24/0.26/0.18 | rebalanced profile |
| `mirage3e.txt` | Dassault Mirage IIIE | fast interceptor | 4.089 | 0.032 | 0.38/0.42/0.28 | rebalanced profile |
| `mirageiv.txt` | Mirage IVP | fast interceptor | 4.072 | 0.032 | 0.38/0.42/0.28 | rebalanced profile |
| `mq-9.txt` | MQ-9 Reaper | prop/low-speed UAV | 0.839 | 0.018 | 0.3/0.3/0.225 | unchanged: prop/low-speed drone baseline already usable |
| `mq-9debug.txt` | MQ-9 Reaper | prop/low-speed UAV | 0.522 | - | -/-/- | unchanged: prop/low-speed drone baseline already usable |
| `mqm170.txt` | MQM-170 Outlaw (Target drone) | prop/low-speed UAV | 0.322 | 0.018 | 0.32/0.32/0.24 | unchanged: prop/low-speed drone baseline already usable |
| `mv-22.txt` | MV-22 Osprey | prop / piston / turboprop | 0.983 | 0.018 | 0.24/0.24/0.18 | unchanged: prop baseline preserved |
| `n1k1.txt` | Kawanishi N1K | prop / piston / turboprop | 1.016 | 0.018 | 0.35/0.35/0.262 | unchanged: prop baseline preserved |
| `ov-10a.txt` | OV-10A Bronco | prop / piston / turboprop | 0.786 | 0.018 | 0.3/0.3/0.225 | unchanged: prop baseline preserved |
| `p-51d.txt` | P-51D Mustang | prop / piston / turboprop | 0.76734 | 0.25 | 2.8/1.5/1.2 | unchanged: prop baseline preserved |
| `pzl-m18.txt` | PZL M-18 Dromader | prop / piston / turboprop | 0.435 | 0.018 | 0.25/0.25/0.188 | unchanged: prop baseline preserved |
| `q-5d.txt` | Nanchang Q-5D | jet strike / attack | 2.105 | 0.030 | 0.39/0.42/0.29 | rebalanced profile |
| `qf-80.txt` | Lockheed QF-80A Shooting Star (Target drone) | early jet / jet drone | 1.663 | 0.026 | 0.38/0.42/0.28 | rebalanced profile |
| `rafalem.txt` | Dassault Rafale M | modern fighter | 3.327 | 0.034 | 0.43/0.48/0.32 | rebalanced profile |
| `skylark.txt` | Elbit Skylark | prop/low-speed UAV | 0.16 | 0.018 | 0.42/0.42/0.315 | unchanged: prop/low-speed drone baseline already usable |
| `spitfire-mkvb.txt` | SuperMarine Spitfire Mk.Vb | prop / piston / turboprop | 1.034 | 0.018 | 0.35/0.35/0.262 | unchanged: prop baseline preserved |
| `sr71.txt` | Lockheed SR-71 Blackbird | superfast recon/interceptor | 6.16 | 0.030 | 0.24/0.26/0.18 | rebalanced profile |
| `su-33.txt` | Su-33 Flanker-D | modern fighter | 4.002 | 0.034 | 0.43/0.48/0.32 | rebalanced profile |
| `su24.txt` | Su-24 | prop/heavy or special | 2.878 | 0.018 | 0.28/0.28/0.21 | unchanged: non-jet or special aircraft baseline preserved |
| `su25.txt` | Su-25T | jet strike / attack | 1.697 | 0.030 | 0.39/0.42/0.29 | rebalanced profile |
| `su27bru.txt` | Su-27 Flanker-B | modern fighter | 4.35 | 0.034 | 0.43/0.48/0.32 | rebalanced profile |
| `su34.txt` | Su-34 | modern fighter | 3.306 | 0.034 | 0.43/0.48/0.32 | rebalanced profile |
| `su34b.txt` | Su-34 (Bombs) | modern fighter | 3.306 | 0.034 | 0.43/0.48/0.32 | rebalanced profile |
| `su34n.txt` | Su-34 (Rocket) | modern fighter | 3.306 | 0.034 | 0.43/0.48/0.32 | rebalanced profile |
| `su37.txt` | Sukhoi Su-35 | agile / 5th-gen fighter | 4.35 | 0.038 | 0.46/0.52/0.34 | rebalanced profile |
| `su57.txt` | Su-57 | agile / 5th-gen fighter | 4.524 | 0.038 | 0.46/0.52/0.34 | rebalanced profile |
| `tornado-gr4.txt` | Panavia Tornado GR.4 | modern fighter | 4.176 | 0.034 | 0.43/0.48/0.32 | rebalanced profile |
| `tornado-ids.txt` | Panavia Tornado IDS | modern fighter | 4.176 | 0.034 | 0.43/0.48/0.32 | rebalanced profile |
| `tu142real.txt` | TU-142 | prop/heavy or special | 1.609 | 0.018 | 0.18/0.18/0.135 | unchanged: non-jet or special aircraft baseline preserved |
| `tu160m.txt` | Tu-160M Super Blackjack Conventional Bombs | heavy jet / large transport / bomber | 3.863 | 0.024 | 0.25/0.25/0.18 | rebalanced profile |
| `tu160mmsl.txt` | Tu-160M Super Blackjack with Rotary Launchers | heavy jet / large transport / bomber | 3.863 | 0.024 | 0.25/0.25/0.18 | rebalanced profile |
| `tu22m3.txt` | Tu-22M3 | heavy jet / large transport / bomber | 3.48 | 0.024 | 0.25/0.25/0.18 | rebalanced profile |
| `tu4.txt` | Tupolev Tu-4A | prop / piston / turboprop | 0.971 | 0.018 | 0.22/0.22/0.165 | unchanged: prop baseline preserved |
| `tu4light.txt` | Tupolev Tu-4 | prop / piston / turboprop | 0.971 | 0.018 | 0.22/0.22/0.165 | unchanged: prop baseline preserved |
| `tu95k22.txt` | TU-95K-22 (3x KH-22 Nuclear) | prop/heavy or special | 1.601 | 0.018 | 0.18/0.18/0.135 | unchanged: non-jet or special aircraft baseline preserved |
| `tu95ms.txt` | TU-95MSM | prop/heavy or special | 1.609 | 0.018 | 0.18/0.18/0.135 | unchanged: non-jet or special aircraft baseline preserved |
| `tu95org.txt` | TU-95 Bear | prop/heavy or special | 1.601 | 0.018 | 0.18/0.18/0.135 | unchanged: non-jet or special aircraft baseline preserved |
| `victor_b2.txt` | Handley Page Victor B.2 | heavy jet / large transport / bomber | 1.757 | 0.024 | 0.25/0.25/0.18 | rebalanced profile |
| `x-47b.txt` | X-47B Pegasus | heavy jet / large transport / bomber | 1.914 | 0.024 | 0.25/0.25/0.18 | rebalanced profile |
| `yak38.txt` | Yakovlev Yak-38 with UB-32 | jet strike / attack | 2.227 | 0.030 | 0.39/0.42/0.29 | rebalanced profile |
| `yak38_r60.txt` | Yakovlev Yak-38 with R-60 | jet strike / attack | 2.227 | 0.030 | 0.39/0.42/0.29 | rebalanced profile |
| `yak38_upk.txt` | Yakovlev Yak-38 with GSh-23 | jet strike / attack | 2.227 | 0.030 | 0.39/0.42/0.29 | rebalanced profile |
| `yak38_x23.txt` | Yakovlev Yak-38 with Kh-23M | jet strike / attack | 2.227 | 0.030 | 0.39/0.42/0.29 | rebalanced profile |

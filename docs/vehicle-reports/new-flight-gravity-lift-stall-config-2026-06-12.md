# New flight gravity/lift/stall config pass - 2026-06-12

## Scope

- Reviewed plane configs under `assets/mcheli/planes` and only modified files already opting into `UseNewMobilitySystem = true`.
- Legacy mobility planes were left untouched.
- Used `docs/vehicle-config/planes.md` as the tuning reference for the explicit gravity/lift, stall lift-loss, stall nose-down, and ground-bounce fields.

## Tuning summary

- Added `GravityStrength`, `LiftGravityCompensation`, `StallNoseDownForce`, `StallNoseDownMinSpeed`, `GroundBounceDamping`, and `GroundVerticalVelocityClamp` to every opted-in plane.
- Filled missing `StallLiftLoss` values on new-flight aircraft that lacked the field, and adjusted VTOL/STOVL/special cases where the prior copied value did not match the new fixed-wing gravity model.
- WW2 and light prop fighters received high lift compensation and strong stall nose-down recovery so they can glide and recover without hovering at idle.
- Modern fighters received moderate gravity with high but not perfect lift compensation so they maintain energy at cruise yet descend when slow, high-AoA, or stalled.
- Heavy bombers/transports received stronger gravity, lower lift compensation, later/weaker stall recovery, and tighter ground clamps so they need airspeed and do not bounce upward after landing.
- VTOL/STOVL aircraft were tuned separately from conventional fighters to avoid treating hover capability as free fixed-wing lift.
- UAVs and loitering munitions were split between micro/light and fast UCAV behavior rather than using fighter defaults.

## Modified aircraft

| File | Aircraft | Grav | Lift comp | Stall loss | Nose-down | Nose min | Bounce damp | Y clamp |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `a-10.txt` | A-10 Thunderbolt II | `0.032` | `1.1` | `0.66` | `0.14` | `0.065` | `0.2` | `0.013` |
| `a4.txt` | A-4E Skyhawk Early | `0.033` | `1.07` | `0.7` | `0.14` | `0.085` | `0.2` | `0.014` |
| `a400m.txt` | Airbus A400M Atlas | `0.039` | `0.96` | `0.68` | `0.085` | `0.14` | `0.13` | `0.01` |
| `a6.txt` | A-6 Intruder | `0.033` | `1.07` | `0.7` | `0.14` | `0.085` | `0.2` | `0.014` |
| `a6m2.txt` | A6M5 Zero Type 21 | `0.031` | `1.16` | `0.55` | `0.2` | `0.055` | `0.18` | `0.012` |
| `a6m2n.txt` | A6M2-N Rufe | `0.031` | `1.16` | `0.62` | `0.2` | `0.055` | `0.18` | `0.012` |
| `a7.txt` | A-7 Corsair | `0.033` | `1.07` | `0.7` | `0.14` | `0.085` | `0.2` | `0.014` |
| `ac-130.txt` | AC-130H Spectre | `0.042` | `0.92` | `0.72` | `0.07` | `0.17` | `0.11` | `0.008` |
| `ac-47.txt` | Douglas AC-47 Spooky "Puff, the Magic Dragon" | `0.039` | `0.96` | `0.68` | `0.085` | `0.14` | `0.13` | `0.01` |
| `an2.txt` | An-2 | `0.03` | `1.08` | `0.62` | `0.12` | `0.055` | `0.17` | `0.012` |
| `au23.txt` | Fairchild AU-23A Peacemaker | `0.03` | `1.08` | `0.68` | `0.12` | `0.055` | `0.17` | `0.012` |
| `b-1.txt` | B-1B Lancer (Conventional Payload) | `0.039` | `0.94` | `0.7` | `0.085` | `0.15` | `0.13` | `0.01` |
| `b-1nuclear.txt` | B-1B Lancer (Nuclear Payload) | `0.039` | `0.94` | `0.7` | `0.085` | `0.15` | `0.13` | `0.01` |
| `b-2a.txt` | B-2A Spirit (Conventional) | `0.039` | `0.94` | `0.7` | `0.085` | `0.15` | `0.13` | `0.01` |
| `b-2a2.txt` | B-2A Spirit (GBU-57 MOP) | `0.039` | `0.94` | `0.7` | `0.085` | `0.15` | `0.13` | `0.01` |
| `b-2a3.txt` | B-2A Spirit (Mixed Nuclear Loadout) | `0.039` | `0.94` | `0.7` | `0.085` | `0.15` | `0.13` | `0.01` |
| `b-2a4.txt` | B-2A Spirit (Full Nuclear Loadout) | `0.039` | `0.94` | `0.7` | `0.085` | `0.15` | `0.13` | `0.01` |
| `b29.txt` | B-29 Superfortress | `0.036` | `1` | `0.7` | `0.1` | `0.12` | `0.14` | `0.01` |
| `b29sp.txt` | B-29 Superfortress (Silverplate Program) | `0.036` | `1` | `0.7` | `0.1` | `0.12` | `0.14` | `0.01` |
| `b52.txt` | B-52H Stratofortress (Conventional) | `0.042` | `0.92` | `0.7` | `0.07` | `0.17` | `0.11` | `0.008` |
| `b52d.txt` | B-52D Big Belly | `0.042` | `0.92` | `0.7` | `0.07` | `0.17` | `0.11` | `0.008` |
| `b52n.txt` | B-52H Stratofortress (Nuclear Loadout) | `0.042` | `0.92` | `0.7` | `0.07` | `0.17` | `0.11` | `0.008` |
| `bayraktar tb 2.txt` | Baykar Bayraktar TB2 | `0.026` | `1.04` | `0.56` | `0.08` | `0.035` | `0.16` | `0.01` |
| `bf109.txt` | Bf.109 | `0.031` | `1.14` | `0.64` | `0.2` | `0.06` | `0.18` | `0.012` |
| `bqm_74e.txt` | BQM-74E CHUKAR III (Target Drone) | `0.03` | `0.98` | `0.6` | `0.09` | `0.065` | `0.17` | `0.011` |
| `bv138.txt` | BV-138 C-1 | `0.03` | `1.08` | `0.68` | `0.12` | `0.055` | `0.17` | `0.012` |
| `c-47.txt` | Douglas C-47 Skytrain | `0.039` | `0.96` | `0.68` | `0.085` | `0.14` | `0.13` | `0.01` |
| `c5.txt` | C5A galaxy | `0.039` | `0.96` | `0.7` | `0.085` | `0.14` | `0.13` | `0.01` |
| `c5m.txt` | C5M Super Galaxy | `0.039` | `0.96` | `0.7` | `0.085` | `0.14` | `0.13` | `0.01` |
| `e767.txt` | E767 AWACS | `0.039` | `0.96` | `0.7` | `0.085` | `0.14` | `0.13` | `0.01` |
| `emb314.txt` | EMB 314 Super Tucano | `0.03` | `1.08` | `0.64` | `0.12` | `0.055` | `0.17` | `0.012` |
| `eurofighter_typhoon_2.txt` | Eurofighter Typhoon II (Storm Shadow) | `0.034` | `1.08` | `0.7` | `0.15` | `0.09` | `0.22` | `0.014` |
| `eurofighter_typhoon_2_t.txt` | Eurofighter Typhoon II (Taurus) | `0.034` | `1.08` | `0.7` | `0.15` | `0.09` | `0.22` | `0.014` |
| `f-104.txt` | f-104 | `0.035` | `0.98` | `0.74` | `0.1` | `0.13` | `0.15` | `0.01` |
| `f-15e.txt` | F-15E Strike Eagle | `0.034` | `1.05` | `0.7` | `0.14` | `0.095` | `0.22` | `0.014` |
| `f-15s_mtd.txt` | F-15 S/MTD | `0.034` | `1.08` | `0.7` | `0.15` | `0.09` | `0.22` | `0.014` |
| `f-35a.txt` | F-35A Lightning II | `0.034` | `1.05` | `0.65` | `0.14` | `0.095` | `0.22` | `0.014` |
| `f-35b.txt` | F-35B Lightning II | `0.033` | `1.01` | `0.68` | `0.12` | `0.085` | `0.18` | `0.012` |
| `f-35c.txt` | F-35C Lightning II | `0.034` | `1.05` | `0.65` | `0.14` | `0.095` | `0.22` | `0.014` |
| `f-5e.txt` | F-5E Tiger II | `0.033` | `1.07` | `0.7` | `0.14` | `0.085` | `0.2` | `0.014` |
| `f-80.txt` | Lockheed P-80/F-80 Shooting Star | `0.032` | `1.09` | `0.7` | `0.15` | `0.075` | `0.2` | `0.013` |
| `f-86f.txt` | F-86F Sabre | `0.032` | `1.1` | `0.66` | `0.16` | `0.07` | `0.2` | `0.013` |
| `f117.txt` | F-117 Nighthawk (GBU-12 Paveway II) | `0.034` | `0.99` | `0.7` | `0.1` | `0.1` | `0.16` | `0.011` |
| `f117gbu27.txt` | F-117 Nighthawk (GBU-27 Paveway III) | `0.034` | `0.99` | `0.7` | `0.1` | `0.1` | `0.16` | `0.011` |
| `f117nuc.txt` | F-117 Nighthawk (B61 Nuclear Bombs) | `0.034` | `0.99` | `0.7` | `0.1` | `0.1` | `0.16` | `0.011` |
| `f14.txt` | F-14D Tomcat | `0.034` | `1.03` | `0.7` | `0.13` | `0.11` | `0.22` | `0.014` |
| `f14d.txt` | F-14D Tomcat (alt) | `0.034` | `1.05` | `0.72` | `0.14` | `0.095` | `0.22` | `0.014` |
| `f16c.txt` | F-16C | `0.034` | `1.05` | `0.65` | `0.14` | `0.095` | `0.22` | `0.014` |
| `f1m.txt` | Mitsubishi F1M "Pete" | `0.031` | `1.16` | `0.62` | `0.2` | `0.055` | `0.18` | `0.012` |
| `f22a.txt` | F-22A Raptor | `0.034` | `1.08` | `0.7` | `0.15` | `0.09` | `0.22` | `0.014` |
| `f4a.txt` | F-4A Phantom II | `0.033` | `1.05` | `0.7` | `0.13` | `0.1` | `0.2` | `0.014` |
| `f8f.txt` | F8F-1B Bearcat | `0.031` | `1.14` | `0.62` | `0.2` | `0.06` | `0.18` | `0.012` |
| `fa18e.txt` | F/A-18E Super Hornet | `0.034` | `1.05` | `0.65` | `0.14` | `0.095` | `0.22` | `0.014` |
| `fa18fold.txt` | F/A-18F Super Hornet | `0.034` | `1.03` | `0.7` | `0.13` | `0.11` | `0.22` | `0.014` |
| `fa50.txt` | FA-50 | `0.034` | `1.05` | `0.7` | `0.14` | `0.095` | `0.22` | `0.014` |
| `geran2.txt` | Geran 2 | `0.024` | `0.98` | `0.58` | `0.06` | `0.03` | `0.12` | `0.008` |
| `h6k.txt` | Xi'an H-6K "God Of War" | `0.039` | `0.96` | `0.7` | `0.085` | `0.14` | `0.13` | `0.01` |
| `h8k.txt` | Kawanishi H8K "Emily" | `0.036` | `1` | `0.68` | `0.1` | `0.12` | `0.14` | `0.01` |
| `harrier.txt` | AV-8B Harrier II | `0.033` | `1` | `0.69` | `0.12` | `0.095` | `0.17` | `0.012` |
| `harrier_en.txt` | BAe Harrier II | `0.033` | `1` | `0.69` | `0.12` | `0.095` | `0.17` | `0.012` |
| `il28sh.txt` | Il-28Sh | `0.032` | `1.06` | `0.7` | `0.14` | `0.085` | `0.19` | `0.013` |
| `il76ua.txt` | Il-76MD-90A | `0.039` | `0.96` | `0.7` | `0.085` | `0.14` | `0.13` | `0.01` |
| `j11b.txt` | J-11B | `0.034` | `1.08` | `0.7` | `0.15` | `0.09` | `0.22` | `0.014` |
| `j15.txt` | J-15 Fly Shark | `0.034` | `1.08` | `0.7` | `0.15` | `0.09` | `0.22` | `0.014` |
| `j8.txt` | Shenyang J-8 II | `0.034` | `1.05` | `0.7` | `0.14` | `0.095` | `0.22` | `0.014` |
| `jas39.txt` | jas39 | `0.034` | `1.05` | `0.7` | `0.14` | `0.095` | `0.22` | `0.014` |
| `ju87.txt` | Ju-87D-3 Stuka | `0.031` | `1.16` | `0.66` | `0.2` | `0.055` | `0.18` | `0.012` |
| `kf-21.txt` | KF-21 Boramae | `0.034` | `1.08` | `0.7` | `0.15` | `0.09` | `0.22` | `0.014` |
| `m2000-5.txt` | Mirage 2000-5F | `0.034` | `1.08` | `0.7` | `0.15` | `0.09` | `0.22` | `0.014` |
| `m2000c.txt` | Mirage 2000C | `0.034` | `1.08` | `0.7` | `0.15` | `0.09` | `0.22` | `0.014` |
| `mc130.txt` | MC-130H Combat Talon II | `0.042` | `0.92` | `0.72` | `0.07` | `0.17` | `0.11` | `0.008` |
| `mc130j.txt` | MC-130J Commando II | `0.042` | `0.92` | `0.72` | `0.07` | `0.17` | `0.11` | `0.008` |
| `md90.txt` | MD-90-30 | `0.039` | `0.96` | `0.7` | `0.085` | `0.14` | `0.13` | `0.01` |
| `mig-15.txt` | Mikoyan-Gurevich MiG-15 (No Payload) | `0.032` | `1.09` | `0.7` | `0.15` | `0.075` | `0.2` | `0.013` |
| `mig-19s.txt` | MiG-19S Farmer | `0.032` | `1.09` | `0.7` | `0.15` | `0.075` | `0.2` | `0.013` |
| `mig-21pf.txt` | MiG-21PF Fishbed | `0.033` | `1.07` | `0.7` | `0.14` | `0.085` | `0.2` | `0.014` |
| `mig17f.txt` | MIG-17 F | `0.032` | `1.09` | `0.7` | `0.15` | `0.075` | `0.2` | `0.013` |
| `mig21.txt` | Mig-21 F-13 | `0.033` | `1.07` | `0.7` | `0.14` | `0.085` | `0.2` | `0.014` |
| `mig23.txt` | MIG-23MLD | `0.033` | `1.05` | `0.7` | `0.13` | `0.1` | `0.2` | `0.014` |
| `mig25.txt` | Mikoyan-Gurevich MiG-25 | `0.036` | `0.98` | `0.7` | `0.12` | `0.12` | `0.16` | `0.011` |
| `mig29.txt` | MiG-29 Fulcrum | `0.034` | `1.08` | `0.7` | `0.15` | `0.09` | `0.22` | `0.014` |
| `mig3.txt` | MiG-3-15 | `0.031` | `1.14` | `0.64` | `0.2` | `0.06` | `0.18` | `0.012` |
| `mig31.txt` | MiG-31 Foxhound | `0.037` | `0.96` | `0.76` | `0.095` | `0.14` | `0.14` | `0.01` |
| `mig31k.txt` | Mig-31K | `0.036` | `0.98` | `0.7` | `0.12` | `0.12` | `0.16` | `0.011` |
| `mirage3e.txt` | Dassault Mirage IIIE | `0.033` | `1.07` | `0.7` | `0.14` | `0.085` | `0.2` | `0.014` |
| `mirageiv.txt` | Mirage IVP | `0.036` | `0.98` | `0.7` | `0.11` | `0.125` | `0.16` | `0.011` |
| `mq-9.txt` | MQ-9 Reaper | `0.026` | `1.04` | `0.56` | `0.08` | `0.035` | `0.16` | `0.01` |
| `mqm170.txt` | MQM-170 Outlaw (Target drone) | `0.026` | `1.04` | `0.56` | `0.08` | `0.035` | `0.16` | `0.01` |
| `mv-22.txt` | MV-22 Osprey | `0.034` | `0.98` | `0.7` | `0.09` | `0.12` | `0.13` | `0.009` |
| `n1k1.txt` | Kawanishi N1K | `0.031` | `1.14` | `0.6` | `0.2` | `0.06` | `0.18` | `0.012` |
| `ov-10a.txt` | OV-10A Bronco | `0.03` | `1.08` | `0.68` | `0.12` | `0.055` | `0.17` | `0.012` |
| `p-51d.txt` | P-51D Mustang | `0.031` | `1.14` | `0.64` | `0.2` | `0.06` | `0.18` | `0.012` |
| `pzl-m18.txt` | PZL M-18 Dromader | `0.03` | `1.08` | `0.62` | `0.12` | `0.055` | `0.17` | `0.012` |
| `q-5d.txt` | Nanchang Q-5D | `0.033` | `1.07` | `0.7` | `0.14` | `0.085` | `0.2` | `0.014` |
| `qf-80.txt` | Lockheed QF-80A Shooting Star (Target drone) | `0.032` | `1.09` | `0.7` | `0.15` | `0.075` | `0.2` | `0.013` |
| `rafalem.txt` | Dassault Rafale M | `0.034` | `1.08` | `0.7` | `0.15` | `0.09` | `0.22` | `0.014` |
| `skylark.txt` | Elbit Skylark | `0.02` | `1.06` | `0.54` | `0.055` | `0.02` | `0.14` | `0.008` |
| `spitfire-mkvb.txt` | SuperMarine Spitfire Mk.Vb | `0.031` | `1.16` | `0.55` | `0.2` | `0.055` | `0.18` | `0.012` |
| `sr71.txt` | Lockheed SR-71 Blackbird | `0.037` | `0.94` | `0.7` | `0.085` | `0.16` | `0.12` | `0.009` |
| `su-33.txt` | Su-33 Flanker-D | `0.034` | `1.08` | `0.7` | `0.15` | `0.09` | `0.22` | `0.014` |
| `su24.txt` | Su-24 | `0.034` | `1.05` | `0.7` | `0.14` | `0.095` | `0.22` | `0.014` |
| `su25.txt` | Su-25T | `0.033` | `1.07` | `0.7` | `0.14` | `0.085` | `0.2` | `0.014` |
| `su27bru.txt` | Su-27 Flanker-B | `0.034` | `1.08` | `0.7` | `0.15` | `0.09` | `0.22` | `0.014` |
| `su34.txt` | Su-34 | `0.034` | `1.05` | `0.7` | `0.14` | `0.095` | `0.22` | `0.014` |
| `su34b.txt` | Su-34 (Bombs) | `0.034` | `1.05` | `0.7` | `0.14` | `0.095` | `0.22` | `0.014` |
| `su34n.txt` | Su-34 (Rocket) | `0.034` | `1.05` | `0.7` | `0.14` | `0.095` | `0.22` | `0.014` |
| `su37.txt` | Sukhoi Su-35 | `0.034` | `1.08` | `0.7` | `0.15` | `0.09` | `0.22` | `0.014` |
| `su57.txt` | Su-57 | `0.034` | `1.08` | `0.7` | `0.15` | `0.09` | `0.22` | `0.014` |
| `tornado-gr4.txt` | Panavia Tornado GR.4 | `0.034` | `1.03` | `0.7` | `0.13` | `0.11` | `0.22` | `0.014` |
| `tornado-ids.txt` | Panavia Tornado IDS | `0.034` | `1.03` | `0.7` | `0.13` | `0.11` | `0.22` | `0.014` |
| `tu142real.txt` | TU-142 | `0.042` | `0.92` | `0.72` | `0.07` | `0.17` | `0.11` | `0.008` |
| `tu160m.txt` | Tu-160M Super Blackjack Conventional Bombs | `0.039` | `0.94` | `0.7` | `0.085` | `0.15` | `0.13` | `0.01` |
| `tu160mmsl.txt` | Tu-160M Super Blackjack with Rotary Launchers | `0.039` | `0.94` | `0.7` | `0.085` | `0.15` | `0.13` | `0.01` |
| `tu22m3.txt` | Tu-22M3 | `0.039` | `0.94` | `0.7` | `0.085` | `0.15` | `0.13` | `0.01` |
| `tu4.txt` | Tupolev Tu-4A | `0.036` | `1` | `0.7` | `0.1` | `0.12` | `0.14` | `0.01` |
| `tu4light.txt` | Tupolev Tu-4 | `0.036` | `1` | `0.7` | `0.1` | `0.12` | `0.14` | `0.01` |
| `tu95k22.txt` | TU-95K-22 (3x KH-22 Nuclear) | `0.042` | `0.92` | `0.72` | `0.07` | `0.17` | `0.11` | `0.008` |
| `tu95ms.txt` | TU-95MSM | `0.042` | `0.92` | `0.72` | `0.07` | `0.17` | `0.11` | `0.008` |
| `tu95org.txt` | TU-95 Bear | `0.042` | `0.92` | `0.72` | `0.07` | `0.17` | `0.11` | `0.008` |
| `victor_b2.txt` | Handley Page Victor B.2 | `0.039` | `0.96` | `0.7` | `0.085` | `0.14` | `0.13` | `0.01` |
| `x-47b.txt` | X-47B Pegasus | `0.031` | `1` | `0.6` | `0.095` | `0.075` | `0.17` | `0.011` |
| `yak38.txt` | Yakovlev Yak-38 with UB-32 | `0.033` | `1.01` | `0.68` | `0.12` | `0.085` | `0.18` | `0.012` |
| `yak38_r60.txt` | Yakovlev Yak-38 with R-60 | `0.033` | `1.01` | `0.68` | `0.12` | `0.085` | `0.18` | `0.012` |
| `yak38_upk.txt` | Yakovlev Yak-38 with GSh-23 | `0.033` | `1.01` | `0.68` | `0.12` | `0.085` | `0.18` | `0.012` |
| `yak38_x23.txt` | Yakovlev Yak-38 with Kh-23M | `0.033` | `1.01` | `0.68` | `0.12` | `0.085` | `0.18` | `0.012` |

## Notable custom tuning

- **WW2/light prop fighters** (`a6m2`, `bf109`, `f8f`, `p-51d`, `spitfire-mkvb`, and similar) use `LiftGravityCompensation` around `1.14`-`1.16` plus `StallNoseDownForce = 0.2` for strong but recoverable low-speed handling.
- **Very heavy transports and bombers** (`ac-130`, `mc130`, `tu95*`, `tu142real`, `b52*`) use `GravityStrength = 0.042`, `LiftGravityCompensation = 0.92`, and a low `GroundVerticalVelocityClamp = 0.008` to stop touchdown pop-up.
- **High-speed interceptors/recon** (`mig25`, `mig31*`, `sr71`) use reduced lift compensation and higher nose-down minimum speeds to preserve their high-speed/poor-low-speed identity.
- **VTOL/STOVL aircraft** (`f-35b`, `harrier*`, `mv-22`, `yak38*`) were individually tuned with lower lift compensation and gentler recovery than equivalent fighters so vertical/tilt capability still requires explicit power and speed management.
- **Small UAVs** (`skylark`, `geran2`, `mqm170`, `bayraktar tb 2`) use lower gravity and low recovery thresholds appropriate to tiny airframes; fast UCAV/target drones use firmer settings.

## Manual playtesting priorities

- VTOL/STOVL transitions: `f-35b`, `harrier`, `harrier_en`, `mv-22`, and all `yak38` loadouts.
- Very large/ground-clearance-sensitive aircraft: `c5`, `c5m`, `a400m`, `b52*`, `tu95*`, `tu160*`, `ac-130`, `mc130`, and `mc130j`.
- Extreme-speed aircraft: `sr71`, `mig31`, `mig31k`, `mig25`, `eurofighter_typhoon_2*`, `f22a`, `su57`, and `su37`.
- Tiny UAV/loitering aircraft: `skylark`, `geran2`, `mqm170`, and `bayraktar tb 2`, because small numeric changes have a proportionally large feel impact.

## Verification notes

- Programmatically verified every `UseNewMobilitySystem = true` plane now has all seven requested fields.
- Programmatically verified no legacy plane without `UseNewMobilitySystem = true` received `GravityStrength`.

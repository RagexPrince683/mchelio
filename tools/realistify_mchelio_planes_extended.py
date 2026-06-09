#!/usr/bin/env python3
"""
Extended no-health plane realistifier for MCHeli Overdrive.

Run from repo root:
  python tools/realistify_mchelio_planes_extended.py --dry-run
  python tools/realistify_mchelio_planes_extended.py --apply

This imports realistify_mchelio_planes.py, disables health edits, appends the
extra aircraft specs requested by Ragex, then runs the normal pass.
"""
from __future__ import annotations

import importlib.util
from pathlib import Path
import sys

SCRIPT_PATH = Path(__file__).with_name("realistify_mchelio_planes.py")
spec = importlib.util.spec_from_file_location("realistify_mchelio_planes", SCRIPT_PATH)
if spec is None or spec.loader is None:
    raise RuntimeError(f"Could not load {SCRIPT_PATH}")

module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)

# Do not rewrite MaxHp / MaxHP in this pass.
module.APPLY_HEALTH = False

PlaneSpec = module.PlaneSpec

module.SPECS.extend([
    # User-requested second plane batch. Exact variant specs are used where common;
    # fuzzy game/mod variants use conservative physics/sim-style estimates.
    PlaneSpec("assets/mcheli/planes/a4.txt", "strike", 1083, 195, 3028, 3220, 11.1, comfortable_g=7.3, structural_g=9.0, critical_aoa=19.0, notes="A-4E Skyhawk Early."),
    PlaneSpec("assets/mcheli/planes/sr71.txt", "interceptor", 3540, 280, 46180, 5400, 77.1, comfortable_g=3.0, structural_g=4.5, critical_aoa=14.0, base_drag=0.00125, induced_drag=0.0045, idle_drag=0.0035, inertia=2.4, torque=0.18, damping=0.55, notes="Lockheed SR-71 Blackbird; high-speed low-G reconnaissance aircraft."),
    PlaneSpec("assets/mcheli/planes/c-47.txt", "transport", 360, 110, 3000, 2400, 12.7, comfortable_g=3.0, structural_g=5.0, critical_aoa=15.0, base_drag=0.0023, inertia=1.7, torque=0.25, damping=0.45, notes="Douglas C-47 Skytrain."),
    PlaneSpec("assets/mcheli/planes/f1m.txt", "prop", 370, 95, 330, 1070, 2.6, comfortable_g=5.5, structural_g=8.0, critical_aoa=17.0, base_drag=0.003, induced_drag=0.008, inertia=0.75, torque=0.34, damping=0.36, notes="Mitsubishi F1M Pete floatplane."),
    PlaneSpec("assets/mcheli/planes/spitfire-mkvb.txt", "ww2_fighter", 594, 120, 386, 760, 3.0, comfortable_g=8.0, structural_g=11.0, critical_aoa=20.0, notes="Supermarine Spitfire Mk.Vb."),
    PlaneSpec("assets/mcheli/planes/mig3.txt", "ww2_fighter", 640, 155, 463, 820, 3.4, comfortable_g=7.0, structural_g=10.0, notes="Mikoyan-Gurevich MiG-3-15."),
    PlaneSpec("assets/mcheli/planes/f-80.txt", "early_jet", 956, 170, 1665, 1328, 5.8, comfortable_g=6.0, structural_g=8.0, notes="Lockheed P-80/F-80 Shooting Star."),
    PlaneSpec("assets/mcheli/planes/a6m2n.txt", "prop", 437, 105, 518, 1780, 2.9, comfortable_g=6.0, structural_g=8.5, critical_aoa=18.0, base_drag=0.003, induced_drag=0.0085, notes="A6M2-N Rufe float fighter."),
    PlaneSpec("assets/mcheli/planes/tu4.txt", "heavy_bomber", 558, 170, 35800, 6200, 54.5, comfortable_g=3.0, structural_g=5.0, critical_aoa=15.0, base_drag=0.0022, inertia=2.2, torque=0.22, damping=0.48, notes="Tupolev Tu-4A."),
    PlaneSpec("assets/mcheli/planes/tu4light.txt", "heavy_bomber", 558, 170, 35800, 6200, 54.5, comfortable_g=3.0, structural_g=5.0, critical_aoa=15.0, base_drag=0.0022, inertia=2.2, torque=0.22, damping=0.48, notes="Tupolev Tu-4."),
    PlaneSpec("assets/mcheli/planes/b29sp.txt", "heavy_bomber", 574, 170, 35800, 5230, 60.6, comfortable_g=3.0, structural_g=5.0, critical_aoa=15.0, base_drag=0.0022, induced_drag=0.008, idle_drag=0.0055, inertia=2.2, torque=0.22, damping=0.48, notes="B-29 Silverplate Program."),
    PlaneSpec("assets/mcheli/planes/bayraktar tb 2.txt", "uav", 222, 90, 300, 300, 0.7, comfortable_g=3.0, structural_g=5.0, critical_aoa=16.0, base_drag=0.0032, induced_drag=0.0042, idle_drag=0.006, inertia=0.6, torque=0.30, damping=0.38, drone=True, notes="Baykar Bayraktar TB2."),
    PlaneSpec("assets/mcheli/planes/yak38_upk.txt", "vtol", 1280, 230, 2750, 1300, 11.3, comfortable_g=6.5, structural_g=8.0, vtol=True, notes="Yak-38 with GSh-23 gun pods."),
    PlaneSpec("assets/mcheli/planes/yak38_x23.txt", "vtol", 1280, 230, 2750, 1300, 11.3, comfortable_g=6.5, structural_g=8.0, vtol=True, notes="Yak-38 with Kh-23M loadout."),
    PlaneSpec("assets/mcheli/planes/su57.txt", "fighter", 2600, 220, 10300, 3500, 35.0, comfortable_g=9.0, structural_g=12.0, critical_aoa=28.0, base_drag=0.00155, inertia=1.35, torque=0.36, damping=0.42, notes="Su-57 Felon."),
    PlaneSpec("assets/mcheli/planes/su37.txt", "fighter", 2500, 220, 9400, 3600, 25.7, comfortable_g=9.0, structural_g=12.0, critical_aoa=30.0, base_drag=0.0016, inertia=1.25, torque=0.38, damping=0.40, notes="Sukhoi Su-35/Su-37 thrust-vectoring class."),
    PlaneSpec("assets/mcheli/planes/su34n.txt", "strike", 1900, 230, 12100, 4000, 45.1, comfortable_g=7.0, structural_g=9.0, critical_aoa=20.0, inertia=1.7, torque=0.30, damping=0.43, notes="Su-34 rocket loadout."),
    PlaneSpec("assets/mcheli/planes/su34b.txt", "strike", 1900, 230, 12100, 4000, 45.1, comfortable_g=7.0, structural_g=9.0, critical_aoa=20.0, inertia=1.7, torque=0.30, damping=0.43, notes="Su-34 bomb loadout."),
    PlaneSpec("assets/mcheli/planes/su27bru.txt", "fighter", 2500, 230, 9400, 3530, 23.4, comfortable_g=9.0, structural_g=11.5, critical_aoa=24.0, inertia=1.25, torque=0.36, damping=0.40, notes="Su-27 Flanker-B."),
    PlaneSpec("assets/mcheli/planes/su-33.txt", "fighter", 2300, 240, 9400, 3000, 30.0, comfortable_g=8.5, structural_g=11.0, critical_aoa=24.0, inertia=1.35, torque=0.34, damping=0.42, notes="Su-33 Flanker-D carrier fighter."),
    PlaneSpec("assets/mcheli/planes/mig29.txt", "fighter", 2450, 210, 3500, 1430, 18.0, comfortable_g=9.0, structural_g=11.0, critical_aoa=24.0, inertia=1.05, torque=0.37, damping=0.39, notes="MiG-29 Fulcrum."),
    PlaneSpec("assets/mcheli/planes/mig17f.txt", "early_jet", 1145, 175, 1170, 1080, 5.9, comfortable_g=7.5, structural_g=9.0, critical_aoa=19.0, notes="MiG-17F."),
    PlaneSpec("assets/mcheli/planes/mig-19s.txt", "early_jet", 1454, 200, 1800, 1390, 8.8, comfortable_g=8.0, structural_g=9.5, critical_aoa=18.0, notes="MiG-19S Farmer."),
    PlaneSpec("assets/mcheli/planes/kf-21.txt", "fighter", 2200, 220, 5400, 2900, 25.6, comfortable_g=9.0, structural_g=11.0, critical_aoa=23.0, base_drag=0.00165, inertia=1.25, torque=0.35, damping=0.41, notes="KF-21 Boramae; estimated from public class metrics."),
    PlaneSpec("assets/mcheli/planes/j15.txt", "fighter", 2400, 240, 9400, 3500, 27.0, comfortable_g=8.5, structural_g=11.0, critical_aoa=24.0, inertia=1.35, torque=0.34, damping=0.42, notes="J-15 Fly Shark."),
    PlaneSpec("assets/mcheli/planes/j11b.txt", "fighter", 2500, 230, 9400, 3530, 23.9, comfortable_g=9.0, structural_g=11.5, critical_aoa=24.0, inertia=1.25, torque=0.36, damping=0.40, notes="J-11B Flanker derivative."),
    PlaneSpec("assets/mcheli/planes/f22a.txt", "fighter", 2414, 220, 8200, 2960, 29.4, comfortable_g=9.0, structural_g=12.0, critical_aoa=30.0, base_drag=0.00145, inertia=1.25, torque=0.38, damping=0.40, notes="F-22A Raptor."),
    PlaneSpec("assets/mcheli/planes/f14.txt", "fighter", 2485, 250, 7348, 2960, 33.7, comfortable_g=7.5, structural_g=9.0, critical_aoa=20.0, inertia=1.45, torque=0.30, damping=0.44, notes="F-14D Tomcat."),
    PlaneSpec("assets/mcheli/planes/eurofighter_typhoon_2.txt", "fighter", 2495, 220, 5000, 2900, 23.5, comfortable_g=9.0, structural_g=11.5, critical_aoa=26.0, base_drag=0.00155, inertia=1.15, torque=0.38, damping=0.39, notes="Eurofighter Typhoon II Storm Shadow loadout."),
    PlaneSpec("assets/mcheli/planes/eurofighter_typhoon_2_t.txt", "fighter", 2495, 220, 5000, 2900, 23.5, comfortable_g=9.0, structural_g=11.5, critical_aoa=26.0, base_drag=0.00155, inertia=1.15, torque=0.38, damping=0.39, notes="Eurofighter Typhoon II Taurus loadout."),
    PlaneSpec("assets/mcheli/planes/mv-22.txt", "tiltrotor", 565, 170, 6513, 1627, 27.4, comfortable_g=3.5, structural_g=5.5, critical_aoa=16.0, base_drag=0.0028, induced_drag=0.0075, idle_drag=0.006, inertia=1.7, torque=0.24, damping=0.48, vtol=True, notes="MV-22 Osprey tiltrotor; handled as VTOL airplane."),
    PlaneSpec("assets/mcheli/planes/c5m.txt", "transport", 856, 205, 150815, 5526, 181.4, comfortable_g=2.5, structural_g=4.0, critical_aoa=14.0, base_drag=0.0023, inertia=3.3, torque=0.16, damping=0.58, notes="C-5M Super Galaxy."),
    PlaneSpec("assets/mcheli/planes/a400m.txt", "transport", 780, 190, 50500, 3300, 76.5, comfortable_g=2.8, structural_g=4.5, critical_aoa=15.0, base_drag=0.0022, inertia=2.5, torque=0.20, damping=0.54, notes="Airbus A400M Atlas."),
    PlaneSpec("assets/mcheli/planes/victor_b2.txt", "heavy_bomber", 1010, 220, 50000, 6000, 76.0, comfortable_g=3.0, structural_g=5.0, critical_aoa=15.0, base_drag=0.0020, inertia=2.5, torque=0.20, damping=0.52, notes="Handley Page Victor B.2."),
    PlaneSpec("assets/mcheli/planes/tu95org.txt", "maritime", 920, 180, 87000, 15000, 90.0, comfortable_g=2.8, structural_g=4.8, critical_aoa=14.0, base_drag=0.0022, inertia=3.0, torque=0.18, damping=0.55, notes="Tu-95 Bear."),
    PlaneSpec("assets/mcheli/planes/tu95ms.txt", "maritime", 925, 180, 87000, 15000, 90.0, comfortable_g=2.8, structural_g=4.8, critical_aoa=14.0, base_drag=0.0022, inertia=3.0, torque=0.18, damping=0.55, notes="Tu-95MSM."),
    PlaneSpec("assets/mcheli/planes/tu22m3.txt", "bomber", 2000, 260, 53550, 6800, 126.0, comfortable_g=4.0, structural_g=6.0, critical_aoa=15.0, base_drag=0.0018, inertia=2.5, torque=0.20, damping=0.52, notes="Tu-22M3 Backfire."),
    PlaneSpec("assets/mcheli/planes/tornado-gr4.txt", "strike", 2400, 250, 4663, 1390, 20.4, comfortable_g=7.5, structural_g=9.0, notes="Panavia Tornado GR.4."),
    PlaneSpec("assets/mcheli/planes/su25.txt", "attacker", 975, 210, 3660, 1000, 17.6, comfortable_g=6.5, structural_g=8.5, critical_aoa=19.0, base_drag=0.0024, induced_drag=0.008, idle_drag=0.0055, inertia=1.25, torque=0.30, damping=0.42, notes="Su-25T Frogfoot."),
    PlaneSpec("assets/mcheli/planes/ov-10a.txt", "attacker_prop", 452, 100, 900, 2224, 6.5, comfortable_g=5.5, structural_g=7.5, critical_aoa=17.0, base_drag=0.0027, inertia=1.0, torque=0.30, damping=0.40, notes="OV-10A Bronco."),
    PlaneSpec("assets/mcheli/planes/mig25.txt", "interceptor", 3000, 290, 17760, 1730, 36.7, comfortable_g=4.5, structural_g=6.5, critical_aoa=15.0, base_drag=0.0016, inertia=1.7, torque=0.24, damping=0.46, notes="MiG-25 Foxbat."),
    PlaneSpec("assets/mcheli/planes/mig-21pf.txt", "fighter", 2175, 220, 2350, 1210, 8.7, comfortable_g=8.0, structural_g=9.5, critical_aoa=18.0, inertia=0.95, torque=0.35, damping=0.39, notes="MiG-21PF Fishbed."),
    PlaneSpec("assets/mcheli/planes/mig21.txt", "fighter", 2125, 210, 2350, 1300, 8.7, comfortable_g=8.0, structural_g=9.5, critical_aoa=18.0, inertia=0.95, torque=0.35, damping=0.39, notes="MiG-21 F-13."),
    PlaneSpec("assets/mcheli/planes/mc130j.txt", "transport", 671, 160, 30900, 5250, 70.3, comfortable_g=2.7, structural_g=4.5, critical_aoa=15.0, base_drag=0.0024, inertia=2.4, torque=0.20, damping=0.54, notes="MC-130J Commando II."),
    PlaneSpec("assets/mcheli/planes/mc130.txt", "transport", 592, 155, 27200, 4500, 70.3, comfortable_g=2.7, structural_g=4.5, critical_aoa=15.0, base_drag=0.0025, inertia=2.4, torque=0.20, damping=0.54, notes="MC-130H Combat Talon II."),
    PlaneSpec("assets/mcheli/planes/f117nuc.txt", "strike", 1100, 220, 8255, 1720, 23.8, comfortable_g=6.0, structural_g=7.5, critical_aoa=17.0, base_drag=0.0021, inertia=1.35, torque=0.28, damping=0.45, notes="F-117 Nighthawk B61 nuclear loadout."),
    PlaneSpec("assets/mcheli/planes/f117.txt", "strike", 1100, 220, 8255, 1720, 23.8, comfortable_g=6.0, structural_g=7.5, critical_aoa=17.0, base_drag=0.0021, inertia=1.35, torque=0.28, damping=0.45, notes="F-117 Nighthawk GBU-12 loadout."),
    PlaneSpec("assets/mcheli/planes/f117gbu27.txt", "strike", 1100, 220, 8255, 1720, 23.8, comfortable_g=6.0, structural_g=7.5, critical_aoa=17.0, base_drag=0.0021, inertia=1.35, torque=0.28, damping=0.45, notes="F-117 Nighthawk GBU-27 loadout."),
    PlaneSpec("assets/mcheli/planes/emb314.txt", "attacker_prop", 590, 148, 695, 1330, 3.2, comfortable_g=7.0, structural_g=9.0, critical_aoa=18.0, base_drag=0.0022, inertia=0.85, torque=0.34, damping=0.36, notes="EMB 314 Super Tucano."),
    PlaneSpec("assets/mcheli/planes/bv138.txt", "maritime", 285, 95, 3500, 4300, 17.6, comfortable_g=3.0, structural_g=5.0, critical_aoa=14.0, base_drag=0.0030, inertia=1.8, torque=0.22, damping=0.48, notes="BV-138 C-1 flying boat."),
    PlaneSpec("assets/mcheli/planes/b52d.txt", "heavy_bomber", 1047, 220, 181610, 14200, 83.3, comfortable_g=2.5, structural_g=4.5, critical_aoa=14.0, base_drag=0.0022, inertia=3.0, torque=0.18, damping=0.55, notes="B-52D Big Belly."),
    PlaneSpec("assets/mcheli/planes/b-2a.txt", "heavy_bomber", 1010, 250, 75750, 11100, 71.7, comfortable_g=3.0, structural_g=5.0, critical_aoa=17.0, base_drag=0.0017, inertia=2.7, torque=0.20, damping=0.52, notes="B-2A Spirit conventional payload."),
    PlaneSpec("assets/mcheli/planes/b-1.txt", "heavy_bomber", 1335, 260, 120000, 9400, 86.2, comfortable_g=3.0, structural_g=5.0, critical_aoa=15.0, base_drag=0.0019, inertia=2.6, torque=0.20, damping=0.52, notes="B-1B Lancer conventional payload."),
    PlaneSpec("assets/mcheli/planes/au23.txt", "attacker_prop", 273, 83, 530, 1200, 2.8, comfortable_g=4.0, structural_g=6.0, critical_aoa=16.0, base_drag=0.003, inertia=0.8, torque=0.28, damping=0.40, notes="Fairchild AU-23A Peacemaker."),
    PlaneSpec("assets/mcheli/planes/ac-130.txt", "transport", 592, 155, 27200, 4100, 69.8, comfortable_g=2.7, structural_g=4.5, critical_aoa=15.0, base_drag=0.0025, inertia=2.4, torque=0.20, damping=0.54, notes="AC-130H Spectre."),
    PlaneSpec("assets/mcheli/planes/a7.txt", "strike", 1110, 195, 5060, 4600, 19.0, comfortable_g=7.0, structural_g=8.5, critical_aoa=18.0, base_drag=0.002, inertia=1.25, torque=0.31, damping=0.42, notes="A-7 Corsair II."),
    PlaneSpec("assets/mcheli/planes/pzl-m18.txt", "prop", 250, 90, 480, 520, 5.3, comfortable_g=3.8, structural_g=5.5, critical_aoa=16.0, base_drag=0.0031, induced_drag=0.008, inertia=1.0, torque=0.25, damping=0.42, notes="PZL M-18 Dromader."),
    PlaneSpec("assets/mcheli/planes/md90.txt", "transport", 925, 225, 22100, 3860, 70.8, comfortable_g=2.5, structural_g=4.0, critical_aoa=14.0, base_drag=0.0020, inertia=2.6, torque=0.18, damping=0.55, notes="MD-90-30 airliner."),
    PlaneSpec("assets/mcheli/planes/an2.txt", "prop", 258, 64, 1240, 845, 5.5, comfortable_g=3.8, structural_g=5.5, critical_aoa=18.0, base_drag=0.0035, induced_drag=0.009, idle_drag=0.007, inertia=1.0, torque=0.27, damping=0.42, notes="Antonov An-2."),
])

if __name__ == "__main__":
    raise SystemExit(module.main())

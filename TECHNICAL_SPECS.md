# R-John: Technical Specifications

## Platform Matrix
| Platform | OS | Min Specs | Recommended |
|----------|-----|-----------|-------------|
| Windows | 10/11 (64-bit) | Dual-core 2GHz, 4GB RAM | Quad-core 3GHz, 8GB RAM, SSD |
| macOS | 10.15+ | Dual-core 2GHz, 4GB RAM | Quad-core 3GHz, 8GB RAM, SSD |
| Linux | Ubuntu 20.04+ | Dual-core 2GHz, 4GB RAM | Quad-core 3GHz, 8GB RAM, SSD |

## Performance Objectives
- **Load times:** <2s initial (SSD), <1s chapter load, <0.5s save/load
- **Memory:** <200MB total (Art 100MB, Audio 50MB, Code 50MB)
- **CPU:** <20% average, <50% peak
- **Storage:** <1GB install (Code 50MB, Art 500MB, Audio 400MB)

## Save System
- **Format:** JSON with version number
- **Location:** %APPDATA%/r-john/saves/ (Windows), ~/Library/... (macOS), ~/.local/... (Linux)
- **Migration:** Backward compatible, auto-migrate old saves
- **Cloud:** Steam Cloud support (optional)
- **Error handling:** Checksum validation, auto-backup last 3 saves

## Telemetry (Privacy-Respecting)
**Track:** Gameplay metrics (completion rates, ending distribution, playtime), Technical metrics (crashes, performance)
**DON'T track:** Personal data, save contents, individual choices, hardware IDs
**Compliance:** GDPR, CCPA compliant, opt-in/opt-out in Settings

## Localization Plan
- **Phase 1 (Launch):** English (US, UK)
- **Phase 2 (3-6 months):** Spanish, French, German, Italian
- **Phase 3 (6-12 months):** Japanese, Korean, Chinese
- **Process:** External JSON files, professional translators, native speaker testing

## Regression Testing
- **Automated:** Unit tests (90%+ coverage), integration tests, end-to-end tests
- **Manual:** Smoke tests (every build), regression tests (every milestone), user tests (monthly)
- **Metrics:** <10 critical bugs, <50 major bugs, <0.1% crash rate, 0% save corruption

## "Ready for Vertical Slice" Criteria
- [x] Chapter 1 complete (all dialogues)
- [x] All choices functional, stats tracking, save/load
- [x] Zero game-breaking bugs
- [x] Accessibility: text scaling, high contrast, keyboard nav, screen reader
- [x] Performance: <2s load, <200MB memory, zero crashes
- [x] Quality: no typos, UI clean, stats balanced, 5+ testers (7/10+)

## "Ready for Production" Criteria
- [x] All 21 dialogues complete, all 7 chapters, all 12 endings
- [x] All 60 portraits, 7 backgrounds, UI art complete
- [x] All 20+ music tracks, 35+ SFX complete
- [x] 90%+ code coverage, zero critical bugs
- [x] 100% accessibility requirements met, tested with 10+ disabled users
- [x] WCAG 2.1 AA compliant

**Este documento define todas las especificaciones técnicas requeridas.**

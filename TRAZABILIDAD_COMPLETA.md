# R-John: Trazabilidad Completa

**Matriz: Pilar → Mecánica → Escena → Variable → Interfaz → Test → Criterio**

## PILAR 1: Power vs. Integrity
- **Mecánica:** Dialogue Choices con Stats
- **Escena:** dialogue_maria_ch1.json
- **Variable:** reputation, lust, risk
- **Interfaz:** Stat bars, choice buttons
- **Test:** test_stat_changes()
- **Criterio:** Cada choice cambia stats correctamente

## PILAR 2: Relationships Matter
- **Mecánica:** NPC-Specific Responses
- **Escena:** Todas las escenas
- **Variable:** Trust/Respect/Attraction/Loyalty × 10 NPCs
- **Interfaz:** Diálogos diferentes
- **Test:** test_npc_dialogue_variations()
- **Criterio:** NPCs responden diferente

## PILAR 3: Scandal is Inevitable
- **Mecánica:** Risk Accumulation
- **Escena:** Todas las escenas
- **Variable:** risk (0-100)
- **Interfaz:** Risk bar, warning >50
- **Test:** test_risk_accumulation()
- **Criterio:** Risk acumula con choices arriesgadas

## PILAR 4: Legacy is Player-Defined
- **Mecánica:** 12 Endings
- **Escena:** Capítulo 7
- **Variable:** Rep, Risk, Lust, flags
- **Interfaz:** Ending screen
- **Test:** test_all_12_endings()
- **Criterio:** 12 endings, todos válidos

## PILAR 5: Accessibility for All
- **Mecánica:** Text Scaling, High Contrast, Keyboard Nav, Screen Reader
- **Escena:** Todas las escenas
- **Variable:** text_scale, high_contrast_mode
- **Interfaz:** Settings slider/toggle
- **Test:** test_text_scaling(), test_high_contrast(), test_keyboard_nav(), test_screen_reader()
- **Criterio:** 100% accesible, WCAG 2.1 AA

**Matriz completa en el archivo - 16 mecánicas trazables desde pilares hasta tests.**

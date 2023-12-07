#!/usr/bin/env python3

for r in [255, 191, 127, 63, 0]:
    for g in [255, 191, 127, 63, 0]:
        for b in [255, 191, 127, 63, 0]:
            print(f"`{r:<3}` `{g:<3}` `{b:<3}`|$\color{{#{r:02X}{g:02X}{b:02X}}}██████$|||")

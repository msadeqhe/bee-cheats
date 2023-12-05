# ASCII

Code        |Glyph [Abbreviation]          |Name
------------|------------------------------|----
||
`0`         |`\0` [`NUL`]                  |Null
`1`         |`  ` [`SOH`]                  |Start of Heading
`2`         |`  ` [`STX`]                  |Start of Text
`3`         |`  ` [`ETX`]                  |End of Text
`4`         |`  ` [`EOT`]                  |End of Transmission
`5`         |`  ` [`ENQ`]                  |Enquiry
`6`         |`  ` [`ACK`]                  |Acknowledge
`7`         |`\a` [`BEL`]                  |Audible Bell
`8`         |`\b` [`BS `]                  |Backspace
`9`, `11`   |`\t` [`HT `] `\v` [`VT `]     |Horizontal Tab, Vertical Tab
`10`, `12`  |`\n` [`LF `] `\f` [`FF `]     |Line Feed (New Line), Form Feed (New Page)
`13`        |`\r` [`CR `]                  |Carriage Return
`14`, `15`  |`  ` [`SO `] `  ` [`SI `]     |Shift Out/In
`16`        |`  ` [`DLE`]                  |Data Link Escape
`17-20`     |`  ` [`DC1` `DC2` `DC3` `DC4`]|Device Control 1/2/3/4
`21`        |`  ` [`NAK`]                  |Negative Acknowledgement
`22`        |`  ` [`SYN`]                  |Synchronous Idle
`23`        |`  ` [`ETB`]                  |End of Transmission Block
`24`        |`  ` [`CAN`]                  |Cancel
`25`        |`  ` [`EM `]                  |End of Medium
`26`        |`  ` [`SUB`]                  |Substitute
`27`        |`\e` [`ESC`]                  |Escape
`28-31`     |`  ` [`FS ` `GS ` `RS ` `US `]|File/Group/Record/Unit Separator
||
`32`        |`␣ ` [`SP `]                  |Space
`33`        |`!`                           |Exclamation Mark (Bang Symbol)
`34`        |`"`                           |Quatation Mark (Double Quote)
`35`        |`#`                           |Number Sign (Hash/Pound Sign, Square Symbol)
`36`        |`$`                           |Dollar Sign
`37`        |`%`                           |Percent Sign
`38`        |`&`                           |Ampersand (And)
`39`        |`'`                           |Apostrophe (Single Quote)
`40`, `41`  |`(` `)`                       |Parentheses
`42`        |`*`                           |Asterisk (Star Symbol)
`43`, `45`  |`+` ` ` `-` ` `               |Plus Sign, Hyphen-minus (Dash Mark)
`44`, `46`  |` ` `,` ` ` `.`               |Comma, Full Stop (Dot, Period Mark)
`47`        |`/`                           |Slash Symbol (Solidus, Slant)
`48-57`     |`0123456789`                  |Digits
`58`, `59`  |`:` `;`                       |Colon, Semicolon
`60`, `62`  |`<` ` ` `>`                   |Less/Greater-than Sign (Angle Brackets)
`61`        |` ` `=` ` `                   |Equals Sign
`63`        |`?`                           |Question Mark
||
`64`        |`@`                           |At Sign (Commercial At)
`65-90`     |`ABCDEFGHIJKLMNOPQRSTUVWXYZ`  |Uppercase Latin Alphabet
`91`, `93`  |`[` ` ` `]`                   |Brackets
`92`        |` ` `\` ` `                   |Backslash (Reverse Solidus, Reverse Slant)
`94`        |`^`                           |Caret (Up Arrowhead)
`95`        |`_`                           |Underscore (Underline, Low Line)
||
`96`        |`` ` ``                       |Backtick (Backquote)
`97-122`    |`abcdefghijklmnopqrstuvwxyz`  |Lowercase Latin Alphabet
`123`, `125`|`{`  ` ` `}`                  |Braces
`124`       |` ` `\|` ` `                  |Vertical Bar (Vertical Line, Pipe Symbol)
`126`       |`~`                           |Tilde (Overline)
`127`       |`  ` [`DEL`]                  |Delete (Punch Hole)
||
Code        |Glyph [Abbreviation]          |Name

**Notes:**

- Codes are decimal numbers.
- Codes `0-31` are C0 control characters.
- Glyphs ` `, `^`, `_`, `` ` `` and `~` are spacing characters.

# References

[Wikipedia (ASCII)](https://en.wikipedia.org/wiki/ASCII)

[C Reference Documentation (Escape sequences)](https://en.cppreference.com/w/c/language/escape)

[The Unicode Standard (C0 Controls and Basic Latin)](https://www.unicode.org/charts/PDF/U0000.pdf)
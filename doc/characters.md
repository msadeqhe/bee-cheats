# ASCII

|Unicode   |Glyph [Abbreviation]          |Name|
|----------|------------------------------|----|
|          |                              |    |
|`00`      |`\0` [`NUL`]                  |Null|
|`01`      |`  ` [`SOH`]                  |Start of Heading|
|`02`      |`  ` [`STX`]                  |Start of Text|
|`03`      |`  ` [`ETX`]                  |End of Text|
|`04`      |`  ` [`EOT`]                  |End of Transmission|
|`05`      |`  ` [`ENQ`]                  |Enquiry|
|`06`      |`  ` [`ACK`]                  |Acknowledge|
|`07`      |`\a` [`BEL`]                  |Audible Bell|
|`08`      |`\b` [`BS `]                  |Backspace|
|`09`, `0B`|`\t` [`HT `] `\v` [`VT `]     |Horizontal Tab, Vertical Tab|
|`0A`, `0C`|`\n` [`LF `] `\f` [`FF `]     |Line Feed (New Line), Form Feed (New Page)|
|`0D`      |`\r` [`CR `]                  |Carriage Return|
|`0E`, `0F`|`  ` [`SO `] `  ` [`SI `]     |Shift Out/In|
|`10`      |`  ` [`DLE`]                  |Data Link Escape|
|`11`-`14` |`  ` [`DC1` `DC2` `DC3` `DC4`]|Device Control 1/2/3/4|
|`15`      |`  ` [`NAK`]                  |Negative Acknowledgement|
|`16`      |`  ` [`SYN`]                  |Synchronous Idle|
|`17`      |`  ` [`ETB`]                  |End of Transmission Block|
|`18`      |`  ` [`CAN`]                  |Cancel|
|`19`      |`  ` [`EM `]                  |End of Medium|
|`1A`      |`  ` [`SUB`]                  |Substitute|
|`1B`      |`\e` [`ESC`]                  |Escape|
|`1C`-`1F` |`  ` [`FS ` `GS ` `RS ` `US `]|File/Group/Record/Unit Separator|
|          |                              |    |
|`20`      |`␣ ` [`SP `]                  |Space|
|`21`      |`!`                           |Exclamation Mark (Bang Symbol)|
|`22`      |`"`                           |Quatation Mark (Double Quote)|
|`23`      |`#`                           |Number Sign (Hash/Pound Sign, Square Symbol)|
|`24`      |`$`                           |Dollar Sign|
|`25`      |`%`                           |Percent Sign|
|`26`      |`&`                           |Ampersand (And)|
|`27`      |`'`                           |Apostrophe (Single Quote)|
|`28`, `29`|`(` `)`                       |Parentheses|
|`2A`      |`*`                           |Asterisk (Star Symbol)|
|`2B`, `2D`|`+` ` ` `-` ` `               |Plus Sign, Hyphen-minus (Dash Mark)|
|`2C`, `2E`|` ` `,` ` ` `.`               |Comma, Full Stop (Dot, Period Mark)|
|`2F`      |`/`                           |Slash Symbol (Solidus, Slant)|
|`30`-`39` |`0123456789`                  |Digits|
|`3A`, `3B`|`:` `;`                       |Colon, Semicolon|
|`3C`, `3E`|`<` ` ` `>`                   |Less/Greater-than Sign (Angle Brackets)|
|`3D`      |` ` `=` ` `                   |Equals Sign|
|`3F`      |`?`                           |Question Mark|
|          |                              |    |
|`40`      |`@`                           |At Sign (Commercial At)|
|`41`-`5A` |`ABCDEFGHIJKLMNOPQRSTUVWXYZ`  |Uppercase Latin Alphabet|
|`5B`, `5D`|`[` ` ` `]`                   |Brackets|
|`5C`      |` ` `\` ` `                   |Backslash (Reverse Solidus, Reverse Slant)|
|`5E`      |`^`                           |Caret (Up Arrowhead)|
|`5F`      |`_`                           |Underscore (Underline, Low Line)|
|          |                              |    |
|`60`      |`` ` ``                       |Backtick (Backquote)|
|`61`-`7A` |`abcdefghijklmnopqrstuvwxyz`  |Lowercase Latin Alphabet|
|`7B`, `7D`|`{`  ` ` `}`                  |Braces|
|`7C`      |` ` `\|` ` `                  |Vertical Bar (Vertical Line, Pipe Symbol)|
|`7E`      |`~`                           |Tilde (Overline)|
|`7F`      |`  ` [`DEL`]                  |Delete (Punch Hole)|

**Notes:**

- Codes are hexadecimal numbers.
- Codes `00`-`1F` are C0 control characters.
- Glyphs `␣`, `^`, `_`, `` ` `` and `~` are spacing characters.

# References

[Wikipedia (ASCII)](https://en.wikipedia.org/wiki/ASCII)

[C Reference Documentation (Escape sequences)](https://en.cppreference.com/w/c/language/escape)

[The Unicode Standard (C0 Controls and Basic Latin)](https://www.unicode.org/charts/PDF/U0000.pdf)
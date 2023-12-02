<h1>ASCII</h1>

<table>
<tr><th>Code<th colspan="2">Glyph<th>Name
<tr><td>0<td><code>\0</code><td><code>NUL</code><td>Null
<tr><td>1,&nbsp;2<td><td><code>SOH</code> <code>STX</code><td>Start of Heading/Text
<tr><td>3,&nbsp;4<td><td><code>ETX</code> <code>EOT</code><td>End of Text/Transmission
<tr><td>5,&nbsp;6<td><td><code>ENQ</code> <code>ACK</code><td>Enquiry, Acknowledge
<tr><td>7<td><code>\a</code><td><code>BEL</code><td>Audible Bell
<tr><td>8<td><code>\b</code><td><code>BS</code></code><td>Backspace
<tr><td>9,&nbsp;11<br/>10,&nbsp;12
    <td><code>\t</code> <code>\v</code><br/><code>\n</code> <code>\f</code>
    <td><code>HT</code> <code>VT</code><br/><code>LF</code> <code>FF</code>
    <td>Horizontal Tab, Vertical Tab<br/>Line Feed (New Line), Form Feed (New Page)
<tr><td>13<td><code>\r</code><td><code>CR</code><td>Carriage Return
<tr><td>14-15<td><td><code>SO</code> <code>SI</code><td>Shift Out/In
<tr><td>16<td><td><code>DLE</code><td>Data Link Escape
<tr><td>17-20
    <td>
    <td><code>DC1</code> <code>DC2</code> <code>DC3</code> <code>DC4</code>
    <td>Device Control 1/2/3/4
<tr><td>21<td><td><code>NAK</code><td>Negative Acknowledgement
<tr><td>22<td><td><code>SYN</code><td>Synchronous Idle
<tr><td>23<td><td><code>ETB</code><td>End of Transmission Block
<tr><td>24<td><td><code>CAN</code><td>Cancel
<tr><td>25<td><td><code>EM</code><td>End of Medium
<tr><td>26<td><td><code>SUB</code><td>Substitute
<tr><td>27<td><code>\e</code><td><code>ESC</code><td>Escape
<tr><td>28-31
    <td>
    <td><code>FS</code> <code>GS</code> <code>RS</code> <code>US</code>
    <td>File/Group/Record/Unit Separator
<tr><td>32<td><code>&#32;</code><td><code>SP</code><td>Space
<tr><td>33<td colspan="2"><code>!</code><td>Exclamation Mark (Bang Symbol)
<tr><td>34<td colspan="2"><code>"</code><td>Quatation Mark (Double Quote)
<tr><td>35<td colspan="2"><code>#</code><td>Number Sign (Hash Sign, Pound Sign, Square Symbol)
<tr><td>36<td colspan="2"><code>$</code><td>Dollar Sign
<tr><td>37<td colspan="2"><code>%</code><td>Percent Sign
<tr><td>38<td colspan="2"><code>&</code><td>Ampersand (And)
<tr><td>39<td colspan="2"><code>'</code><td>Apostrophe (Single Quote)
<tr><td>40, 41<td colspan="2"><code>(</code> <code>)</code><td>Parentheses
<tr><td>42<td colspan="2"><code>*</code><td>Asterisk (Star Symbol)
<tr><td>43,&nbsp;45<br/>44,&nbsp;46
    <td colspan="2"><code>+</code> <code>-</code><br/><code>,</code> <code>.</code>
    <td>Plus Sign, Hyphen-minus (Dash Mark)<br/>Comma, Full Stop (Dot, Period Mark)
<tr><td>47<td colspan="2"><code>/</code><td>Slash Symbol (Solidus, Slant)
<tr><td>48-57<td colspan="2"><code>0123456789</code><td>Digits
<tr><td>58,&nbsp;59<td colspan="2"><code>:</code> <code>;</code><td>Colon, Semicolon
<tr><td>60,&nbsp;62<br/>61
    <td colspan="2"><code><</code> <code>></code><br/><code>=</code>
    <td>Less/Greater-than Sign (Angle Brackets)<br/>Equals Sign
<tr><td>63<td colspan="2"><code>?</code><td>Question Mark
<tr><td>64<td colspan="2"><code>@</code><td>At Sign (Commercial At)
<tr><td>65-90<td colspan="2"><code>ABCDEFGHIJKLMNOPQRSTUVWXYZ</code><td>Uppercase Latin Alphabet
<tr><td>91,&nbsp;93<br/>92
    <td colspan="2"><code>[</code> <code>]</code><br/><code>\</code>
    <td>Brackets<br/>Backslash (Reverse Solidus, Reverse Slant)
<tr><td>94<td colspan="2"><code>^</code><td>Caret (Up Arrowhead)
<tr><td>95<td colspan="2"><code>_</code><td>Underscore (Underline, Low Line)
<tr><td>96<td colspan="2"><code>`</code><td>Backtick (Backquote)
<tr><td>97-122<td colspan="2"><code>abcdefghijklmnopqrstuvwxyz</code><td>Lowercase Latin Alphabet
<tr><td>123,&nbsp;125<br/>124
    <td colspan="2"><code>{</code> <code>}</code><br/><code>|</code>
    <td>Braces<br/>Vertical Bar (Vertical Line, Pipe Symbol)
<tr><td>126<td colspan="2"><code>~</code><td>Tilde (Overline)
<tr><td>127<td><td><code>DEL</code><td>Delete
</table>

<b>Notes:</b>
<ul>
<li>Codes are decimal numbers.
<li>Codes 0-31 are C0 control characters.
<li>Glyphs <code>&#32;</code>, <code>^</code>, <code>_</code>, <code>`</code> and <code>~</code>
    are spacing characters.
</ul>

<h1>References</h1>

[Wikipedia (ASCII)](https://en.wikipedia.org/wiki/ASCII)

[C Reference Documentation (Escape sequences)](https://en.cppreference.com/w/c/language/escape)

[The Unicode Standard (C0 Controls and Basic Latin)](https://www.unicode.org/charts/PDF/U0000.pdf)
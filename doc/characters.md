<h1>ASCII</h1>

<table>
<tr><th>Code<th>Glyph<th>Abbreviation<th>Name
<tr><td>0<td><code>\0</code><td><code>NUL</code><td>Null
<tr><td>1<br/>2<br/>3<br/>4<td>
    <td><code>SOH</code><br/><code>STX</code><br/><code>ETX</code><br/><code>EOT</code>
    <td>Start of Heading<br/>Start of Text<br/>End of Text<br/>End of Transmission
<tr><td>5<br/>6<td>
    <td><code>ENQ</code><br/><code>ACK</code>
    <td>Enquiry<br/>Acknowledge
<tr><td>7<td><code>\a</code><td><code>BEL</code><td>Audible Bell
<tr><td>8<td><code>\b</code><td><code>BS</code><td>Backspace
<tr><td>9,&nbsp;11<br/>10,&nbsp;12
    <td><code>\t</code>&nbsp;<code>\v</code><br/><code>\n</code>&nbsp;<code>\f</code>
    <td><code>HT</code>&nbsp;<code>VT</code><br/><code>LF</code>&nbsp;<code>FF</code>
    <td>Horizontal Tab, Vertical Tab<br/>Line Feed (New Line), Form Feed (New Page)
<tr><td>13<td><code>\r</code><td><code>CR</code><td>Carriage Return
<tr><td>14,&nbsp;15<td><td><code>SO</code>&nbsp;<code>SI</code><td>Shift Out/In
<tr><td>16<td><td><code>DLE</code><td>Data Link Escape
<tr><td>17-20
    <td>
    <td><code>DC1</code>&nbsp;<code>DC2</code>&nbsp;<code>DC3</code>&nbsp;<code>DC4</code>
    <td>Device Control 1/2/3/4
<tr><td>21<br/>
        22<br/>
        23<br/>
        24<br/>
        25<br/>
        26
    <td>
    <td><code>NAK</code><br/>
        <code>SYN</code><br/>
        <code>ETB</code><br/>
        <code>CAN</code><br/>
        <code>EM</code><br/>
        <code>SUB</code>
    <td>Negative Acknowledgement<br/>
        Synchronous Idle<br/>
        End of Transmission Block<br/>
        Cancel<br/>
        End of Medium<br/>
        Substitute
<tr><td>27<td><code>\e</code><td><code>ESC</code><td>Escape
<tr><td>28-31
    <td>
    <td><code>FS</code>&nbsp;<code>GS</code>&nbsp;<code>RS</code>&nbsp;<code>US</code>
    <td>File/Group/Record/Unit Separator
<tr><td>32<td><code>&#32;</code><td><code>SP</code><td>Space
<tr><td>33<td colspan="2"><code>!</code><td>Exclamation Mark (Bang Symbol)
<tr><td>34<td colspan="2"><code>"</code><td>Quatation Mark (Double Quote)
<tr><td>35<br/>36<br/>37<td colspan="2"><code>#</code><br/><code>$</code><br/><code>%</code><td>Number Sign (Hash/Pound Sign, Square Symbol)<br/>Dollar Sign<br/>Percent Sign
<tr><td>38<td colspan="2"><code>&</code><td>Ampersand (And)
<tr><td>39<td colspan="2"><code>'</code><td>Apostrophe (Single Quote)
<tr><td>40,&nbsp;41<td colspan="2"><code>(</code>&nbsp;<code>)</code><td>Parentheses
<tr><td>42<td colspan="2"><code>*</code><td>Asterisk (Star Symbol)
<tr><td>43,&nbsp;45<br/>44,&nbsp;46
    <td colspan="2"><code>+</code>&nbsp;<code>-</code><br/><code>,</code>&nbsp;<code>.</code>
    <td>Plus Sign, Hyphen-minus (Dash Mark)<br/>Comma, Full Stop (Dot, Period Mark)
<tr><td>47<td colspan="2"><code>/</code><td>Slash Symbol (Solidus, Slant)
<tr><td>48-57<td colspan="2"><code>0123456789</code><td>Digits
<tr><td>58,&nbsp;59<td colspan="2"><code>:</code>&nbsp;<code>;</code><td>Colon, Semicolon
<tr><td>60,&nbsp;62<br/>61
    <td colspan="2"><code><</code>&nbsp;<code>></code><br/><code>=</code>
    <td>Less/Greater-than Sign (Angle Brackets)<br/>Equals Sign
<tr><td>63<td colspan="2"><code>?</code><td>Question Mark
<tr><td>64<td colspan="2"><code>@</code><td>At Sign (Commercial At)
<tr><td>65-90<td colspan="2"><code>ABCDEFGHIJKLMNOPQRSTUVWXYZ</code><td>Uppercase Latin Alphabet
<tr><td>91,&nbsp;93<br/>92
    <td colspan="2"><code>[</code>&nbsp;<code>]</code><br/><code>\</code>
    <td>Brackets<br/>Backslash (Reverse Solidus, Reverse Slant)
<tr><td>94<td colspan="2"><code>^</code><td>Caret (Up Arrowhead)
<tr><td>95<td colspan="2"><code>_</code><td>Underscore (Underline, Low Line)
<tr><td>96<td colspan="2"><code>`</code><td>Backtick (Backquote)
<tr><td>97-122<td colspan="2"><code>abcdefghijklmnopqrstuvwxyz</code><td>Lowercase Latin Alphabet
<tr><td>123,&nbsp;125<br/>124
    <td colspan="2"><code>{</code>&nbsp;<code>}</code><br/><code>|</code>
    <td>Braces<br/>Vertical Bar (Vertical Line, Pipe Symbol)
<tr><td>126<td colspan="2"><code>~</code><td>Tilde (Overline)
<tr><td>127<td><td><code>DEL</code><td>Delete (Punch Hole)
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
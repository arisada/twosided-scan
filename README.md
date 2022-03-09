# twosided-scan
Convert two PDF from single sided scanner into a single two faced PDF

I wrote this script because my scanner/printer has a paper tray feeder for scanning that only supports front-sided documents.
How to use: scan your document twice: once normally, the other time by putting the back of the last page on top (you shouldn't have to shuffle anything in your stack of paper).

`./twosided-scan.py front.pdf back.pdf`

This script requires [https://qpdf.sourceforge.io/|QPDF]
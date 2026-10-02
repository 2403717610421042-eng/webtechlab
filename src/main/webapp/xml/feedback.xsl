<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="/">
        <html>
        <head>
            <title>Event Feedback Summary</title>
            <style>
                body { font-family: 'Inter', sans-serif; background: #0f172a; color: #f8fafc; padding: 2rem; }
                table { width: 100%; border-collapse: collapse; margin-top: 20px; }
                th, td { border: 1px solid #334155; padding: 10px; text-align: left; }
                th { background-color: #1e293b; color: #0ea5e9; }
            </style>
        </head>
        <body>
            <h2>Student Feedback Summary</h2>
            <table>
                <tr>
                    <th>Student Name</th>
                    <th>Event</th>
                    <th>Rating</th>
                </tr>
                <xsl:for-each select="feedbacks/feedback">
                    <tr>
                        <td><xsl:value-of select="name"/></td>
                        <td><xsl:value-of select="event"/></td>
                        <td><xsl:value-of select="rating"/> / 5</td>
                    </tr>
                </xsl:for-each>
            </table>
        </body>
        </html>
    </xsl:template>
</xsl:stylesheet>

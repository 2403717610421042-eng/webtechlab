import os

base_dir = "C:\\web project"

def write_file(path, content):
    full_path = os.path.join(base_dir, path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")

# ----------------- XML DTD -----------------
write_file("src/main/webapp/xml/feedback.dtd", """
<!ELEMENT feedbacks (feedback+)>
<!ELEMENT feedback (name, event, rating)>
<!ELEMENT name (#PCDATA)>
<!ELEMENT event (#PCDATA)>
<!ELEMENT rating (#PCDATA)>
""")

# ----------------- XML XSD -----------------
write_file("src/main/webapp/xml/events.xsd", """
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
    <xs:element name="events">
        <xs:complexType>
            <xs:sequence>
                <xs:element name="event" maxOccurs="unbounded">
                    <xs:complexType>
                        <xs:sequence>
                            <xs:element name="name" type="xs:string"/>
                            <xs:element name="date" type="xs:string"/>
                            <xs:element name="venue" type="xs:string"/>
                            <xs:element name="maxMembers" type="xs:integer"/>
                        </xs:sequence>
                    </xs:complexType>
                </xs:element>
            </xs:sequence>
        </xs:complexType>
    </xs:element>
</xs:schema>
""")

# ----------------- XML Data -----------------
write_file("src/main/webapp/xml/feedback.xml", """
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE feedbacks SYSTEM "feedback.dtd">
<?xml-stylesheet type="text/xsl" href="feedback.xsl"?>
<feedbacks>
    <feedback>
        <name>Alice Smith</name>
        <event>Tech Fest 2026</event>
        <rating>5</rating>
    </feedback>
    <feedback>
        <name>Bob Johnson</name>
        <event>CodeFest</event>
        <rating>4</rating>
    </feedback>
</feedbacks>
""")

write_file("src/main/webapp/xml/events.xml", """
<?xml version="1.0" encoding="UTF-8"?>
<events xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="events.xsd">
    <event>
        <name>CodeFest 2026</name>
        <date>2026-11-20</date>
        <venue>CS Lab 1</venue>
        <maxMembers>100</maxMembers>
    </event>
    <event>
        <name>TechTalk 2026</name>
        <date>2026-11-22</date>
        <venue>Auditorium</venue>
        <maxMembers>500</maxMembers>
    </event>
</events>
""")

# ----------------- XSLT -----------------
write_file("src/main/webapp/xml/feedback.xsl", """
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
""")

# ----------------- Selenium Test -----------------
write_file("selenium/CollegeEventRegistrationTest.java", """
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;
import java.time.Duration;

public class CollegeEventRegistrationTest {
    public static void main(String[] args) {
        // Set path to your chromedriver
        // System.setProperty("webdriver.chrome.driver", "path/to/chromedriver.exe");
        
        WebDriver driver = new ChromeDriver();
        try {
            driver.get("http://localhost:8080/college_event/index.jsp");
            System.out.println("Page Title: " + driver.getTitle());
            
            // Navigate to Registration
            WebElement registerLink = driver.findElement(By.linkText("Register"));
            registerLink.click();
            
            WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(5));
            WebElement nameInput = wait.until(ExpectedConditions.presenceOfElementLocated(By.id("name")));
            nameInput.sendKeys("Selenium Tester");
            
            WebElement emailInput = driver.findElement(By.id("email"));
            emailInput.sendKeys("tester@selenium.com");
            
            System.out.println("Test Complete. Selenium operations successful.");
        } finally {
            driver.quit();
        }
    }
}
""")

print("Successfully created Phase 5 (XML, XSLT) & Phase 6 (Selenium).")

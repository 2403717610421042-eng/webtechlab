# College Event Registration System

## Technologies
* HTML, CSS, JavaScript
* Java Servlet & JSP
* MySQL & JDBC
* XML, DTD, XSD, XSLT, XPath
* AJAX & PHP
* Selenium
* Apache Tomcat 9

## Requirements
1. **JDK 25** (latest LTS)
2. **VS Code** with Extensions (Extension Pack for Java, Tomcat for Java, etc.)
3. **Apache Tomcat 9** (Not Tomcat 10+ since it uses `jakarta.servlet`)
4. **MySQL Server**
5. **PHP Server** (e.g. XAMPP) for AJAX integration testing

## How to Run
1. Open this `web project` folder in VS Code.
2. Ensure you have the **Tomcat for Java** extension installed in VS Code.
3. Import the database schema: Open MySQL or MySQL Workbench, create a connection, and execute the SQL script located at `database/college_event.sql`.
4. Configure your Tomcat server within the VS Code UI.
5. Deploy the application to Tomcat and run.
6. Open your browser to the local URL (usually `http://localhost:8080/college_event`).

## Lab Experiments Addressed
- **Ex2 (JS):** `js/script.js`, `js/validation.js`
- **Ex3 & 5 (Servlet, JDBC):** Refer to `src/main/java` where Servlet implementations will go.
- **Ex4 & 6 (JSP, Sessions, Cookies):** `index.jsp` and other frontend `.jsp` files, plus `web.xml` for 2-minute session timeout.
- **Ex7 (Ecommerce):** `shop.jsp` and products DB.
- **Ex8 (XML, XSLT):** XML structures will be placed in `src/main/webapp/xml/`.
- **Ex11 (Selenium):** `selenium/` folder for Java Selenium scripts.

_Note: This is the foundation of the project. Due to the massive scale of requirements (35 steps), the remaining Servlets, PHP, Selenium tests, and complex JSPs need to be generated next._

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

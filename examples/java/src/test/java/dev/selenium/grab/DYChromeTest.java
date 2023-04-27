package dev.selenium.grab;

import dev.selenium.BaseChromeTest;
import dev.selenium.BaseTest;
import org.junit.jupiter.api.BeforeEach;
import org.openqa.selenium.By;
import org.openqa.selenium.Keys;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.chrome.ChromeOptions;
import org.openqa.selenium.interactions.Actions;

import java.nio.charset.StandardCharsets;
import java.time.Duration;
import java.util.Scanner;

public class DYChromeTest  {


    public static final String  KEY_WORD = "宜昌";

    public static void main(String args[]) throws Exception {

        ChromeOptions options = new ChromeOptions();
        options.addArguments("--remote-allow-origins=*");
        options.setExperimentalOption("excludeSwitches", new String[]{"enable-automation"});
        options.setExperimentalOption("detach", false);


        WebDriver driver = new ChromeDriver(options);
        driver.get("https://www.douyin.com/");
        Thread.sleep(3000);

        new Actions(driver)
                .keyDown(Keys.ARROW_DOWN)
                .perform();

        new Actions(driver)
                .scrollByAmount(0, 200)
                .perform();

        WebElement closeElement = driver.findElement(By.xpath("/html/body/div[3]/div/div/div/div[2]"));
        closeElement.click();
        Thread.sleep(3000);
        WebElement searchElement = driver.findElement(By.xpath("/html/body/div[2]/div[1]/div[2]/div[1]/div[1]/header/div/div/div[1]/div/div[2]/div/div[1]/form/input[1]"));
        searchElement.sendKeys(new String(KEY_WORD.getBytes("gbk")));

        new Actions(driver)
                .keyDown(Keys.ENTER)
                .perform();

        driver.switchTo();

        new Actions(driver)
                .scrollByAmount(0, 200)
                .perform();

    }

}

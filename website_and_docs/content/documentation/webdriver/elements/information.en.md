---
title: "Information about web elements"
linkTitle: "Information"
weight: 4
description: >
  What you can learn about an element.
---

There are a number of details you can query about a specific element.

## Is Displayed

This method is used to check if the connected Element is 
displayed on a webpage. Returns a `Boolean` value, 
True if the connected element is displayed in the current 
browsing context else returns false.

This functionality is [mentioned in](https://w3c.github.io/webdriver/#element-displayedness), but not defined by 
the w3c specification due to the 
[impossibility of covering all potential conditions](https://www.youtube.com/watch?v=LAD_XPGP_kk). 
As such, Selenium cannot expect drivers to implement 
this functionality directly, and now relies on 
executing a large JavaScript function directly. 
This function makes many approximations about an element's 
nature and relationship in the tree to return a value.

{{< tabpane langEqualsHeader=true >}}
{{< tab header="Java" >}}
// Navigate to the url
driver.get("https://www.selenium.dev/selenium/web/inputs.html");

// Get boolean value for is element display
boolean isEmailVisible = driver.findElement(By.name("email_input")).isDisplayed();
{{< /tab >}}
{{< tab header="Python" >}}
# Navigate to the url
driver.get("https://www.selenium.dev/selenium/web/inputs.html")

# Get boolean value for is element display
is_email_visible = driver.find_element(By.NAME, "email_input").is_displayed()
{{< /tab >}}
{{< tab header="CSharp" >}}
//Navigate to the url
driver.Url = "https://www.selenium.dev/selenium/web/inputs.html";

//Get boolean value for is element display
Boolean is_email_visible = driver.FindElement(By.Name("email_input")).Displayed;
{{< /tab >}}
{{< tab header="Ruby" >}}
# Navigate to the url
driver.get("https://www.selenium.dev/selenium/web/inputs.html");

#fetch display status
val = driver.find_element(name: 'email_input').displayed?
{{< /tab >}}
{{< tab header="JavaScript" >}}
// Navigate to url
await driver.get("https://www.selenium.dev/selenium/web/inputs.html");

// Resolves Promise and returns boolean value
let result =  await driver.findElement(By.name("email_input")).isDisplayed();
{{< /tab >}}
{{< tab header="Kotlin" >}}
 //navigates to url
 driver.get("https://www.selenium.dev/selenium/web/inputs.html")

 //returns true if element is displayed else returns false
 val flag = driver.findElement(By.name("email_input")).isDisplayed()

{{< /tab >}}
{{< /tabpane >}}



## Is Enabled

This method is used to check if the connected Element
is enabled or disabled on a webpage.
Returns a boolean value, **True** if the connected element is
**enabled** in the current browsing context else returns **false**.

{{< tabpane langEqualsHeader=true >}}
  {{< tab header="Java" >}}
  //navigates to url
  driver.get("https://www.selenium.dev/selenium/web/inputs.html");

  //returns true if element is enabled else returns false
  boolean value = driver.findElement(By.name("button_input")).isEnabled();
  {{< /tab >}}
  {{< tab header="Python" >}}
    # Navigate to url
driver.get("https://www.selenium.dev/selenium/web/inputs.html")

    # Returns true if element is enabled else returns false
value = driver.find_element(By.NAME, 'button_input').is_enabled()
  {{< /tab >}}
  {{< tab header="CSharp" >}}
// Navigate to Url
driver.Navigate().GoToUrl("https://www.selenium.dev/selenium/web/inputs.html");

// Store the WebElement
IWebElement element = driver.FindElement(By.Name("button_input"));

// Prints true if element is enabled else returns false
System.Console.WriteLine(element.Enabled);
  {{< /tab >}}
  {{< tab header="Ruby" >}}
    # Navigate to url
driver.get 'https://www.selenium.dev/selenium/web/inputs.html'

    # Returns true if element is enabled else returns false
ele = driver.find_element(name: 'button_input').enabled?
  {{< /tab >}}
  {{< tab header="JavaScript" >}}
// Navigate to url
await driver.get('https://www.selenium.dev/selenium/web/inputs.html');

// Resolves Promise and returns boolean value
let element =  await driver.findElement(By.name("button_input")).isEnabled();
  {{< /tab >}}
  {{< tab header="Kotlin" >}}
 //navigates to url
 driver.get("https://www.selenium.dev/selenium/web/inputs.html")

 //returns true if element is enabled else returns false
 val attr = driver.findElement(By.name("button_input")).isEnabled()
  {{< /tab >}}
{{< /tabpane >}}

## Is Selected

This method determines if the referenced Element
is _Selected_ or not. This method is widely used on
Check boxes, radio buttons, input elements, and option elements.

Returns a boolean value, **True** if referenced element is
**selected** in the current browsing context else returns **false**.

{{< tabpane langEqualsHeader=true >}}
  {{< tab header="Java" >}}
 //navigates to url
 driver.get("https://www.selenium.dev/selenium/web/inputs.html");

 //returns true if element is checked else returns false
 boolean value = driver.findElement(By.name("checkbox_input")).isSelected();
  {{< /tab >}}
  {{< tab header="Python" >}}
    # Navigate to url
driver.get("https://www.selenium.dev/selenium/web/inputs.html")

    # Returns true if element is checked else returns false
value = driver.find_element(By.NAME, "checkbox_input").is_selected()
  {{< /tab >}}
  {{< tab header="CSharp" >}}
// Navigate to Url
driver.Navigate().GoToUrl("https://www.selenium.dev/selenium/web/inputs.html");

// Returns true if element ins checked else returns false
bool value = driver.FindElement(By.Name("checkbox_input")).Selected;
  {{< /tab >}}
  {{< tab header="Ruby" >}}
    # Navigate to url
driver.get 'https://www.selenium.dev/selenium/web/inputs.html'

    # Returns true if element is checked else returns false
ele = driver.find_element(name: "checkbox_input").selected?
  {{< /tab >}}
  {{< tab header="JavaScript" >}}
// Navigate to url
await driver.get('https://www.selenium.dev/selenium/web/inputs.html');

// Returns true if element ins checked else returns false
let res = await driver.findElement(By.name("checkbox_input")).isSelected();
  {{< /tab >}}
  {{< tab header="Kotlin" >}}
 //navigates to url
 driver.get("https://www.selenium.dev/selenium/web/inputs.html")

 //returns true if element is checked else returns false
 val attr =  driver.findElement(By.name("checkbox_input")).isSelected()
  {{< /tab >}}
{{< /tabpane >}}

## Tag Name

It is used to fetch the [TagName](https://www.w3.org/TR/webdriver/#dfn-get-element-tag-name)
of the referenced Element which has the focus in the current browsing context.

{{< tabpane langEqualsHeader=true >}}
  {{< tab header="Java" >}}
 //navigates to url
 driver.get("https://www.selenium.dev/selenium/web/inputs.html");

 //returns TagName of the element
 String value = driver.findElement(By.name("email_input")).getTagName();
  {{< /tab >}}
  {{< tab header="Python" >}}
    # Navigate to url
driver.get("https://www.selenium.dev/selenium/web/inputs.html")

    # Returns TagName of the element
attr = driver.find_element(By.NAME, "email_input").tag_name
  {{< /tab >}}
  {{< tab header="CSharp" >}}
// Navigate to Url
driver.Navigate().GoToUrl("https://www.selenium.dev/selenium/web/inputs.html");

// Returns TagName of the element
string attr = driver.FindElement(By.Name("email_input")).TagName;
  {{< /tab >}}
  {{< tab header="Ruby" >}}
    # Navigate to url
driver.get 'https://www.selenium.dev/selenium/web/inputs.html'

    # Returns TagName of the element
attr = driver.find_element(name: "email_input").tag_name
  {{< /tab >}}
  {{< tab header="JavaScript" >}}
// Navigate to URL
await driver.get('https://www.selenium.dev/selenium/web/inputs.html');

// Returns TagName of the element
let value = await driver.findElement(By.name('email_input')).getTagName();
  {{< /tab >}}
  {{< tab header="Kotlin" >}}
 //navigates to url
 driver.get("https://www.selenium.dev/selenium/web/inputs.html")

 //returns TagName of the element
 val attr =  driver.findElement(By.name("email_input")).getTagName()
  {{< /tab >}}
{{< /tabpane >}}

## Size and Position

It is used to fetch the dimensions and coordinates
of the referenced element.

The fetched data body contain the following details:
* X-axis position from the top-left corner of the element
* y-axis position from the top-left corner of the element
* Height of the element
* Width of the element

{{< tabpane langEqualsHeader=true >}}
  {{< tab header="Java" >}}
// Navigate to url
driver.get("https://www.selenium.dev/selenium/web/inputs.html");

// Returns height, width, x and y coordinates referenced element
Rectangle res =  driver.findElement(By.name("range_input")).getRect();

// Rectangle class provides getX,getY, getWidth, getHeight methods
System.out.println(res.getX());
  {{< /tab >}}
  {{< tab header="Python" >}}
    # Navigate to url
driver.get("https://www.selenium.dev/selenium/web/inputs.html")

    # Returns height, width, x and y coordinates referenced element
res = driver.find_element(By.NAME, "range_input").rect
  {{< /tab >}}
  {{< tab header="CSharp" >}}
// Navigate to Url
driver.Navigate().GoToUrl("https://www.selenium.dev/selenium/web/inputs.html");

var res = driver.FindElement(By.Name("range_input"));
// Return x and y coordinates referenced element
System.Console.WriteLine(res.Location);
// Returns height, width
System.Console.WriteLine(res.Size);
  {{< /tab >}}
  {{< tab header="Ruby" >}}
    # Navigate to url
driver.get 'https://www.selenium.dev/selenium/web/inputs.html'

    # Returns height, width, x and y coordinates referenced element
res = driver.find_element(name: "range_input").rect
  {{< /tab >}}
  {{< tab header="JavaScript" >}}
// Navigate to url
await driver.get('https://www.selenium.dev/selenium/web/inputs.html');

// Returns height, width, x and y coordinates referenced element
let element =  await driver.findElement(By.name("range_input")).getRect();
  {{< /tab >}}
  {{< tab header="Kotlin" >}}
// Navigate to url
driver.get("https://www.selenium.dev/selenium/web/inputs.html")

// Returns height, width, x and y coordinates referenced element
val res = driver.findElement(By.name("range_input")).rect

// Rectangle class provides getX,getY, getWidth, getHeight methods
println(res.getX())
  {{< /tab >}}
{{< /tabpane >}}

## Get CSS Value

Retrieves the value of specified computed style property
of an element in the current browsing context.

{{< tabpane langEqualsHeader=true >}}
  {{< tab header="Java" >}}

// Navigate to Url
driver.get("https://www.selenium.dev/selenium/web/colorPage.html");

// Retrieves the computed style property 'color' of linktext
String cssValue = driver.findElement(By.id("namedColor")).getCssValue("background-color");

  {{< /tab >}}
  {{< tab header="Python" >}}

    # Navigate to Url
driver.get('https://www.selenium.dev/selenium/web/colorPage.html')

    # Retrieves the computed style property 'color' of linktext
cssValue = driver.find_element(By.ID, "namedColor").value_of_css_property('background-color')

  {{< /tab >}}
  {{< tab header="CSharp" >}}

// Navigate to Url
driver.Navigate().GoToUrl("https://www.selenium.dev/selenium/web/colorPage.html");

// Retrieves the computed style property 'color' of linktext
String cssValue = driver.FindElement(By.Id("namedColor")).GetCssValue("background-color");

  {{< /tab >}}
  {{< tab header="Ruby" >}}

    # Navigate to Url
driver.get 'https://www.selenium.dev/selenium/web/colorPage.html'

    # Retrieves the computed style property 'color' of linktext
cssValue = driver.find_element(:id, 'namedColor').css_value('background-color')

  {{< /tab >}}
    {{< tab header="JavaScript" >}}

// Navigate to Url
await driver.get('https://www.selenium.dev/selenium/web/colorPage.html');

// Retrieves the computed style property 'color' of linktext
let cssValue = await driver.findElement(By.id("namedColor")).getCssValue('background-color');

    {{< /tab >}}
  {{< tab header="Kotlin" >}}

// Navigate to Url
driver.get("https://www.selenium.dev/selenium/web/colorPage.html")

// Retrieves the computed style property 'color' of linktext
val cssValue = driver.findElement(By.id("namedColor")).getCssValue("background-color")

  {{< /tab >}}
{{< /tabpane >}}

## Text Content

Retrieves the rendered text of the specified element.

{{< tabpane langEqualsHeader=true >}}
  {{< tab header="Java" >}}
// Navigate to url
driver.get("https://www.selenium.dev/selenium/web/linked_image.html");

// Retrieves the text of the element
String text = driver.findElement(By.id("justanotherlink")).getText();
  {{< /tab >}}
  {{< tab header="Python" >}}
    # Navigate to url
driver.get("https://www.selenium.dev/selenium/web/linked_image.html")

    # Retrieves the text of the element
text = driver.find_element(By.ID, "justanotherlink").text
  {{< /tab >}}
  {{< tab header="CSharp" >}}
// Navigate to url
driver.Url="https://www.selenium.dev/selenium/web/linked_image.html";

// Retrieves the text of the element
String text = driver.FindElement(By.Id("justanotherlink")).Text;
  {{< /tab >}}
  {{< tab header="Ruby" >}}
    # Navigate to url
driver.get 'https://www.selenium.dev/selenium/web/linked_image.html'

    # Retrieves the text of the element
text = driver.find_element(:id, 'justanotherlink').text
  {{< /tab >}}
    {{< tab header="JavaScript" >}}
// Navigate to URL
await driver.get('https://www.selenium.dev/selenium/web/linked_image.html');

// retrieves the text of the element
let text = await driver.findElement(By.id('justanotherlink')).getText();
    {{< /tab >}}
  {{< tab header="Kotlin" >}}
// Navigate to URL
driver.get("https://www.selenium.dev/selenium/web/linked_image.html")

// retrieves the text of the element
val text = driver.findElement(By.id("justanotherlink")).getText()
  {{< /tab >}}
{{< /tabpane >}}



## Fetching Attributes or Properties

Fetches the run time value associated with a 
DOM attribute. It returns the data associated 
with the DOM attribute or property of the element. 

{{< tabpane langEqualsHeader=true >}}
  {{< tab header="Java" >}}
//Navigate to the url
driver.get("https://www.selenium.dev/selenium/web/inputs.html");

//identify the email text box
WebElement emailTxt = driver.findElement(By.name(("email_input")));

//fetch the value property associated with the textbox
String valueInfo = eleSelLink.getAttribute("value");
  {{< /tab >}}
  {{< tab header="Python" >}}
# Navigate to the url
driver.get("https://www.selenium.dev/selenium/web/inputs.html")

# Identify the email text box
email_txt = driver.find_element(By.NAME, "email_input")

# Fetch the value property associated with the textbox
value_info = email_txt.get_attribute("value")
  {{< /tab >}}
  {{< tab header="CSharp" >}}
 //Navigate to the url
driver.Url="https://www.selenium.dev/selenium/web/inputs.html";

//identify the email text box
IWebElement emailTxt = driver.FindElement(By.Name(("email_input")));

//fetch the value property associated with the textbox
String valueInfo = eleSelLink.GetAttribute("value");
  {{< /tab >}}
  {{< tab header="Ruby" >}}
# Navigate to the url
driver.get("https://www.selenium.dev/selenium/web/inputs.html");

#identify the email text box
email_element=driver.find_element(name: 'email_input')

#fetch the value property associated with the textbox
emailVal = email_element.attribute("value");
  {{< /tab >}}
    {{< tab header="JavaScript" >}}
// Navigate to the Url
await driver.get("https://www.selenium.dev/selenium/web/inputs.html");

// identify the email text box
const emailElement = await driver.findElements(By.xpath('//input[@name="email_input"]'));

//fetch the attribute "name" associated with the textbox
const nameAttribute = await emailElement.getAttribute("name");
    {{< /tab >}}
  {{< tab header="Kotlin" >}}
// Navigate to URL
driver.get("https://www.selenium.dev/selenium/web/inputs.html")

//fetch the value property associated with the textbox
val attr = driver.findElement(By.name("email_input")).getAttribute("value")
  {{< /tab >}}
{{< /tabpane >}}

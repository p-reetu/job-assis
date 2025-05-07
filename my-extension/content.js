document.addEventListener("click", (e) => {
  console.log("Click detected:");
  const JDelement = document.getElementById("job-details");
  //const RoleElement = document.getElementById("ember54");
  const xpath = "//*[contains(@class, 'job-title')]//a";
  const result = document.evaluate(
    xpath,
    document,
    null,
    XPathResult.FIRST_ORDERED_NODE_TYPE,
    null
  );
  const jobTitleElement = result.singleNodeValue;
  console.log(jobTitleElement.textContent);
  if (JDelement && jobTitleElement) {
    const JDText = JDelement.innerText;
    const RoleText = jobTitleElement.textContent;
    fetch("http://localhost:5000/scrape", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        JDText: JDText,
        RoleText: RoleText,
      }),
    });
  }
});

const GEMINI_API_KEY = "YOUR_GEMINI_API_KEY";
const SPREADSHEET_ID = SpreadsheetApp.getActiveSpreadsheet().getId();

function runAutonomousGenerator() {
  const ss = SpreadsheetApp.openById(SPREADSHEET_ID);
  const sheet = ss.getSheetByName("Products");
  
  const niches = [
    "Residential Solar Installation Inspection Checklist",
    "Food Truck Sanitation Compliance Protocol",
    "Independent Contractor Safety Briefing Template",
    "Commercial Airbnb Turnover Standard Operating Procedure"
  ];
  
  const selectedNiche = niches[Math.floor(Math.random() * niches.length)];
  const productId = "PROD-" + Date.now();
  
  const prompt = `Generate a comprehensive, professional, 10-point actionable operational checklist for: ${selectedNiche}. Format clearly with headings and sub-bullets.`;
  const content = callGeminiApi(prompt);
  
  if (!content) return;
  
  const doc = DocumentApp.create(selectedNiche + " - Operational Guide");
  doc.getBody().setText(content);
  const file = DriveApp.getFileById(doc.getId());
  file.setSharing(DriveApp.Access.ANYONE_WITH_LINK, DriveApp.Permission.VIEW);
  
  sheet.appendRow([productId, selectedNiche, doc.getName(), doc.getId(), "ACTIVE"]);
  Logger.log("Generated & Published: " + productId);
}

function callGeminiApi(promptText) {
  const url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=" + GEMINI_API_KEY;
  const payload = {
    contents: [{ parts: [{ text: promptText }] }]
  };
  const options = {
    method: "post",
    contentType: "application/json",
    payload: JSON.stringify(payload),
    muteHttpExceptions: true
  };
  
  const response = UrlFetchApp.fetch(url, options);
  const json = JSON.parse(response.getContentText());
  return json.candidates[0].content.parts[0].text;
}

function doPost(e) {
  try {
    const data = JSON.parse(e.postData.contents);
    const customerEmail = data.email || data.customer_details.email;
    const productId = data.product_id || data.metadata.product_id;
    
    const ss = SpreadsheetApp.openById(SPREADSHEET_ID);
    const prodSheet = ss.getSheetByName("Products");
    const orderSheet = ss.getSheetByName("Orders");
    
    const prodData = prodSheet.getDataRange().getValues();
    let fileId = "";
    let itemTitle = "";
    
    for (let i = 1; i < prodData.length; i++) {
      if (prodData[i][0] === productId) {
        fileId = prodData[i][3];
        itemTitle = prodData[i][2];
        break;
      }
    }
    
    if (fileId) {
      const downloadUrl = "https://drive.google.com/uc?export=download&id=" + fileId;
      
      GmailApp.sendEmail(
        customerEmail,
        "Your Order Download: " + itemTitle,
        "Thank you for your order!\n\nYou can access and download your document here:\n" + downloadUrl
      );
      
      orderSheet.appendRow([new Date(), customerEmail, productId, "FULFILLED"]);
      return ContentService.createTextOutput(JSON.stringify({ status: "success" })).setMimeType(ContentService.MimeType.JSON);
    }
  } catch (err) {
    return ContentService.createTextOutput(JSON.stringify({ status: "error", message: err.toString() })).setMimeType(ContentService.MimeType.JSON);
  }
}

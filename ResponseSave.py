import json, os
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') 
file = open(desktop + "/SIDTokens.txt", "a")
if(not messageIsRequest):
	if callbacks.getToolName(toolFlag) == "Proxy":
		requestInfo = helpers.analyzeRequest(messageInfo)
		#headers = requestInfo.getHeaders()
		url = requestInfo.getUrl()
		uri = "https://" + url.host + url.path
		if str(uri) == "https://m.vodafone.com.tr/maltgtwaycbu/api":
			responseInfo = helpers.analyzeResponse(messageInfo.getResponse())
			responseByte = messageInfo.getResponse()[responseInfo.getBodyOffset():]
			response = json.loads(helpers.bytesToString(responseByte))
			for sessionToken in response["nvfMsisdnsByTokens"]:
				file.write(sessionToken["sid"] + "\n")
file.close()

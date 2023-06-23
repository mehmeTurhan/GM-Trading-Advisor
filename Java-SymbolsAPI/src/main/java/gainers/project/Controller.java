package gainers.project;


import org.springframework.web.bind.annotation.*;

import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.UnsupportedEncodingException;
import java.net.URL;
import java.util.ArrayList;
import java.util.List;

@RestController
public class Controller {
    
	@RequestMapping(value = "/gainers", method = RequestMethod.GET)
    public List<String> gainers() throws UnsupportedEncodingException, IOException {
		URL url = new URL("https://financialmodelingprep.com/api/v3/stock_market/gainers?apikey=3588dcfb23f5f05c54a69ccc08d83cad");
		ObjectMapper mapper = new ObjectMapper();
		JsonNode response = mapper.readTree(url);
	
		List<String> symbols = new ArrayList<>();
		for (JsonNode gainer : response) {
			symbols.add(gainer.get("symbol").asText());
			if (symbols.size() == 5) {
				break;
			}
		}
	
		return symbols;
	}
    

	@RequestMapping(value = "/test", method = RequestMethod.GET)
    public String test() {
				return "test";
	
    }
 
}
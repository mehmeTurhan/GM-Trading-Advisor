package gainers.project;

import java.io.IOException;
import java.io.UnsupportedEncodingException;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;


@SpringBootApplication
public class ProjectApplication {	

	public static void main(String[] args) throws UnsupportedEncodingException, IOException {
		SpringApplication.run(ProjectApplication.class, args);
	}

}

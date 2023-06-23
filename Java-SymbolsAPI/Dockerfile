FROM openjdk:17

#working directory
WORKDIR /symbols

#copying the jar file
COPY build/libs/project-0.0.1-SNAPSHOT.jar symbols.jar

#exposing on the port 8080
EXPOSE 8080

#setting the entry point
ENTRYPOINT ["java","-jar","symbols.jar"]